"""Validate public legal routes and generated HTML using the standard library."""
import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.links, self.footer, self.alternates = [], [], {}
        self.canonical, self.lang = None, None
        self.notes, self.headings, self.in_footer = 0, 0, False
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'html':
            self.lang = attrs.get('lang')
        if tag == 'footer':
            self.in_footer = True
        if attrs.get('role') == 'note' or 'legal-review-note' in attrs.get('class', '').split():
            self.notes += 1
        if tag == 'h2':
            self.headings += 1
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical = attrs['href']
        if tag == 'link' and attrs.get('rel') == 'alternate' and 'hreflang' in attrs:
            self.alternates[attrs['hreflang']] = attrs['href']
        for attr in ('href', 'src'):
            if attr in attrs:
                self.links.append(attrs[attr])
                if self.in_footer and tag == 'a':
                    self.footer.append((attrs[attr], attrs.get('hreflang')))

    def handle_endtag(self, tag):
        if tag == 'footer':
            self.in_footer = False


parser = argparse.ArgumentParser()
parser.add_argument('--production', type=Path, required=True)
root = parser.parse_args().production
routes = {'/impressum/': 'de', '/datenschutz/': 'de', '/en/privacy/': 'en', '/ru/privacy/': 'ru'}
privacy = {'de': '/datenschutz/', 'en': '/en/privacy/', 'ru': '/ru/privacy/'}
bad = ('info1@example.com', '+49 123', 'Hauptstraße 123', 'Contact Information', 'Office Hours',
       'Education &amp; Training', 'Professional Memberships', 'Ludwig Maximilian', 'Appointments are available')
files = list(root.rglob('*.html'))
assert len(files) == 21, len(files)
for path in files:
    html = path.read_text(encoding='utf-8')
    page = Page(html)
    relative = path.relative_to(root).as_posix()
    assert not any(text in html for text in bad), relative
    assert 'kuranova.synology.me' not in html and 'kuranova.pages.dev' not in html, relative
    assert 'gmail' not in html.lower(), relative
    if relative == 'index.html':
        assert 'https://kuranova.de/ru/' in html
        continue
    route = '/' + relative.removesuffix('index.html')
    lang = routes.get(route, relative.split('/')[0])
    assert page.lang == lang, (relative, page.lang)
    assert page.footer == [('/impressum/', 'de'), (privacy[lang], lang)], (relative, page.footer)
    for link in page.links:
        url = urlsplit(link)
        if url.scheme == 'mailto':
            assert url.path == 'liudmila@kuranova.de', (relative, link)
        assert url.scheme != 'tel', (relative, link)
        if url.scheme == 'mailto' or not url.path:
            continue
        if url.netloc and url.hostname not in ('localhost', '127.0.0.1', 'kuranova.de'):
            continue
        dest = root / unquote(url.path.lstrip('/'))
        if url.path.endswith('/'):
            dest /= 'index.html'
        assert dest.is_file(), (relative, link)
    if route in routes:
        assert not page.notes and 'noindex' not in html, relative
        assert page.canonical == 'https://kuranova.de' + route, (relative, page.canonical)
        for field in ('Liudmila Kuranova', 'Kranzhornstrasse 5a', '81825 München', 'mailto:liudmila@kuranova.de'):
            assert field in html, (relative, field)
        if route == '/impressum/':
            assert page.headings == 2 and page.alternates == {'de': page.canonical}
            assert 'Kandidatin der medizinischen Wissenschaften' in html
            assert 'Кандидат медицинских наук' in html and 'Высшая аттестационная комиссия' in html
        else:
            assert page.headings == 5, (relative, page.headings)
            assert page.alternates == {lang: 'https://kuranova.de' + url for lang, url in privacy.items()}
            for url in ('https://www.cloudflare.com/cloudflare-customer-dpa/',
                        'https://www.ionos.de/datenschutzerklaerung', 'https://www.lda.bayern.de/de/aufgaben.html'):
                assert url in html, (relative, url)
for lang in ('de', 'ru', 'en'):
    home = (root/lang/'index.html').read_text(encoding='utf-8')
    assert 'Kranzhornstrasse' not in home and 'mailto:liudmila@kuranova.de' in home
    assert 'Dr.' not in home and 'ENT medical practice' not in home
    for slug in ('impressum', 'datenschutz'):
        assert not (root/lang/slug/'index.html').exists()
assert not (root/'en/imprint/index.html').exists()
source = Path(__file__).resolve().parent.parent / 'hugo-site/content'
for path in (source/'de/impressum.md', source/'de/datenschutz.md', source/'en/privacy.md', source/'ru/privacy.md'):
    text = path.read_text(encoding='utf-8')
    assert 'draft:' not in text and 'legalApproved:' not in text and 'reviewNotice:' not in text, path
    if path.name != 'impressum.md':
        for forbidden in ('localstorage', 'site-theme', 'hell/dunkel', 'light/dark', 'оформлен', 'browser storage',
                          'freiwillig', 'voluntary', 'добровольно', '3 monat', '3 month', '3 месяца', 'nel', 'report-to', 'privacypolicy'):
            assert forbidden not in text.lower(), (path, forbidden)
        assert text.count('https://www.cloudflare.com/') == 1
        assert len(text.split('\n## ')) == 6
assert len(list(source.rglob('impressum.md'))) == 1
for path in root.rglob('*.xml'):
    xml = path.read_text(encoding='utf-8')
    assert 'kuranova.pages.dev' not in xml, path
    if path.name == 'index.xml':
        assert not any(route in xml for route in routes), path
assert not (root/'docs').exists()
assert not any('LEGAL-AUDIT' in p.name or 'PRIVACY_AUDIT' in p.name for p in root.rglob('*'))
print(f'{root}: 21 HTML; four legal routes, canonical/hreflang, languages, footer, assets and content OK')

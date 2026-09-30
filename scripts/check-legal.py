"""Check generated local review and production files without third-party packages."""
import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.links = []
        self.footer_links = []
        self.lang = None
        self.in_footer = False
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'html':
            self.lang = attrs.get('lang')
        if tag == 'footer':
            self.in_footer = True
        for attr in ('href', 'src'):
            if attr in attrs:
                self.links.append(attrs[attr])
                if self.in_footer and tag == 'a':
                    self.footer_links.append(attrs[attr])

    def handle_endtag(self, tag):
        if tag == 'footer':
            self.in_footer = False


parser = argparse.ArgumentParser()
parser.add_argument('--production', type=Path, required=True)
parser.add_argument('--review', type=Path, required=True)
args = parser.parse_args()
bad_text = ('info1@example.com', '+49 123', 'Hauptstraße 123',
            'Contact Information', 'Office Hours', 'Education &amp; Training',
            'Education & Training', 'Professional Memberships',
            'Ludwig Maximilian', 'Appointments are available')
for root, review in ((args.production, False), (args.review, True)):
    files = list(root.rglob('*.html'))
    assert len(files) == (23 if review else 17), (root, len(files))
    for path in files:
        html = path.read_text(encoding='utf-8')
        page = Page(html)
        relative = path.relative_to(root).as_posix()
        assert 'kuranova.synology.me' not in html, relative
        assert not any(text in html for text in bad_text), relative
        if relative == 'index.html':  # Hugo's root language redirect
            continue
        lang = relative.split('/')[0]
        assert page.lang == lang, relative
        expected = [f'/{lang}/impressum/', f'/{lang}/datenschutz/']
        footer = [urlsplit(link).path for link in page.footer_links]
        assert footer == (expected if review else []), (relative, footer)
        for link in page.links:
            url = urlsplit(link)
            if url.scheme in ('mailto', 'tel') or not url.path:
                continue
            if url.netloc and url.hostname not in ('localhost', 'kuranova.pages.dev'):
                continue
            dest = root / unquote(url.path.lstrip('/'))
            if url.path.endswith('/'):
                dest /= 'index.html'
            assert dest.is_file(), (relative, link)
    for lang in ('de', 'ru', 'en'):
        home = (root / lang / 'index.html').read_text(encoding='utf-8')
        assert 'Kranzhornstrasse' not in home and 'lbkuranova@gmail.com' not in home
        for slug in ('impressum', 'datenschutz'):
            path = root / lang / slug / 'index.html'
            assert path.is_file() == review, path
            if review:
                html = path.read_text(encoding='utf-8')
                assert 'legal-review-note' in html and 'noindex' in html, path
                for field in ('Liudmila Kuranova', 'Kranzhornstrasse 5a',
                              '81825 München', 'mailto:lbkuranova@gmail.com'):
                    assert field in html, (path, field)
                for target_lang in ('de', 'ru', 'en'):
                    assert f'/{target_lang}/{slug}/' in html, (path, target_lang)
        listing = (root / lang / 'articles' / 'index.html').read_text(encoding='utf-8')
        assert 'legal-review-note' not in listing
    # Legal documents must never become medical articles or RSS entries.
    for path in root.rglob('*.xml'):
        xml = path.read_text(encoding='utf-8')
        assert '/impressum/' not in xml and '/datenschutz/' not in xml, path
    print(f'{root}: {len(files)} HTML; routes, content, lang, footer, assets and RSS OK')

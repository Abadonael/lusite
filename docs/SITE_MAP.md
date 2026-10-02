# Карта сайта

Обновлено: 2 октября 2026 года. T01 выполнен 30 сентября 2026 года.
Карта отражает финальную production-сборку юридической задачи PR #3 от 02.10.
Публикация PR #3 подтверждена на kuranova.de; прежние наблюдения production ниже
относятся к проверке до публикации. Текущая редакция: [LEGAL-AUDIT.md](LEGAL-AUDIT.md).
Подробные доказательства и ограничения: [PRIVACY_AUDIT.md](PRIVACY_AUDIT.md).
Основание: исходники commit `ebb3df1ad7e8bebeea43bf8fcce83c711170fa74`,
свежая сборка Hugo и публичные GET-запросы к production. Панель Cloudflare не проверена.
Все пути исходников ниже — относительно корня Git-репозитория.
Production: https://kuranova.de/; корень Hugo: `hugo-site/`.

## Общие страницы

| Страница | Реальный URL | Исходный файл | Шаблон / результат |
|---|---|---|---|
| Корень | `/` | Нет Markdown; Hugo генерирует `public/index.html` | Свежая сборка: meta refresh на `https://kuranova.de/ru/`; production 02.10 ещё использует старый домен в fallback |
| Главная RU | `/ru/` | `hugo-site/content/ru/_index.md` | `hugo-site/layouts/index.html`; имя без Dr., наёмный статус и новый email в hero; временная биография и Contact Information удалены в PR |
| Главная DE | `/de/` | `hugo-site/content/de/_index.md` | Тот же шаблон; имя без Dr., наёмный статус и новый email в hero; временная биография и Contact Information удалены в PR |
| Главная EN | `/en/` | `hugo-site/content/en/_index.md` | Тот же шаблон; имя без Dr., наёмный статус и новый email |
| Список RU | `/ru/articles/` | `hugo-site/content/ru/articles/_index.md` | `hugo-site/layouts/articles/list.html` |
| Список DE | `/de/articles/` | `hugo-site/content/de/articles/_index.md` | Тот же шаблон |
| Список EN | `/en/articles/` | `hugo-site/content/en/articles/_index.md` | Тот же шаблон |
| Тема «Аллергия» | `/ru/articles/allergy/` | `hugo-site/content/ru/articles/allergy/_index.md` | Тот же list.html; три дочерние статьи |
| Старые «Аденоиды» DE | `/de/articles/adenoids/` | `hugo-site/content/de/articles/adenoids.md` | Русский текст старой редакции, не готовый немецкий перевод |
| Старые «Аденоиды» EN | `/en/articles/adenoids/` | `hugo-site/content/en/articles/adenoids.md` | Русский текст старой редакции, не готовый английский перевод |
| Impressum DE | `/impressum/` | `hugo-site/content/de/impressum.md` | Один немецкий документ; canonical, hreflang de |
| Datenschutz DE | `/datenschutz/` | `hugo-site/content/de/datenschutz.md` | Основная версия privacy; canonical и три hreflang |
| Privacy EN | `/en/privacy/` | `hugo-site/content/en/privacy.md` | Перевод немецкого Datenschutz |
| Политика RU | `/ru/privacy/` | `hugo-site/content/ru/privacy.md` | Перевод немецкого Datenschutz |
| 404 | Отдельной страницы нет | Нет `hugo-site/layouts/404.html`; сборка не создаёт 404.html | Production на четырёх несуществующих путях возвращает HTTP 200 и корневой meta refresh на `/ru/` |

До публикации прежние общие страницы и семь статей вернули HTTP 200.
Финальная обычная сборка: 21 HTML, включая четыре юридические страницы.
Legal с build.list=never не входит в списки/RSS/sitemap; статьи не изменены.
Старые `/{de,en,ru}/impressum/` и `/{de,en,ru}/datenschutz/` не генерируются;
переведённые Impressum удалены, EN/RU Datenschutz переименованы в privacy.md.

## Семь русских статей

| ID | Тема | Заголовок | URL RU | Исходный файл |
|---|---|---|---|---|
| A01 | Аллергия | Аллергия на домашнюю пыль | `/ru/articles/allergy/house-dust-allergy/` | `hugo-site/content/ru/articles/allergy/house-dust-allergy.md` |
| A02 | Аллергия | Аллергия на цветение | `/ru/articles/allergy/pollen-allergy/` | `hugo-site/content/ru/articles/allergy/pollen-allergy.md` |
| A03 | Аллергия | Терапия аллергии | `/ru/articles/allergy/allergy-treatment/` | `hugo-site/content/ru/articles/allergy/allergy-treatment.md` |
| A04 | Без темы | Аденоиды | `/ru/articles/adenoids/` | `hugo-site/content/ru/articles/adenoids.md` |
| A05 | Без темы | Храп и остановки дыхания во сне | `/ru/articles/snoring-and-sleep-apnea/` | `hugo-site/content/ru/articles/snoring-and-sleep-apnea.md` |
| A06 | Без темы | Гигиена сна | `/ru/articles/sleep-hygiene/` | `hugo-site/content/ru/articles/sleep-hygiene.md` |
| A07 | Без темы | Боль в горле | `/ru/articles/sore-throat/` | `hugo-site/content/ru/articles/sore-throat.md` |

Новые переводы DE/EN отложены (T09). Для A04 уже есть старые языковые страницы,
но они содержат русский текст; не создавать дубликаты при переводе.
Русские статьи добавлены/обновлены; утверждение заказчиком отдельно не подтверждено (T08).

Формат статей: YAML front matter `title`, `date`, `summary`, `translationKey`;
тело Markdown с H2/H3 и списками. Шаблон: `hugo-site/layouts/articles/single.html`.
Группировка — вложенные разделы Hugo с `_index.md`, не taxonomy:
`disableKinds = ["taxonomy", "term"]`. Список использует `.Pages`, поэтому на
`/ru/articles/` представлены четыре самостоятельные статьи и карточка «Аллергия»;
три аллергологические статьи находятся внутри темы. Заголовок обоих списков
жёстко задан как `Articles`, описание — `Medical articles and publications.`
Даты форматируются по-английски. Это текущее поведение, не новая локализация.

## Генерируемые XML и ресурсы

- `/sitemap.xml` — индекс карт сайта; `/ru/sitemap.xml`, `/de/sitemap.xml`, `/en/sitemap.xml` — карты языков.
- RSS главных: `/ru/index.xml`, `/de/index.xml`, `/en/index.xml`.
- RSS списков: `/ru/articles/index.xml`, `/de/articles/index.xml`, `/en/articles/index.xml`.
- RSS темы: `/ru/articles/allergy/index.xml`.
- XML генерирует Hugo встроенными шаблонами; отдельных исходных XML в проекте нет.
- Статика: `hugo-site/static/` → корень output: `/css/*.css`, `/js/theme-toggle.js`, `/images/doctor.jpg`.
- В PR 13 CSS (добавлен legal.css), один JS и одна фотография. Общий HTML подключает 12 CSS;
  `components.css` лежит в output, но в общем шаблоне не подключён.
- Canonical и hreflang добавлены только у четырёх юридических страниц.
В остальных содержательных HTML они не добавлялись. Canonical есть у корневого redirect;
  альтернативные языки представлены в sitemap. Ссылок на старый synology-домен
  в свежей сборке HTML/XML/JS/CSS не найдено.

## Глобальные элементы

| Элемент | Реальная реализация | Текущее поведение |
|---|---|---|
| Общий каркас | `hugo-site/layouts/_default/baseof.html` | CSS, header, main, footer, JS; legal canonical/hreflang, без approval guard |
| Шапка/меню/языки | `hugo-site/layouts/partials/header.html` | Home и Articles через relLangURL; `.AllTranslations` и `.RelPermalink` |
| Связь переводов | `translationKey` у статей; одинаковые пути у главных и разделов | Аденоиды связаны во всех трёх языках; остальные шесть статей и тема только RU |
| Отсутствующий перевод | Тот же header | Меню показывает только существующие варианты, включая текущий язык; фиктивных ссылок DE/EN у новых статей нет |
| Тема | `hugo-site/static/js/theme-toggle.js`, `static/css/themes.css`, `static/css/variables.css` | localStorage `site-theme`, значения dark/light, атрибут data-theme |
| Начальная тема | `themes.css` | Без сохранённого выбора: светлые переменные, системная тёмная тема через prefers-color-scheme |
| Сохранение темы | Тот же JS | В PR чтение при загрузке без записи; запись только по клику; TTL нет, try/catch при блокировке storage |
| Возврат со статьи | `hugo-site/layouts/articles/single.html` | Ссылка на список статей текущего языка, в том числе из темы |
| Общий single | `hugo-site/layouts/_default/single.html` | H1/.Content; reviewNotice выводится только при непустом тексте, используется текущая типографика |
| Футер | `hugo-site/layouts/partials/footer.html`, `static/css/legal.css` | На всех содержательных страницах Impressum → /impressum/; DE Datenschutz → /datenschutz/, EN Privacy → /en/privacy/, RU политика → /ru/privacy/ |
| Контакты | Временный Contact Information удалён из index.html и трёх _index.md | Единственный email liudmila@kuranova.de показан на главных и в legal; почта IONOS; публичный критерий удаления — необходимость для цели с учётом законных обязанностей. Почтовый адрес только в legal; формы пока нет (T10 TODO) |

В PR storage-исключения обработаны; первый клик учитывает системную тему.
10 Node-сценариев проверяют эти случаи и отсутствие записи при загрузке.
Production пока использует старый JS; browser-проверка блокировки storage остаётся открытой.
В navigation.css уменьшены мобильные отступы для устранения переполнения на 360 px.

## Сборка и публикация

- Конфигурация: `hugo-site/hugo.toml`; других hugo/config TOML/YAML и `config/` нет.
- baseURL: `https://kuranova.de/`; defaultContentLanguage: `ru`;
  defaultContentLanguageInSubdir: `true`.
- Контент: `content/ru`, `content/de`, `content/en`; веса языков EN=1, DE=2, RU=3.
- Внешняя Hugo-тема и модули не настроены; используются локальные layouts/static.
- Hugo локально: `v0.163.3+extended windows/amd64`.
- Из корня репозитория: `hugo --source hugo-site --minify`;
  локальный preview: `hugo server --source hugo-site --destination C:\Nik\LuSite\.local\release-preview-20261002 --bind 127.0.0.1 --port 1313`.
  Финальные legal входят в обычную сборку без специальных environment/buildDrafts.
- Обычный output: `hugo-site/public/`; исключён из Git вместе с resources и build lock.
- Финальная проверочная сборка: `.local/release-20261002`; preview: `.local/release-preview-20261002`. Предыдущие `.local/production`, `.local/review`, `.local/legal-review` — артефакты draft-этапа; `.local/` исключён из Git.
- Для аудита выполнена свежая сборка вне репозитория, чтобы не менять output проекта:

```powershell
$auditDir = Join-Path $env:TEMP 'lusite-t02-20260930'
hugo --source hugo-site --destination "$auditDir\public" --cacheDir "$auditDir\cache" --noBuildLock --minify
```

Сборка успешна; предупреждения об устаревших languageName/.Language.LanguageName.
Cloudflare: публичный сайт обслуживается, но точные build command, версия Hugo,
production branch, deployment SHA, custom domains и preview-настройки в панели
не проверены. Упомянутая в исходном workflow схема main → production baseURL,
прочие ветки → CF_PAGES_URL остаётся неподтверждённой, не выводится из репозитория.
Preview URL для проверки не предоставлен. CI/workflow/wrangler/functions и
`_headers`/`_redirects` в проекте не обнаружены.

Результат T02 и вопросы оператору: [TASKS.md](TASKS.md).
Чек-лист последующих проверок: [QA_CHECKLIST.md](QA_CHECKLIST.md).

## Уточнения 02.10.2026

Локальный main содержит отдельный commit владельца 16ae439 с новым baseURL;
GitHub main при чтении ещё ebb3df1. В PR включается текущая локальная конфигурация.
Реквизиты, степень, Cloudflare и IONOS обновлены. В финальном поручении
маршруты заменены четырьмя URL выше, переводы privacy связаны translationKey;
draft/approval guard снят. Предыдущая draft-стадия завершена.
Свежая сборка использует kuranova.de в redirect и sitemap/RSS.
До финальной публикации production показывал временный профиль/контакты;
неизвестные и legal-пути давали HTTP 200 с redirect на прежний pages.dev.
Это наблюдение предыдущего этапа; результат нового deployment проверяется после merge.
Имя оператора и юридический контактный адрес не обозначают адрес приёма.

## Результат публикации 02.10.2026

PR #3 merged, main `3e2103a03cee0fd127e76802403888c68989f401`.
Cloudflare Pages check этого commit completed/success. Все четыре legal URL
выше открываются на kuranova.de с нужными lang/canonical и новым footer.
Единственный email и отсутствие временных сведений главной подтверждены в IAB.
Preview перенаправляется на production; отдельная проверка preview не засчитана.

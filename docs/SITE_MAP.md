# Карта сайта

Обновлено: 1 октября 2026 года. T01 выполнен 30 сентября 2026 года.
Изменения юридической задачи ниже относятся к рабочим файлам и черновому PR; production пока прежний.
Подробные доказательства и ограничения: [PRIVACY_AUDIT.md](PRIVACY_AUDIT.md).
Основание: исходники commit `ebb3df1ad7e8bebeea43bf8fcce83c711170fa74`,
свежая сборка Hugo и публичные GET-запросы к production. Панель Cloudflare не проверена.
Все пути исходников ниже — относительно корня Git-репозитория.
Production: https://kuranova.pages.dev/; корень Hugo: `hugo-site/`.

## Общие страницы

| Страница | Реальный URL | Исходный файл | Шаблон / результат |
|---|---|---|---|
| Корень | `/` | Нет Markdown; Hugo генерирует `public/index.html` | HTML meta refresh на `https://kuranova.pages.dev/ru/`; HTTP 200 |
| Главная RU | `/ru/` | `hugo-site/content/ru/_index.md` | `hugo-site/layouts/index.html`; имя/профиль в hero; временная биография и Contact Information удалены в PR |
| Главная DE | `/de/` | `hugo-site/content/de/_index.md` | Тот же шаблон; имя/профиль в hero; временная биография и Contact Information удалены в PR |
| Главная EN | `/en/` | `hugo-site/content/en/_index.md` | Тот же шаблон |
| Список RU | `/ru/articles/` | `hugo-site/content/ru/articles/_index.md` | `hugo-site/layouts/articles/list.html` |
| Список DE | `/de/articles/` | `hugo-site/content/de/articles/_index.md` | Тот же шаблон |
| Список EN | `/en/articles/` | `hugo-site/content/en/articles/_index.md` | Тот же шаблон |
| Тема «Аллергия» | `/ru/articles/allergy/` | `hugo-site/content/ru/articles/allergy/_index.md` | Тот же list.html; три дочерние статьи |
| Старые «Аденоиды» DE | `/de/articles/adenoids/` | `hugo-site/content/de/articles/adenoids.md` | Русский текст старой редакции, не готовый немецкий перевод |
| Старые «Аденоиды» EN | `/en/articles/adenoids/` | `hugo-site/content/en/articles/adenoids.md` | Русский текст старой редакции, не готовый английский перевод |
| Impressum DE/RU/EN | `/{de,ru,en}/impressum/` — только local legal-review | `hugo-site/content/{de,ru,en}/impressum.md` | Общий single.html; draft=true, legalApproved=false; production URL ещё отсутствуют |
| Datenschutz DE/RU/EN | `/{de,ru,en}/datenschutz/` — только local legal-review | `hugo-site/content/{de,ru,en}/datenschutz.md` | Общий single.html; согласованные translationKey, HTML lang и черновик/noindex |
| 404 | Отдельной страницы нет | Нет `hugo-site/layouts/404.html`; сборка не создаёт 404.html | Production на четырёх несуществующих путях возвращает HTTP 200 и корневой meta refresh на `/ru/` |

Все существующие HTML-маршруты выше и семь статей ниже вернули HTTP 200.
В обычной сборке по-прежнему 17 HTML: корневой redirect и 16 страниц контента/разделов.
В локальном legal-review с --buildDrafts — 23 HTML, включая 6 юридических черновиков.
Черновики build.list=never не входят в списки/RSS/sitemap; статьи не изменены.

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
- В обычном HTML нет canonical и hreflang. Canonical есть у корневого redirect;
  альтернативные языки представлены в sitemap. Ссылок на старый synology-домен
  в свежей сборке HTML/XML/JS/CSS не найдено.

## Глобальные элементы

| Элемент | Реальная реализация | Текущее поведение |
|---|---|---|
| Общий каркас | `hugo-site/layouts/_default/baseof.html` | CSS, header, main, footer, JS; errorf блокирует unapproved legal вне local legal-review |
| Шапка/меню/языки | `hugo-site/layouts/partials/header.html` | Home и Articles через relLangURL; `.AllTranslations` и `.RelPermalink` |
| Связь переводов | `translationKey` у статей; одинаковые пути у главных и разделов | Аденоиды связаны во всех трёх языках; остальные шесть статей и тема только RU |
| Отсутствующий перевод | Тот же header | Меню показывает только существующие варианты, включая текущий язык; фиктивных ссылок DE/EN у новых статей нет |
| Тема | `hugo-site/static/js/theme-toggle.js`, `static/css/themes.css`, `static/css/variables.css` | localStorage `site-theme`, значения dark/light, атрибут data-theme |
| Начальная тема | `themes.css` | Без сохранённого выбора: светлые переменные, системная тёмная тема через prefers-color-scheme |
| Сохранение темы | Тот же JS | В PR чтение при загрузке без записи; запись только по клику; TTL нет, try/catch при блокировке storage |
| Возврат со статьи | `hugo-site/layouts/articles/single.html` | Ссылка на список статей текущего языка, в том числе из темы |
| Общий single | `hugo-site/layouts/_default/single.html` | Реализованы H1/.Content и локальная пометка черновика; используется текущая типографика |
| Футер | `hugo-site/layouts/partials/footer.html`, `static/css/legal.css` | Две локализованные ссылки на всех содержательных страницах local review; DE fallback с Deutsch при отсутствии перевода. В обычной сборке до готовности страниц ссылки скрыты |
| Контакты | Временный Contact Information удалён из index.html и трёх _index.md | Подтверждённые реквизиты/mailto только в юридических черновиках; формы пока нет (T10 TODO) |

В PR storage-исключения обработаны; первый клик учитывает системную тему.
10 Node-сценариев проверяют эти случаи и отсутствие записи при загрузке.
Production пока использует старый JS; browser-проверка блокировки storage остаётся открытой.
В navigation.css уменьшены мобильные отступы для устранения переполнения на 360 px.

## Сборка и публикация

- Конфигурация: `hugo-site/hugo.toml`; других hugo/config TOML/YAML и `config/` нет.
- baseURL: `https://kuranova.pages.dev/`; defaultContentLanguage: `ru`;
  defaultContentLanguageInSubdir: `true`.
- Контент: `content/ru`, `content/de`, `content/en`; веса языков EN=1, DE=2, RU=3.
- Внешняя Hugo-тема и модули не настроены; используются локальные layouts/static.
- Hugo локально: `v0.163.3+extended windows/amd64`.
- Из корня репозитория: `hugo --source hugo-site --minify`;
  локальное юридическое ревью: `hugo server --source hugo-site --environment legal-review --buildDrafts --destination C:\Nik\LuSite\.local\legal-review --bind 127.0.0.1 --port 1313`.
  Обычный -D без этого environment теперь намеренно завершается ошибкой. Не использовать legal-review в Cloudflare.
- Обычный output: `hugo-site/public/`; исключён из Git вместе с resources и build lock.
- Проверочные сборки этой задачи: `.local/production`, `.local/review`, `.local/legal-review`; `.local/` исключён из Git и не предназначен для deployment.
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

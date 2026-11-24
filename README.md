# Meta_001: Kiprop Haggai, portfolio dashboard

A static site in plain HTML, CSS and JavaScript. No build step to run it, no tracking, no cookies.

| Page | What it holds |
|---|---|
| `index.html` | Dashboard: impact console (filters, KPI tiles, career line), stacked stories, Medium and video strips |
| `work.html` | Nine projects, proposals and businesses, filterable, each with a full write-up sheet (deep links like `work.html#k4rc`) |
| `business.html` | Business portfolio: TerraHeal Pharmaceuticals and TerraOre Mineral Resources |
| `more.html` | Fields of expertise, method, experience, education, services, FAQ, handles, colour schemes |
| `media.html` | YouTube thumbnails with play-in-place |
| `medium.html` | Designed landing page for the Medium stories |
| `articles.html` | Searchable archive of the stories |
| `contact.html` | Call and WhatsApp (0716 494 214), message builder, handles, save-to-contacts |

Design file (user flows, dashboard layout, four colour schemes, hover-card states, Medium landing): https://www.figma.com/design/pQMq5zq0D9bbvNvQpLfiD8

## Editing content

All words and numbers live in `gen/data.py`. After editing, run:

    python3 gen/build.py

This rewrites the HTML pages. Commit the result.

- **Social handles:** edit `HANDLES` in `gen/data.py`. Uncomment and fill the LinkedIn, Instagram, X, Facebook or TikTok lines. Only handles that exist are shown.
- **YouTube videos:** edit `VIDEOS` (the 11-character video id, title, length). Thumbnails come from YouTube automatically.
- **Medium stories:** edit `ARTICLES`.
- **Colour schemes:** variables at the top of `assets/css/app.css` (`Lagoon` is the default; `midnight`, `savanna` and `reef` are alternatives chosen from the Colours button).

## Publish on GitHub Pages (free)

Settings > Pages > Build and deployment > Deploy from a branch > `main` / `(root)` > Save.
The site appears at https://kip-01.github.io/Meta_001/ after a minute or two.

## Left out on purpose

Budgets from the source proposals, personal details of private individuals, licence and tax numbers, bank details, and photos of identifiable learners.

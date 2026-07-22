# GitHub Pages — Instruqt loading iframe

Static site for the **“please wait”** experience in Cisco Instruqt labs.

## Enable Pages (once per repo)

1. GitHub → **elastic/cisco-demo-ai-fed_sources-agent_builder** → **Settings** → **Pages**
2. **Build and deployment** → Source: **GitHub Actions** (workflow below) *or* **Deploy from branch** → `main` → **`/docs`**

After deploy, the site is live at:

**https://elastic.github.io/cisco-demo-ai-fed_sources-agent_builder/**

| Page | Use |
|------|-----|
| [presentation/cisco-search-ai.html](presentation/cisco-search-ai.html) | **Primary briefing** — fslides player (Metrics Analyst–style), 16 slides |
| [presentation/](presentation/) | Source slides + `fslides` build (`README.md` there) |
| [slides.html](slides.html) | **Canonical URL** — redirects to `presentation/cisco-search-ai.html` |
| [instruqt.html](instruqt.html) | Compact static loader |
| [index.html](index.html) | Landing summary |

## Instruqt embed

```html
<iframe
  src="https://elastic.github.io/cisco-demo-ai-fed_sources-agent_builder/presentation/cisco-search-ai.html"
  width="100%"
  height="720"
  frameborder="0"
  style="border-radius:8px;border:1px solid #2a3140;display:block;">
</iframe>
```

The lab VM also iframes this URL from nginx `/loading` during Kibana proxy startup (see `scripts/es3-setup-base.sh`).

## Local preview

```bash
# Full fslides deck (recommended)
cd docs/presentation && npm install && npm run serve

# Or static Pages tree
python3 -m http.server 8765 --directory docs
# open http://localhost:8765/presentation/cisco-search-ai.html
```

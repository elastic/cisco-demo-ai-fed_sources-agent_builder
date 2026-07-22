# GitHub Pages — Instruqt loading iframe

Static site for the **“please wait”** experience in Cisco Instruqt labs.

## Enable Pages (once per repo)

1. GitHub → **elastic/cisco-demo-ai-fed_sources-agent_builder** → **Settings** → **Pages**
2. **Build and deployment** → Source: **GitHub Actions** (workflow below) *or* **Deploy from branch** → `main` → **`/docs`**

After deploy, the site is live at:

**https://elastic.github.io/cisco-demo-ai-fed_sources-agent_builder/**

| Page | Use |
|------|-----|
| [slides.html](slides.html) | **8-slide deck** — what/why infographics (← →), facilitator or fullscreen |
| [slides.html?embed=1](slides.html?embed=1) | **Instruqt iframe** (Notes + nginx `/loading`) |
| [instruqt.html](instruqt.html) | Compact static loader |
| [index.html](index.html) | Landing summary |

## Instruqt embed

```html
<iframe
  src="https://elastic.github.io/cisco-demo-ai-fed_sources-agent_builder/slides.html?embed=1"
  width="100%"
  height="720"
  frameborder="0"
  style="border-radius:8px;border:1px solid #2a3140;display:block;">
</iframe>
```

The lab VM also iframes this URL from nginx `/loading` during Kibana proxy startup (see `scripts/es3-setup-base.sh`).

## Local preview

```bash
python3 -m http.server 8765 --directory docs
# open http://localhost:8765/instruqt.html
```

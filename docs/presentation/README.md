# Cisco × Elastic — Search / AI presentation (`fslides`)

Same stack as the [Metrics Analyst briefing](https://elastic.github.io/observability-team/collaterals/metrics-analysts-presentation/metrics-analyst.html): **1280×720 HTML slides** + **fslides player** (filmstrip, speaker notes, laser, timer, `#slide` deep links).

## Live URL (GitHub Pages)

https://elastic.github.io/cisco-demo-ai-fed_sources-agent_builder/presentation/cisco-search-ai.html

Deep link example: `…/cisco-search-ai.html#future.html` or `#0`

## Edit & rebuild

```bash
cd docs/presentation
npm install
python3 generate_slides.py   # regenerate HTML from the Python templates
npm run build                # → cisco-search-ai.html player
npm run serve                # local preview (fslides serve, port 3015)
```

- **Content / layout:** edit `generate_slides.py` (or individual `*.html` slides), then `npm run build`.
- **Order / labels:** `fuckslides.config.js`
- **Speaker notes:** `notes.json`
- **Player shell:** `build-player.js` (copied from Metrics Analyst pattern)

Commit the built `cisco-search-ai.html` **and** each slide `*.html` so Pages can load iframes without a Node build step.

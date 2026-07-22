'use strict';

const fs   = require('fs');
const path = require('path');

const cwd    = process.cwd();
const config = require(path.join(cwd, 'fuckslides.config.js'));
let pkgDir;
try { pkgDir = path.dirname(require.resolve('fslides/package.json')); }
catch (_) {
  console.error('Install fslides first: npm install');
  process.exit(1);
}
const out    = path.join(cwd, (config.name || 'presentation') + '.html');

const fsJs   = fs.readFileSync(path.join(pkgDir, 'js', 'fuckslides.js'), 'utf8');
const logoPath = path.join(pkgDir, 'logo.png');
const logoDat  = fs.existsSync(logoPath) && fs.statSync(logoPath).size < 100 * 1024
  ? 'data:image/png;base64,' + fs.readFileSync(logoPath).toString('base64')
  : '';

let html = fs.readFileSync(path.join(pkgDir, 'player.html'), 'utf8');

const notesPath = path.join(cwd, 'notes.json');
const notesDat  = fs.existsSync(notesPath) ? fs.readFileSync(notesPath, 'utf8') : '{}';

const AUDIO_EXTS = ['.webm', '.m4a', '.mp3', '.ogg', '.wav'];
const recDir = path.join(cwd, 'recordings');
const recordings = {};
if (fs.existsSync(recDir)) {
  const best = {};
  for (const f of fs.readdirSync(recDir)) {
    const ext = path.extname(f).toLowerCase();
    if (!AUDIO_EXTS.includes(ext)) continue;
    const base = path.basename(f, ext);
    const mtime = fs.statSync(path.join(recDir, f)).mtimeMs;
    if (!best[base] || mtime > best[base].mtime) best[base] = { file: f, mtime };
  }
  for (const base of Object.keys(best)) recordings[base + '.html'] = 'recordings/' + best[base].file;
}

const snippet = `<script>
window.FUCKSLIDES_SLIDES   = ${JSON.stringify(config.slides)};
window.FUCKSLIDES_LABELS   = ${JSON.stringify(config.labels || config.slides.map(s => s.replace('.html', '')))};
window.FUCKSLIDES_NAME     = ${JSON.stringify(config.name || 'presentation')};
window.FUCKSLIDES_TITLE    = ${JSON.stringify(config.title || config.name || 'presentation')};
window.FUCKSLIDES_DISABLED = ${JSON.stringify(config.disabled || [])};
window.FUCKSLIDES_NOTES    = ${notesDat};
window.FUCKSLIDES_RECORDINGS = ${JSON.stringify(recordings)};
</script>`;

html = html.replace('</head>', snippet + '\n</head>');
html = html.replace('let allNotes  = {};', 'let allNotes  = window.FUCKSLIDES_NOTES || {};');
html = html.replace(/<title>[^<]*<\/title>/i, `<title>${config.title || config.name || 'Presentation'}</title>`);
html = html.replace(/<script src="\/js\/fuckslides\.js"><\/script>/g, `<script>${fsJs}</script>`);
if (logoDat) html = html.replace(/src="\/logo\.png"/g, `src="${logoDat}"`);
else html = html.replace(/<img class="nav-logo"[^>]*>/g, '');

fs.writeFileSync(out, html, 'utf8');
const size = (fs.statSync(out).size / 1024).toFixed(0);
console.log(`\n  ✓  Built player → ${path.relative(cwd, out)}  (${size} KB)\n`);

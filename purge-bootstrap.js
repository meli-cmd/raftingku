/**
 * Script untuk men-purge Bootstrap CSS yang tidak dipakai.
 * Menggunakan raw content mode agar kompatibel dengan Windows paths.
 */
const { PurgeCSS } = require('purgecss');
const fs = require('fs');
const path = require('path');
const https = require('https');

const BOOTSTRAP_URL = 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css';
const BOOTSTRAP_LOCAL = 'c:\\\\Users\\\\Dell\\\\Downloads\\\\wisata-gm\\\\assets\\\\css\\\\bootstrap.min.css';
const TMP_BOOTSTRAP = 'c:\\\\Users\\\\Dell\\\\Downloads\\\\wisata-gm\\\\tmp-bootstrap-full.css';
const DIR = 'c:\\\\Users\\\\Dell\\\\Downloads\\\\wisata-gm';

function downloadFile(url, dest) {
    return new Promise((resolve, reject) => {
        if (fs.existsSync(dest)) {
            console.log('Using cached Bootstrap CSS...');
            return resolve();
        }
        console.log('Downloading Bootstrap CSS from CDN...');
        const file = fs.createWriteStream(dest);
        const makeRequest = (u) => {
            https.get(u, (res) => {
                if (res.statusCode >= 300 && res.statusCode < 400) {
                    makeRequest(res.headers.location);
                } else {
                    res.pipe(file);
                    file.on('finish', () => { file.close(); resolve(); });
                }
            }).on('error', reject);
        };
        makeRequest(url);
    });
}

function getHtmlFiles(d) {
    let results = [];
    const list = fs.readdirSync(d);
    list.forEach(file => {
        if (['node_modules', '.git'].includes(file)) return;
        const full = path.join(d, file);
        if (fs.statSync(full).isDirectory()) {
            results = results.concat(getHtmlFiles(full));
        } else if (full.endsWith('.html')) {
            results.push(full);
        }
    });
    return results;
}

async function main() {
    await downloadFile(BOOTSTRAP_URL, TMP_BOOTSTRAP);
    
    const bsCSS = fs.readFileSync(TMP_BOOTSTRAP, 'utf8');
    const origSize = Buffer.byteLength(bsCSS, 'utf8');
    console.log(`Bootstrap full: ${(origSize/1024).toFixed(1)} KB`);

    // Gather all HTML content
    const htmlFiles = getHtmlFiles(DIR);
    const cssFiles = [
        path.join(DIR, 'assets', 'css', 'style.css'),
        path.join(DIR, 'assets', 'js', 'script.js'),
    ];

    const contentRaw = htmlFiles.map(f => ({
        raw: fs.readFileSync(f, 'utf8'),
        extension: 'html'
    }));

    // Also add JS files
    cssFiles.forEach(f => {
        if (fs.existsSync(f)) {
            contentRaw.push({
                raw: fs.readFileSync(f, 'utf8'),
                extension: path.extname(f).slice(1)
            });
        }
    });

    console.log(`Scanning ${htmlFiles.length} HTML files + ${cssFiles.length} JS/CSS files...`);
    console.log('Running PurgeCSS...');
    
    const purgecss = new PurgeCSS();
    const result = await purgecss.purge({
        content: contentRaw,
        css: [{ raw: bsCSS }],
        safelist: {
            standard: [
                'show', 'active', 'collapse', 'collapsing', 'fade', 'in',
                'open', 'disabled', 'was-validated', 'valid', 'invalid',
                'aos-animate', 'aos-init', 'slideInUp',
            ],
            deep: [
                /^navbar/, /^btn/, /^card/, /^modal/, /^collapse/,
                /^dropdown/, /^nav-/, /^tab-/, /^swiper/, /^offcanvas/,
                /^toast/, /^bs-/, /^form-/,
            ],
            greedy: [/data-bs/, /aria-/]
        }
    });

    if (!result || result.length === 0 || !result[0].css) {
        throw new Error('PurgeCSS returned empty result');
    }

    const purgedCSS = result[0].css;
    fs.writeFileSync(BOOTSTRAP_LOCAL, purgedCSS, 'utf8');
    
    const newSize = Buffer.byteLength(purgedCSS, 'utf8');
    const saving = ((1 - newSize/origSize) * 100).toFixed(0);
    
    console.log(`âœ“ Purged Bootstrap: ${(newSize/1024).toFixed(1)} KB (${saving}% smaller)`);
    console.log(`âœ“ Saved to: ${BOOTSTRAP_LOCAL}`);
    
    if (fs.existsSync(TMP_BOOTSTRAP)) fs.unlinkSync(TMP_BOOTSTRAP);
    console.log('Done!');
}

main().catch(e => { console.error('Error:', e.message); process.exit(1); });

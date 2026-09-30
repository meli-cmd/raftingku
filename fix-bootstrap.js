/**
 * Script untuk:
 * 1. Ganti Bootstrap CDN link dari blocking ke non-blocking (preload pattern)
 * 2. Ganti CDN URL ke file lokal purged bootstrap (assets/css/bootstrap.min.css)
 * 3. Implementasi <picture> + srcset untuk hero.webp di index.html
 */
const fs = require('fs');
const path = require('path');
const cheerio = require('cheerio');

const dir = 'c:\\wisata-gm';

function findHtmlFiles(d) {
    let results = [];
    const list = fs.readdirSync(d);
    list.forEach(file => {
        if (['node_modules', '.git'].includes(file)) return;
        const full = path.join(d, file);
        if (fs.statSync(full).isDirectory()) {
            results = results.concat(findHtmlFiles(full));
        } else if (full.endsWith('.html')) {
            results.push(full);
        }
    });
    return results;
}

const BOOTSTRAP_CDN = 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css';
const htmlFiles = findHtmlFiles(dir);
let filesChanged = 0;

htmlFiles.forEach(file => {
    const relativePath = path.relative(dir, file).replace(/\\/g, '/');
    // Determine path depth for relative URL
    const depth = relativePath.split('/').length - 1;
    const prefix = depth === 0 ? 'assets/css/bootstrap.min.css' : '../assets/css/bootstrap.min.css';

    let content = fs.readFileSync(file, 'utf-8');
    const $ = cheerio.load(content, { decodeEntities: false });
    let changed = false;

    // Task 1+2: Replace Bootstrap CDN blocking link with local non-blocking
    $('link').each((i, el) => {
        const href = $(el).attr('href') || '';
        if (href.includes('bootstrap@5.3.0/dist/css/bootstrap.min.css')) {
            const rel = $(el).attr('rel');
            // Skip if already preload (already converted)
            if (rel === 'preload') {
                // Just update href to local
                $(el).attr('href', prefix);
                changed = true;
                return;
            }
            // Replace blocking link with preload + noscript pattern
            $(el).replaceWith(
                `<link href="${prefix}" rel="preload" as="style" onload="this.onload=null;this.rel='stylesheet'">\n    <noscript><link rel="stylesheet" href="${prefix}"></noscript>`
            );
            changed = true;
        }
    });

    // Task 3: Add <picture> element for hero in index.html only
    if (relativePath === 'index.html') {
        const heroImg = $('img.hero-bg-img');
        if (heroImg.length > 0 && !$(heroImg).parent().is('picture')) {
            const imgOuterHtml = $.html(heroImg);
            $(heroImg).replaceWith(
                `<picture>\n      <source media="(max-width: 768px)" srcset="assets/images/hero-mobile.webp" type="image/webp">\n      ${imgOuterHtml}\n    </picture>`
            );
            changed = true;
            console.log('Added <picture> srcset to', file);
        }
    }

    if (changed) {
        fs.writeFileSync(file, $.html(), 'utf-8');
        filesChanged++;
        console.log('Updated:', relativePath);
    }
});

console.log(`\nDone! ${filesChanged} files updated.`);

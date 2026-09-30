const fs = require('fs');
const path = require('path');
const cheerio = require('cheerio');

const dir = 'c:\\wisata-gm';

// Files to check globally for domain replacement
function getFiles(d) {
    let results = [];
    const list = fs.readdirSync(d);
    list.forEach(file => {
        if (['node_modules', '.git', 'scratch', 'assets'].includes(file)) return;
        const full = path.join(d, file);
        if (fs.statSync(full).isDirectory()) {
            results = results.concat(getFiles(full));
        } else if (file.endsWith('.html') || file.endsWith('.xml') || file.endsWith('.txt') || file.endsWith('.json')) {
            results.push(full);
        }
    });
    return results;
}

const allFiles = getFiles(dir);

const ogImageMap = {
    'index.html': 'assets/images/hero.webp',
    'about.html': 'assets/images/hero-bg-tentang-kami.webp',
    'blog.html': 'assets/images/hero-bg-blog.webp',
    'layanan.html': 'assets/images/hero-bg-layanan.webp',
    'paket.html': 'assets/images/hero-bg-paket.webp',
    'galeri.html': 'assets/images/hero-bg-galeri.webp',
    'blog/artikel-1.html': 'assets/images/blog/blog1_11zon.webp',
    'blog/artikel-2.html': 'assets/images/blog/blog2_11zon.webp',
    'blog/artikel-3.html': 'assets/images/blog/blog3.webp',
    'paket/adventure.html': 'assets/images/paket/paket-adventure.webp',
    'paket/corporate.html': 'assets/images/paket/paket-corporate.webp',
    'paket/keluarga.html': 'assets/images/paket/paket-keluarga.webp',
    'paket/pelajar.html': 'assets/images/paket/paket-pelajar.webp',
    'paket/rafting-outbound.html': 'assets/images/paket/paket-rafting-outbound.webp',
    'paket/reguler.html': 'assets/images/paket/paket-reguler.webp'
};

let filesChanged = 0;
let fixesCount = 0;

allFiles.forEach(file => {
    const relativePath = path.relative(dir, file).replace(/\\/g, '/');
    let content = fs.readFileSync(file, 'utf-8');
    let origContent = content;

    // 1. Global domain replacement (raftingbatu.com -> rafting.web.id)
    if (content.includes('raftingbatu.com')) {
        content = content.replace(/raftingbatu\.com/g, 'rafting.web.id');
        fixesCount++;
    }

    if (file.endsWith('.html')) {
        const $ = cheerio.load(content, { decodeEntities: false });
        let htmlChanged = false;

        // 4. Fix artikel-1.html title and description
        if (relativePath === 'blog/artikel-1.html') {
            const oldTitle = $('title').text();
            if (oldTitle.includes('Team Building') || oldTitle !== 'Tips Persiapan Rafting di Batu untuk Pemula - RaftingBatu') {
                $('title').text('Tips Persiapan Rafting di Batu untuk Pemula - RaftingBatu');
                htmlChanged = true;
                fixesCount++;
            }
            
            const desc = $('meta[name="description"]').attr('content') || '';
            if (desc.includes('Team Building')) {
                $('meta[name="description"]').attr('content', 'Panduan lengkap persiapan rafting untuk pemula di Batu Malang. Tips aman, pakaian yang tepat, dan apa saja yang perlu disiapkan.');
                htmlChanged = true;
                fixesCount++;
            }
        }

        // 5. Fix alt texts
        if (relativePath === 'blog/artikel-2.html') {
            $('img').each((i, el) => {
                if ($(el).attr('src') && $(el).attr('src').includes('blog2_11zon.webp')) {
                    if ($(el).attr('alt') === 'Tips Persiapan Rafting') {
                        $(el).attr('alt', 'Manfaat Arung Jeram untuk Team Building Perusahaan');
                        htmlChanged = true;
                        fixesCount++;
                    }
                }
            });
        } else if (relativePath === 'blog.html') {
            $('img').each((i, el) => {
                if ($(el).attr('src') && $(el).attr('src').includes('blog1_11zon.webp')) {
                    if ($(el).attr('alt') === 'Rekomendasi Tempat Rafting di Batu') {
                        $(el).attr('alt', 'Tips Persiapan Rafting di Batu untuk Pemula');
                        htmlChanged = true;
                        fixesCount++;
                    }
                }
            });
        }

        // 3. Complete missing meta tags
        const isBlog = relativePath.startsWith('blog/artikel-');
        const isPaket = relativePath.startsWith('paket/');
        
        if (isBlog || isPaket) {
            const head = $('head');
            
            // Check og:title
            if ($('meta[property="og:title"]').length === 0) {
                head.append(`\n    <meta content="${$('title').text()}" property="og:title" />`);
                htmlChanged = true;
                fixesCount++;
            } else {
                $('meta[property="og:title"]').attr('content', $('title').text());
            }

            // Check og:description
            if ($('meta[property="og:description"]').length === 0) {
                let desc = $('meta[name="description"]').attr('content') || $('title').text();
                head.append(`\n    <meta content="${desc}" property="og:description" />`);
                htmlChanged = true;
                fixesCount++;
            } else {
                $('meta[property="og:description"]').attr('content', $('meta[name="description"]').attr('content') || $('title').text());
            }

            // Type
            const ogType = isBlog ? 'article' : 'website';
            if ($('meta[property="og:type"]').length === 0) {
                head.append(`\n    <meta content="${ogType}" property="og:type" />`);
                htmlChanged = true;
                fixesCount++;
            }
            
            // Twitter card
            if ($('meta[name="twitter:card"]').length === 0) {
                head.append(`\n    <meta content="summary_large_image" name="twitter:card" />`);
                htmlChanged = true;
                fixesCount++;
            }
        }

        // 2. Fix og:image paths and twitter:image
        if (ogImageMap[relativePath]) {
            const absUrl = 'https://rafting.web.id/' + ogImageMap[relativePath];
            
            if ($('meta[property="og:image"]').length > 0) {
                $('meta[property="og:image"]').attr('content', absUrl);
                htmlChanged = true;
                fixesCount++;
            } else {
                $('head').append(`\n    <meta content="${absUrl}" property="og:image" />`);
                htmlChanged = true;
                fixesCount++;
            }

            if ($('meta[name="twitter:image"]').length > 0) {
                $('meta[name="twitter:image"]').attr('content', absUrl);
                htmlChanged = true;
                fixesCount++;
            } else {
                $('head').append(`\n    <meta content="${absUrl}" name="twitter:image" />`);
                htmlChanged = true;
                fixesCount++;
            }

            // Update JSON-LD in index.html
            if (relativePath === 'index.html') {
                $('script[type="application/ld+json"]').each((i, el) => {
                    try {
                        let json = JSON.parse($(el).html());
                        if (json.image !== absUrl) {
                            json.image = absUrl;
                            $(el).html('\n      ' + JSON.stringify(json, null, 2).split('\n').join('\n      ') + '\n    ');
                            htmlChanged = true;
                            fixesCount++;
                        }
                    } catch (e) {}
                });
            }
        }
        
        if (htmlChanged) {
            content = $.html();
        }
    }

    if (content !== origContent) {
        fs.writeFileSync(file, content, 'utf-8');
        filesChanged++;
    }
});

console.log(`Files changed: ${filesChanged}`);
console.log(`Fixes applied: ${fixesCount}`);

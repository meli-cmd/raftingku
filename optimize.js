const fs = require('fs');
const path = require('path');
const cheerio = require('cheerio');

const dir = 'c:\\wisata-gm';

function findHtmlFiles(d) {
    let results = [];
    const list = fs.readdirSync(d);
    list.forEach(file => {
        if (file === 'node_modules' || file === '.git') return;
        const full = path.join(d, file);
        if (fs.statSync(full).isDirectory()) {
            results = results.concat(findHtmlFiles(full));
        } else if (full.endsWith('.html')) {
            results.push(full);
        }
    });
    return results;
}

const htmlFiles = findHtmlFiles(dir);

const dimensions = {
    'logo.webp': {w: 200, h: 200},
    'favicon.webp': {w: 200, h: 200},
    'profil-penulis.webp': {w: 100, h: 100},
    'testimoni-1.webp': {w: 100, h: 100},
    'testimoni-2.webp': {w: 100, h: 100},
    'testimoni-3.webp': {w: 100, h: 100},
    'testimoni-4.webp': {w: 100, h: 100},
    'hero.webp': {w: 1200, h: 896},
    'cta-bg.webp': {w: 1200, h: 896},
    'hero-bg-layanan.webp': {w: 1200, h: 896},
    'tentang-kami.webp': {w: 800, h: 597},
    'tentang-kami2.webp': {w: 800, h: 597},
    'layanan.webp': {w: 800, h: 597},
    'layanan2.webp': {w: 800, h: 597},
    'layanan3.webp': {w: 800, h: 597},
    'hero-bg-paket.webp': {w: 800, h: 597},
    'hero-bg-tentang-kami.webp': {w: 800, h: 597},
    'hero-bg-blog.webp': {w: 800, h: 597},
    'hero-bg-galeri.webp': {w: 800, h: 597},
    'galeri1.webp': {w: 800, h: 600},
    'rafting-action.webp': {w: 800, h: 450},
    'blog3.webp': {w: 800, h: 450},
    'blog1_11zon.webp': {w: 800, h: 532},
    'blog2_11zon.webp': {w: 800, h: 449},
    'brush.webp': {w: 876, h: 227}
};

function getDimensions(src) {
    const filename = path.basename(src);
    if (dimensions[filename]) return dimensions[filename];
    if (src.includes('/paket/') || src.includes('/galeri/')) {
        return {w: 800, h: 597};
    }
    return null;
}

const deferCss = [
    'bootstrap-icons.css',
    'aos.css',
    'swiper-bundle.min.css'
];

htmlFiles.forEach(file => {
    let content = fs.readFileSync(file, 'utf-8');
    const $ = cheerio.load(content, { decodeEntities: false });

    // 1. Hero Image
    let heroSrc = null;
    $('[style*="background-image"]').each((i, el) => {
        const style = $(el).attr('style');
        const match = style.match(/background-image:\s*url\((['"]?)(.*?)\1\)/i);
        if (match && match[2].includes('hero')) { // assume hero images have 'hero' or are on header
            heroSrc = match[2];
            let newStyle = style.replace(/background-image:\s*url\((['"]?)(.*?)\1\);?/i, '');
            if (newStyle.trim() === '') {
                $(el).removeAttr('style');
            } else {
                $(el).attr('style', newStyle);
            }
            $(el).addClass('position-relative'); // ensure container is relative
            // remove overflow-hidden if it breaks something, but let's just make it relative
            // The overlay or content needs z-index. The existing hero-content usually has it.
            // insert image at the beginning
            const img = `<img src="${heroSrc}" class="hero-bg-img" fetchpriority="high" alt="Hero Background" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; z-index: 0; pointer-events: none;">`;
            $(el).prepend(img);
            
            // make sure children that are containers have relative + z-index
            $(el).children('.container, .hero-content').each((j, child) => {
                $(child).addClass('position-relative');
                if(!$(child).attr('style') || !$(child).attr('style').includes('z-index')) {
                     // Add z-index: 1 to ensure it's above the image
                     let cStyle = $(child).attr('style') || '';
                     $(child).attr('style', (cStyle + '; z-index: 1;').replace(/^;\s*/, ''));
                }
            });
        }
    });

    if (heroSrc) {
        // Preload
        $('head').append(`\n    <link rel="preload" as="image" href="${heroSrc}">`);
    }

    // 2. Add width and height
    $('img').each((i, el) => {
        const src = $(el).attr('src');
        if (src) {
            const dims = getDimensions(src);
            if (dims) {
                if (!$(el).attr('width')) $(el).attr('width', dims.w);
                if (!$(el).attr('height')) $(el).attr('height', dims.h);
            }
        }
    });

    // 3. Lazy Load
    $('img').each((i, el) => {
        const src = $(el).attr('src');
        // don't lazy load logo or hero images
        if (src && !src.includes('logo') && !$(el).hasClass('hero-bg-img')) {
            $(el).attr('loading', 'lazy');
        }
    });

    // 4. Defer CSS
    $('link[rel="stylesheet"]').each((i, el) => {
        const href = $(el).attr('href');
        if (href && deferCss.some(css => href.includes(css))) {
            $(el).attr('rel', 'preload');
            $(el).attr('as', 'style');
            $(el).attr('onload', "this.onload=null;this.rel='stylesheet'");
            $(el).after(`\n    <noscript><link rel="stylesheet" href="${href}"></noscript>`);
        }
    });

    // 5. Accessibility
    // Wrap main content in <main> if not already
    if ($('main').length === 0) {
        // Find everything between nav/header and footer
        const $nav = $('nav, header.hero-section');
        const $footer = $('footer');
        
        let $elementsToWrap = $();
        if ($nav.length > 0 && $footer.length > 0) {
            // Get last nav/header
            const lastHeader = $nav.last()[0];
            const footer = $footer.first()[0];
            
            // All top-level children of body between lastHeader and footer
            let current = lastHeader.nextSibling;
            while (current && current !== footer) {
                // if it's a section or div that isn't a script/modal
                if (current.nodeType === 1 && current.tagName !== 'SCRIPT' && current.tagName !== 'STYLE' && current.tagName !== 'NOSCRIPT') {
                     $elementsToWrap = $elementsToWrap.add(current);
                }
                current = current.nextSibling;
            }
        } else if ($('section').length > 0) {
            $elementsToWrap = $('section');
        }

        if ($elementsToWrap.length > 0) {
            $elementsToWrap.wrapAll('<main id="main-content"></main>');
        }
    }

    // Fix heading order - skipped complex auto-fix, just check or do simple H1 check.
    // Usually only 1 H1. We'll leave heading check for manual review or just ensure H1 exists.
    
    // Icon-only links aria-label
    $('a').each((i, el) => {
        const text = $(el).text().trim();
        const hasIcon = $(el).find('i, svg').length > 0;
        const hasAria = $(el).attr('aria-label');
        if (text === '' && hasIcon && !hasAria) {
            // give it an aria-label based on icon class or href
            let href = $(el).attr('href') || '';
            let label = 'Link';
            if (href.includes('whatsapp') || href.includes('wa.me')) label = 'Chat WhatsApp';
            else if (href.includes('instagram')) label = 'Instagram';
            else if (href.includes('facebook')) label = 'Facebook';
            else if (href.includes('tiktok')) label = 'TikTok';
            else if (href.includes('youtube')) label = 'YouTube';
            else if (href === '#') label = 'Button';
            $(el).attr('aria-label', label);
        }
    });

    fs.writeFileSync(file, $.html());
    console.log('Processed', file);
});

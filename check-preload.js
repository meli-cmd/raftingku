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

let errors = [];
htmlFiles.forEach(file => {
    let content = fs.readFileSync(file, 'utf-8');
    const $ = cheerio.load(content, { decodeEntities: false });
    
    const preload = $('link[rel="preload"][as="image"]').attr('href');
    const heroImg = $('.hero-bg-img').attr('src');
    
    if (heroImg && preload !== heroImg) {
        errors.push(`Mismatch in ${file}:\n Preload: ${preload}\n Img Src: ${heroImg}`);
    } else if (heroImg && preload === heroImg) {
        console.log(`Match in ${file}: ${preload}`);
    } else if (!heroImg) {
        console.log(`No hero-bg-img found in ${file}`);
    }
});

if (errors.length > 0) {
    console.error("ERRORS FOUND:");
    console.error(errors.join('\n'));
} else {
    console.log("All preload tags match their hero-bg-img srcs.");
}

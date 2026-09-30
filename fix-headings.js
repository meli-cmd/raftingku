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

htmlFiles.forEach(file => {
    let content = fs.readFileSync(file, 'utf-8');
    const $ = cheerio.load(content, { decodeEntities: false });

    // Ensure we start with H1 at the top of the body
    let currentLevel = 0; 
    let changed = false;

    // We select all headings
    $(':header').each((i, el) => {
        const tag = el.tagName.toLowerCase();
        const level = parseInt(tag.charAt(1));

        if (currentLevel === 0) {
            // First heading should be H1. If not, we don't necessarily change it if it's supposed to be H1 but it's not.
            // Usually first is H1.
            currentLevel = level;
            return;
        }

        // If the level jumped by more than 1
        if (level > currentLevel + 1) {
            const newLevel = currentLevel + 1;
            const newTag = `h${newLevel}`;
            
            // Keep original styling by adding the old heading class if it doesn't have it
            let cls = $(el).attr('class') || '';
            if (!cls.includes(`fs-`) && !cls.includes(`h${level}`)) {
                cls += ` h${level}`;
            }
            
            // Create a new element with the new tag
            const newEl = $(`<${newTag}>`).html($(el).html());
            if (cls.trim()) newEl.attr('class', cls.trim());
            
            // Copy other attributes
            Array.from(el.attributes).forEach(attr => {
                if (attr.name !== 'class') {
                    newEl.attr(attr.name, attr.value);
                }
            });

            $(el).replaceWith(newEl);
            changed = true;
            currentLevel = newLevel; // update to the actual level we just wrote
        } else {
            currentLevel = level;
        }
    });

    if (changed) {
        fs.writeFileSync(file, $.html());
        console.log('Fixed headings in', file);
    }
});

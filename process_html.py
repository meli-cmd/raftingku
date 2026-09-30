import os, re
from PIL import Image

def process_html(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if not file.endswith('.html'): continue
            fpath = os.path.join(root, file)
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()

            # 1. Add Google Fonts to head
            if 'fonts.googleapis.com' not in content:
                fonts_link = '<link rel="preconnect" href="https://fonts.googleapis.com">\n    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600&display=swap" rel="stylesheet">\n    <link href="assets/css/style.css"'
                content = content.replace('<link href="assets/css/style.css"', fonts_link)

            # 2. Update images
            def repl_img(match):
                img_tag = match.group(0)
                
                # add loading lazy
                src_match = re.search(r'src=["\']([^"\']+)["\']', img_tag)
                if not src_match: return img_tag
                src = src_match.group(1)
                
                is_hero = 'hero' in src.lower() or 'logo' in src.lower()
                if not is_hero and 'loading=' not in img_tag:
                    img_tag = img_tag.replace('<img ', '<img loading="lazy" ')
                
                # add width and height
                if src.startswith('assets/images') and src.endswith('.webp'):
                    # relative path to root dir
                    img_path = os.path.join(path, src)
                    if os.path.exists(img_path) and 'width=' not in img_tag:
                        try:
                            with Image.open(img_path) as img:
                                w, h = img.size
                                img_tag = img_tag.replace('<img ', f'<img width="{w}" height="{h}" ')
                        except Exception as e:
                            pass
                return img_tag
                
            content = re.sub(r'<img[^>]+>', repl_img, content)
            
            # 3. Add aria-labels
            content = content.replace('<button\n          class="navbar-toggler', '<button aria-label="Toggle navigation"\n          class="navbar-toggler')
            content = content.replace('<button class="navbar-toggler"', '<button aria-label="Toggle navigation" class="navbar-toggler"')
            content = content.replace('class="swiper-button-prev', 'aria-label="Previous slide" class="swiper-button-prev')
            content = content.replace('class="swiper-button-next', 'aria-label="Next slide" class="swiper-button-next')

            # 4. Heading structure (h6 used as pre-titles)
            # Find h6 tags that are pre-titles and convert to div or p
            content = re.sub(r'<h6([^>]*)>(.*?)</h6>', r'<div\1 style="font-size: 1rem;">\2</div>', content, flags=re.DOTALL)
            
            # 5. Script defer
            content = re.sub(r'<script src=([^>]+)></script>', r'<script src=\1 defer></script>', content)
            content = content.replace(' defer defer', ' defer')
            
            # Remove swiper if not used in this file
            if 'swiper' not in content.lower().replace('swiper-bundle', ''):
                content = re.sub(r'<link[^>]+swiper-bundle\.min\.css[^>]*>', '', content)
                content = re.sub(r'<script[^>]+swiper-bundle\.min\.js[^>]*></script>', '', content)
                
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print('Processed', fpath)

if __name__ == '__main__':
    process_html('.')

import os
import glob
from bs4 import BeautifulSoup

links = {
    'bi-facebook': 'https://www.facebook.com/share/1KJWWZq6Ln/',
    'bi-threads': 'https://www.threads.com/@baturafting_id',
    'bi-instagram': 'https://www.instagram.com/baturafting_id',
    'bi-tiktok': 'https://www.tiktok.com/@baturafting.id'
}

for filepath in glob.glob(r"c:\wisata-gm\**\*.html", recursive=True):
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
    modified = False
    
    # Find all social icon divs by checking if class contains d-flex gap-3 mt-4
    for div in soup.find_all('div'):
        classes = div.get('class', [])
        if 'd-flex' in classes and 'gap-3' in classes and 'mt-4' in classes:
            for a in div.find_all('a'):
                i_tag = a.find('i')
                if not i_tag:
                    continue
                i_classes = i_tag.get('class', [])
                
                # Check which icon it is and update the link
                for icon, url in links.items():
                    if icon in i_classes:
                        # update href if it doesn't match
                        if a.get('href') != url:
                            a['href'] = url
                            a['target'] = '_blank'
                            a['rel'] = 'noopener noreferrer'
                            modified = True
                        break
                        
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Updated {filepath}")

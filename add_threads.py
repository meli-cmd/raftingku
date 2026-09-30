import os
import glob
from bs4 import BeautifulSoup

for filepath in glob.glob(r"c:\wisata-gm\**\*.html", recursive=True):
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
    modified = False
    
    # Find all social icon divs by checking if class contains d-flex gap-3 mt-4
    for div in soup.find_all('div'):
        classes = div.get('class', [])
        if 'd-flex' in classes and 'gap-3' in classes and 'mt-4' in classes:
            # check if it contains a tiktok or instagram icon to be sure
            has_social = False
            for i in div.find_all('i'):
                if 'bi-instagram' in i.get('class', []) or 'bi-tiktok' in i.get('class', []):
                    has_social = True
                    break
            
            if not has_social:
                continue

            # check if bi-threads is already there
            has_threads = False
            for i in div.find_all('i'):
                if 'bi-threads' in i.get('class', []):
                    has_threads = True
                    break
            
            if not has_threads:
                # <a class="fs-4 hover-lift" href="#"><i class="bi bi-threads"></i></a>
                new_a = soup.new_tag('a', href='#', attrs={'class': 'fs-4 hover-lift'})
                new_i = soup.new_tag('i', attrs={'class': 'bi bi-threads'})
                new_a.append(new_i)
                div.append(new_a)
                modified = True
            
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Updated {filepath}")

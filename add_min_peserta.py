import os
from bs4 import BeautifulSoup

min_peserta = {
    'Paket Reguler': 'Min. 2 orang',
    'Paket Keluarga': 'Min. 3 orang',
    'Paket Pelajar/Rombongan': 'Min. 20 orang',
    'Paket Corporate/Outing': 'Min. 15 orang',
    'Paket Adventure': 'Min. 4 orang',
    'Rafting + Outbound': 'Min. 8 orang',
    'Paket Rafting + Outbound': 'Min. 8 orang'
}

for filename in ['index.html', 'paket.html']:
    filepath = os.path.join(r"c:\wisata-gm", filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
    modified = False
    
    # Find all h4 inside .card-body that might contain the package title
    for card in soup.find_all(class_='card-body'):
        h4 = card.find('h4')
        if not h4:
            continue
            
        a = h4.find('a')
        title = a.text.strip() if a else h4.text.strip()
        
        if title in min_peserta:
            ul = card.find('ul')
            if ul:
                # Check if it already has Min. X orang
                already_has = False
                for li in ul.find_all('li'):
                    if 'Min.' in li.text:
                        already_has = True
                        break
                
                if not already_has:
                    new_li = soup.new_tag('li')
                    new_li.string = min_peserta[title]
                    ul.insert(0, new_li)
                    modified = True
                    
            # Fix Pelajar desc
            if title == 'Paket Pelajar/Rombongan':
                p = card.find('p', class_='text-muted fs-6 mb-2')
                if p and 'min. 20 peserta' in p.text:
                    p.string = p.text.replace(', min. 20 peserta', '').replace('min. 20 peserta', '')
                    modified = True

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Updated {filename}")

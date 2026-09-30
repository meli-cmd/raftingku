import os
from PIL import Image

def process_images(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if not file.endswith('.webp'):
                continue
            fpath = os.path.join(root, file)
            try:
                with Image.open(fpath) as img:
                    orig_width, orig_height = img.size
                    new_width, new_height = orig_width, orig_height
                    
                    # Determine new size based on folder/name
                    if 'favicon' in file.lower() or 'logo' in file.lower():
                        new_width, new_height = 200, 200
                    elif 'testimoni' in file.lower() or 'profil' in file.lower():
                        new_width, new_height = 100, 100
                    elif 'galeri' in fpath.lower() or 'paket' in fpath.lower() or 'blog' in fpath.lower():
                        new_width, new_height = 800, int(800 * (orig_height / orig_width))
                    elif 'tentang-kami' in file.lower() or 'layanan' in file.lower() and 'hero' not in file.lower():
                        new_width, new_height = 800, int(800 * (orig_height / orig_width))
                    else:
                        # For hero or backgrounds, limit to 1200 max width just in case
                        if orig_width > 1200:
                            new_width, new_height = 1200, int(1200 * (orig_height / orig_width))
                            
                    # Only resize if new size is smaller
                    if new_width < orig_width:
                        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                        
                    # Save with quality 75
                    img.save(fpath, 'webp', quality=75, method=6)
                    print(f'Processed {fpath}: {orig_width}x{orig_height} -> {new_width}x{new_height}')
            except Exception as e:
                print(f'Error processing {fpath}: {e}')

if __name__ == '__main__':
    process_images('assets/images')

from PIL import Image
import os

src = "c:/wisata-gm/assets/images/brush.webp"
img = Image.open(src)
if img.mode not in ('RGB', 'RGBA'):
    img = img.convert('RGBA')

# It's 113KB, resize it to 50%
w, h = img.size
img = img.resize((int(w*0.5), int(h*0.5)), Image.LANCZOS)
img.save(src, format='WEBP', quality=40, method=0)

final_kb = os.path.getsize(src) / 1024
print(f"Done! Final size: {final_kb:.1f} KB")

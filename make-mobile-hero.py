"""
Script untuk membuat versi mobile dari hero.webp menggunakan Pillow.
Resize ke lebar 640px, simpan sebagai hero-mobile.webp dengan kualitas tinggi.
"""
from PIL import Image
import os

input_path = r"c:\wisata-gm\assets\images\hero.webp"
output_path = r"c:\wisata-gm\assets\images\hero-mobile.webp"

with Image.open(input_path) as img:
    orig_w, orig_h = img.size
    print(f"Original: {orig_w}x{orig_h}")
    
    target_w = 640
    ratio = target_w / orig_w
    target_h = int(orig_h * ratio)
    
    img_resized = img.resize((target_w, target_h), Image.LANCZOS)
    img_resized.save(output_path, "WEBP", quality=82, method=6)
    
    orig_size = os.path.getsize(input_path)
    new_size = os.path.getsize(output_path)
    print(f"Mobile: {target_w}x{target_h}")
    print(f"Original size: {orig_size/1024:.1f} KB")
    print(f"Mobile size:   {new_size/1024:.1f} KB")
    print(f"Saved: {(1 - new_size/orig_size)*100:.0f}%")
    print("Done! Saved to:", output_path)

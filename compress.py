from PIL import Image
import os

# Files yang perlu dikompresi/konversi
targets = [
    ("c:/wisata-gm/assets/images/cta-bg.jpeg", "c:/wisata-gm/assets/images/cta-bg.webp"),
    ("c:/wisata-gm/assets/images/blog/rafting-action.webp", None),   # in-place
    ("c:/wisata-gm/assets/images/brush.webp", None),                  # in-place
    ("c:/wisata-gm/assets/images/blog/blog3.webp", None),             # in-place
    ("c:/wisata-gm/assets/images/tentang-kami.webp", None),           # in-place
]

def compress_to_webp(src, dst=None, target_kb=88):
    if dst is None:
        dst = src
    img = Image.open(src)
    if img.mode in ('RGBA', 'LA'):
        pass  # keep alpha
    elif img.mode != 'RGB':
        img = img.convert('RGB')

    target_bytes = target_kb * 1024
    quality = 85
    # Binary search quality
    lo, hi = 10, 85
    best_quality = lo
    import io
    while lo <= hi:
        mid = (lo + hi) // 2
        buf = io.BytesIO()
        img.save(buf, format='WEBP', quality=mid, method=6)
        size = buf.tell()
        if size <= target_bytes:
            best_quality = mid
            lo = mid + 1
        else:
            hi = mid - 1

    img.save(dst, format='WEBP', quality=best_quality, method=6)
    final_kb = os.path.getsize(dst) / 1024
    print(f"  -> Saved '{os.path.basename(dst)}' at quality={best_quality}, size={final_kb:.1f} KB")
    return dst

print("Starting compression...")
for src, dst in targets:
    orig_kb = os.path.getsize(src) / 1024
    print(f"\n[{os.path.basename(src)}] Original: {orig_kb:.1f} KB")
    result_path = compress_to_webp(src, dst)

# If cta-bg.jpeg was converted to webp, delete the original jpeg
old_jpeg = "c:/wisata-gm/assets/images/cta-bg.jpeg"
if os.path.exists("c:/wisata-gm/assets/images/cta-bg.webp") and os.path.exists(old_jpeg):
    os.remove(old_jpeg)
    print(f"\nDeleted original: cta-bg.jpeg")
    print("NOTE: Update HTML references from 'cta-bg.jpeg' to 'cta-bg.webp'")

print("\nDone!")

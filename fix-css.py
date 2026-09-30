with open('c:/wisata-gm/assets/css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace single line border radius
text = text.replace('    .cta-section { border-radius: 20px; }\n', '')

# Replace block border radius
search_block = '''    .cta-section {
        border-radius: 20px;
        padding: 1.5rem !important;
    }'''
replacement_block = '''    .cta-section {
        padding: 1.5rem !important;
    }'''
text = text.replace(search_block, replacement_block)

with open('c:/wisata-gm/assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated style.css!")

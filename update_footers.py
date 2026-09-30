import glob
import os

html_files = glob.glob('c:/wisata-gm/*.html')

new_footer_html = '''          <div class="col-lg-2 mb-4 text-lg-start">
            <h5 class="fw-bold mb-4">Menu Cepat</h5>
            <ul class="list-unstyled d-flex flex-column gap-1" style="color: rgba(255, 255, 255, 0.7)">
              <li><a href="/">Beranda</a></li>
              <li><a href="/about">Tentang Kami</a></li>
              <li><a href="/layanan">Layanan</a></li>
              <li><a href="/paket">Paket</a></li>
              <li><a href="/galeri">Galeri</a></li>
              <li><a href="/blog">Blog</a></li>
            </ul>
          </div>
          <div class="col-lg-4 mb-4 text-lg-start offset-lg-3">
            <h5 class="fw-bold mb-4">Kontak Kami</h5>
            <ul class="list-unstyled d-flex flex-column gap-3" style="color: rgba(255, 255, 255, 0.7)">
              <li class="d-flex align-items-start justify-content-lg-start">
                <i class="bi bi-geo-alt text-success me-3 mt-1 fs-5"></i>
                <span>Jl. Ringroad Utara No. 88, Malang</span>
              </li>
              <li class="d-flex align-items-center justify-content-lg-start">
                <i class="bi bi-telephone text-success me-3 fs-5"></i>
                <span>0822-1122-1909</span>
              </li>
              <li class="d-flex align-items-center justify-content-lg-start">
                <i class="bi bi-clock text-success me-3 fs-5"></i>
                <span>Buka Setiap Hari: 07.00 - 17.00 WIB</span>
              </li>
            </ul>
          </div>
        </div>
        
        <hr class="mb-4" style="border-color: rgba(255, 255, 255, 0.1)" />
        
        <div class="network-section mb-4 text-start">
          <h6 class="fw-bold text-uppercase mb-4" style="color: #f39c12; letter-spacing: 1px; font-size: 0.85rem;">Network</h6>
          <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-lg-5 g-3" style="font-size: 0.85rem; color: rgba(255, 255, 255, 0.7);">
            <div class="col"><a href="https://provideroutbound.web.id" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='inherit'"><span style="color: #f39c12; margin-right: 5px; font-weight: bold;">&gt;</span>provideroutbound.web.id</a></div>
            <div class="col"><a href="https://outboundbatumalang.web.id" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='inherit'"><span style="color: #f39c12; margin-right: 5px; font-weight: bold;">&gt;</span>outboundbatumalang.web.id</a></div>
            <div class="col"><a href="https://provideroutboundmalang.web.id" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='inherit'"><span style="color: #f39c12; margin-right: 5px; font-weight: bold;">&gt;</span>provideroutboundmalang.web.id</a></div>
            <div class="col"><a href="https://outboundmalang.web.id" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='inherit'"><span style="color: #f39c12; margin-right: 5px; font-weight: bold;">&gt;</span>outboundmalang.web.id</a></div>
            <div class="col"><a href="https://paketoutboundmalang.web.id" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='inherit'"><span style="color: #f39c12; margin-right: 5px; font-weight: bold;">&gt;</span>paketoutboundmalang.web.id</a></div>
            <div class="col"><a href="https://vendoroutboundmalang.web.id" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='inherit'"><span style="color: #f39c12; margin-right: 5px; font-weight: bold;">&gt;</span>vendoroutboundmalang.web.id</a></div>
            <div class="col"><a href="https://offroad.web.id" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='inherit'"><span style="color: #f39c12; margin-right: 5px; font-weight: bold;">&gt;</span>offroad.web.id</a></div>
            <div class="col"><a href="https://paintball.web.id" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='inherit'"><span style="color: #f39c12; margin-right: 5px; font-weight: bold;">&gt;</span>paintball.web.id</a></div>
            <div class="col"><a href="https://cobantalun.web.id" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='inherit'"><span style="color: #f39c12; margin-right: 5px; font-weight: bold;">&gt;</span>cobantalun.web.id</a></div>
            <div class="col"><a href="https://rafting.web.id" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='inherit'"><span style="color: #f39c12; margin-right: 5px; font-weight: bold;">&gt;</span>rafting.web.id</a></div>
            <div class="col"><a href="https://familygathering.web.id" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='inherit'"><span style="color: #f39c12; margin-right: 5px; font-weight: bold;">&gt;</span>familygathering.web.id</a></div>
            <div class="col"><a href="https://outboundpantai.web.id" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='inherit'"><span style="color: #f39c12; margin-right: 5px; font-weight: bold;">&gt;</span>outboundpantai.web.id</a></div>
            <div class="col"><a href="https://paintballbatumalang.web.id" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='inherit'"><span style="color: #f39c12; margin-right: 5px; font-weight: bold;">&gt;</span>paintballbatumalang.web.id</a></div>
            <div class="col"><a href="https://vendorhampers.web.id" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='inherit'"><span style="color: #f39c12; margin-right: 5px; font-weight: bold;">&gt;</span>vendorhampers.web.id</a></div>
            <div class="col"><a href="https://vendorpaintball.web.id" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='inherit'"><span style="color: #f39c12; margin-right: 5px; font-weight: bold;">&gt;</span>vendorpaintball.web.id</a></div>
            <div class="col"><a href="https://paketoutbound.web.id" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='inherit'"><span style="color: #f39c12; margin-right: 5px; font-weight: bold;">&gt;</span>paketoutbound.web.id</a></div>
            <div class="col"><a href="https://cobanrondo.web.id" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='inherit'"><span style="color: #f39c12; margin-right: 5px; font-weight: bold;">&gt;</span>cobanrondo.web.id</a></div>
            <div class="col"><a href="https://malangtraveler.web.id" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='inherit'"><span style="color: #f39c12; margin-right: 5px; font-weight: bold;">&gt;</span>malangtraveler.web.id</a></div>
            <div class="col"><a href="https://outboundkediri.web.id" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='inherit'"><span style="color: #f39c12; margin-right: 5px; font-weight: bold;">&gt;</span>outboundkediri.web.id</a></div>
            <div class="col"><a href="https://pantaimalangselatan.web.id" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='inherit'"><span style="color: #f39c12; margin-right: 5px; font-weight: bold;">&gt;</span>pantaimalangselatan.web.id</a></div>
            <div class="col"><a href="https://jasaoutboundmalang.web.id" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='inherit'"><span style="color: #f39c12; margin-right: 5px; font-weight: bold;">&gt;</span>jasaoutboundmalang.web.id</a></div>
            <div class="col"><a href="https://vendoroffroad.web.id" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='inherit'"><span style="color: #f39c12; margin-right: 5px; font-weight: bold;">&gt;</span>vendoroffroad.web.id</a></div>
            <div class="col"><a href="https://vendorgathering.web.id" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='inherit'"><span style="color: #f39c12; margin-right: 5px; font-weight: bold;">&gt;</span>vendorgathering.web.id</a></div>
            <div class="col"><a href="https://outboundindonesia.web.id" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='inherit'"><span style="color: #f39c12; margin-right: 5px; font-weight: bold;">&gt;</span>outboundindonesia.web.id</a></div>
            <div class="col"><a href="https://indonesiaoutbound.web.id" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='inherit'"><span style="color: #f39c12; margin-right: 5px; font-weight: bold;">&gt;</span>indonesiaoutbound.web.id</a></div>
            <div class="col"><a href="https://gemilangkatunoutbound.web.id" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='inherit'"><span style="color: #f39c12; margin-right: 5px; font-weight: bold;">&gt;</span>gemilangkatunoutbound.web.id</a></div>
            <div class="col"><a href="https://outboundjatim.web.id" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;" onmouseover="this.style.color='white'" onmouseout="this.style.color='inherit'"><span style="color: #f39c12; margin-right: 5px; font-weight: bold;">&gt;</span>outboundjatim.web.id</a></div>
          </div>
        </div>
        
        <hr class="mb-4" style="border-color: rgba(255, 255, 255, 0.1)" />\n'''

for file in html_files:
    if os.path.basename(file) == 'about.html':
        continue
    print(f"Updating {file}")
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    start_idx = -1
    end_idx = -1
    for i, line in enumerate(lines):
        if '<div class="col-lg-2 mb-4 text-lg-start">' in line:
            start_idx = i
        if '<hr class="mb-4" style="border-color: rgba(255, 255, 255, 0.1)" />' in line and start_idx != -1:
            end_idx = i + 1
            break
            
    if start_idx != -1 and end_idx != -1:
        lines[start_idx:end_idx] = [new_footer_html]
        with open(file, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        print(f"Success for {file}")
    else:
        print(f"Skipped {file} (footer not found)")

import re

with open('c:/wisata-gm/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# I will find the part after the last card
search_str = '''                        </div>
                    </div>
                </div>

                    <h4 class="fw-bold mb-3 d-flex align-items-center justify-content-lg-start">'''

replacement_str = '''                        </div>
                    </div>
                </div>

            </div>
            <div class="text-center mt-5">
                <a href="paket.html" class="btn btn-success rounded-pill px-5 py-3 fw-bold">Lihat Semua Paket <i class="bi bi-arrow-right ms-2"></i></a>
            </div>
        </div>
    </section>

    <section id="cta" class="cta-section text-center text-white" data-aos="zoom-in">
        <div class="container position-relative" style="z-index: 1;">
            <h2 class="display-6 fw-bold mb-3">Siap Mewujudkan Gathering Impian?</h2>
            <p class="lead mb-4 mx-auto" style="max-width: 600px;">Dapatkan proposal penawaran harga terbaik dan konsultasi gratis untuk rencana wisata atau acara perusahaan Anda hari ini.</p>
            <a href="https://wa.me/6282211221909" target="_blank" class="btn btn-success btn-lg rounded-pill px-4 px-md-5 py-2 py-md-3 fw-bold text-white shadow-lg">
                <i class="bi bi-whatsapp me-2"></i> Hubungi Spesialis Kami
            </a>
        </div>
    </section>

    <footer class="pt-5 pb-3">
        <div class="container pt-4">
            <div class="row mb-4">
                <div class="col-lg-4 mb-4 text-lg-start">
                    <h4 class="fw-bold mb-3 d-flex align-items-center justify-content-lg-start">'''

if search_str in text:
    new_text = text.replace(search_str, replacement_str)
    with open('c:/wisata-gm/index.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Fixed index.html!")
else:
    print("Could not find the target string in index.html!")

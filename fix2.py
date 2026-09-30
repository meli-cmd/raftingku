import re

with open('c:/wisata-gm/about.html', 'r', encoding='utf-8') as f:
    text = f.read()

search_str = '''                            <h2 class="text-success fw-bolder mb-1">30+</h2>
                            <span class="text-muted fw-bold d-block" style="font-size: 0.85rem;">Pilihan Destinasi</span>
                        </div>
                    <i class="bi bi-quote fs-1 text-success mb-3 d-block"></i>'''

replacement_str = '''                            <h2 class="text-success fw-bolder mb-1">30+</h2>
                            <span class="text-muted fw-bold d-block" style="font-size: 0.85rem;">Pilihan Destinasi</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="cta" class="cta-section text-center text-white" data-aos="zoom-in">
        <div class="container position-relative" style="z-index: 1;">
            <h2 class="display-6 fw-bold mb-3">Siap Mencoba Keseruan Rafting di Batu?</h2>
            <p class="lead mb-4 mx-auto" style="max-width: 680px;">Diskusikan rencana petualangan rafting, gathering, atau liburan keluarga Anda bersama tim RaftingBatu.</p>
            <a href="https://wa.me/6282211221909" target="_blank" class="btn btn-success btn-lg rounded-pill px-4 px-md-5 py-2 py-md-3 fw-bold text-white shadow-lg">
                <i class="bi bi-whatsapp me-2"></i> Konsultasi Gratis
            </a>
        </div>
    </section>

    <section class="py-5 bg-dark text-white position-relative">
        <div class="container py-5 text-center">
            <div class="row justify-content-center">
                <div class="col-lg-8" data-aos="zoom-in">
                    <i class="bi bi-quote fs-1 text-success mb-3 d-block"></i>'''

if search_str in text:
    new_text = text.replace(search_str, replacement_str)
    with open('c:/wisata-gm/about.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Fixed about.html!")
else:
    print("Could not find the target string in about.html!")

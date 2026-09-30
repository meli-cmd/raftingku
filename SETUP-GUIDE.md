# SETUP GUIDE - SEO, AEO, PageSpeed & Floating Buttons

## 1. FAVICON SETUP
File `favicon.svg` sudah dibuat di root folder. Tambahkan ini di `<head>` setiap HTML:

```html
<!-- Favicon -->
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<link rel="apple-touch-icon" href="favicon.svg">
```

## 2. META TAGS (LENGKAP)
Tambahkan setelah `<title>` di setiap file HTML:

```html
<!-- SEO Meta Tags -->
<meta name="description" content="[Deskripsi halaman - max 160 chars]">
<meta name="keywords" content="[keywords dengan koma]">
<meta name="author" content="JogjaExplore">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
<meta name="googlebot" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
<meta name="theme-color" content="#059669">

<!-- Open Graph (untuk social sharing) -->
<meta property="og:type" content="website">
<meta property="og:url" content="[Current URL]">
<meta property="og:title" content="[Page Title]">
<meta property="og:description" content="[Deskripsi singkat]">
<meta property="og:image" content="https://jogjaexplore.com/images/[image].jpg">
<meta property="og:site_name" content="JogjaExplore">
<meta property="og:locale" content="id_ID">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="[Page Title]">
<meta name="twitter:description" content="[Deskripsi]">
<meta name="twitter:image" content="https://jogjaexplore.com/images/[image].jpg">
```

## 3. FLOATING BUTTONS HTML
Tambahkan sebelum `</body>` di setiap file HTML:

```html
<!-- Floating WhatsApp Button -->
<a href="https://wa.me/6281234567890?text=Halo%20saya%20tertarik%20dengan%20paket%20tour%20Anda" 
   class="floating-wa" 
   target="_blank" 
   rel="noopener noreferrer" 
   aria-label="Chat WhatsApp">
   <i class="bi bi-whatsapp"></i>
</a>

<!-- Back to Top Button -->
<a href="#" class="back-to-top" aria-label="Scroll to top">
   <i class="bi bi-arrow-up"></i>
</a>
```

## 4. CSS & JS LINK
Update di `<head>`:

Tambahkan setelah `<link rel="stylesheet" href="style.css">`:
```html
<link rel="stylesheet" href="floating-buttons.css">
```

## 5. SCRIPT UPDATE
Ganti isi `script.js` dengan isi dari `script-updated.js`
- Sudah support floating buttons show/hide
- Sudah support back-to-top smooth scroll

## 6. OPTIMASI PAGESPEED
- ✓ Lazy loading images (tambahkan `loading="lazy"` ke img tags)
- ✓ Use modern image formats (WebP)
- ✓ Font display swap (sudah di CSS)
- ✓ Defer non-critical CSS
- ✓ Async load analytics

Contoh image:
```html
<img src="image.webp" alt="description" loading="lazy" width="800" height="600">
```

## 7. SCHEMA MARKUP (JSON-LD) - untuk AI Overview
Tambahkan sebelum `</head>`:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "JogjaExplore",
  "description": "Event Organizer dan Travel Agency Premium di Yogyakarta",
  "url": "https://jogjaexplore.com",
  "image": "https://jogjaexplore.com/images/logo.jpg",
  "telephone": "+62812-345-67890",
  "email": "hello@jogjaexplore.com",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Jl. Ringroad Utara No. 88",
    "addressLocality": "Yogyakarta",
    "addressRegion": "DI Yogyakarta",
    "postalCode": "55282",
    "addressCountry": "ID"
  },
  "sameAs": [
    "https://www.instagram.com/jogjaexplore",
    "https://www.facebook.com/jogjaexplore"
  ]
}
</script>
```

## FILE YANG SUDAH DIBUAT:
1. ✓ favicon.svg - Icon website
2. ✓ floating-buttons.css - Styling untuk floating buttons
3. ✓ script-updated.js - JavaScript dengan floating buttons logic

## NEXT STEPS:
1. Backup file HTML lama
2. Update semua HTML files dengan meta tags
3. Tambahkan floating buttons HTML di setiap halaman
4. Replace script.js dengan script-updated.js (atau copy isinya)
5. Link floating-buttons.css di <head>
6. Upload favicon.svg

## CHECKLIST:
- [ ] Meta tags di semua halaman (index, blog, artikel-1, artikel-2, artikel-3, about)
- [ ] Favicon linked
- [ ] Floating buttons HTML di semua halaman
- [ ] script-updated.js active
- [ ] floating-buttons.css linked
- [ ] Images dengan loading="lazy"
- [ ] Schema markup (JSON-LD) di halaman utama

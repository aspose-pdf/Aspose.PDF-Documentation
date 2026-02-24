---
title: Mengamankan dan menandatangani PDF dengan Python
linktitle: Mengamankan dan menandatangani PDF
type: docs
weight: 210
url: /id/python-net/securing-and-signing/
description: Bagian ini menjelaskan fitur-fitur penggunaan tanda tangan dan mengamankan dokumen PDF Anda dengan Python
lastmod: "2025-06-23"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tandatangani dokumen PDF dengan Python
Abstract: Bagian ini dari dokumentasi Aspose.PDF untuk Python via .NET memberikan panduan komprehensif tentang mengamankan dan menandatangani dokumen PDF secara programatik. Ini mencakup topik penting termasuk perlindungan sandi, algoritma enkripsi, penerapan dan verifikasi tanda tangan digital, penanganan sertifikat, serta izin dokumen. Pengembang akan mempelajari cara mengimplementasikan berbagai tingkat keamanan untuk melindungi konten sensitif, memastikan integritas dokumen, dan mematuhi standar regulasi. Contoh dan referensi API memungkinkan integrasi cepat fitur keamanan ke dalam aplikasi Python, sehingga memudahkan melindungi alur kerja PDF dengan percaya diri.
---

Bagian ini menjelaskan cara menerapkan tanda tangan digital secara aman pada dokumen PDF menggunakan Python Library. Meskipun istilah tanda tangan elektronik dan tanda tangan digital kadang digunakan secara bergantian, keduanya tidak sama. Tanda tangan digital didukung oleh sebuah [otoritas sertifikat](https://en.wikipedia.org/wiki/Certificate_authority), memberikan segel tepercaya yang melindungi dokumen dari manipulasi. Sebaliknya, tanda tangan elektronik biasanya digunakan untuk menunjukkan niat seseorang menandatangani dokumen, tanpa tingkat validasi keamanan yang sama.

Aspose.PDF mendukung tanda tangan digital:

- PKCS1 dengan algoritma tanda tangan RSA dan digest SHA-1.
- PKCS7 dengan algoritma tanda tangan RSA dan digest SHA-1.
- PKCS7 terpisah dengan algoritma tanda tangan DSA, RSA, dan ECDSA. Algoritma digest yang didukung tergantung pada algoritma tanda tangan.
- Tanda tangan stempel waktu.

Algoritma digest untuk PKCS7 terpisah:

- DSA - SHA-1.
- RSA - SHA-1, SHA-256, SHA-384, SHA-512.
- ECDSA - SHA-256, SHA-384, SHA-512, SHA3-256, SHA3-384, SHA3-512.

Disarankan untuk menghindari tanda tangan digital dengan algoritma digest SHA-1 karena tidak aman.

- [Tandatangani PDF secara digital](/pdf/python-net/digitally-sign-pdf-file/)
- [Atur Hak Istimewa, Enkripsi dan Dekripsi File PDF](/pdf/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)
- [Ekstrak Gambar dan Informasi Tanda Tangan](/pdf/python-net/extract-image-and-signature-information/)
- [Tandatangani Dokumen PDF dari Kartu Pintar](/pdf/python-net/sign-pdf-document-from-smart-card/)

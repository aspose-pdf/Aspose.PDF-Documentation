---
title: Amankan dan Tandatangani File PDF di Python
linktitle: Mengamankan dan menandatangani dalam PDF
type: docs
weight: 210
url: /id/python-net/securing-and-signing/
description: Pelajari cara menandatangani, mengenkripsi, mendekripsi, dan mengamankan file PDF di Python, termasuk tanda tangan digital, kartu pintar, dan izin dokumen.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tandatangani, enkripsi, dekripsi, dan lindungi dokumen PDF di Python
Abstract: Bagian ini menjelaskan cara mengamankan dan menandatangani dokumen PDF menggunakan Aspose.PDF for Python via .NET. Pelajari cara menerapkan tanda tangan digital, menggunakan kartu pintar dan sertifikat, mengekstrak informasi tanda tangan, serta mengelola enkripsi PDF, kata sandi, dan hak akses di Python.
---

Bagian ini menjelaskan cara menerapkan tanda tangan digital secara aman pada dokumen PDF menggunakan Python Library. Meskipun istilah tanda tangan elektronik dan tanda tangan digital kadang-kadang digunakan secara bergantian, keduanya tidak sama. Tanda tangan digital didukung oleh sebuah [otoritas sertifikat](https://en.wikipedia.org/wiki/Certificate_authority), menyediakan segel tepercaya yang melindungi dokumen dari manipulasi. Sebaliknya, tanda tangan elektronik biasanya digunakan untuk menunjukkan niat seseorang menandatangani dokumen, tanpa tingkat validasi keamanan yang sama.

Gunakan panduan ini ketika Anda perlu melindungi konten PDF, mengontrol izin dokumen, memverifikasi kepercayaan, atau menerapkan tanda tangan berbasis sertifikat dalam alur kerja Python.

## Tugas Keamanan dan Penandatanganan yang Dicakup

Aspose.PDF mendukung tanda tangan digital:

- PKCS1 dengan algoritma tanda tangan RSA dan digest SHA-1.
- PKCS7 dengan algoritma tanda tangan RSA dan digest SHA-1.
- PKCS7 terpisah dengan algoritma tanda tangan DSA, RSA, dan ECDSA. Algoritma digest yang didukung tergantung pada algoritma tanda tangan.
- Tanda tangan cap waktu.

Algoritma digest untuk PKCS7 terpisah:

- DSA - SHA-1.
- RSA - SHA-1, SHA-256, SHA-384, SHA-512.
- ECDSA - SHA-256, SHA-384, SHA-512, SHA3-256, SHA3-384, SHA3-512.

Disarankan untuk menghindari tanda tangan digital dengan algoritma digest SHA-1 karena ketidakamanannya.

- [Tandatangani file PDF secara digital](/pdf/id/python-net/digitally-sign-pdf-file/)
- [Atur Hak Istimewa, Enkripsi, dan Dekripsi File PDF](/pdf/id/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)
- [Ekstrak Informasi Gambar dan Tanda Tangan](/pdf/id/python-net/extract-image-and-signature-information/)
- [Tandatangani Dokumen PDF dari Kartu Pintar](/pdf/id/python-net/sign-pdf-document-from-smart-card/)

---
title: Ekstrak Font dari PDF melalui Python
linktitle: Ekstrak Font dari PDF
type: docs
weight: 30
url: /id/python-net/extract-fonts-from-pdf/
description: Gunakan pustaka Aspose.PDF for Python untuk mengekstrak semua font yang tertanam dari dokumen PDF Anda.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara Mengekstrak Font dari PDF menggunakan Python
Abstract: Artikel ini menjelaskan cara memeriksa font yang digunakan dalam dokumen PDF dengan Aspose.PDF for Python. Artikel ini menunjukkan cara membuka PDF dengan kelas Document, memanggil font_utilities.get_all_fonts() untuk mengambil objek font yang tersedia, dan mengiterasi hasilnya untuk membaca nama font untuk analisis, audit, atau alur kerja pemrosesan dokumen.
---

Gunakan [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) untuk membuka PDF dan memanggil `font_utilities.get_all_fonts()` untuk mengambil semua yang tersedia [Font](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/font/) objek yang direferensikan oleh dokumen. Ini berguna saat mengaudit font yang tertanam, memeriksa ketersediaan font sebelum konversi, atau menganalisis sumber daya dokumen.

1. Buka PDF sumber sebagai `Document`.
1. Panggilan `document.font_utilities.get_all_fonts()` untuk mendapatkan koleksi font.
1. Iterasi melalui hasil yang dikembalikan `Font` objek.
1. Baca dan cetak masing-masing `font.font_name` nilai.

```python

    import aspose.pdf as apdf
    from os import path

    path_infile = path.join(self.dataDir, infile)

    # Open PDF document
    document = apdf.Document(path_infile)

    fonts = document.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```

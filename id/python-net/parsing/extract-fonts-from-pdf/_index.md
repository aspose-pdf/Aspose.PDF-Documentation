---
title: Ekstrak Font dari PDF via Python
linktitle: Ekstrak Font dari PDF
type: docs
weight: 30
url: /id/python-net/extract-fonts-from-pdf/
description: Gunakan pustaka Aspose.PDF untuk Python untuk mengekstrak semua font yang disematkan dari dokumen PDF Anda.
lastmod: "2025-03-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara Mengekstrak Font dari PDF menggunakan Python
Abstract: Artikel ini memberikan panduan tentang mengekstrak semua font dari dokumen PDF menggunakan metode khusus dari pustaka Aspose.PDF. Artikel ini memperkenalkan metode `font_utilities.get_all_fonts()` yang tersedia dalam kelas `Document`, yang memudahkan pengambilan informasi font. Artikel ini menyertakan potongan kode Python yang menunjukkan prosesnya, yang melibatkan mengimpor modul yang diperlukan, membuka dokumen PDF, dan iterasi melalui font untuk mencetak nama setiap font. Pendekatan ini berguna bagi pengembang yang perlu menganalisis atau memanipulasi data font dalam file PDF.
---

Jika Anda ingin mendapatkan semua font dari dokumen PDF, Anda dapat menggunakan metode 'font_utilities.get_all_fonts()' yang disediakan dalam kelas Document. Silakan periksa potongan kode berikut untuk mendapatkan semua font dari dokumen PDF yang ada:

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)

    # Open PDF document
    document = apdf.Document(path_infile)

    fonts = document.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```


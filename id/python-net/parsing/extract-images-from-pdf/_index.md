---
title: Ekstrak Gambar dari PDF menggunakan Python
linktitle: Ekstrak Gambar dari PDF
type: docs
weight: 20
url: /id/python-net/extract-images-from-the-pdf-file/
description: Cara mengekstrak bagian gambar dari PDF menggunakan Aspose.PDF untuk Python
lastmod: "2023-03-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara Mengekstrak Gambar dari PDF via Python
Abstract: Artikel ini menyediakan panduan singkat tentang mengekstrak gambar yang tertanam dari dokumen PDF menggunakan Python. Proses ini melibatkan tiga langkah utama – memuat dokumen PDF, mengakses sumber gambar, dan menyimpan gambar ke file. Potongan kode menggunakan pustaka Aspose.PDF untuk memfasilitasi operasi tersebut. Awalnya, dokumen PDF dimuat dari jalur yang ditentukan, dan gambar yang diinginkan diakses dari sumber daya halaman pertama. Akhirnya, gambar disimpan ke file output yang ditentukan menggunakan operasi I/O file, memungkinkan analisis lebih lanjut, penyuntingan, atau penggunaan kembali dalam dokumen lain.
---

Potongan kode ini mengekstrak gambar yang tertanam dari dokumen PDF untuk analisis terpisah, penyuntingan, atau penggunaan kembali dalam dokumen lain:

1. Muat Dokumen PDF
1. Akses Sumber Gambar
1. Simpan Gambar ke File

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    xImage = document.pages[1].resources.images[1]
    with FileIO(path_outfile, "w") as output_image:
        xImage.save(output_image)
```


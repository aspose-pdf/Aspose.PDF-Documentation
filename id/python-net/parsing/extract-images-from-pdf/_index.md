---
title: Ekstrak Gambar dari PDF menggunakan Python
linktitle: Ekstrak Gambar dari PDF
type: docs
weight: 20
url: /id/python-net/extract-images-from-the-pdf-file/
description: Pelajari cara mengekstrak gambar tersemat dari file PDF dengan Aspose.PDF for Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara Mengekstrak Gambar dari PDF via Python
Abstract: Artikel ini menjelaskan cara mengekstrak gambar tersemat dari dokumen PDF dengan Aspose.PDF for Python. Artikel ini mencakup membuka PDF sumber dengan kelas Document, mengakses gambar dari koleksi sumber daya halaman, dan menyimpan XImage yang diekstrak ke file eksternal untuk digunakan kembali, inspeksi, atau pemrosesan lebih lanjut.
---

Gunakan [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) untuk membuka PDF, kemudian mengakses sumber daya halaman untuk mengambil sebuah [XImage](https://reference.aspose.com/pdf/python-net/aspose.pdf/ximage/) objek dan simpan sebagai file terpisah. Pendekatan ini berguna ketika Anda perlu menggunakan ulang gambar, memeriksa aset yang diekstrak, atau membangun alur kerja pemrosesan gambar dari konten PDF.

1. Buka PDF sebagai `Document`.
1. Akses sumber daya gambar dari halaman target.
1. Ambil yang diperlukan `XImage` dari koleksi gambar halaman.
1. Simpan gambar yang diekstrak ke file output.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    xImage = document.pages[1].resources.images[1]
    with FileIO(path_outfile, "w") as output_image:
        xImage.save(output_image)
```

---
title: Konversi PDF/x ke format PDF dalam Python
linktitle: Konversi PDF/x ke format PDF
type: docs
weight: 120
url: /id/python-net/convert-pdf_x-to-pdf/
lastmod: "2025-09-27"
description: Topik ini menunjukkan cara mengonversi PDF/x ke format PDF menggunakan Aspose.PDF untuk Python melalui .NET.
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Cara mengonversi PDF/x ke format PDF
Abstract: Artikel ini memberikan panduan komprehensif tentang mengonversi PDF/UA, dan PDF/A ke file PDF menggunakan Aspose.PDF untuk Python.
---

**Format PDF/x ke PDF berarti kemampuan untuk mengonversi PDF/UA, dan PDF/A ke file PDF.**

## Konversi PDF/A ke PDF

1. Muat dokumen PDF menggunakan 'ap.Document'.
1. Panggil 'remove_pdfa_compliance()' untuk menghapus semua pengaturan kepatuhan dan metadata terkait PDF/A.
1. Simpan PDF yang dihasilkan ke jalur output.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.remove_pdfa_compliance()
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## Menghapus kepatuhan PDF/UA

Fungsi ini menunjukkan proses konversi dua langkah: pertama menghapus kepatuhan PDF/UA (Aksesibilitas Universal), kemudian mengonversi PDF yang dihasilkan ke format PDF/A-1B dengan penandaan otomatis untuk aksesibilitas dan struktur semantik.

1. Muat dokumen PDF menggunakan 'ap.Document()'.
1. Panggil 'document.remove_pdfa_compliance()' untuk menghapus semua pembatasan atau pengaturan kepatuhan PDF/A.
1. Simpan PDF yang dimodifikasi ke 'path_outfile'.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.remove_pdfa_compliance()
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

---
title: Cara Menggabungkan PDF menggunakan Python
linktitle: Gabungkan file PDF
type: docs
weight: 50
url: /id/python-net/merge-pdf-documents/
description: Halaman ini menjelaskan cara menggabungkan dokumen PDF menjadi satu file PDF dengan Python.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gabungkan halaman PDF menggunakan Python
Abstract: Artikel ini membahas kebutuhan umum untuk menggabungkan beberapa file PDF menjadi satu dokumen, proses yang berharga untuk mengatur serta mengoptimalkan penyimpanan dan berbagi konten PDF. Artikel ini mengeksplorasi penggunaan Aspose.PDF untuk Python via .NET guna menggabungkan file PDF secara efisien, dengan mengakui bahwa menggabungkan PDF di Python dapat menjadi tantangan tanpa perpustakaan pihak ketiga. Artikel ini menyediakan panduan langkah demi langkah untuk menggabungkan file PDF – membuat dokumen baru, menggabungkan file-file tersebut, dan menyimpan dokumen yang sudah digabungkan. Sebuah potongan kode menunjukkan implementasi menggunakan Aspose.PDF, menyoroti kemampuan perpustakaan tersebut untuk menyederhanakan proses penggabungan. Selain itu, artikel ini memperkenalkan Aspose.PDF Merger, alat daring untuk menggabungkan PDF, memungkinkan pengguna untuk menjelajahi fungsionalitasnya dalam lingkungan berbasis web.
---

## Menggabungkan atau mengkombinasikan beberapa PDF menjadi satu PDF dalam Python

Penggabungan file PDF adalah pertanyaan yang sangat populer di antara pengguna. Ini dapat berguna ketika Anda memiliki beberapa file PDF yang ingin Anda bagikan atau simpan bersama sebagai satu dokumen.

Menggabungkan file PDF dapat membantu Anda mengatur dokumen, mengosongkan ruang penyimpanan di PC Anda, dan berbagi beberapa file PDF dengan orang lain dengan menggabungkannya menjadi satu dokumen.

Menggabungkan PDF di Python melalui .NET bukan tugas yang mudah tanpa menggunakan perpustakaan pihak ketiga.
Artikel ini menunjukkan cara menggabungkan beberapa file PDF menjadi satu dokumen PDF menggunakan Aspose.PDF untuk Python via .NET.

## Menggabungkan File PDF menggunakan Python dan DOM

Untuk menggabungkan dua file PDF:

1. Buat Dokumen Baru.
1. Gabungkan File PDF
1. Simpan Dokumen yang Digabungkan

Menggabungkan beberapa dokumen PDF menjadi satu file:

```python

    import aspose.pdf as apdf
    import aspose.pydrawing as asdrw
    from io import FileIO
    from os import path

    path_infile1 = path.join(self.dataDir, infile1)
    path_infile2 = path.join(self.dataDir, infile2)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document()
    document.merge(files=[path_infile1, path_infile2])
    document.save(path_outfile)
```

## Contoh Langsung

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) adalah aplikasi web gratis daring yang memungkinkan Anda menyelidiki cara kerja fungsi penggabungan presentasi.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)



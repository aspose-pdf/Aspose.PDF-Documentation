---
title: Tambahkan Bentuk Lingkaran ke PDF dengan Python
linktitle: Tambahkan Lingkaran
type: docs
weight: 20
url: /id/python-net/add-circle/
description: Pelajari cara menggambar dan mengisi bentuk lingkaran dalam file PDF menggunakan Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gambar bentuk lingkaran dalam file PDF menggunakan Python
Abstract: Artikel ini menunjukkan cara menambahkan bentuk lingkaran ke dokumen PDF dengan Aspose.PDF for Python via .NET. Artikel ini mencakup pembuatan lingkaran berbingkai, mengisi lingkaran dengan warna, dan menempatkan teks di dalam objek lingkaran.
---

## Tambahkan objek Lingkaran

Aspose.PDF for Python via .NET memungkinkan Anda menambahkan [Lingkaran](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/circle/) bentuk ke halaman PDF melalui [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) kelas. Gunakan lingkaran untuk diagram, anotasi, dan elemen visual sederhana.

Ikuti langkah-langkah di bawah ini:

1. Buat [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) instansi.
1. Buat [objek Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) dengan dimensi tertentu.
1. Atur [border](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) untuk objek Graph.
1. Tambah [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) objek ke koleksi `paragraphs` halaman.
1. Simpan file PDF kami.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_circle(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 200)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    circle = drawing.Circle(100, 100, 40)
    circle.graph_info.color = ap.Color.green_yellow
    graph.shapes.add(circle)

    page.paragraphs.add(graph)
    document.save(outfile)
```

Lingkaran yang kami gambar akan terlihat seperti ini:

![Menggambar Lingkaran](drawing_circle.png)

## Buat Objek Lingkaran Terisi

Contoh ini menunjukkan cara menambahkan lingkaran dan mengisinya dengan warna.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_circle_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 200)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    circle = drawing.Circle(100, 100, 40)
    circle.graph_info.color = ap.Color.green_yellow
    circle.graph_info.fill_color = ap.Color.green
    circle.text = ap.text.TextFragment("Circle")
    graph.shapes.add(circle)

    page.paragraphs.add(graph)
    document.save(outfile)
```

Hasil penambahan lingkaran berisi:

![Lingkaran Berisi](filled_circle.png)

## Topik Grafik Terkait

- [Bekerja dengan grafik PDF di Python](/pdf/id/python-net/working-with-graphs/)
- [Tambahkan bentuk busur ke PDF dalam Python](/pdf/id/python-net/add-arc/)
- [Tambahkan bentuk elips ke PDF di Python](/pdf/id/python-net/add-ellipse/)
- [Tambahkan bentuk persegi panjang ke PDF di Python](/pdf/id/python-net/add-rectangle/)
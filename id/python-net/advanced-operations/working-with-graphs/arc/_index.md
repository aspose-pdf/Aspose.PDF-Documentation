---
title: Tambahkan Bentuk Arc ke PDF dengan Python
linktitle: Tambahkan Arc
type: docs
weight: 10
url: /id/python-net/add-arc/
description: Pelajari cara menggambar dan mengisi bentuk arc di file PDF dengan Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gambar bentuk arc di file PDF menggunakan Python
Abstract: Artikel ini menunjukkan cara menambahkan bentuk arc ke dokumen PDF dengan Aspose.PDF for Python via .NET. Artikel ini mencakup pembuatan arc berbingkai, menggambar segmen arc terisi, dan menambahkannya ke dalam kontainer Graph.
---

## Tambahkan objek Arc

Aspose.PDF for Python via .NET memungkinkan Anda menambahkan [Arc](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/arc/) bentuk ke halaman PDF menggunakan [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) class. Anda dapat menggambar busur berpinggir dan segmen busur berisi untuk diagram dan ilustrasi teknis.

Ikuti langkah-langkah di bawah ini:

1. Buat [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) instansi.
1. Buat [Objek grafik](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) dengan dimensi tertentu.
1. Atur [batas](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) untuk objek Graph.
1. Buat objek busur yang sesuai.
1. Tambahkan objek ini ke koleksi Shapes dalam objek graph.
1. Tambah [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) objek ke koleksi paragraf halaman.
1. Simpan file PDF kami.

Potongan kode berikut menunjukkan cara menambahkan sebuah [Arc](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/arc/) objek.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_arc(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    arc1 = drawing.Arc(100, 100, 95, 0, 90)
    arc1.graph_info.color = ap.Color.green_yellow
    graph.shapes.add(arc1)

    arc2 = drawing.Arc(100, 100, 90, 70, 180)
    arc2.graph_info.color = ap.Color.dark_blue
    graph.shapes.add(arc2)

    arc3 = drawing.Arc(100, 100, 85, 120, 210)
    arc3.graph_info.color = ap.Color.red
    graph.shapes.add(arc3)

    page.paragraphs.add(graph)
    document.save(outfile)
```

## Buat Objek Busur Terisi

Contoh ini menunjukkan cara menambahkan segmen busur yang terisi dengan warna.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_arc_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    arc = drawing.Arc(100, 100, 95, 0, 90)

    arc.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(arc)

    line = drawing.Line([195, 100, 100, 100, 100, 195])
    line.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(line)

    page.paragraphs.add(graph)
    document.save(outfile)
```

Hasil menambahkan busur berisi:

![Busur Terisi](filled_arc.png)

## Topik Grafik Terkait

- [Bekerja dengan grafik PDF di Python](/pdf/id/python-net/working-with-graphs/)
- [Tambahkan bentuk lingkaran ke PDF di Python](/pdf/id/python-net/add-circle/)
- [Tambahkan bentuk kurva ke PDF di Python](/pdf/id/python-net/add-curve/)
- [Tambahkan bentuk garis ke PDF di Python](/pdf/id/python-net/add-line/)
---
title: Tambahkan Bentuk Kurva ke PDF dengan Python
linktitle: Tambahkan Kurva
type: docs
weight: 30
url: /id/python-net/add-curve/
description: Pelajari cara menggambar dan mengisi bentuk kurva dalam file PDF menggunakan Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gambar bentuk kurva dalam file PDF menggunakan Python
Abstract: Artikel ini menunjukkan cara menambahkan bentuk kurva ke dokumen PDF dengan Aspose.PDF for Python via .NET. Artikel ini mencakup pembuatan kurva berbingkai, mengisi objek kurva, dan merender jalur kurva kustom dalam kontainer Graph.
---

## Tambahkan objek Kurva

Aspose.PDF for Python via .NET memungkinkan Anda menambahkan [Kurva](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/curve/) bentuk ke halaman PDF melalui [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) kelas.

Artikel ini menunjukkan cara membuat kurva berbingkai dan terisi.

Ikuti langkah-langkah di bawah ini:

1. Buat [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) instansi.
1. Buat [Objek grafik](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) dengan dimensi tertentu.
1. Atur [batas](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) untuk objek Graph.
1. Tambah [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) objek ke koleksi paragraf halaman.
1. Simpan file PDF kami.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_curve(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 200)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    curve1 = drawing.Curve([10, 10, 50, 60, 70, 10, 100, 120])
    curve1.graph_info.color = ap.Color.green_yellow
    graph.shapes.add(curve1)

    page.paragraphs.add(graph)
    document.save(outfile)
```

Gambar berikut menunjukkan hasil yang dieksekusi dengan cuplikan kode kami:

![Menggambar Curve](drawing_curve.png)

## Membuat Objek Curve Terisi

Contoh ini menunjukkan cara menambahkan objek Curve yang terisi dengan warna.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing


def add_curve_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 200)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    curve1 = drawing.Curve([10, 10, 50, 60, 70, 10, 100, 120])
    curve1.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(curve1)

    page.paragraphs.add(graph)
    document.save(outfile)
```

Hasil menambahkan kurva terisi:

![Kurva Terisi](filled_curve.png)

## Topik Grafik Terkait

- [Bekerja dengan grafik PDF di Python](/pdf/id/python-net/working-with-graphs/)
- [Tambahkan bentuk busur ke PDF dalam Python](/pdf/id/python-net/add-arc/)
- [Tambahkan bentuk garis ke PDF di Python](/pdf/id/python-net/add-line/)
- [Tambahkan bentuk elips ke PDF di Python](/pdf/id/python-net/add-ellipse/)
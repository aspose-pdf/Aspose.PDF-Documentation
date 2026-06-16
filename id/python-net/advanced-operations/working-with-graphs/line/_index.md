---
title: Tambahkan Bentuk Garis ke PDF dengan Python
linktitle: Tambah Garis
type: docs
weight: 40
url: /id/python-net/add-line/
description: Pelajari cara menggambar bentuk garis dan garis bergaya dalam file PDF menggunakan Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gambar bentuk garis dalam file PDF menggunakan Python
Abstract: Artikel ini menunjukkan cara menambahkan bentuk garis ke dokumen PDF dengan Aspose.PDF for Python via .NET. Artikel ini mencakup pembuatan garis dasar, mengkonfigurasi gaya garis putus-putus, dan menggambar garis di seluruh halaman.
---

## Tambahkan objek Line

Aspose.PDF for Python via .NET memungkinkan Anda menambahkan [Line](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) bentuk ke halaman PDF menggunakan [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) kelas. Anda dapat mengontrol warna garis, pola dash, dan penempatan.

Ikuti langkah-langkah di bawah ini:

1. Buat [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) instansi.
1. Buat Objek Grafik
1. Tambah [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) objek ke koleksi `paragraphs` halaman.
1. Buat dan Konfigurasikan Garis
1. Tambahkan [Line](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) ke Grafik
1. Simpan file PDF kami.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing


def add_line(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(100, 400)
    page.paragraphs.add(graph)

    line = drawing.Line([100, 100, 200, 100])
    line.graph_info.dash_array = [0, 1, 0]
    line.graph_info.dash_phase = 1
    graph.shapes.add(line)

    document.save(outfile)
```

![Tambah Garis](add_line.png)

## Cara menambahkan Garis Dotted Dashed ke dokumen PDF Anda

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_dotted_dashed_line(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(100, 400)
    page.paragraphs.add(graph)

    line = drawing.Line([100, 100, 200, 100])
    line.graph_info.color = ap.Color.red
    line.graph_info.dash_array = [0, 1, 0]
    line.graph_info.dash_phase = 1
    graph.shapes.add(line)

    document.save(outfile)
```

Hasil penambahan garis dotted dashed:

![Garis Putus-putus](dash_line.png)

## Gambar Garis Melintasi Halaman

Anda juga dapat menggambar garis melintasi halaman untuk membentuk sebuah salib.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def draw_line_across_page(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    page.page_info.margin.left = 0
    page.page_info.margin.right = 0
    page.page_info.margin.bottom = 0
    page.page_info.margin.top = 0

    graph = drawing.Graph(page.page_info.width, page.page_info.height)
    line = drawing.Line([page.rect.llx, 0, page.page_info.width, page.rect.ury])
    graph.shapes.add(line)
    line2 = drawing.Line([0, page.rect.ury, page.page_info.width, page.rect.llx])
    graph.shapes.add(line2)
    page.paragraphs.add(graph)

    document.save(outfile)
```

![Menggambar Garis](draw_line.png)

## Topik Grafik Terkait

- [Bekerja dengan grafik PDF di Python](/pdf/id/python-net/working-with-graphs/)
- [Tambahkan bentuk kurva ke PDF di Python](/pdf/id/python-net/add-curve/)
- [Tambahkan bentuk persegi panjang ke PDF di Python](/pdf/id/python-net/add-rectangle/)
- [Periksa batas bentuk dalam grafik PDF dengan Python](/pdf/id/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/)

---
title: Tambahkan Bentuk Persegi Panjang ke PDF dalam Python
linktitle: Tambahkan Persegi Panjang
type: docs
weight: 50
url: /id/python-net/add-rectangle/
description: Pelajari cara menggambar dan mengisi bentuk persegi panjang dalam file PDF menggunakan Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gambar bentuk persegi panjang dalam file PDF menggunakan Python
Abstract: Artikel ini menunjukkan cara menambahkan bentuk persegi panjang ke dokumen PDF dengan Aspose.PDF for Python via .NET. Ini mencakup persegi panjang berbingkai, isian padat dan gradasi, transparansi alfa, dan kontrol Z-order.
---

## Tambahkan objek Rectangle

Aspose.PDF for Python via .NET memungkinkan Anda menambahkan [Persegi panjang](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) bentuk ke halaman PDF melalui [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) kelas. Anda dapat menggambar persegi panjang berbingkai dan menerapkan isian padat, gradasi, atau transparan.

Ikuti langkah-langkah di bawah ini:

1. Buat PDF baru [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Tambah [Halaman](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) ke koleksi halaman file PDF.
1. Tambah [Fragmen teks](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) ke koleksi paragraf dari instance halaman.
1. Buat [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) instansi.
1. Setel batas untuk [Objek grafik](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/).
1. Tambah [Persegi panjang](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) objek ke koleksi bentuk dari objek Graph.
1. Tambahkan objek grafik ke koleksi paragraf dari instance halaman.
1. Tambah [Fragmen teks](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) ke koleksi paragraf dari instance halaman.
1. Dan simpan file PDF Anda

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_rectangle(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    text_fragment = ap.text.TextFragment("Rectangle")
    page.paragraphs.add(text_fragment)

    graph = drawing.Graph(400, 300)
    page.paragraphs.add(graph)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)

    rect = drawing.Rectangle(20, 20, 350, 250)
    graph.shapes.add(rect)
    page.paragraphs.add(text_fragment)

    document.save(outfile)
```

![Buat Persegi Panjang](create_rectangle.png)

## Buat Objek Persegi Panjang Terisi

Aspose.PDF for Python via .NET juga menawarkan fitur untuk mengisi objek persegi panjang dengan warna tertentu.

Potongan kode berikut menunjukkan cara menambahkan sebuah [Persegi panjang](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) objek yang diisi dengan warna.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def create_rectangle_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(100, 400)
    page.paragraphs.add(graph)

    rect = drawing.Rectangle(100, 100, 200, 120)
    rect.graph_info.fill_color = ap.Color.red
    graph.shapes.add(rect)

    document.save(outfile)
```

Hasil dari persegi panjang yang diisi dengan warna solid:

![Persegi Panjang Terisi](fill_rectangle.png)

## Tambahkan Gambar dengan Isian Gradien

Aspose.PDF for Python via .NET mendukung fitur untuk menambahkan objek grafik ke dokumen PDF dan terkadang diperlukan untuk mengisi objek grafik dengan Warna Gradien.

Potongan kode berikut menunjukkan cara menambahkan sebuah [Persegi panjang](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) objek yang diisi dengan Warna Gradien.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_drawing_with_gradient_fill(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    page.paragraphs.add(graph)

    rect = drawing.Rectangle(0, 0, 300, 300)
    gradient_color = ap.Color()
    gradient_settings = drawing.GradientAxialShading(ap.Color.red, ap.Color.blue)
    gradient_settings.start = ap.Point(0, 0)
    gradient_settings.end = ap.Point(350, 350)
    gradient_color.pattern_color_space = gradient_settings
    rect.graph_info.fill_color = gradient_color
    graph.shapes.add(rect)

    document.save(outfile)
```

![Persegi Panjang Gradien](gradient.png)

## Buat Persegi Panjang dengan Saluran Warna Alfa

Aspose.PDF untuk Python via .NET juga mendukung transparansi melalui saluran warna alfa.

Potongan kode berikut menunjukkan cara menambahkan sebuah [Persegi panjang](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) objek dengan nilai alfa.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def create_rectangle_with_alpha_color_channel(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(100, 400)
    page.paragraphs.add(graph)

    rect = drawing.Rectangle(100, 100, 200, 120)
    rect.graph_info.fill_color = ap.Color.from_argb(128, 244, 180, 0)
    graph.shapes.add(rect)

    rect1 = drawing.Rectangle(200, 150, 200, 100)
    rect1.graph_info.fill_color = ap.Color.from_argb(160, 120, 0, 120)
    graph.shapes.add(rect1)

    document.save(outfile)
```

![Warna Saluran Alfa Persegi Panjang](rectangle_color.png)

## Kontrol Z-Order bentuk

Aspose.PDF for .NET mendukung fitur untuk menambahkan objek grafik (misalnya grafik, garis, persegi panjang, dll.) ke dokumen PDF. Saat menambahkan lebih dari satu instance dari objek yang sama dalam file PDF, kami dapat mengontrol render mereka dengan menentukan Z-Order. Z-Order juga digunakan ketika kita perlu merender objek di atas satu sama lain.

Potongan kode berikut menunjukkan langkah-langkah untuk merender [Persegi panjang](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) objek di atas satu sama lain.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing


def _add_rectangle_to_page(
    page: ap.Page,
    x: float,
    y: float,
    width: float,
    height: float,
    color: ap.Color,
    zindex: int,
):
    graph = drawing.Graph(width, height)
    graph.is_change_position = False
    graph.left = x
    graph.top = y
    rect = drawing.Rectangle(0, 0, width, height)
    rect.graph_info.fill_color = color
    rect.graph_info.color = color
    graph.shapes.add(rect)
    graph.z_index = zindex
    page.paragraphs.add(graph)


def control_z_order_of_rectangle(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(375, 300)
    page.page_info.margin.left = 0
    page.page_info.margin.top = 0

    _add_rectangle_to_page(page, 50, 40, 60, 40, ap.Color.red, 2)
    _add_rectangle_to_page(page, 20, 20, 30, 30, ap.Color.blue, 1)
    _add_rectangle_to_page(page, 40, 40, 60, 30, ap.Color.green, 0)

    document.save(outfile)
```

![Mengontrol Urutan Z](control.png)

## Topik Grafik Terkait

- [Bekerja dengan grafik PDF di Python](/pdf/id/python-net/working-with-graphs/)
- [Periksa batas bentuk dalam grafik PDF dengan Python](/pdf/id/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/)
- [Tambahkan bentuk garis ke PDF di Python](/pdf/id/python-net/add-line/)
- [Tambahkan bentuk elips ke PDF di Python](/pdf/id/python-net/add-ellipse/)
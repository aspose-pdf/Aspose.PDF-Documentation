---
title: Tambahkan Bentuk Elips ke PDF dalam Python
linktitle: Tambahkan Elips
type: docs
weight: 60
url: /id/python-net/add-ellipse/
description: Pelajari cara menggambar, mengisi, dan memberi label pada bentuk elips dalam file PDF menggunakan Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gambar bentuk elips dalam file PDF menggunakan Python
Abstract: Artikel ini menunjukkan cara menambahkan bentuk elips ke dokumen PDF dengan Aspose.PDF for Python via .NET. Artikel ini mencakup elips berpinggir, elips terisi, dan menambahkan teks di dalam objek elips.
---

## Tambahkan objek Ellipse

Aspose.PDF for Python via .NET memungkinkan Anda menambahkan [Elips](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/ellipse/) bentuk ke halaman PDF dengan [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) class. Anda dapat menggambar outline elips, menerapkan warna isi, dan menempatkan teks di dalam objek elips.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_ellipse(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    ellipse1 = drawing.Ellipse(150, 100, 120, 60)
    ellipse1.graph_info.color = ap.Color.green_yellow
    ellipse1.text = ap.text.TextFragment("Ellipse")
    graph.shapes.add(ellipse1)

    ellipse2 = drawing.Ellipse(50, 50, 18, 300)
    ellipse2.graph_info.color = ap.Color.dark_red
    graph.shapes.add(ellipse2)

    page.paragraphs.add(graph)
    document.save(outfile)
```

![Tambahkan Elips](ellipse.png)

## Buat Objek Elips Terisi

Potongan kode berikut menunjukkan cara menambahkan sebuah [Elips](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/ellipse/) objek yang diisi dengan warna.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def create_ellipse_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    ellipse1 = drawing.Ellipse(100, 100, 120, 180)
    ellipse1.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(ellipse1)

    ellipse2 = drawing.Ellipse(200, 150, 180, 120)
    ellipse2.graph_info.fill_color = ap.Color.dark_red
    graph.shapes.add(ellipse2)

    page.paragraphs.add(graph)
    document.save(outfile)
```

![Elips Terisi](fill_ellipse.png)

## Tambahkan Teks di dalam Elips

Aspose.PDF for Python via .NET juga memungkinkan Anda menempatkan teks di dalam objek bentuk. Contoh berikut menambahkan teks ke bentuk elips.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_text_inside_ellipse(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    text_fragment = ap.text.TextFragment("Ellipse")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Helvetica")
    text_fragment.text_state.font_size = 24

    ellipse1 = ap.drawing.Ellipse(100, 100, 120, 180)
    ellipse1.graph_info.fill_color = ap.Color.green_yellow
    ellipse1.text = text_fragment
    graph.shapes.add(ellipse1)

    ellipse2 = ap.drawing.Ellipse(200, 150, 180, 120)
    ellipse2.graph_info.fill_color = ap.Color.dark_red
    ellipse2.text = text_fragment
    graph.shapes.add(ellipse2)

    page.paragraphs.add(graph)
    document.save(outfile)
```

![Teks di dalam Ellipse](text_ellipse.png)

## Topik Grafik Terkait

- [Bekerja dengan grafik PDF di Python](/pdf/id/python-net/working-with-graphs/)
- [Tambahkan bentuk lingkaran ke PDF di Python](/pdf/id/python-net/add-circle/)
- [Tambahkan bentuk kurva ke PDF di Python](/pdf/id/python-net/add-curve/)
- [Tambahkan bentuk persegi panjang ke PDF di Python](/pdf/id/python-net/add-rectangle/)

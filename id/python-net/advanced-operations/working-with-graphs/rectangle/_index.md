---
title: Tambahkan Objek Persegi Panjang ke File PDF
linktitle: Tambahkan Persegi Panjang
type: docs
weight: 50
url: /id/python-net/add-rectangle/
description: Artikel ini menjelaskan cara membuat objek Persegi Panjang pada PDF Anda menggunakan Aspose.PDF untuk Python via .NET.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menambahkan Objek Persegi Panjang ke PDF menggunakan Python
Abstract: Artikel ini memberikan panduan komprehensif tentang cara menambahkan dan memanipulasi objek Persegi Panjang dalam dokumen PDF menggunakan Aspose.PDF untuk Python via .NET. Artikel ini menjelaskan proses pembuatan Persegi Panjang dan integrasinya ke dalam dokumen PDF, termasuk mengatur batas dan mengisi dengan warna solid atau isian gradasi. Artikel ini mencakup instruksi langkah demi langkah dengan cuplikan kode yang menunjukkan pembuatan dokumen PDF, menambahkan halaman, dan menyisipkan objek Persegi Panjang dengan berbagai properti visual, seperti isian warna solid, isian gradasi, dan transparansi menggunakan saluran alfa. Selain itu, artikel ini menjelaskan cara mengontrol Z-Order objek Persegi Panjang untuk mengatur urutan rendernya ketika beberapa bentuk ditambahkan ke PDF yang sama. Setiap bagian didukung dengan contoh visual untuk menggambarkan output dari cuplikan kode.
---

## Tambahkan objek Persegi Panjang

Aspose.PDF untuk Python via .NET mendukung fitur menambahkan objek grafik (misalnya grafik, garis, persegi panjang, dll.) ke dokumen PDF. Anda juga dapat menambahkan objek [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) yang juga menawarkan fitur mengisi objek persegi panjang.

Pertama, mari kita lihat kemungkinan membuat objek Persegi Panjang.

Ikuti langkah-langkah di bawah ini:

1. Buat [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) PDF baru.
1. Tambahkan [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) ke dalam koleksi halaman file PDF.
1. Tambahkan [Text fragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) ke koleksi paragraf pada instance halaman.
1. Buat instance [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/).
1. Atur batas untuk [Drawing object](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/).
1. Tambahkan objek [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) ke koleksi bentuk pada objek Graph.
1. Tambahkan objek grafik ke koleksi paragraf pada instance halaman.
1. Tambahkan [Text fragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) ke koleksi paragraf pada instance halaman.
1. Dan simpan file PDF Anda

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()
    text_fragment = ap.text.TextFragment("Rectangle")

    # Add Text fragment to paragraphs collection of page instance
    page.paragraphs.add(text_fragment)

    # Create Graph instance
    graph = drawing.Graph(400, 300)

    # Add graph object to paragraphs collection of page instance
    page.paragraphs.add(graph)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)
    graph.border = border_info

    # Create Rectangle instance
    rect = drawing.Rectangle(20, 20, 350, 250)

    # Add rectangle object to shape collection of Graph object
    graph.shapes.append(rect)

    # Add Text fragment to paragraphs collection of page instance
    page.paragraphs.add(text_fragment)

    # Save PDF file
    document.save(path_outfile)
```

![Buat Persegi Panjang](create_rectangle.png)

## Buat Objek Persegi Panjang Terisi

Aspose.PDF untuk Python via .NET juga menawarkan fitur mengisi objek persegi panjang dengan warna tertentu.

Cuplikan kode berikut menunjukkan cara menambahkan objek [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) yang terisi dengan warna.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add a page
    page = document.pages.add()

    # Create Graph instance
    graph = drawing.Graph(100, 400)

    # Add graph object to the paragraphs collection of the page instance
    page.paragraphs.add(graph)

    # Create Rectangle instance with specified dimensions
    rect = drawing.Rectangle(100, 100, 200, 120)

    # Specify fill color for the Rectangle object
    rect.graph_info.fill_color = ap.Color.red

    # Add rectangle object to the shapes collection of the Graph object
    graph.shapes.add(rect)

    # Save PDF document
    document.save(path_outfile)
```

Lihat hasil persegi panjang yang diisi warna solid:

![Persegi Panjang Terisi](fill_rectangle.png)

## Tambahkan Gambar dengan Isi Gradasi

Aspose.PDF untuk Python via .NET mendukung fitur menambahkan objek grafik ke dokumen PDF dan terkadang diperlukan mengisi objek grafik dengan Warna Gradasi.

Cuplikan kode berikut menunjukkan cara menambahkan objek [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) yang diisi dengan Warna Gradasi.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Create Graph instance
    graph = drawing.Graph(400, 400)

    # Add graph object to paragraphs collection of page instance
    page.paragraphs.add(graph)

    # Create Rectangle instance
    rect = drawing.Rectangle(0, 0, 300, 300)

    # Specify fill color for Graph object
    gradient_color = ap.Color()
    gradient_settings = drawing.GradientAxialShading(ap.Color.red, ap.Color.blue)
    gradient_settings.start = ap.Point(0, 0)
    gradient_settings.end = ap.Point(350, 350)
    gradient_color.pattern_color_space = gradient_settings
    rect.graph_info.fill_color = gradient_color

    # Add rectangle object to shape collection of Graph object
    graph.shapes.append(rect)

    # Save PDF file
    document.save(output_file)
```

![Persegi Panjang Gradasi](gradient.png)

## Buat Persegi Panjang dengan Saluran Warna Alfa

Aspose.PDF untuk Python .NET mendukung mengisi objek persegi panjang dengan warna tertentu. Objek persegi panjang juga dapat memiliki saluran warna Alfa untuk memberikan tampilan transparan. Cuplikan kode berikut menunjukkan cara menambahkan objek [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) dengan saluran warna Alfa.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Create Graph instance
    graph = drawing.Graph(100, 400)

    # Add graph object to paragraphs collection of page instance
    page.paragraphs.add(graph)

    # Create Rectangle instance
    rect = drawing.Rectangle(100, 100, 200, 120)

    # Specify fill color for Graph object
    rect.graph_info.fill_color = ap.Color.from_argb(128, 244, 180, 0)

    # Add rectangle object to shape collection of Graph object
    graph.shapes.append(rect)

    # Create second rectangle object
    rect1 = drawing.Rectangle(200, 150, 200, 100)
    rect1.graph_info.fill_color = ap.Color.from_argb(160, 120, 0, 120)
    graph.shapes.append(rect1)

    # Save PDF file
    document.save(output_file)
```

![Warna Saluran Alfa Persegi Panjang](rectangle_color.png)

## Kontrol Z-Order Bentuk

Aspose.PDF untuk .NET mendukung fitur menambahkan objek grafik (misalnya grafik, garis, persegi panjang, dll.) ke dokumen PDF. Saat menambahkan lebih dari satu instance objek yang sama dalam file PDF, kita dapat mengontrol rendernya dengan menentukan Z-Order. Z-Order juga digunakan ketika kita perlu merender objek di atas satu sama lain.

Cuplikan kode berikut menunjukkan langkah-langkah untuk merender objek [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) satu di atas yang lain.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Set size of PDF page
    page.set_page_size(375, 300)

    # Set left margin for page object as 0
    page.page_info.margin.left = 0

    # Set top margin of page object as 0
    page.page_info.margin.top = 0

    # Create a new rectangle with Color as Red, Z-Order as 0 and certain dimensions
    add_rectangle(page, 50, 40, 60, 40, ap.Color.red, 2)

    # Create a new rectangle with Color as Blue, Z-Order as 0 and certain dimensions
    add_rectangle_to_page(page, 20, 20, 30, 30, ap.Color.blue, 1)

    # Create a new rectangle with Color as Green, Z-Order as 0 and certain dimensions
    add_rectangle_to_page(page, 40, 40, 60, 30, ap.Color.green, 0)

    # Save resultant PDF file
    document.save(output_file)
```

![Mengontrol Z Order](control.png)

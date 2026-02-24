---
title: Tambahkan Objek Garis ke File PDF
linktitle: Tambahkan Garis
type: docs
weight: 40
url: /id/python-net/add-line/
description: Artikel ini menjelaskan cara membuat objek garis pada PDF Anda menggunakan Aspose.PDF untuk Python via .NET.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menambahkan Objek Garis ke PDF menggunakan Python
Abstract: Artikel ini membahas cara menambahkan objek garis ke dokumen PDF menggunakan Aspose.PDF untuk Python via .NET. Artikel ini menjelaskan proses membuat instance `Document` dan menambahkan objek `Graph` ke PDF. Artikel ini menyediakan langkah‑langkah terperinci untuk membuat dan mengonfigurasi objek `Line`, termasuk menentukan pola dash dan warna. Artikel ini menyertakan cuplikan kode yang mendemonstrasikan cara menambahkan garis sederhana, garis bertitik‑dash, serta cara menggambar garis melintasi halaman untuk membentuk pola silang. Setiap bagian dilengkapi dengan representasi visual PDF yang dihasilkan. Panduan ini berfungsi sebagai sumber praktis bagi pengembang yang ingin meningkatkan dokumen PDF mereka dengan elemen grafis menggunakan Aspose.PDF.
---

## Tambahkan objek garis

Aspose.PDF untuk Python via .NET mendukung fitur menambahkan objek grafik (misalnya grafik, garis, persegi panjang, dll.) ke dokumen PDF. Anda juga dapat menambahkan objek [Line](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) di mana Anda dapat menentukan pola dash, warna, dan pemformatan lain untuk elemen Line.

Ikuti langkah-langkah di bawah ini:

1. Buat instance [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Buat Objek Graph
1. Tambahkan objek [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) ke koleksi paragraf halaman.
1. Buat dan Konfigurasikan Line
1. Tambahkan [Line](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/line/) ke Graph
1. Simpan file PDF kami.

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
    line = drawing.Line([100, 100, 200, 100])

    # Specify fill color for Graph object
    line.graph_info.dash_array = [0, 1, 0]
    line.graph_info.dash_phase = 1

    # Add rectangle object to shape collection of Graph object
    graph.shapes.append(line)

    # Save PDF file
    document.save(path_outfile)
```

![Tambahkan Garis](add_line.png)

## Cara menambahkan Garis Dotted Dashed ke dokumen PDF Anda

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
    line = drawing.Line([100, 100, 200, 100])

    # Set color for Line object
    line.graph_info.color = ap.Color.red

    # Specify fill color for Graph object
    line.graph_info.dash_array = [0, 1, 0]
    line.graph_info.dash_phase = 1

    # Add rectangle object to shape collection of Graph object
    graph.shapes.append(line)

    # Save PDF file
    document.save(path_outfile)
```

Mari kita periksa hasilnya:

![Garis Putus](dash_line.png)

## Gambar Garis Melintasi Halaman

Anda juga dapat menggunakan objek garis untuk menggambar sebuah salib yang dimulai dari sudut kiri-bawah ke sudut kanan-atas dan sudut kiri-atas ke sudut kanan-bawah.

Silakan lihat cuplikan kode berikut untuk memenuhi kebutuhan ini.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Set page margin on all sides as 0
    page.page_info.margin.left = 0
    page.page_info.margin.right = 0
    page.page_info.margin.bottom = 0
    page.page_info.margin.top = 0

    # Create Graph object with Width and Height equal to page dimensions
    graph = drawing.Graph(page.page_info.width, page.page_info.height)

    # Create first line object starting from Lower-Left to Top-Right corner of page
    line = drawing.Line([page.rect.llx, 0, page.page_info.width, page.rect.ury])

    # Add line to shape collection of Graph object
    graph.shapes.append(line)

    # Draw line from Top-Left corner of page to Bottom-Right corner of page
    line2 = drawing.Line([0, page.rect.ury, page.page_info.width, page.rect.llx])

    # Add line to shape collection of Graph object
    graph.shapes.append(line2)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF file
    document.save(path_outfile)
```

![Menggambar Garis](draw_line.png)



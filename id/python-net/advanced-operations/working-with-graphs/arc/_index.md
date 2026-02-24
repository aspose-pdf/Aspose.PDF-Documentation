---
title: Tambah Objek Busur ke File PDF
linktitle: Tambah Busur
type: docs
weight: 10
url: /id/python-net/add-arc/
description: Artikel ini menjelaskan cara membuat objek busur pada PDF Anda menggunakan Aspose.PDF untuk Python via .NET.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menambahkan Objek Busur ke PDF menggunakan Python
Abstract: Artikel ini menyediakan panduan terperinci tentang cara menambahkan dan menyesuaikan objek busur dalam dokumen PDF menggunakan Aspose.PDF untuk Python via .NET. Artikel ini menyoroti kemampuan perpustakaan untuk menyertakan elemen grafis seperti busur, yang penting bagi aplikasi yang memerlukan pembuatan konten PDF dinamis seperti diagram teknis dan ilustrasi khusus. Artikel ini mencakup instruksi langkah demi langkah dan potongan kode yang menunjukkan cara membuat instance `Document`, menyiapkan objek `Drawing` dengan dimensi dan properti batas yang ditentukan, serta menambahkan objek `Graph` dan `Arc` ke halaman PDF. Selain itu, artikel ini membahas proses mengisi objek busur dengan warna, memperlihatkan cara mengatur properti isi untuk busur dan garis, dan akhirnya menyimpan dokumen PDF. Contoh-contoh yang disediakan berfungsi sebagai panduan praktis bagi pengembang yang ingin memanfaatkan Aspose.PDF untuk manipulasi grafis yang tepat dalam file PDF.
---

## Tambah Objek Busur

Aspose.PDF untuk Python via .NET mendukung fitur menambahkan objek grafik (misalnya grafik, garis, persegi panjang, dll.) ke dokumen PDF. Ia juga menawarkan fitur mengisi objek busur dengan warna tertentu.

Contoh ini menggambarkan cara menggambar busur secara programatis dalam dokumen PDF menggunakan Aspose.PDF untuk Python via .NET. Dengan memanfaatkan modul drawing, pengembang dapat membuat elemen grafis kompleks, seperti busur, dengan kontrol yang tepat atas penampilan dan penempatannya. Kemampuan ini penting bagi aplikasi yang memerlukan pembuatan konten grafis dinamis dalam PDF, seperti diagram teknis, grafik, atau ilustrasi khusus.

Ikuti langkah-langkah di bawah ini:

1. Buat instance [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Buat [Drawing object](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) dengan dimensi tertentu.
1. Atur [border](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) untuk objek Drawing.
1. Tambahkan objek [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) ke koleksi paragraf halaman.
1. Simpan file PDF kami.

Potongan kode berikut menunjukkan cara menambahkan objek [Arc](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/arc/) .

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 400)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create arcs and set their properties
    arc1 = drawing.Arc(100, 100, 95, 0, 90)
    arc1.graph_info = drawing.GraphInfo()
    arc1.graph_info.color = ap.Color.green_yellow
    graph.shapes.add(arc1)

    arc2 = drawing.Arc(100, 100, 90, 70, 180)
    arc2.graph_info = drawing.GraphInfo()
    arc2.graph_info.color = ap.Color.dark_blue
    graph.shapes.add(arc2)

    arc3 = drawing.Arc(100, 100, 85, 120, 210)
    arc3.graph_info = drawing.GraphInfo()
    arc3.graph_info.color = ap.Color.red
    graph.shapes.add(arc3)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

## Buat Objek Busur Terisi

Contoh berikut menunjukkan cara menambahkan objek Arc yang terisi dengan warna dan dimensi tertentu.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 400)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create an arc and set fill color
    arc = drawing.Arc(100, 100, 95, 0, 90)
    arc.graph_info = drawing.GraphInfo()
    arc.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(arc)

    # Create a line and set fill color
    line = drawing.Line([195, 100, 100, 100, 100, 195])
    line.graph_info = drawing.GraphInfo()
    line.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(line)

    # Add Graph object to the paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

Mari lihat hasil penambahan Arc yang terisi:

![Busur Terisi](filled_arc.png)


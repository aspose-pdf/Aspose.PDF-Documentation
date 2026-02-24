---
title: Tambahkan Objek Lingkaran ke File PDF
linktitle: Tambah Lingkaran
type: docs
weight: 20
url: /id/python-net/add-circle/
description: Artikel ini menjelaskan cara membuat objek lingkaran ke PDF Anda menggunakan Aspose.PDF untuk Python via .NET.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menambahkan Objek Lingkaran ke PDF menggunakan Python
Abstract: Artikel ini menyediakan panduan tentang cara menggunakan Aspose.PDF untuk Python via .NET untuk membuat objek lingkaran dalam dokumen PDF. Artikel ini menjelaskan proses menambahkan grafik lingkaran berbingkai maupun terisi, menyoroti bagaimana grafik lingkaran dapat menjadi alat yang berguna untuk menampilkan data di beberapa kategori ketika data tersebut mewakili keseluruhan. Artikel ini mencakup instruksi langkah demi langkah untuk membuat instance `Document`, menyiapkan objek `Drawing` dengan dimensi tertentu, menerapkan border, dan menambahkan objek `Graph` ke halaman PDF. Contoh kode menunjukkan cara menggambar lingkaran sederhana dan lingkaran terisi, dengan instruksi detail tentang pengaturan warna dan menambahkan teks ke lingkaran. Hasil visual dari operasi ini juga disajikan, menampilkan kemampuan Aspose.PDF dalam meningkatkan konten PDF dengan elemen grafis dinamis.
---

## Tambahkan objek Lingkaran

Seperti grafik batang, grafik lingkaran dapat digunakan untuk menampilkan data dalam sejumlah kategori terpisah. Namun, tidak seperti grafik batang, grafik lingkaran hanya dapat digunakan ketika Anda memiliki data untuk semua kategori yang membentuk keseluruhan. Jadi mari kita lihat cara menambahkan objek [Circle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/circle/) dengan Aspose.PDF untuk Python .NET.

Contoh ini menggambarkan cara menggambar lingkaran secara programatis di dalam dokumen PDF menggunakan Aspose.PDF untuk Python via .NET. Dengan memanfaatkan modul drawing, pengembang dapat membuat elemen grafis kompleks dengan kontrol presisi atas tampilan dan penempatannya. Kemampuan ini penting bagi aplikasi yang memerlukan pembuatan konten grafis dinamis dalam PDF, seperti diagram teknis, bagan, atau ilustrasi kustom.

Ikuti langkah-langkah di bawah ini:

1. Buat instance [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Buat [Drawing object](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) dengan dimensi tertentu.
1. Atur [border](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/#properties) untuk objek Drawing.
1. Tambahkan objek [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) ke koleksi paragraf halaman.
1. Simpan file PDF kami.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 200)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create a circle with the specified coordinates and radius
    circle = drawing.Circle(100, 100, 40)

    # Set the circle's color
    circle.graph_info = drawing.GraphInfo()
    circle.graph_info.color = ap.Color.green_yellow

    # Add the circle to the graph shapes
    graph.shapes.add(circle)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

Lingkaran yang kami gambar akan terlihat seperti ini:

![Drawing Circle](drawing_circle.png)

## Buat Objek Lingkaran Terisi

Contoh ini menunjukkan cara menambahkan objek Circle yang terisi dengan warna.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 200)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create a filled circle
    circle = drawing.Circle(100, 100, 40)
    circle.graph_info = drawing.GraphInfo()
    circle.graph_info.color = ap.Color.green_yellow
    circle.graph_info.fill_color = ap.Color.green
    circle.text = ap.text.TextFragment("Circle")

    # Add the circle to the graph shapes
    graph.shapes.add(circle)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

Mari lihat hasil penambahan Circle terisi:

![Filled Circle](filled_circle.png)



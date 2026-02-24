---
title: Tambahkan Objek Kurva ke File PDF
linktitle: Tambahkan Kurva
type: docs
weight: 30
url: /id/python-net/add-curve/
description: Artikel ini menjelaskan cara membuat objek kurva ke PDF Anda menggunakan Aspose.PDF untuk Python via .NET.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menambahkan Objek Kurva ke PDF menggunakan Python
Abstract: Artikel ini membahas penerapan kurva grafik dalam dokumen PDF menggunakan perpustakaan Aspose.PDF untuk Python via .NET. Artikel ini memperkenalkan konsep kurva grafik, yang merupakan gabungan garis proyektif, dan merinci proses pembuatan baik kurva Bézier sederhana maupun terisi secara programatik. Artikel ini menyediakan instruksi langkah demi langkah dan cuplikan kode untuk menggambar kurva dalam PDF, menyoroti manipulasi elemen grafis menggunakan modul gambar Aspose.PDF. Prosesnya meliputi membuat instance `Document`, mendefinisikan objek `Drawing` dengan dimensi tertentu, mengatur border, dan menambahkan objek `Graph` ke halaman PDF. Hasil visual dari contoh kode ini diilustrasikan melalui gambar yang menunjukkan kurva yang dihasilkan. Artikel ini juga mengeksplorasi pembuatan objek kurva terisi, memperlihatkan cara mengatur warna isi untuk kurva, yang penting untuk menghasilkan konten grafis dinamis seperti diagram teknis, grafik, atau ilustrasi khusus dalam PDF.
---

## Tambahkan objek Kurva

Sebuah graf [Kurva](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/curve/) adalah gabungan terhubung dari garis proyektif, setiap garis bertemu tiga lainnya pada titik ganda biasa.

Dalam artikel ini, kami akan menyelidiki kurva graf sederhana, dan kurva terisi, yang dapat Anda buat dalam dokumen PDF Anda.

Contoh ini mengilustrasikan cara menggambar kurva Bézier secara programatik dalam dokumen PDF menggunakan Aspose.PDF untuk Python via .NET. Dengan memanfaatkan modul gambar, pengembang dapat membuat elemen grafis kompleks dengan kontrol presisi atas tampilan dan posisinya. Kemampuan ini penting bagi aplikasi yang memerlukan pembuatan dinamis konten grafis dalam PDF, seperti diagram teknis, grafik, atau ilustrasi khusus.

Ikuti langkah-langkah di bawah ini:

1. Buat instance [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Buat [objek Drawing](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/) dengan dimensi tertentu.
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

    # Create a curve and set its properties
    curve1 = drawing.Curve([10, 10, 50, 60, 70, 10, 100, 120])
    curve1.graph_info = drawing.GraphInfo()
    curve1.graph_info.color = ap.Color.green_yellow

    # Add the curve to the graph shapes
    graph.shapes.add(curve1)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

Gambar berikut menunjukkan hasil yang dihasilkan dengan cuplikan kode kami:

![Menggambar Kurva](drawing_curve.png)

## Buat Objek Kurva Terisi

Contoh ini menunjukkan cara menambahkan objek Kurva yang terisi dengan warna.

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

    # Create a curve and set fill color
    curve1 = drawing.Curve([10, 10, 50, 60, 70, 10, 100, 120])
    curve1.graph_info = drawing.GraphInfo()
    curve1.graph_info.fill_color = ap.Color.green_yellow

    # Add the curve to the graph shapes
    graph.shapes.add(curve1)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

Lihat hasil penambahan Kurva terisi:

![Kurva Terisi](filled_curve.png)


---
title: Tambahkan Objek Elips ke File PDF
linktitle: Tambahkan Elips
type: docs
weight: 60
url: /id/python-net/add-ellipse/
description: Artikel ini menjelaskan cara membuat objek Elips pada PDF Anda menggunakan Aspose.PDF untuk Python melalui .NET.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menambahkan Objek Elips ke PDF menggunakan Python
Abstract: Artikel ini menyediakan panduan lengkap tentang cara menggunakan Aspose.PDF untuk Python melalui .NET untuk menambahkan dan menyesuaikan objek Elips dalam dokumen PDF. Artikel ini menjelaskan proses pembuatan dan manipulasi elips, termasuk pengaturan dimensi, warna, dan posisi mereka, menggunakan modul drawing. Menunjukkan cara menggambar elips pada halaman PDF, menampilkan kemampuan mengontrol tampilan dan posisinya. Contoh tersebut mencakup pengaturan properti batas dan penambahan beberapa elips ke dalam grafik. Mengilustrasikan cara mengisi elips dengan warna tertentu, memberikan contoh di mana dua elips diisi dengan warna berbeda dan ditambahkan ke dokumen PDF. Menjelaskan cara menyisipkan teks di dalam objek Elips dengan memanfaatkan properti teks dari Objek Grafik. Contoh yang disediakan menunjukkan cara mengatur properti font dan menambahkan teks ke
---

## Tambahkan objek Elips

Aspose.PDF untuk Python melalui .NET mendukung penambahan objek [Elips](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/ellipse/) ke dokumen PDF. Ia juga menyediakan fitur untuk mengisi objek elips dengan warna tertentu.

Contoh ini mengilustrasikan cara menggambar dan menyesuaikan elips secara programatis dalam dokumen PDF menggunakan Aspose.PDF untuk Python melalui .NET. Dengan memanfaatkan modul drawing, pengembang dapat membuat elemen grafis yang kompleks dengan kontrol tepat atas tampilan dan posisi mereka. Kemampuan ini penting untuk aplikasi yang memerlukan pembuatan konten grafis dinamis dalam PDF, seperti diagram teknis, bagan, atau ilustrasi khusus.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add a page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 400)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create first ellipse with specified coordinates and radii
    ellipse1 = drawing.Ellipse(150, 100, 120, 60)
    ellipse1.graph_info.color = ap.Color.green_yellow
    ellipse1.text = ap.TextFragment("Ellipse")

    # Add first ellipse to graph
    graph.shapes.add(ellipse1)

    # Create second ellipse with different dimensions and color
    ellipse2 = drawing.Ellipse(50, 50, 18, 300)
    ellipse2.graph_info.color = ap.Color.dark_red

    # Add second ellipse to graph
    graph.shapes.add(ellipse2)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)

```

![Tambahkan Elips](ellipse.png)

## Buat Objek Elips Terisi

Potongan kode berikut menunjukkan cara menambahkan objek [Elips](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/ellipse/) yang diisi dengan warna.

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create PDF document
    document = ap.Document()

    # Add a page
    page = document.pages.add()

    # Create Drawing object with certain dimensions
    graph = drawing.Graph(400, 400)

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    # Create first ellipse and set its fill color
    ellipse1 = drawing.Ellipse(100, 100, 120, 180)
    ellipse1.graph_info.fill_color = ap.Color.green_yellow

    # Add first ellipse to graph
    graph.shapes.add(ellipse1)

    # Create second ellipse and set its fill color
    ellipse2 = drawing.Ellipse(200, 150, 180, 120)
    ellipse2.graph_info.fill_color = ap.Color.dark_red

    # Add second ellipse to graph
    graph.shapes.add(ellipse2)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF document
    document.save(path_outfile)
```

![Elips Terisi](fill_ellipse.png)

## Tambahkan Teks di dalam Elips

Aspose.PDF untuk Python melalui .NET mendukung penambahan teks di dalam Objek Grafik. Properti Text dari Objek Grafik menyediakan opsi untuk mengatur teks Objek Grafik. Potongan kode berikut menunjukkan cara menambahkan teks di dalam objek Elips.

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

    # Set border for Drawing object
    border_info = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)
    graph.border = border_info

    text_fragment = ap.text.TextFragment("Ellipse")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Helvetica")
    text_fragment.text_state.font_size = 24

    ellipse1 = ap.drawing.Ellipse(100, 100, 120, 180)
    ellipse1.graph_info.fill_color = ap.Color.green_yellow
    ellipse1.text = text_fragment
    graph.shapes.append(ellipse1)

    ellipse2 = ap.drawing.Ellipse(200, 150, 180, 120)
    ellipse2.graph_info.fill_color = ap.Color.dark_red
    ellipse2.text = text_fragment
    graph.shapes.append(ellipse2)

    # Add Graph object to paragraphs collection of page
    page.paragraphs.add(graph)

    # Save PDF file
    document.save(path_outfile)
```

![Teks di dalam Elips](text_ellipse.png)


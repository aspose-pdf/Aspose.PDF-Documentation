---
title: Periksa batas bentuk dalam koleksi Shapes menggunakan Python
type: docs
weight: 70
url: /id/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/
description: Pelajari cara memeriksa batas sebuah bentuk saat dimasukkan ke dalam koleksi Shapes untuk memastikan itu sesuai dengan kontainer induknya.
lastmod: "2025-05-14"
draft: false
TechArticle: true
AlternativeHeadline: Panduan memeriksa batas bentuk dalam Shapes
Abstract: Artikel ini menawarkan panduan komprehensif tentang penggunaan fitur pemeriksaan batas dalam koleksi Shapes, khususnya dalam dokumen PDF menggunakan Python. Fitur ini berperan penting dalam memastikan bahwa elemen grafis, seperti bentuk, cocok dengan tepat dalam kontainer induknya. Fitur ini dapat dikonfigurasi untuk melemparkan pengecualian jika komponen melebihi batas kontainer, memastikan penanganan kesalahan yang kuat. Panduan ini menguraikan proses membuat dokumen PDF baru, menambahkan halaman, dan membuat elemen grafis (sebuah bentuk persegi panjang) dalam objek graph. Instruksi terperinci diberikan untuk menginstansiasi sebuah `Document`, menambahkan `Page`, dan membuat objek `Graph`. Dijelaskan cara menyiapkan bentuk `Rectangle` dan mengonfigurasi `BoundsCheckMode` menjadi `THROW_EXCEPTION_IF_DOES_NOT_FIT`, yang memastikan pengecualian dilemparkan jika bentuk tidak cocok dengan dimensi yang ditentukan dari graph. Proses ini diilustrasikan dengan contoh kode Python menggunakan pustaka Aspose.PDF, menyoroti implementasi praktis dari fitur-fitur ini.
---

Artikel ini memberikan panduan terperinci tentang penggunaan fitur pemeriksaan batas dalam koleksi Shapes. Fitur ini memastikan bahwa elemen cocok dengan kontainer induknya dan dapat dikonfigurasi untuk melemparkan pengecualian jika komponen tidak cocok.

1. Buat PDF baru [Dokumen](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. Tambahkan Halaman
1. Buat sebuah [Grafik](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/)
1. Buat Bentuk Persegi Panjang
1. Mode Pemeriksaan Batas
1. Tambahkan [Persegi Panjang](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) ke Grafik

```python

    import aspose.pdf as ap
    import aspose.pdf.drawing as drawing
    import datetime

    # Create Document instance
    document = ap.Document()

    # Add page to pages collection of PDF file
    page = document.pages.add()

    # Create a Graph object with specified dimensions
    graph = ap.drawing.Graph(100, 100)
    graph.top = 10
    graph.left = 15
    graph.border = ap.BorderInfo(ap.BorderSide.BOX, 1, ap.Color.black)
    page.paragraphs.add(graph)

    # Create a shape object(for example, Rectangle) with specified dimensions
    rect = drawing.Rectangle(-1, 0, 50, 50)
    rect.graph_info.fill_color = ap.Color.tomato

    # Set the BoundsCheck mode to THROW_EXCEPTION_IF_DOES_NOT_FIT
    graph.shapes.update_bounds_check_mode(ap.BoundsCheckMode.THROW_EXCEPTION_IF_DOES_NOT_FIT)

    # Add the rectangle to the graph
    graph.shapes.add(rect)
```            

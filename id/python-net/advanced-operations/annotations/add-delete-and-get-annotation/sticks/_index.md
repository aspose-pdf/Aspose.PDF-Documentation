---
title: Anotasi Sticky PDF menggunakan Python
linktitle: Anotasi Sticky
type: docs
weight: 50
url: /id/python-net/sticky-annotations/
description: Temukan cara menambahkan anotasi sticky dalam dokumen PDF menggunakan Aspose.PDF di Python via .NET untuk komentar dan umpan balik.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Panduan cara memanipulasi anotasi sticky dalam PDF
Abstract: Artikel ini memberikan panduan rinci tentang cara mengelola anotasi watermark dalam dokumen PDF menggunakan pustaka Aspose.PDF untuk Python. Artikel ini menjelaskan proses menambahkan, mengambil, dan menghapus anotasi watermark untuk memastikan keaslian dan merek dokumen. Anotasi watermark dapat digunakan untuk menyisipkan grafik, seperti logo, dengan ukuran dan posisi tetap pada halaman. Panduan ini mencakup cuplikan kode yang menunjukkan cara menambahkan anotasi watermark pada posisi tertentu dengan opasitas yang dapat disesuaikan, serta cara mengambil dan menghapus anotasi watermark yang ada. Contoh kode tersebut menggambarkan penggunaan pustaka Aspose.PDF untuk memanipulasi dokumen PDF secara programatis, menawarkan pendekatan praktis bagi pengembang untuk mengintegrasikan fungsionalitas watermark ke dalam aplikasi mereka.
---

## Tambah Anotasi Watermark

Anotasi Watermark adalah yang paling terlihat dan mudah divisualisasikan serta ditransmisikan. Ini merupakan cara terbaik untuk menempatkan logo atau tanda lain dalam dokumen PDF Anda yang menegaskan keasliannya.

Anotasi watermark harus digunakan untuk merepresentasikan grafik yang akan dicetak dengan ukuran dan posisi tetap pada halaman, terlepas dari dimensi halaman yang dicetak.

Anda dapat menambahkan Teks Watermark menggunakan [WatermarkAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/watermarkannotation/) pada posisi tertentu pada halaman PDF. Opasitas Watermark juga dapat dikontrol dengan menggunakan properti [opacity](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/watermarkannotation/#properties).

Silakan periksa cuplikan kode berikut untuk menambahkan WatermarkAnnotation.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    # Create Annotation
    # Load Page object to add Annotation
    page = document.pages[1]

    # Create Annotation
    wa = ap.annotations.WatermarkAnnotation(page, ap.Rectangle(100, 0, 400, 100, True))

    # Add annotaiton into Annotation collection of Page
    page.annotations.append(wa)

    # Create TextState for Font settings
    ts = ap.text.TextState()
    ts.foreground_color = ap.Color.blue
    ts.font_size = 25
    ts.font = ap.text.FontRepository.find_font("Arial");

    # Set opacity level of Annotaiton Text
    wa.opacity = 0.5

    # Add Text in Annotation
    wa.set_text_and_state([ "HELLO", "Line 1", "Line 2" ], ts)

    document.save(output_file)
```

## Ambil Anotasi Watermark

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    watermarkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.WATERMARK)
    ]

    for ta in watermarkAnnotations:
        print(ta.rect)
```

## Hapus Anotasi Watermark

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    watermarkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.WATERMARK)
    ]

    for ta in watermarkAnnotations:
        document.pages[1].annotations.delete(ta)

    document.save(output_file)
```



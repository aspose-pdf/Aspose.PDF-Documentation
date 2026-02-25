---
title: Anotasi Tambahan menggunakan Python
linktitle: Anotasi Tambahan
type: docs
weight: 60
url: /id/python-net/extra-annotations/
description: Pelajari cara menambahkan anotasi tambahan seperti penyorotan atau catatan ke PDF menggunakan Python dengan Aspose.PDF untuk meningkatkan konten PDF.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Panduan tentang cara memanipulasi anotasi tambahan dalam PDF
Abstract: Artikel ini menyediakan panduan komprehensif tentang cara menambahkan, mengambil, dan menghapus berbagai jenis anotasi dalam file PDF menggunakan Python, khususnya dengan pustaka Aspose.PDF. Artikel ini mencakup tiga jenis anotasi - Caret, Link, dan Redaction. Artikel menjelaskan bahwa anotasi Caret digunakan untuk saran penyuntingan teks. Dijelaskan proses memuat file PDF, membuat anotasi Caret dengan parameter spesifik (seperti rectangle, title, subject, flags, dan color), menambahkannya ke dokumen, dan menyimpan perubahan. Potongan kode disediakan untuk menambahkan, mengambil, dan menghapus anotasi Caret. Anotasi Link digunakan untuk membuat area yang dapat diklik yang mengarah ke URL atau posisi dokumen tertentu. Panduan mencakup instruksi dan kode untuk menambahkan anotasi Link dengan mengidentifikasi fragmen teks (mis., nomor telepon), mengatur aksi, dan mengelola anotasi tersebut.
---

## Cara menambahkan Anotasi Caret ke file PDF yang ada via Python

Anotasi Caret adalah simbol yang menunjukkan penyuntingan teks. Anotasi Caret juga merupakan anotasi markup, sehingga kelas Caret diturunkan dari kelas Markup dan juga menyediakan fungsi untuk mendapatkan atau mengatur properti Anotasi Caret serta mengatur ulang alur tampilan Anotasi Caret.
Anotasi Caret sering digunakan untuk menyarankan perubahan, penambahan, atau revisi pada teks.

Langkah-langkah untuk membuat anotasi Caret:

1. Muat file PDF - baru [Dokumen](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Buat baru [CaretAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/caretannotation/) dan atur parameter Caret (Rectangle baru, title, subject, flags, color). Anotasi ini digunakan untuk menunjukkan penyisipan teks.
1. Setelah kami dapat menambahkan anotasi ke halaman.

Potongan kode berikut menunjukkan cara menambahkan Anotasi Caret ke file PDF:

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_file)

    caretAnnotation1 = ap.annotations.CaretAnnotation(
        document.pages[1], ap.Rectangle(200, 700.664, 308.708, 740.769, True)
    )
    caretAnnotation1.title = "Aspose User"
    caretAnnotation1.subject = "Inserted text 1"
    caretAnnotation1.flags = ap.annotations.AnnotationFlags.PRINT
    caretAnnotation1.color = ap.Color.blue

    document.pages[1].annotations.append(caretAnnotation1)
    document.save(output_file)
```

### Dapatkan Anotasi Caret

Silakan coba menggunakan potongan kode berikut untuk Mendapatkan Anotasi Caret dalam dokumen PDF

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    caretAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CARET)
    ]

    for ca in caretAnnotations:
        print(ca.rect)
```

### Hapus Anotasi Caret

Potongan kode berikut menunjukkan cara Menghapus Anotasi Caret dari file PDF menggunakan Python.

```python

    import aspose.pdf as ap

    # Load the PDF file
    document = ap.Document(input_file)
    caretAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CARET)
    ]

    for ca in caretAnnotations:
        document.pages[1].annotations.delete(ca)

    document.save(output_file)
```

## Redaksi wilayah halaman tertentu dengan Anotasi Redaction menggunakan Aspose.PDF untuk Python

Aspose.PDF untuk Python via .NET mendukung fitur untuk menambahkan serta memanipulasi Anotasi dalam file PDF yang ada. Anotasi Redaction dalam dokumen PDF berfungsi untuk secara permanen menghapus atau menyembunyikan informasi rahasia dari dokumen. Proses penyuntingan informasi melibatkan menutupi atau memberi bayangan pada konten tertentu, seperti teks, gambar, atau grafis, dengan cara yang membatasi visibilitas dan aksesibilitasnya bagi orang lain. Hal ini memastikan bahwa informasi sensitif tetap tersembunyi dan terlindungi dalam dokumen. Untuk memenuhi kebutuhan ini, disediakan kelas bernama [RedactionAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/redactionannotation/), yang dapat digunakan untuk meredaksi wilayah halaman tertentu atau dapat digunakan untuk memanipulasi RedactionAnnotations yang ada dan meredaksinya (mis. meratakan anotasi dan menghapus teks di bawahnya).

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    page = document.pages[1]
    redactionAnnotation = ap.annotations.RedactionAnnotation(page, ap.Rectangle(270, 190, 371, 250, True))
    redactionAnnotation.title = "John Smith"
    redactionAnnotation.fill_color = ap.Color.light_gray
    redactionAnnotation.color = ap.Color.red
    redactionAnnotation.redact()

    page.annotations.append(redactionAnnotation)
    document.save(output_file)
```

### Dapatkan Anotasi Redaction

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    redactionAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.REDACTION)
    ]

    for pa in redactionAnnotations:
        print(pa.rect)
```

### Hapus Anotasi Redaction

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    redactionAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.REDACTION)
    ]

    for pa in redactionAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```




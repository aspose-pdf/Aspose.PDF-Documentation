---
title: Menggunakan Anotasi Teks untuk PDF via Python
linktitle: Anotasi Teks
type: docs
weight: 10
url: /id/python-net/text-annotation/
description: Aspose.PDF untuk Python memungkinkan Anda menambahkan, mengambil, dan menghapus Anotasi Teks dari dokumen PDF Anda.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Panduan cara memanipulasi anotasi teks dalam PDF
Abstract: Artikel ini menyediakan panduan komprehensif tentang cara memanipulasi anotasi teks dalam file PDF menggunakan pustaka Aspose.PDF untuk Python. Artikel ini mencakup penambahan, pengambilan, dan penghapusan berbagai jenis anotasi, termasuk Text, Free Text, dan StrikeOutAnnotations. Anotasi Teks adalah catatan yang ditempelkan pada lokasi tertentu dalam PDF, ditampilkan sebagai ikon yang menampilkan teks dalam popup ketika dibuka. Anotasi Free Text menampilkan teks langsung pada halaman, sementara StrikeOutAnnotations menandai teks dengan garis untuk menunjukkan penghapusan atau pengabaian. Proses ini melibatkan penambahan anotasi ke koleksi Annotations pada halaman menggunakan metode `add()`, dan contoh disediakan untuk setiap jenis anotasi. Cuplikan kode menggambarkan cara mengimplementasikan tugas-tugas ini, termasuk membuat anotasi dengan properti spesifik seperti judul, subjek, warna, dan flag, serta mengambil dan menghapus anotasi dari halaman PDF. Panduan ini berfungsi sebagai sumber praktis bagi pengembang yang ingin meningkatkan dokumen PDF melalui manipulasi anotasi menggunakan Aspose.PDF.
---

## Cara menambahkan Anotasi Teks ke dalam file PDF yang ada

Anotasi Teks adalah anotasi yang ditempelkan pada lokasi tertentu dalam dokumen PDF. Ketika ditutup, anotasi ditampilkan sebagai ikon; ketika dibuka, akan menampilkan jendela pop-up yang berisi teks catatan dalam font dan ukuran yang dipilih pembaca.

Anotasi disimpan dalam koleksi [Annotations](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/) dari sebuah Halaman tertentu. Koleksi ini hanya berisi anotasi untuk halaman tersebut; setiap halaman memiliki koleksi Annotations masing-masing.

Untuk menambahkan anotasi ke halaman tertentu, tambahkan ke koleksi Annotations halaman tersebut dengan metode [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/#methods).

1. Pertama, buat anotasi yang ingin Anda tambahkan ke PDF.
1. Kemudian buka PDF masukan.
1. Tambahkan anotasi ke koleksi [Annotations](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/) dari objek 'page'.

Cuplikan kode berikut menunjukkan cara menambahkan anotasi pada halaman PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    textAnnotation = ap.annotations.TextAnnotation(
        document.pages[1], ap.Rectangle(300, 700.664, 320, 720.769, True)
    )
    textAnnotation.title = "Aspose User"
    textAnnotation.subject = "Inserted text 1"
    textAnnotation.contents = "qwerty"
    textAnnotation.flags = ap.annotations.AnnotationFlags.PRINT
    textAnnotation.color = ap.Color.blue

    document.pages[1].annotations.append(textAnnotation)
    document.save(output_file)
```

## Mengambil Anotasi Teks dari file PDF

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    textAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.TEXT)
    ]

    for ta in textAnnotations:
        print(ta.rect)
```

## Menghapus Anotasi Teks dari file PDF

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    textAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.TEXT)
    ]

    for ta in textAnnotations:
        document.pages[1].annotations.delete(ta)

    document.save(output_file)
```


## Cara menambahkan (atau Membuat) Anotasi Free Text baru

Anotasi free text menampilkan teks langsung pada halaman. Kelas [FreeTextAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/freetextannotation/) memungkinkan pembuatan jenis anotasi ini. Pada cuplikan berikut, kami menambahkan anotasi free text di atas kemunculan pertama string tersebut.

```python

    import aspose.pdf as ap

    # Load the PDF file
    document = ap.Document(input_file)

    freeTextAnnotation = ap.annotations.FreeTextAnnotation(
        document.pages[1], ap.Rectangle(299, 713, 308, 720, True), ap.annotations.DefaultAppearance()
    )
    freeTextAnnotation.title = "Aspose User"
    freeTextAnnotation.color = ap.Color.light_green

    document.pages[1].annotations.append(freeTextAnnotation)
    document.save(output_file)
```

## Mengambil Anotasi Free Text dari file PDF

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    freeTextAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.FREE_TEXT)
    ]

    for fa in freeTextAnnotations:
        print(fa.rect)
```

## Menghapus Anotasi Free Text dari file PDF

```python

    import aspose.pdf as ap

    # Load the PDF file
    document = ap.Document(input_file)
    freeTextAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.FREE_TEXT)
    ]

    for fa in freeTextAnnotations:
        document.pages[1].annotations.delete(fa)

    document.save(output_file)
```


### Menyilang Kata menggunakan StrikeOutAnnotation

Aspose.PDF untuk Python memungkinkan Anda menambahkan, menghapus, dan memperbarui anotasi dalam dokumen PDF. Salah satu kelas memungkinkan Anda juga menyilang anotasi. Ketika StrikeOutAnnotation diterapkan pada PDF, sebuah garis digambar melintasi teks yang ditentukan, menunjukkan bahwa teks tersebut harus dihapus atau diabaikan.

Cuplikan kode berikut menunjukkan cara menambahkan [StrikeOutAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/strikeoutannotation/) ke PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    strikeoutAnnotation = ap.annotations.StrikeOutAnnotation(
        document.pages[1], ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
    )
    strikeoutAnnotation.title = "Aspose User"
    strikeoutAnnotation.subject = "Inserted text 1"
    strikeoutAnnotation.flags = ap.annotations.AnnotationFlags.PRINT
    strikeoutAnnotation.color = ap.Color.blue

    document.pages[1].annotations.append(strikeoutAnnotation)
    document.save(output_file)
```


## Mengambil StrikeOutAnnotation dari PDF

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    StrikeoutAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT)
    ]

    for pa in StrikeoutAnnotations:
        print(pa.rect)
```

## Menghapus StrikeOutAnnotation dari PDF

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    StrikeoutAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT)
    ]

    for pa in StrikeoutAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```




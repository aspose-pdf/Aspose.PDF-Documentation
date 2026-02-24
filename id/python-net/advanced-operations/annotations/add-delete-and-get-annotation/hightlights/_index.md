---
title: Anotasi Sorotan PDF menggunakan Python
linktitle: Anotasi Sorotan
type: docs
weight: 20
url: /id/python-net/highlights-annotation/
description: Pelajari cara menambahkan anotasi sorotan ke file PDF dalam Python menggunakan Aspose.PDF untuk penekanan teks.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Panduan tentang cara memanipulasi anotasi Sorotan dalam PDF
Abstract: Artikel ini memberikan panduan komprehensif tentang cara menggunakan anotasi markup teks dalam dokumen PDF, dengan fokus pada fungsionalitas yang disediakan oleh pustaka Aspose.PDF di Python. Artikel ini menjelaskan tujuan dan penggunaan berbagai jenis anotasi, termasuk anotasi sorotan, garis bawah, coret, dan bergelombang, masing‑masing dirancang untuk menekankan atau memodifikasi teks dengan berbagai cara. Dokumen ini merinci langkah‑langkah yang diperlukan untuk menambahkan anotasi tersebut ke PDF, termasuk memuat dokumen, membuat anotasi dengan parameter spesifik seperti judul dan warna, serta menambahkannya ke halaman yang diinginkan. Selain itu, artikel ini menyertakan potongan kode untuk mengambil anotasi dari PDF, memungkinkan pengguna menyaring dan mencetak detail anotasi berdasarkan tipe. Akhirnya, artikel ini menjelaskan proses menghapus anotasi, memberikan contoh kode untuk menghapus setiap jenis anotasi markup teks dari dokumen. Panduan ini berfungsi sebagai sumber praktis bagi pengembang yang ingin memanipulasi anotasi teks dalam file PDF secara programatik menggunakan Python.
---

Anotasi Markup Teks dalam PDF digunakan untuk menyorot, memberi garis bawah, melewati, atau menambahkan catatan pada teks dalam dokumen. Anotasi ini dimaksudkan untuk menyorot atau menarik perhatian pada bagian tertentu dari teks. Anotasi tersebut memungkinkan pengguna secara visual menandai atau memodifikasi konten file PDF.

Anotasi sorotan digunakan untuk menandai teks dengan latar belakang berwarna, biasanya kuning, untuk menunjukkan pentingnya atau relevansinya.

Anotasi garis bawah adalah garis yang ditempatkan di bawah teks yang dipilih untuk menunjukkan pentingnya, penekanan, atau mengindikasikan saran edit.

Anotasi coret termasuk mencoret atau menandai teks tertentu untuk menunjukkan bahwa teks tersebut telah dihapus, diganti, atau tidak lagi berlaku.

Garis bergelombang digunakan untuk memberi garis bawah pada teks guna menunjukkan jenis aksen yang berbeda, seperti kesalahan ejaan, potensi masalah, atau perubahan yang diusulkan.

## Tambahkan Anotasi Markup Teks

Untuk menambahkan Anotasi Markup Teks ke dokumen PDF, kita perlu melakukan tindakan berikut:

1. Muat file PDF - objek [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) baru.
1. Buat anotasi:
- [HighlightAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/highlightannotation/) dan atur parameter (judul, warna).
- [StrikeOutAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/strikeoutannotation/) dan atur parameter (judul, warna).
- [SquigglyAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squigglyannotation/) dan atur parameter (judul, warna).
- [UnderlineAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/underlineannotation/) dan atur parameter (judul, warna).
1. Setelah itu, kita harus menambahkan semua anotasi ke halaman.

### Tambahkan Anotasi Sorotan

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_file)

    # Create Circle Annotation
    highlightAnnotation = ap.annotations.HighlightAnnotation(
        document.pages[1], ap.Rectangle(300, 750, 320, 770, True)
    )
    document.pages[1].annotations.append(highlightAnnotation)
    document.save(output_file)
```

### Tambahkan Anotasi Coret

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

### Tambahkan Anotasi Bergelombang

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    page = document.pages[1]
    squigglyAnnotation = ap.annotations.SquigglyAnnotation(page, ap.Rectangle(67, 317, 261, 459, True))
    squigglyAnnotation.title = "John Smith"
    squigglyAnnotation.color = ap.Color.blue

    page.annotations.append(squigglyAnnotation)

    document.save(output_file)
```

### Tambahkan Anotasi Garis Bawah

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    underlineAnnotation = ap.annotations.UnderlineAnnotation(
        document.pages[1], ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
    )
    underlineAnnotation.title = "Aspose User"
    underlineAnnotation.subject = "Inserted Underline 1"
    underlineAnnotation.flags = ap.annotations.AnnotationFlags.PRINT
    underlineAnnotation.color = ap.Color.blue

    document.pages[1].annotations.append(underlineAnnotation)
    document.save(output_file)
```

## Dapatkan Anotasi Markup Teks

Silakan coba gunakan potongan kode berikut untuk Mendapatkan Anotasi Markup Teks dari dokumen PDF.

### Dapatkan Anotasi Sorotan

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT)
    ]

    for ha in highlightAnnotations:
        print(ha.rect)
```

### Dapatkan Anotasi Coret

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


### Dapatkan Anotasi Bergelombang

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squigglyAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUIGGLY)
    ]

    for pa in squigglyAnnotations:
        print(pa.rect)
```

### Dapatkan Anotasi Garis Bawah

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    UnderlineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.UNDERLINE)
    ]

    for ta in UnderlineAnnotations:
        print(ta.rect)
```

## Hapus Anotasi Markup Teks

Potongan kode berikut menunjukkan cara Menghapus Anotasi Markup Teks dari file PDF.

### Hapus Anotasi Sorotan

```python

    import aspose.pdf as ap

    # Load the PDF file
    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT)
    ]

    for hs in highlightAnnotations:
        document.pages[1].annotations.delete(hs)

    document.save(output_file)
```

### Hapus Anotasi Coret

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

### Hapus Anotasi Bergelombang

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squigglyAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUIGGLY)
    ]

    for pa in squigglyAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```

### Hapus Anotasi Garis Bawah

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    underlineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.UNDERLINE)
    ]

    for ta in underlineAnnotations:
        document.pages[1].annotations.delete(ta)

    document.save(output_file)
```




---
title: Anotasi Keamanan menggunakan Python
linktitle: Anotasi Keamanan
type: docs
weight: 75
url: /id/python-net/security-annotations/
description: Pelajari cara menandai teks untuk penyensoran, menerapkan anotasi penyensoran, dan menyensor area gambar dalam file PDF menggunakan Aspose.PDF for Python via .NET.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Redact konten PDF sensitif di Python dengan anotasi keamanan.
Abstract: Artikel ini menjelaskan cara bekerja dengan anotasi keamanan dalam dokumen PDF menggunakan Aspose.PDF for Python via .NET. Artikel ini mencakup penandaan teks yang cocok dengan anotasi redaction, penerapan redaction secara permanen, dan men-redaction area gambar terpilih berdasarkan persegi panjang penempatan gambar yang terdeteksi.
---

Artikel ini menunjukkan cara menggunakan anotasi keamanan dalam dokumen PDF dengan Aspose.PDF for Python via .NET.

Skrip contoh menunjukkan tiga alur kerja redaksi yang umum:

- tandai fragmen teks dengan anotasi redaksi
- terapkan secara permanen anotasi redaksi yang ada
- menyensor area gambar yang terdeteksi pada halaman

## Tandai Redaksi Teks

Alur kerja ini mencari teks yang cocok dalam dokumen dan menempatkan anotasi penyensoran pada setiap kecocokan. Ia belum menghapus kontennya; hanya menandai teks untuk penyensoran nanti.

### Buka PDF dan cari teks target

Buat sebuah `TextFragmentAbsorber` untuk istilah pencarian dan aktifkan opsi pencarian teks biasa sebelum memindai semua halaman.

```python
document = ap.Document(infile)
text_fragment_absorber = ap.text.TextFragmentAbsorber(search_term)

text_search_options = ap.text.TextSearchOptions(True)
text_fragment_absorber.text_search_options = text_search_options
document.pages.accept(text_fragment_absorber)
```

### Buat anotasi redaksi untuk setiap kecocokan

Untuk setiap fragmen teks yang cocok, buat sebuah `RedactionAnnotation` menggunakan persegi fragmen dan mengonfigurasi penampilan visualnya.

```python
for text_fragment in text_fragment_absorber.text_fragments:
    page = text_fragment.page
    annotation_rectangle = text_fragment.rectangle
    redaction_annotation = ap.annotations.RedactionAnnotation(
        page, annotation_rectangle
    )
    redaction_annotation.fill_color = ap.Color.gray
    redaction_annotation.border_color = ap.Color.red
    redaction_annotation.color = ap.Color.white
    redaction_annotation.overlay_text = "REDACTED"
    redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
    redaction_annotation.repeat = True
    page.annotations.add(redaction_annotation, True)
```

### Simpan PDF yang ditandai

```python
document.save(outfile)
```

### Contoh lengkap

```python
def mark_text_redaction(infile, outfile, search_term):
    document = ap.Document(infile)
    text_fragment_absorber = ap.text.TextFragmentAbsorber(search_term)

    text_search_options = ap.text.TextSearchOptions(True)
    text_fragment_absorber.text_search_options = text_search_options
    document.pages.accept(text_fragment_absorber)

    for text_fragment in text_fragment_absorber.text_fragments:
        page = text_fragment.page
        annotation_rectangle = text_fragment.rectangle
        redaction_annotation = ap.annotations.RedactionAnnotation(
            page, annotation_rectangle
        )
        redaction_annotation.fill_color = ap.Color.gray
        redaction_annotation.border_color = ap.Color.red
        redaction_annotation.color = ap.Color.white
        redaction_annotation.overlay_text = "REDACTED"
        redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
        redaction_annotation.repeat = True
        page.annotations.add(redaction_annotation, True)

    document.save(outfile)
```



## Terapkan Redaksi

Setelah anotasi redaksi ditambahkan, alur kerja ini menerapkannya secara permanen pada halaman pertama. Setelah diterapkan, konten asli dihapus dari output dokumen.

### Muat PDF dan kumpulkan anotasi penyensoran

```python
document = ap.Document(infile)
redaction_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.REDACTION
]
```

### Terapkan setiap anotasi redaksi

Contoh ini memeriksa bahwa setiap anotasi dapat diperlakukan sebagai `RedactionAnnotation` sebelum memanggil `redact()`.

```python
for redaction_annotation in redaction_annotations:
    if is_assignable(redaction_annotation, ap.annotations.RedactionAnnotation):
        cast(ap.annotations.RedactionAnnotation, redaction_annotation).redact()
```

### Simpan PDF yang telah disunting

```python
document.save(outfile)
```

### Contoh lengkap

```python
def apply_redaction(infile, outfile):
    document = ap.Document(infile)
    redaction_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.REDACTION
    ]

    for redaction_annotation in redaction_annotations:
        if is_assignable(redaction_annotation, ap.annotations.RedactionAnnotation):
            cast(ap.annotations.RedactionAnnotation, redaction_annotation).redact()

    document.save(outfile)
```



## Area Redaksi

Contoh ini menyensor area gambar yang terdeteksi alih-alih teks. Itu memindai halaman untuk penempatan gambar, memilih satu persegi penempatan, dan menambahkan anotasi penyensoran di atas area tersebut.

### Buka PDF dan deteksi penempatan gambar

Gunakan `ImagePlacementAbsorber` untuk menemukan posisi gambar pada halaman pertama.

```python
document = ap.Document(infile)

image_placement_absorber = ap.ImagePlacementAbsorber()
page = document.pages[1]
page.accept(image_placement_absorber)
```

### Buat anotasi redaksi untuk area gambar yang dipilih

Contoh tersebut menggunakan penempatan gambar terdeteksi ketiga dan menerapkan gaya redaksi yang sama seperti yang digunakan dalam contoh penandaan teks.

```python
target_rect = image_placement_absorber.image_placements[2].rectangle
redaction_annotation = ap.annotations.RedactionAnnotation(page, target_rect)
redaction_annotation.fill_color = ap.Color.gray
redaction_annotation.border_color = ap.Color.red
redaction_annotation.color = ap.Color.white
redaction_annotation.overlay_text = "REDACTED"
redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
redaction_annotation.repeat = True
```

### Tambahkan anotasi dan simpan PDF

```python
page.annotations.add(redaction_annotation, True)
document.save(outfile)
```

### Contoh lengkap

```python
def redact_area(infile, outfile):
    document = ap.Document(infile)

    image_placement_absorber = ap.ImagePlacementAbsorber()
    page = document.pages[1]
    page.accept(image_placement_absorber)

    target_rect = image_placement_absorber.image_placements[2].rectangle
    redaction_annotation = ap.annotations.RedactionAnnotation(page, target_rect)
    redaction_annotation.fill_color = ap.Color.gray
    redaction_annotation.border_color = ap.Color.red
    redaction_annotation.color = ap.Color.white
    redaction_annotation.overlay_text = "REDACTED"
    redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
    redaction_annotation.repeat = True

    page.annotations.add(redaction_annotation, True)
    document.save(outfile)
```

## Topik Terkait

- [Impor dan Ekspor Anotasi](/python-net/import-export-annotations/)
- [Anotasi Interaktif](/python-net/interactive-annotations/)
- [Anotasi Penandaan](/python-net/markup-annotations/)
- [Anotasi Media](/python-net/media-annotations/)
- [Anotasi Bentuk](/python-net/shape-annotations/)
- [Anotasi Berbasis Teks](/python-net/text-based-annotations/)
- [Anotasi Watermark](/python-net/watermark-annotations/)

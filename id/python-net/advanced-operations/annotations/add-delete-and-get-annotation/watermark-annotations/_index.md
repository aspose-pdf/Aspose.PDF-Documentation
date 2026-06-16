---
title: Anotasi Watermark menggunakan Python
linktitle: Anotasi Watermark
type: docs
weight: 70
url: /id/python-net/watermark-annotations/
description: Pelajari cara menambahkan, memeriksa, dan menghapus anotasi watermark pada dokumen PDF menggunakan Aspose.PDF for Python via .NET.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Bekerja dengan anotasi watermark pada file PDF menggunakan Python.
Abstract: Artikel ini menjelaskan cara membuat, membaca, dan menghapus anotasi watermark dalam dokumen PDF menggunakan Aspose.PDF for Python via .NET. Artikel ini mencakup penambahan anotasi watermark teks dengan keadaan teks khusus dan opasitas, memeriksa anotasi watermark yang ada, serta menghapus anotasi watermark dari halaman PDF.
---

Artikel ini menunjukkan cara bekerja dengan anotasi watermark dalam dokumen PDF menggunakan Aspose.PDF for Python via .NET.

Skrip contoh menunjukkan tiga alur kerja umum:

- tambahkan anotasi watermark
- ambil persegi panjang anotasi watermark
- hapus anotasi watermark

## Tambahkan Anotasi Watermark

Contoh ini menambahkan anotasi watermark ke halaman pertama dokumen PDF. Watermark menggunakan keadaan teks untuk mengontrol pengaturan Font dan menerapkan opacity khusus untuk tampilan semi-transparan.

### Buka PDF dan dapatkan halaman target

```python
document = ap.Document(infile)
page = document.pages[1]
```

### Buat anotasi watermark

Definisikan persegi panjang anotasi dan tambahkan ke koleksi anotasi halaman.

```python
watermark_annotation = ap.annotations.WatermarkAnnotation(
    page,
    ap.Rectangle(100, 100, 400, 200, True),
)

page.annotations.append(watermark_annotation)
```

### Konfigurasikan tampilan teks

Buat sebuah `TextState` objek untuk mengontrol warna teks, ukuran font, dan keluarga font.

```python
text_state = ap.text.TextState()
text_state.foreground_color = ap.Color.blue
text_state.font_size = 25
text_state.font = ap.text.FontRepository.find_font("Arial")
```

### Atur opasitas dan teks watermark

Contoh tersebut menggunakan opasitas 50% dan menulis tiga baris teks ke anotasi watermark.

```python
watermark_annotation.opacity = 0.5
watermark_annotation.set_text_and_state(["HELLO", "Line 1", "Line 2"], text_state)
```

### Simpan PDF

```python
document.save(outfile)
```

### Contoh lengkap

```python
def watermark_add(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    watermark_annotation = ap.annotations.WatermarkAnnotation(
        page,
        ap.Rectangle(100, 100, 400, 200, True),
    )

    page.annotations.append(watermark_annotation)

    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.blue
    text_state.font_size = 25
    text_state.font = ap.text.FontRepository.find_font("Arial")

    watermark_annotation.opacity = 0.5
    watermark_annotation.set_text_and_state(["HELLO", "Line 1", "Line 2"], text_state)

    document.save(outfile)
```

## Dapatkan Anotasi Watermark

Untuk memeriksa anotasi watermark yang ada, filter anotasi halaman pertama berdasarkan `WATERMARK` ketik dan cetak persegi panjang mereka.

### Muat dokumen dan kumpulkan anotasi watermark

```python
document = ap.Document(infile)
watermark_annotations = [
    a
    for a in document.pages[1].annotations
    if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
]
```

### Cetak persegi panjang anotasi

```python
for watermark_annotation in watermark_annotations:
    print(watermark_annotation.rect)
```

### Contoh lengkap

```python
def watermark_get(infile, outfile):
    document = ap.Document(infile)
    watermark_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
    ]

    for watermark_annotation in watermark_annotations:
        print(watermark_annotation.rect)
```

## Hapus Anotasi Watermark

Alur kerja ini menghapus semua anotasi watermark dari halaman pertama dan menyimpan PDF yang diperbarui.

### Temukan anotasi watermark untuk dihapus

```python
document = ap.Document(infile)
watermark_annotations = [
    a
    for a in document.pages[1].annotations
    if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
]
```

### Hapus anotasi dan simpan PDF

```python
for watermark_annotation in watermark_annotations:
    document.pages[1].annotations.delete(watermark_annotation)

document.save(outfile)
```

### Contoh lengkap

```python
def watermark_delete(infile, outfile):
    document = ap.Document(infile)
    watermark_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
    ]

    for watermark_annotation in watermark_annotations:
        document.pages[1].annotations.delete(watermark_annotation)

    document.save(outfile)
```

## Topik Terkait

- [Impor dan Ekspor Anotasi](/python-net/import-export-annotations/)
- [Anotasi Interaktif](/python-net/interactive-annotations/)
- [Anotasi Penandaan](/python-net/markup-annotations/)
- [Anotasi Media](/python-net/media-annotations/)
- [Anotasi Keamanan](/python-net/security-annotations/)
- [Anotasi Bentuk](/python-net/shape-annotations/)
- [Anotasi Berbasis Teks](/python-net/text-based-annotations/)

---
title: Markup Annotations menggunakan Python
linktitle: Anotasi Penandaan
type: docs
weight: 30
url: /id/python-net/markup-annotations/
description: Pelajari cara menambah, membaca, dan menghapus teks, caret, serta mengganti anotasi dalam dokumen PDF menggunakan Aspose.PDF for Python via .NET.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Bekerja dengan anotasi markup dalam file PDF menggunakan Python.
Abstract: Artikel ini menjelaskan cara membuat, memeriksa, dan menghapus anotasi markup dalam dokumen PDF menggunakan Aspose.PDF for Python via .NET. Ini mencakup anotasi teks, anotasi caret, dan anotasi replace, dengan setiap alur kerja dibagi menjadi langkah-langkah kecil dan contoh kode.
---

Artikel ini menunjukkan cara bekerja dengan anotasi markup dalam dokumen PDF menggunakan Aspose.PDF for Python via .NET.

Skrip contoh menampilkan tiga alur kerja anotasi umum:

- anotasi teks untuk komentar bergaya catatan
- anotasi caret untuk penanda sisipan
- ganti anotasi untuk markup penggantian teks

## Anotasi Teks

### Tambahkan Anotasi Teks

Contoh ini membuat anotasi teks pada halaman pertama dan menautkannya ke jendela popup. Anotasi teks berguna untuk komentar gaya catatan tempel dalam alur kerja tinjauan.

#### Buka PDF sumber

```python
document = ap.Document(infile)
```

#### Buat dan konfigurasikan anotasi teks

Tentukan persegi panjang anotasi dan atur judul, subjek, isi, flag tampilan, warna, serta ikon.

```python
text_annotation = ap.annotations.TextAnnotation(
    document.pages[1],
    ap.Rectangle(299.988, 613.664, 428.708, 680.769, True),
)
text_annotation.title = "Aspose User"
text_annotation.subject = "Sticky Note"
text_annotation.contents = (
    "This is a text annotation added by Aspose.PDF for Python via .NET"
)
text_annotation.flags = ap.annotations.AnnotationFlags.PRINT
text_annotation.color = ap.Color.blue
text_annotation.icon = ap.annotations.TextIcon.HELP
```

#### Buat anotasi pop-up

Buat jendela popup dan hubungkan ke anotasi teks.

```python
popup = ap.annotations.PopupAnnotation(
    document.pages[1],
    ap.Rectangle(428.708, 613.664, 528.708, 713.664, True),
)
popup.open = True

text_annotation.popup = popup
```

#### Tambahkan anotasi dan simpan PDF

```python
document.pages[1].annotations.add(text_annotation, consider_rotation=False)
document.save(outfile)
```

#### Contoh lengkap

```python
def text_annotation_add(infile, outfile):
    document = ap.Document(infile)

    text_annotation = ap.annotations.TextAnnotation(
        document.pages[1],
        ap.Rectangle(299.988, 613.664, 428.708, 680.769, True),
    )
    text_annotation.title = "Aspose User"
    text_annotation.subject = "Sticky Note"
    text_annotation.contents = (
        "This is a text annotation added by Aspose.PDF for Python via .NET"
    )
    text_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    text_annotation.color = ap.Color.blue
    text_annotation.icon = ap.annotations.TextIcon.HELP

    popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(428.708, 613.664, 528.708, 713.664, True),
    )
    popup.open = True

    text_annotation.popup = popup

    document.pages[1].annotations.add(text_annotation, consider_rotation=False)
    document.save(outfile)
```

### Dapatkan Anotasi Teks

Untuk memeriksa anotasi teks yang ada, saring koleksi anotasi pada halaman pertama dan pertahankan hanya item yang tipenya adalah `TEXT`.

#### Muat dokumen dan kumpulkan anotasi teks

```python
document = ap.Document(infile)
text_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
]
```

#### Cetak persegi panjang anotasi

```python
for annotation in text_annotations:
    print(annotation.rect)
```

#### Contoh lengkap

```python
def text_annotation_get(infile, outfile):
    document = ap.Document(infile)
    text_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
    ]

    for annotation in text_annotations:
        print(annotation.rect)
```

### Hapus Anotasi Teks

Alur kerja ini menghapus semua anotasi teks dari halaman pertama dan menyimpan PDF yang telah dimodifikasi.

#### Temukan anotasi teks untuk dihapus

```python
document = ap.Document(infile)
text_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
]
```

#### Hapus anotasi dan simpan file

```python
for annotation in text_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### Contoh lengkap

```python
def text_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    text_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
    ]

    for annotation in text_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

## Anotasi Caret

### Tambahkan Anotasi Caret

Annotasi caret digunakan untuk menandai titik sisipan dalam skenario tinjauan. Contoh ini menambahkan annotasi caret dengan catatan popup yang terlampir.

#### Buka dokumen dan dapatkan halaman target

```python
document = ap.Document(infile)
page = document.pages[1]
```

#### Buat dan konfigurasikan anotasi caret

```python
caret_annotation = ap.annotations.CaretAnnotation(
    page, ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
)
caret_annotation.title = "Aspose User"
caret_annotation.subject = "Inserted text 1"
caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
caret_annotation.color = ap.Color.blue
```

#### Lampirkan popup dan simpan dokumen

```python
caret_annotation.popup = ap.annotations.PopupAnnotation(
    page, ap.Rectangle(310, 713, 410, 730, True)
)
page.annotations.append(caret_annotation)

document.save(outfile)
```

#### Contoh lengkap

```python
def caret_annotations_add(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    caret_annotation = ap.annotations.CaretAnnotation(
        page, ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
    )
    caret_annotation.title = "Aspose User"
    caret_annotation.subject = "Inserted text 1"
    caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    caret_annotation.color = ap.Color.blue
    caret_annotation.popup = ap.annotations.PopupAnnotation(
        page, ap.Rectangle(310, 713, 410, 730, True)
    )
    page.annotations.append(caret_annotation)

    document.save(outfile)
```

### Dapatkan Anotasi Caret

Untuk memeriksa anotasi caret, iterasi melalui anotasi halaman dan filter berdasarkan `CARET` jenis anotasi.

#### Muat dokumen dan halaman

```python
document = ap.Document(infile)
page = document.pages[1]
```

#### Cetak persegi panjang anotasi caret

```python
for annot in page.annotations:
    if annot.annotation_type == ap.annotations.AnnotationType.CARET:
        print(annot.rect)
```

#### Contoh lengkap

```python
def caret_annotations_get(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    for annot in page.annotations:
        if annot.annotation_type == ap.annotations.AnnotationType.CARET:
            print(annot.rect)
```

### Hapus Anotasi Caret

Alur kerja ini mengumpulkan anotasi caret terlebih dahulu, menghapusnya satu per satu, dan kemudian menyimpan file yang diperbarui.

#### Muat dokumen dan kumpulkan anotasi caret

```python
document = ap.Document(infile)
page = document.pages[1]

caret_annotations = [
    annot
    for annot in page.annotations
    if annot.annotation_type == ap.annotations.AnnotationType.CARET
]
```

#### Hapus anotasi dan simpan dokumen

```python
for annot in caret_annotations:
    page.annotations.delete(annot)

document.save(outfile)
```

#### Contoh lengkap

```python
def caret_annotations_delete(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    caret_annotations = [
        annot
        for annot in page.annotations
        if annot.annotation_type == ap.annotations.AnnotationType.CARET
    ]

    for annot in caret_annotations:
        page.annotations.delete(annot)

    document.save(outfile)
```

## Ganti Anotasi

### Tambah Ganti Anotasi

Anotasi penggantian menggabungkan anotasi caret dan anotasi coret yang dikelompokkan. Pola ini menandai teks yang harus diganti dan menautkan catatan pengganti ke konten yang dicoret.

#### Buka dokumen dan dapatkan halaman

```python
document = ap.Document(infile)
page = document.pages[1]
```

#### Buat anotasi caret untuk teks pengganti

```python
caret_annotation = ap.annotations.CaretAnnotation(
    page, ap.Rectangle(361.246, 727.908, 370.081, 735.107, True)
)
caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
caret_annotation.subject = "Inserted text 2"
caret_annotation.title = "Aspose User"
caret_annotation.color = ap.Color.blue
caret_annotation.popup = ap.annotations.PopupAnnotation(
    page, ap.Rectangle(310, 713, 410, 730, True)
)
```

#### Buat anotasi coret berkelompok

Tentukan area coret, tetapkan titik kuad, dan tautkan ke anotasi caret melalui `in_reply_to` dan `reply_type`.

```python
strikeout_annotation = ap.annotations.StrikeOutAnnotation(
    page, ap.Rectangle(318.407, 727.826, 368.916, 740.098, True)
)
strikeout_annotation.color = ap.Color.blue
strikeout_annotation.quad_points = [
    ap.Point(321.66, 739.416),
    ap.Point(365.664, 739.416),
    ap.Point(321.66, 728.508),
    ap.Point(365.664, 728.508),
]
strikeout_annotation.subject = "Cross-out"
strikeout_annotation.in_reply_to = caret_annotation
strikeout_annotation.reply_type = ap.annotations.ReplyType.GROUP
``` 

#### Tambahkan kedua anotasi dan simpan PDF

```python
page.annotations.append(caret_annotation)
page.annotations.append(strikeout_annotation)

document.save(outfile)
```

#### Contoh lengkap

```python
def replace_annotations_add(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    caret_annotation = ap.annotations.CaretAnnotation(
        page, ap.Rectangle(361.246, 727.908, 370.081, 735.107, True)
    )
    caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    caret_annotation.subject = "Inserted text 2"
    caret_annotation.title = "Aspose User"
    caret_annotation.color = ap.Color.blue
    caret_annotation.popup = ap.annotations.PopupAnnotation(
        page, ap.Rectangle(310, 713, 410, 730, True)
    )

    strikeout_annotation = ap.annotations.StrikeOutAnnotation(
        page, ap.Rectangle(318.407, 727.826, 368.916, 740.098, True)
    )
    strikeout_annotation.color = ap.Color.blue
    strikeout_annotation.quad_points = [
        ap.Point(321.66, 739.416),
        ap.Point(365.664, 739.416),
        ap.Point(321.66, 728.508),
        ap.Point(365.664, 728.508),
    ]
    strikeout_annotation.subject = "Cross-out"
    strikeout_annotation.in_reply_to = caret_annotation
    strikeout_annotation.reply_type = ap.annotations.ReplyType.GROUP

    page.annotations.append(caret_annotation)
    page.annotations.append(strikeout_annotation)

    document.save(outfile)
```

### Ambil Ganti Anotasi

Untuk mengidentifikasi anotasi pengganti, temukan anotasi coret yang dikelompokkan sebagai balasan ke anotasi lain. Contoh tersebut melakukan casting pada setiap anotasi coret sebelum memeriksa field hubungan nya.

#### Muat dokumen dan iterasi melalui anotasi

```python
document = ap.Document(infile)
page = document.pages[1]
```

#### Saring anotasi coret yang dikelompokkan

```python
for annot in page.annotations:
    if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT:
        sa = cast(ap.annotations.StrikeOutAnnotation, annot)
        if (
            sa.in_reply_to is not None
            and sa.reply_type == ap.annotations.ReplyType.GROUP
        ):
            print(f"Replace annotation rect: {sa.rect}")
```

#### Contoh lengkap

```python
def replace_annotations_get(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    for annot in page.annotations:
        if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT:
            sa = cast(ap.annotations.StrikeOutAnnotation, annot)
            if (
                sa.in_reply_to is not None
                and sa.reply_type == ap.annotations.ReplyType.GROUP
            ):
                print(f"Replace annotation rect: {sa.rect}")
```

### Hapus Ganti Anotasi

Alur kerja ini mengumpulkan anotasi coret yang digunakan untuk mengganti markup, menghapusnya dari halaman, dan menyimpan PDF output.

#### Muat dokumen dan kumpulkan anotasi pengganti

```python
document = ap.Document(infile)
page = document.pages[1]

replace_annotations = [
    cast(ap.annotations.StrikeOutAnnotation, annot)
    for annot in page.annotations
    if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
]
```

#### Hapus anotasi dan simpan dokumen

```python
for annot in replace_annotations:
    page.annotations.delete(annot)

document.save(outfile)
```

#### Contoh lengkap

```python
def replace_annotations_delete(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    replace_annotations = [
        cast(ap.annotations.StrikeOutAnnotation, annot)
        for annot in page.annotations
        if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
    ]

    for annot in replace_annotations:
        page.annotations.delete(annot)

    document.save(outfile)
```

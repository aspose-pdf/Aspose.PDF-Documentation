---
title: Anotasi Bentuk via Python
linktitle: Anotasi Bentuk
type: docs
weight: 20
url: /id/python-net/shape-annotations/
description: Pelajari cara menambahkan, memeriksa, dan menghapus anotasi garis, kotak, lingkaran, poligon, dan polilin dalam dokumen PDF menggunakan Aspose.PDF for Python via .NET.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Bekerja dengan anotasi PDF geometris di Python.
Abstract: Artikel ini menjelaskan cara membuat, membaca, dan menghapus anotasi bentuk dalam dokumen PDF menggunakan Aspose.PDF for Python via .NET. Artikel ini mencakup anotasi garis, persegi, lingkaran, poligon, dan polilin, dengan setiap alur kerja diuraikan menjadi langkah‑langkah kecil dan contoh kode lengkap.
---

Artikel ini menunjukkan cara bekerja dengan anotasi bentuk dalam dokumen PDF menggunakan Aspose.PDF untuk Python via .NET.

Skrip contoh menunjukkan beberapa alur kerja anotasi berbasis geometri:

- anotasi garis
- anotasi kotak
- anotasi lingkaran
- anotasi poligon
- anotasi polyline

## Anotasi Garis 

### Tambahkan Anotasi Garis 

Contoh ini menambahkan anotasi garis ke halaman pertama dan mengonfigurasi gaya panah, lebar garis, serta jendela popup.

#### Buka PDF sumber

```python
document = ap.Document(infile)
```

#### Buat dan konfigurasikan anotasi garis

```python
line_annotation = ap.annotations.LineAnnotation(
    document.pages[1],
    ap.Rectangle(550, 93, 562, 439, True),
    ap.Point(556, 99),
    ap.Point(556, 443),
)

line_annotation.title = "John Smith"
line_annotation.color = ap.Color.red
line_annotation.width = 3
line_annotation.starting_style = ap.annotations.LineEnding.OPEN_ARROW
line_annotation.ending_style = ap.annotations.LineEnding.OPEN_ARROW
```

#### Lampirkan popup dan simpan PDF

```python
popup = ap.annotations.PopupAnnotation(
    document.pages[1],
    ap.Rectangle(842, 124, 1021, 266, True),
)
line_annotation.popup = popup

document.pages[1].annotations.append(line_annotation)
document.save(outfile)
```

#### Contoh lengkap

```python
def line_annotation_add(infile, outfile):
    document = ap.Document(infile)

    line_annotation = ap.annotations.LineAnnotation(
        document.pages[1],
        ap.Rectangle(550, 93, 562, 439, True),
        ap.Point(556, 99),
        ap.Point(556, 443),
    )

    line_annotation.title = "John Smith"
    line_annotation.color = ap.Color.red
    line_annotation.width = 3
    line_annotation.starting_style = ap.annotations.LineEnding.OPEN_ARROW
    line_annotation.ending_style = ap.annotations.LineEnding.OPEN_ARROW

    popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(842, 124, 1021, 266, True),
    )
    line_annotation.popup = popup

    document.pages[1].annotations.append(line_annotation)
    document.save(outfile)
```

### Dapatkan Anotasi Garis 

Untuk memeriksa anotasi garis, filter koleksi anotasi pada halaman pertama dan cast setiap hasil ke `LineAnnotation` sehingga Anda dapat membaca titik awal dan akhir nya.

#### Muat PDF dan kumpulkan anotasi garis

```python
document = ap.Document(infile)

line_annotation = [
    cast(ap.annotations.LineAnnotation, annotation)
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.LINE
]
```

#### Cetak koordinat garis

```python
for annotation in line_annotation:
    print(
        f"[{annotation.starting.x},{annotation.starting.y}]"
        f"-[{annotation.ending.x},{annotation.ending.y}]"
    )
```

#### Contoh lengkap

```python
def line_annotations_get(infile, outfile):
    document = ap.Document(infile)

    line_annotation = [
        cast(ap.annotations.LineAnnotation, annotation)
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.LINE
    ]

    for annotation in line_annotation:
        print(
            f"[{annotation.starting.x},{annotation.starting.y}]"
            f"-[{annotation.ending.x},{annotation.ending.y}]"
        )
```

### Hapus Anotasi Garis 

Alur kerja ini menghapus semua anotasi garis dari halaman pertama dan menyimpan PDF yang telah diperbarui.

#### Temukan anotasi baris untuk dihapus

```python
document = ap.Document(infile)
page = document.pages[1]

line_annotations = [
    annotation
    for annotation in page.annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.LINE
]
```

#### Hapus anotasi dan simpan PDF

```python
for annotation in line_annotations:
    page.annotations.delete(annotation)

document.save(outfile)
```

#### Contoh lengkap

```python
def line_annotations_delete(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    line_annotations = [
        annotation
        for annotation in page.annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.LINE
    ]

    for annotation in line_annotations:
        page.annotations.delete(annotation)

    document.save(outfile)
```


## Anotasi Kotak dan Lingkaran

### Tambahkan Anotasi Kotak 

Anotasi kotak sangat berguna untuk menandai area persegi panjang dalam sebuah dokumen. Contoh ini membuat anotasi kotak dengan pengaturan border, fill, dan transparansi.

#### Buka PDF dan buat anotasi kotak

```python
document = ap.Document(infile)

square_annotation = ap.annotations.SquareAnnotation(
    document.pages[1],
    ap.Rectangle(60, 600, 250, 450, True),
)
square_annotation.title = "John Smith"
square_annotation.color = ap.Color.blue
square_annotation.interior_color = ap.Color.blue_violet
square_annotation.opacity = 0.25
```

#### Tambahkan anotasi dan simpan PDF

```python
document.pages[1].annotations.append(square_annotation)
document.save(outfile)
```

#### Contoh lengkap

```python
def square_annotation_add(infile, outfile):
    document = ap.Document(infile)

    square_annotation = ap.annotations.SquareAnnotation(
        document.pages[1],
        ap.Rectangle(60, 600, 250, 450, True),
    )
    square_annotation.title = "John Smith"
    square_annotation.color = ap.Color.blue
    square_annotation.interior_color = ap.Color.blue_violet
    square_annotation.opacity = 0.25

    document.pages[1].annotations.append(square_annotation)
    document.save(outfile)
```

### Dapatkan Anotasi Persegi 

Untuk memeriksa anotasi persegi, filter anotasi halaman pertama berdasarkan `SQUARE` ketik dan cetak setiap persegi panjang.

#### Muat dokumen dan kumpulkan anotasi persegi

```python
document = ap.Document(infile)
square_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
]
```

#### Cetak persegi panjang anotasi

```python
for annotation in square_annotations:
    print(annotation.rect)
```

#### Contoh lengkap

```python
def square_annotation_get(infile, outfile):
    document = ap.Document(infile)
    square_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
    ]

    for annotation in square_annotations:
        print(annotation.rect)
```

### Hapus Anotasi Kotak 

Alur kerja ini menghapus semua anotasi persegi dari halaman pertama dan menyimpan dokumen.

#### Temukan dan hapus anotasi kotak

```python
document = ap.Document(infile)
square_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
]

for annotation in square_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### Contoh lengkap

```python
def square_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    square_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
    ]

    for annotation in square_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

### Tambahkan Anotasi Lingkaran 

Anotasi lingkaran menandai area bulat dalam PDF. Contoh ini menambahkan anotasi lingkaran dengan warna isi, opasitas, dan anotasi popup.

#### Buka PDF dan buat anotasi lingkaran

```python
document = ap.Document(infile)

circle_annotation = ap.annotations.CircleAnnotation(
    document.pages[1],
    ap.Rectangle(270, 160, 483, 383, True),
)
circle_annotation.title = "John Smith"
circle_annotation.color = ap.Color.red
circle_annotation.interior_color = ap.Color.misty_rose
circle_annotation.opacity = 0.5
```

#### Lampirkan popup dan simpan PDF

```python
circle_annotation.popup = ap.annotations.PopupAnnotation(
    document.pages[1],
    ap.Rectangle(842, 316, 1021, 459, True),
)

document.pages[1].annotations.append(circle_annotation)
document.save(outfile)
```

#### Contoh lengkap

```python
def circle_annotation_add(infile, outfile):
    document = ap.Document(infile)

    circle_annotation = ap.annotations.CircleAnnotation(
        document.pages[1],
        ap.Rectangle(270, 160, 483, 383, True),
    )
    circle_annotation.title = "John Smith"
    circle_annotation.color = ap.Color.red
    circle_annotation.interior_color = ap.Color.misty_rose
    circle_annotation.opacity = 0.5
    circle_annotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(842, 316, 1021, 459, True),
    )

    document.pages[1].annotations.append(circle_annotation)
    document.save(outfile)
```

### Dapatkan Anotasi Lingkaran 

Untuk memeriksa anotasi lingkaran, filter anotasi halaman berdasarkan `CIRCLE` ketik dan cetak persegi panjang mereka.

#### Muat dokumen dan kumpulkan anotasi lingkaran

```python
document = ap.Document(infile)
circle_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
]
```

#### Cetak persegi panjang anotasi

```python
for annotation in circle_annotations:
    print(annotation.rect)
```

#### Contoh lengkap

```python
def circle_annotation_get(infile, outfile):
    document = ap.Document(infile)
    circle_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
    ]

    for annotation in circle_annotations:
        print(annotation.rect)
```

### Hapus Anotasi Lingkaran 

Alur kerja ini menghapus semua anotasi lingkaran dari halaman pertama dan menyimpan PDF output.

#### Temukan dan hapus anotasi lingkaran

```python
document = ap.Document(infile)
circle_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
]

for annotation in circle_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### Contoh lengkap

```python
def circle_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    circle_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
    ]

    for annotation in circle_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```


## Anotasi Poligon dan PolyLine

### Tambahkan Anotasi Poligon 

Anotasi poligon mendefinisikan bentuk multi-titik tertutup. Contoh ini membuat anotasi poligon dari sebuah persegi panjang dan daftar titik.

#### Buka PDF dan buat anotasi poligon

```python
document = ap.Document(infile)

polygon_annotation = ap.annotations.PolygonAnnotation(
    document.pages[1],
    ap.Rectangle(200, 300, 400, 400, True),
    [
        ap.Point(200, 300),
        ap.Point(220, 300),
        ap.Point(250, 330),
        ap.Point(300, 304),
        ap.Point(300, 400),
    ],
)
polygon_annotation.title = "John Smith"
polygon_annotation.color = ap.Color.blue
polygon_annotation.interior_color = ap.Color.blue_violet
polygon_annotation.opacity = 0.25
```

#### Tambahkan anotasi dan simpan PDF

```python
document.pages[1].annotations.append(polygon_annotation)
document.save(outfile)
```

#### Contoh lengkap

```python
def polygon_annotation_add(infile, outfile):
    document = ap.Document(infile)

    polygon_annotation = ap.annotations.PolygonAnnotation(
        document.pages[1],
        ap.Rectangle(200, 300, 400, 400, True),
        [
            ap.Point(200, 300),
            ap.Point(220, 300),
            ap.Point(250, 330),
            ap.Point(300, 304),
            ap.Point(300, 400),
        ],
    )
    polygon_annotation.title = "John Smith"
    polygon_annotation.color = ap.Color.blue
    polygon_annotation.interior_color = ap.Color.blue_violet
    polygon_annotation.opacity = 0.25

    document.pages[1].annotations.append(polygon_annotation)
    document.save(outfile)
```

### Dapatkan Anotasi Poligon 

Untuk memeriksa anotasi poligon, filter anotasi halaman pertama berdasarkan `POLYGON` ketik dan cetak setiap persegi panjang anotasi.

#### Muat dokumen dan kumpulkan anotasi poligon

```python
document = ap.Document(infile)
polygon_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
]
```

#### Cetak persegi panjang anotasi

```python
for annotation in polygon_annotations:
    print(annotation.rect)
```

#### Contoh lengkap

```python
def polygon_annotation_get(infile, outfile):
    document = ap.Document(infile)
    polygon_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
    ]

    for annotation in polygon_annotations:
        print(annotation.rect)
```

### Hapus Anotasi Poligon 

Alur kerja ini menghapus semua anotasi poligon dari halaman pertama dan menyimpan PDF yang diperbarui.

#### Temukan dan hapus anotasi poligon

```python
document = ap.Document(infile)
polygon_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
]

for annotation in polygon_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### Contoh lengkap

```python
def polygon_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    polygon_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
    ]

    for annotation in polygon_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

### Tambahkan Anotasi PolyLine 

Anotasi polyline mendefinisikan jalur terbuka melalui beberapa titik. Contoh ini membuat anotasi polyline dengan catatan popup.

#### Buka PDF dan buat anotasi polyline

```python
document = ap.Document(infile)

polyline_annotation = ap.annotations.PolylineAnnotation(
    document.pages[1],
    ap.Rectangle(270, 193, 571, 383, True),
    [
        ap.Point(545, 150),
        ap.Point(545, 190),
        ap.Point(667, 190),
        ap.Point(667, 110),
        ap.Point(626, 111),
    ],
)
polyline_annotation.title = "John Smith"
polyline_annotation.color = ap.Color.red
```

#### Lampirkan popup dan simpan PDF

```python
polyline_annotation.popup = ap.annotations.PopupAnnotation(
    document.pages[1],
    ap.Rectangle(842, 196, 1021, 338, True),
)

document.pages[1].annotations.append(polyline_annotation)
document.save(outfile)
```

#### Contoh lengkap

```python
def polyline_annotation_add(infile, outfile):
    document = ap.Document(infile)

    polyline_annotation = ap.annotations.PolylineAnnotation(
        document.pages[1],
        ap.Rectangle(270, 193, 571, 383, True),
        [
            ap.Point(545, 150),
            ap.Point(545, 190),
            ap.Point(667, 190),
            ap.Point(667, 110),
            ap.Point(626, 111),
        ],
    )
    polyline_annotation.title = "John Smith"
    polyline_annotation.color = ap.Color.red
    polyline_annotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(842, 196, 1021, 338, True),
    )

    document.pages[1].annotations.append(polyline_annotation)
    document.save(outfile)
```

### Dapatkan Anotasi PolyLine 

Untuk memeriksa anotasi polyline, filter anotasi halaman berdasarkan `POLY_LINE` ketik dan cetak persegi panjang mereka.

#### Muat dokumen dan kumpulkan anotasi polyline

```python
document = ap.Document(infile)
polyline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
]
```

#### Cetak persegi panjang anotasi

```python
for annotation in polyline_annotations:
    print(annotation.rect)
```

#### Contoh lengkap

```python
def polyline_annotation_get(infile, outfile):
    document = ap.Document(infile)
    polyline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
    ]

    for annotation in polyline_annotations:
        print(annotation.rect)
```

### Hapus Anotasi PolyLine 

Alur kerja ini menghapus semua anotasi polyline dari halaman pertama dan menyimpan PDF output.

#### Temukan dan hapus anotasi polyline

```python
document = ap.Document(infile)
polyline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
]

for annotation in polyline_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### Contoh lengkap

```python
def polyline_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    polyline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
    ]

    for annotation in polyline_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

## Topik Terkait

- [Impor dan Ekspor Anotasi](/python-net/import-export-annotations/)
- [Anotasi Interaktif](/python-net/interactive-annotations/)
- [Anotasi Penandaan](/python-net/markup-annotations/)
- [Anotasi Media](/python-net/media-annotations/)
- [Anotasi Keamanan](/python-net/security-annotations/)
- [Anotasi Berbasis Teks](/python-net/text-based-annotations/)
- [Anotasi Watermark](/python-net/watermark-annotations/)

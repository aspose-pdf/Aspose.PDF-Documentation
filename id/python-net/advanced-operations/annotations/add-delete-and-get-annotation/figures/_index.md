---
title: Tambahkan Anotasi Gambar menggunakan Python
linktitle: Anotasi Gambar
type: docs
weight: 30
url: /id/python-net/figures-annotation/
description: Artikel ini menjelaskan cara menambahkan, mengambil, dan menghapus anotasi gambar dari dokumen PDF Anda dengan Aspose.PDF untuk Python via .NET
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Panduan cara memanipulasi anotasi Gambar dalam PDF
Abstract: Artikel ini menyediakan panduan komprehensif tentang menambahkan, mengambil, dan menghapus anotasi persegi, lingkaran, poligon, dan polyline dalam dokumen PDF menggunakan Aspose.PDF untuk Python. Anotasi persegi dan lingkaran secara visual menyoroti area spesifik pada halaman PDF dengan bentuk persegi panjang dan elips, masing-masing. Artikel ini menyertakan instruksi langkah demi langkah serta potongan kode Python untuk membuat anotasi ini dengan memuat file PDF, mengonfigurasi properti anotasi seperti judul, warna, dan opasitas, dan menambahkannya ke halaman PDF. Selain itu, artikel ini menjelaskan metode untuk mengambil anotasi berdasarkan tipe, mencetak dimensi persegi panjangnya, dan menghapusnya dari dokumen PDF. Anotasi poligon dan polyline juga dibahas, di mana poligon didefinisikan oleh serangkaian titik yang terhubung membentuk bentuk tertutup, sementara polyline menghubungkan titik secara terbuka. Dokumen ini menyediakan contoh kode untuk mengilustrasikan proses penambahan anotasi ini ke PDF, serta metode untuk mengakses dan menghapusnya.

---

## Tambahkan Anotasi Persegi dan Lingkaran

Dalam dokumen PDF, anotasi persegi mengacu pada jenis anotasi tertentu yang direpresentasikan dengan bentuk persegi. Anotasi persegi digunakan untuk menyoroti atau menarik perhatian ke area atau bagian tertentu dalam dokumen.

[Persegi](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation/) dan [Lingkaran](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/circleannotation/) anotasi akan menampilkan, masing-masing, sebuah persegi panjang atau elips pada halaman.

Langkah-langkah untuk membuat Anotasi Persegi atau Lingkaran:

1. Muat file PDF - baru [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Buat [SquareAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation) baru dan atur parameter (Rectangle baru, judul, warna, interior_color, opacity).
1. Setelah itu kita perlu Menambahkan Anotasi Persegi ke halaman.

Potongan kode berikut menunjukkan cara menambahkan Anotasi Persegi dalam halaman PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    squareAnnotation = ap.annotations.SquareAnnotation(document.pages[1], ap.Rectangle(60, 600, 250, 450, True))
    squareAnnotation.title = "John Smith"
    squareAnnotation.color = ap.Color.blue
    squareAnnotation.interior_color = ap.Color.blue_violet
    squareAnnotation.opacity = 0.25

    document.pages[1].annotations.append(squareAnnotation)

    document.save(output_file)
```

Potongan kode berikut menunjukkan cara menambahkan Anotasi Lingkaran dalam halaman PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_file)

    circleAnnotation = ap.annotations.CircleAnnotation(
        document.pages[1], ap.Rectangle(270, 160, 483, 383, True)
    )
    circleAnnotation.title = "John Smith"
    circleAnnotation.color = ap.Color.red
    circleAnnotation.interior_color = ap.Color.misty_rose
    circleAnnotation.opacity = 0.5
    circleAnnotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1], ap.Rectangle(842, 316, 1021, 459, True)
    )

    document.pages[1].annotations.append(circleAnnotation)
    document.save(output_file)
```

Sebagai contoh, kita akan melihat hasil berikut dari penambahan anotasi Persegi dan Lingkaran ke dokumen PDF:

![Demo Anotasi Lingkaran dan Persegi](circle_demo.png)

### Dapatkan Anotasi Lingkaran

Silakan coba menggunakan potongan kode berikut untuk Mendapatkan Anotasi Lingkaran dari dokumen PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    circleAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CIRCLE)
    ]

    for ca in circleAnnotations:
        print(ca.rect)
```

### Dapatkan Anotasi Persegi

Silakan coba menggunakan potongan kode berikut untuk Mendapatkan Anotasi Persegi dari dokumen PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squareAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUARE)
    ]

    for pa in squareAnnotations:
        print(pa.rect)
```


### Hapus Anotasi Lingkaran

Potongan kode berikut menunjukkan cara menghapus Anotasi Lingkaran dari file PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    circleAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CIRCLE)
    ]

    for ca in circleAnnotations:
        document.pages[1].annotations.delete(ca)

    document.save(output_file)
```

### Hapus Anotasi Persegi

Potongan kode berikut menunjukkan cara menghapus Anotasi Persegi dari file PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squareAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUARE)
    ]

    for pa in squareAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```

## Tambahkan Anotasi Poligon dan Polyline

Alat Polyline memungkinkan Anda membuat bentuk dan kontur dengan jumlah sisi yang arbitrer pada dokumen.

[Anotasi Poligon](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polygonannotation/) merepresentasikan poligon pada halaman. Mereka dapat memiliki jumlah titik apa saja yang terhubung dengan garis lurus.

[Anotasi Polyline](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polylineannotation/) juga mirip dengan poligon, satu-satunya perbedaan adalah bahwa titik pertama dan terakhir tidak terhubung secara implisit.

Langkah-langkah kami membuat anotasi Poligon:

1. Muat file PDF - baru [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Buat [Polygon Annotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polygonannotation) baru dan atur parameter Poligon (Rectangle baru, Points baru, judul, warna, interior_color dan opacity).
1. Setelah itu kita dapat Menambahkan anotasi ke halaman.

Potongan kode berikut menunjukkan cara menambahkan Anotasi Poligon ke file PDF:

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    polygonAnnotation = ap.annotations.PolygonAnnotation(
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
    polygonAnnotation.title = "John Smith"
    polygonAnnotation.color = ap.Color.blue
    polygonAnnotation.interior_color = ap.Color.blue_violet
    polygonAnnotation.opacity = 0.25

    document.pages[1].annotations.append(polygonAnnotation)
    document.save(output_file)
```

Potongan kode berikut menunjukkan cara menambahkan Anotasi Polyline ke file PDF:

1. Muat file PDF - baru [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Buat [Anotasi Polyline](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polylineannotation/) baru dan atur parameter Poligon (Rectangle baru, Points baru, judul, warna, interior_color dan opacity).
1. Setelah itu kita dapat Menambahkan anotasi ke halaman.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    polylineAnnotation = ap.annotations.PolylineAnnotation(
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
    polylineAnnotation.title = "John Smith"
    polylineAnnotation.color = ap.Color.red
    polylineAnnotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1], ap.Rectangle(842, 196, 1021, 338, True)
    )

    document.pages[1].annotations.append(polylineAnnotation)
    document.save(output_file)
```

### Dapatkan Anotasi Poligon dan Polyline

Silakan coba menggunakan potongan kode berikut untuk Mendapatkan Anotasi Poligon dalam dokumen PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    polygonAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLYGON)
    ]

    for pa in polygonAnnotations:
        print(pa.rect)
```

Silakan coba menggunakan potongan kode berikut untuk Mendapatkan Anotasi Polyline dalam dokumen PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    polylineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLY_LINE)
    ]

    for pa in polylineAnnotations:
        print(pa.rect)
```

### Hapus Anotasi Poligon dan Polyline

Potongan kode berikut menunjukkan cara menghapus Anotasi Poligon dari file PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    polygonAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLYGON)
    ]

    for pa in polygonAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```

Potongan kode berikut menunjukkan cara menghapus anotasi Polyline dari file PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    polylineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLY_LINE)
    ]

    for pa in polylineAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```



---
title: Tambahkan Anotasi Gambar menggunakan Python
linktitle: Anotasi Gambar
type: docs
weight: 30
url: /python-net/figures-annotation/
description: Artikel ini menjelaskan bagaimana cara menambahkan, mendapatkan, dan menghapus anotasi gambar dari dokumen PDF Anda dengan Aspose.PDF untuk Python melalui .NET
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Tambahkan Anotasi Gambar menggunakan Python",
    "alternativeHeadline": "Cara menambahkan Anotasi Gambar dalam PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, python, anotasi gambar, anotasi poligon, anotasi garis, anotasi persegi, anotasi lingkaran",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Tim Dokumentasi Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "penjualan",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "penjualan",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "penjualan",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/figures-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/figures-annotation/"
    },
    "dateModified": "2023-02-04",
    "description": "Artikel ini menjelaskan bagaimana cara menambahkan, mendapatkan, dan menghapus anotasi gambar dari dokumen PDF Anda dengan Aspose.PDF untuk Python"
}
</script>


## Tambahkan Anotasi Persegi dan Lingkaran

Dalam dokumen PDF, anotasi persegi mengacu pada jenis anotasi tertentu yang diwakili oleh bentuk persegi. Anotasi persegi digunakan untuk menyoroti atau menarik perhatian ke area atau bagian tertentu dalam dokumen.

Anotasi [Persegi](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation/) dan [Lingkaran](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/circleannotation/) akan menampilkan, masing-masing, sebuah persegi panjang atau elips pada halaman.

Langkah-langkah untuk membuat Anotasi Persegi atau Lingkaran:

1. Muat file PDF - baru [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
2. Buat [SquareAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation) baru dan atur parameter (Rectangle baru, judul, warna, warna_interior, opasitas).
3. Setelah itu kita perlu menambahkan Anotasi Persegi ke halaman.

Cuplikan kode berikut menunjukkan bagaimana menambahkan Anotasi Persegi pada halaman PDF.

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

Cuplikan kode berikut menunjukkan kepada Anda cara menambahkan Anotasi Lingkaran di halaman PDF.

```python

    import aspose.pdf as ap

    # Buka dokumen
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


Sebagai contoh, kita akan melihat hasil menambahkan anotasi Persegi dan Lingkaran ke dokumen PDF berikut ini:

![Demo Anotasi Lingkaran dan Persegi](circle_demo.png)

### Dapatkan Anotasi Lingkaran

Silakan coba gunakan potongan kode berikut untuk mendapatkan Anotasi Lingkaran dari dokumen PDF.

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

Silakan coba gunakan potongan kode berikut untuk mendapatkan Anotasi Persegi dari dokumen PDF.

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

The following code snippet shows how to Delete Circle Annotation from PDF file.

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

### Hapus Anotasi Kotak

Cuplikan kode berikut menunjukkan cara Menghapus Anotasi Kotak dari file PDF.

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

## Tambahkan Anotasi Poligon dan Polilinier

Alat Polilinier memungkinkan Anda membuat bentuk dan garis dengan jumlah sisi sembarang pada dokumen.

[Polygon Annotations](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polygonannotation/) mewakili poligon pada halaman. Mereka dapat memiliki sejumlah titik yang dihubungkan oleh garis lurus.

[Polyline Annotations](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polylineannotation/) juga mirip dengan poligon, perbedaannya hanya pada titik pertama dan terakhir yang tidak terhubung secara implisit.

Langkah-langkah dengan mana kita membuat anotasi Poligon:

1. Muat file PDF - baru [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
2. Buat [Polygon Annotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polygonannotation) baru dan atur parameter Poligon (Rectangle baru, Points baru, judul, warna, warna interior, dan opasitas).
3. Setelah itu kita bisa menambahkan anotasi ke halaman.

Cuplikan kode berikut menunjukkan cara menambahkan Anotasi Poligon ke file PDF:

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


Berikut adalah cuplikan kode yang menunjukkan cara menambahkan Anotasi Polyline ke file PDF:

1. Muat file PDF - baru [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
2. Buat [Polyline Annotations](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polylineannotation/) baru dan atur parameter Poligon (Rectangle baru, Points baru, judul, warna, interior_color, dan opacity).
3. Setelah itu kita bisa menambahkan anotasi ke halaman.

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


### Dapatkan Anotasi Poligon dan Garis Poligon

Silakan coba gunakan potongan kode berikut untuk Mendapatkan Anotasi Poligon dalam dokumen PDF.

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

Silakan coba gunakan potongan kode berikut untuk Mendapatkan Anotasi Garis Poligon dalam dokumen PDF.

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

### Hapus Anotasi Poligon dan Garis Poligon

Potongan kode berikut menunjukkan cara Menghapus Anotasi Poligon dari file PDF.

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


Potongan kode berikut menunjukkan cara Menghapus Anotasi Polyline dari file PDF.

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

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF untuk Pustaka Python",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Pustaka Manipulasi PDF untuk Python",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
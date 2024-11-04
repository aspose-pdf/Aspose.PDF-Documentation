---
title: Anotasi Ekstra menggunakan Python
linktitle: Anotasi Ekstra
type: docs
weight: 60
url: /python-net/extra-annotations/
description: Bagian ini menjelaskan cara menambah, mendapatkan, dan menghapus jenis anotasi ekstra dari dokumen PDF Anda.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Anotasi Ekstra menggunakan Python",
    "alternativeHeadline": "Cara menambah Anotasi Ekstra dalam PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generasi dokumen pdf",
    "keywords": "pdf, python, anotasi tautan, anotasi caret",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/python-net/extra-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/extra-annotations/"
    },
    "dateModified": "2023-02-04",
    "description": "Bagian ini menjelaskan cara menambah, mendapatkan, dan menghapus jenis anotasi ekstra dari dokumen PDF Anda dengan Python."
}
</script>


## Cara menambahkan Anotasi Caret ke dalam file PDF yang sudah ada melalui Python

Anotasi Caret adalah simbol yang menunjukkan pengeditan teks. Anotasi Caret juga merupakan anotasi markup, sehingga kelas Caret diturunkan dari kelas Markup dan juga menyediakan fungsi untuk mendapatkan atau mengatur properti Anotasi Caret dan mengatur ulang alur tampilan Anotasi Caret. Anotasi caret sering digunakan untuk menyarankan perubahan, penambahan, atau perubahan pada teks.

Langkah-langkah untuk membuat anotasi Caret:

1. Muat file PDF - baru [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Buat baru [CaretAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/caretannotation/) dan atur parameter Caret (new Rectangle, title, subject, flags, color). Anotasi ini digunakan untuk menunjukkan penyisipan teks.
1. Setelah kami dapat menambahkan anotasi ke halaman.

Cuplikan kode berikut menunjukkan cara menambahkan Anotasi Caret ke file PDF:

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_file)

    caretAnnotation1 = ap.annotations.CaretAnnotation(
        document.pages[1], ap.Rectangle(200, 700.664, 308.708, 740.769, True)
    )
    caretAnnotation1.title = "Pengguna Aspose"
    caretAnnotation1.subject = "Teks yang dimasukkan 1"
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

    # Muat file PDF
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

## Tambahkan Anotasi Tautan

[Tautan](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/linkannotation/) adalah anotasi yang membuka URL atau berpindah ke posisi tertentu di dalam dokumen yang sama atau dokumen eksternal saat Anda mengklik.

A Link Annotations adalah area persegi panjang yang dapat ditempatkan di mana saja pada halaman. Setiap tautan memiliki tindakan PDF yang sesuai yang terkait dengannya. Tindakan ini dilakukan ketika pengguna mengklik area tautan ini.

Cuplikan kode berikut menunjukkan cara menambahkan Link Annotation ke file PDF menggunakan contoh nomor telepon:

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    # Buat objek TextFragmentAbsorber untuk menemukan nomor telepon
    textFragmentAbsorber = ap.text.TextFragmentAbsorber("file")

    # Terima penyerap hanya untuk halaman pertama
    document.pages[1].accept(textFragmentAbsorber)

    phoneNumberFragment = textFragmentAbsorber.text_fragments[1]

    # Buat Link Annotation dan atur tindakan untuk memanggil nomor telepon
    linkAnnotation = ap.annotations.LinkAnnotation(document.pages[1], phoneNumberFragment.rectangle)
    linkAnnotation.action = ap.annotations.GoToURIAction("www.aspose.com")

    # Tambahkan anotasi ke halaman
    document.pages[1].annotations.append(linkAnnotation)
    document.save(output_file)
```


### Dapatkan Anotasi Tautan

Silakan coba gunakan cuplikan kode berikut untuk Mendapatkan [LinkAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations.linkannotation/) dari dokumen PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    linkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in linkAnnotations:
        print(la.rect)
```

### Hapus Anotasi Tautan

Cuplikan kode berikut menunjukkan cara Menghapus Anotasi Tautan dari file PDF. Untuk ini kita perlu menemukan dan menghapus semua anotasi tautan pada halaman pertama. Setelah ini kita akan menyimpan dokumen dengan anotasi yang telah dihapus.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for hs in highlightAnnotations:
        document.pages[1].annotations.delete(hs)

    document.save(output_file)
```


## Menyunting Wilayah Halaman Tertentu dengan Anotasi Redaksi menggunakan Aspose.PDF untuk Python

Aspose.PDF untuk Python via .NET mendukung fitur untuk menambah serta memanipulasi Anotasi dalam file PDF yang ada. Anotasi Redaksi dalam dokumen PDF berfungsi untuk secara permanen menghapus atau menyembunyikan informasi rahasia dari dokumen. Proses pengeditan informasi melibatkan penutupan atau pengarsiran konten tertentu, seperti teks, gambar, atau grafik, dengan cara yang membatasi visibilitas dan aksesibilitasnya kepada orang lain. Ini memastikan bahwa informasi sensitif tetap tersembunyi dan terlindungi dalam dokumen. Untuk memenuhi kebutuhan ini, sebuah kelas bernama [RedactionAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/redactionannotation/) disediakan, yang dapat digunakan untuk menyunting wilayah halaman tertentu atau dapat digunakan untuk memanipulasi Redaksi Anotasi yang ada dan menyuntingnya (yaitu, memipihkan anotasi dan menghapus teks di bawahnya).

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


### Dapatkan Anotasi Redaksi

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

### Hapus Anotasi Redaksi

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

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF untuk Perpustakaan Python",
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
    "applicationCategory": "Perpustakaan Manipulasi PDF untuk Python",
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
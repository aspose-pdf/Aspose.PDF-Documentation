---
title: Hapus Gambar dari File PDF menggunakan Python
linktitle: Hapus Gambar
type: docs
weight: 20
url: id/python-net/delete-images-from-pdf-file/
description: Bagian ini menjelaskan cara menghapus Gambar dari File PDF menggunakan Aspose.PDF untuk Python melalui .NET.
lastmod: "2023-04-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Hapus Gambar dari File PDF menggunakan Python",
    "alternativeHeadline": "Cara menghapus Gambar dari PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generasi dokumen pdf",
    "keywords": "pdf, python, hapus, hapus gambar dari pdf",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Tim Dokumen Aspose.PDF",
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
    "url": "/python-net/delete-images-from-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/delete-images-from-pdf-file/"
    },
    "dateModified": "2023-02-04",
    "description": "Bagian ini menjelaskan cara menghapus Gambar dari File PDF menggunakan Aspose.PDF untuk Python melalui .NET."
}
</script>


Ada banyak alasan untuk menghapus semua atau gambar tertentu dari PDF.

Terkadang file PDF mungkin berisi gambar penting yang perlu dihapus untuk melindungi privasi atau mencegah akses tidak sah ke informasi tertentu.

Menghapus gambar yang tidak diinginkan atau berlebihan dapat membantu mengurangi ukuran file, sehingga lebih mudah untuk membagikan atau menyimpan PDF.

Jika perlu, Anda dapat mengurangi jumlah halaman dengan menghapus semua gambar dari dokumen. Juga, menghapus gambar dari dokumen akan membantu mempersiapkan PDF untuk kompresi atau ekstraksi informasi teks.

**Aspose.PDF untuk Python via .NET** akan membantu Anda dengan tugas ini.

## Hapus Gambar dari File PDF

Untuk menghapus gambar dari file PDF:

1. Buka Dokumen PDF yang ada.
1. Hapus gambar tertentu.
1. Simpan file PDF yang telah diperbarui.

Cuplikan kode berikut menunjukkan cara menghapus gambar dari file PDF.

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_file)

    # Hapus gambar tertentu
    document.pages[2].resources.images.delete(1)

    # Simpan file PDF yang telah diperbarui
    document.save(output_pdf)
```


## Hapus semua gambar dari PDF input

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_file)

    # Hapus semua gambar di semua halaman
    for i in range(len(document.pages)):
        while len(document.pages[i + 1].resources.images) != 0:
            document.pages[i + 1].resources.images.delete(1)

    # Simpan file PDF yang diperbarui
    document.save(output_file)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
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
    "applicationCategory": "PDF Manipulation Library for Python via .NET",
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
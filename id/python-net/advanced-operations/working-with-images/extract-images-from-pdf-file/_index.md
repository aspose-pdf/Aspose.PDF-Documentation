---
title: Ekstrak Gambar dari File PDF menggunakan Python
linktitle: Ekstrak Gambar
type: docs
weight: 30
url: /id/python-net/extract-images-from-pdf-file/
description: Bagian ini menunjukkan cara mengekstrak gambar dari file PDF menggunakan pustaka Python.
lastmod: "2023-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Ekstrak Gambar dari File PDF dengan Python",
    "alternativeHeadline": "Cara mengekstrak Gambar dari PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, Python, ekstrak gambar dari pdf",
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
    "url": "/python-net/extract-images-from-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/extract-images-from-pdf-file/"
    },
    "dateModified": "2023-02-04",
    "description": "Bagian ini menunjukkan cara mengekstrak gambar dari file PDF menggunakan pustaka Python."
}
</script>


Apakah Anda perlu memisahkan gambar dari file PDF Anda? Untuk memudahkan manajemen, pengarsipan, analisis, atau berbagi gambar dari dokumen Anda, gunakan **Aspose.PDF untuk Python** dan ekstrak gambar dari file PDF.

Gambar disimpan dalam koleksi [resources](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) di setiap halaman dalam koleksi [XImage](https://reference.aspose.com/pdf/python-net/aspose.pdf/ximagecollection/). Untuk mengekstrak halaman tertentu, kemudian dapatkan gambar dari koleksi Images menggunakan indeks gambar tertentu.

Indeks gambar mengembalikan objek [XImage](https://reference.aspose.com/pdf/python-net/aspose.pdf/ximage/). Objek ini menyediakan metode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) yang dapat digunakan untuk menyimpan gambar yang diekstrak. Cuplikan kode berikut menunjukkan cara mengekstrak gambar dari file PDF.

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_file)

    # Ekstrak gambar tertentu
    xImage = document.pages[2].resources.images[1]
    outputImage = io.FileIO(output_image, "w")

    # Simpan gambar keluaran
    xImage.save(outputImage)
    outputImage.close()
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF untuk Python Library",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Library Manipulasi PDF untuk Python",
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
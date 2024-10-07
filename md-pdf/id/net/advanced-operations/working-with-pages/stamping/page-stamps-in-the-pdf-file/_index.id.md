---
title: Menambahkan Cap Halaman PDF dalam PDF menggunakan C#
linktitle: Cap halaman dalam Berkas PDF
type: docs
weight: 30
url: /net/page-stamps-in-the-pdf-file/
description: Menambahkan cap halaman pada dokumen PDF menggunakan kelas PdfPageStamp dengan pustaka Aspose.PDF untuk .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Menambahkan Cap Halaman PDF dalam PDF menggunakan C#",
    "alternativeHeadline": "Menambahkan Cap Halaman PDF dalam PDF menggunakan C#",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, pembuatan dokumen",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Tim Dok Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
    "url": "/net/page-stamps-in-the-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/page-stamps-in-the-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Menambahkan cap halaman pada dokumen PDF menggunakan kelas PdfPageStamp dengan pustaka Aspose.PDF untuk .NET."
}
</script>
## Menambahkan Cap Halaman dengan C\#

[PdfPageStamp](https://reference.aspose.com/pdf/net/aspose.pdf/PdfPageStamp) dapat digunakan ketika Anda perlu menerapkan cap komposit yang berisi grafik, teks, tabel. Contoh berikut menunjukkan cara menggunakan cap untuk membuat kertas bergaya seperti menggunakan Adobe InDesign, Illustrator, Microsoft Word. Asumsikan kita memiliki beberapa dokumen masukan dan kita ingin menerapkan 2 jenis bingkai dengan warna biru dan plum.

Potongan kode berikut juga berfungsi dengan perpustakaan [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
public static void AddPageStamp()
{
    var inputFileName = "sample-4pages.pdf";
    var outputFileName = "AddPageStamp_out.pdf";
    var pageStampFileName = "PageStamp.pdf";
    var document = new Document(_dataDir + inputFileName);

    var bluePageStamp = new PdfPageStamp(_dataDir + pageStampFileName, 1)
    {
        Height = 800,
        Background = true
    };

    var plumPageStamp = new PdfPageStamp(_dataDir + pageStampFileName, 2)
    {
        Height = 800,
        Background = true
    };

    for (int i = 1; i < 5; i++)
    {
        if (i % 2 == 0)
            document.Pages[i].AddStamp(bluePageStamp);
        else
            document.Pages[i].AddStamp(plumPageStamp);
    }

    document.Save(_dataDir + outputFileName);
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Perpustakaan Aspose.PDF untuk .NET",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
    "applicationCategory": "Perpustakaan Manipulasi PDF untuk .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```


---
title: Memisahkan PDF secara programatik
linktitle: Memisahkan file PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /id/net/split-pdf-document/
description: Topik ini menunjukkan cara memisahkan halaman PDF menjadi file PDF individu dalam aplikasi .NET Anda dengan C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Split PDF programmatically",
    "alternativeHeadline": "Effortlessly split PDF into individual files with C#",
    "abstract": "Memungkinkan pengembang untuk memisahkan dokumen PDF secara programatik menjadi file individu menggunakan C#. Fitur ini menyederhanakan pengelolaan konten PDF dengan memungkinkan ekstraksi halaman yang berbeda ke dalam file PDF terpisah dalam aplikasi .NET, meningkatkan efisiensi alur kerja dan kemampuan penanganan dokumen",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "326",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
    "url": "/net/split-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/split-pdf-document/"
    },
    "dateModified": "2024-11-26",
    "description": "Topik ini menunjukkan cara memisahkan halaman PDF menjadi file PDF individu dalam aplikasi .NET Anda dengan C#."
}
</script>

## Contoh Langsung

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) adalah aplikasi web gratis online yang memungkinkan Anda menyelidiki bagaimana fungsi pemisahan presentasi bekerja.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

Topik ini menunjukkan cara memisahkan halaman PDF menjadi file PDF individu dalam aplikasi .NET Anda. Untuk memisahkan halaman PDF menjadi file PDF satu halaman menggunakan C#, langkah-langkah berikut dapat diikuti:

1. Loop melalui halaman dokumen PDF melalui koleksi [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Untuk setiap iterasi, buat objek Document baru dan tambahkan objek [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) individu ke dalam dokumen kosong.
1. Simpan PDF baru menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

Cuplikan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

## Memisahkan PDF menjadi beberapa file atau pdf terpisah

Cuplikan kode C# berikut menunjukkan cara memisahkan halaman PDF menjadi file PDF individu.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document1 = new Aspose.Pdf.Document(dataDir + "SplitToPages.pdf"))
    {
        int pageCount = 1;

        // Loop through all the pages
        foreach (var page in document1.Pages)
        {
            // Create PDF document
            using (var document2 = new Aspose.Pdf.Document())
            {
                document2.Pages.Add(page);
                // Save PDF document
                document2.Save(dataDir + "Page_" + pageCount + "_out.pdf");
                pageCount++;
            }
        }
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
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
    "applicationCategory": "PDF Manipulation Library for .NET",
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
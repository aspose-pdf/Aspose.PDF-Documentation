---
title: Cara Menggabungkan PDF menggunakan C#
linktitle: Menggabungkan file PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /id/net/merge-pdf-documents/
description: Halaman ini menjelaskan cara menggabungkan dokumen PDF menjadi satu file PDF dengan C# atau VB.NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "How to Merge PDF using C#",
    "alternativeHeadline": "Combine PDF Effortlessly Using C#",
    "abstract": "Temukan kemampuan kuat untuk dengan mudah menggabungkan beberapa dokumen PDF menjadi satu file menggunakan C# dengan pustaka Aspose.PDF. Fitur ini memungkinkan pengembang untuk menyederhanakan alur kerja mereka dengan menggabungkan PDF secara efisien, menjaga kualitas dan struktur sepanjang proses. Sempurna untuk integrasi perangkat lunak, fungsionalitas ini meningkatkan produktivitas dengan menyederhanakan tugas manajemen dokumen.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "411",
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
    "url": "/net/merge-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/merge-pdf-documents/"
    },
    "dateModified": "2024-11-26",
    "description": "Halaman ini menjelaskan cara menggabungkan dokumen PDF menjadi satu file PDF dengan C# atau VB.NET."
}
</script>

## Menggabungkan atau mengkombinasikan beberapa PDF menjadi satu PDF di C#

Menggabungkan PDF di C# bukanlah tugas yang sederhana tanpa menggunakan pustaka pihak ketiga. Artikel ini menunjukkan cara menggabungkan beberapa file PDF menjadi satu dokumen PDF menggunakan Aspose.PDF for .NET. Contoh ini ditulis dalam C# tetapi API dapat digunakan dalam bahasa pemrograman .NET lainnya seperti VB.NET. File PDF digabungkan sehingga yang pertama disatukan di akhir dokumen lainnya.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Menggabungkan File PDF

Untuk menggabungkan dua file PDF:

1. Buat dua objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document), masing-masing berisi salah satu file PDF input.
1. Kemudian panggil metode Add dari koleksi [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) untuk objek Document yang ingin Anda tambahkan file PDF lainnya.
1. Lewati koleksi PageCollection dari objek Document kedua ke metode Add dari koleksi PageCollection pertama.
1. Terakhir, simpan file PDF output menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

Potongan kode berikut menunjukkan cara menggabungkan file PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MergeDocuments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "Concat1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "Concat2.pdf"))
        {
            // Add pages of second document to the first
            document1.Pages.Add(document2.Pages);

            // Save PDF document
            document1.Save(dataDir + "MergeDocuments_out.pdf");
        }
    }
}
```

## Contoh Langsung

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) adalah aplikasi web gratis online yang memungkinkan Anda untuk menyelidiki bagaimana fungsionalitas penggabungan presentasi bekerja.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)

## Lihat juga

- [Pecah PDF menggunakan DOM](https://docs.aspose.com/pdf/net/split-pdf-document/)
- [Gabungkan dokumen PDF menggunakan Facades](https://docs.aspose.com/pdf/net/concatenate-pdf-documents/)
- [Pecah PDF menggunakan Facades](https://docs.aspose.com/pdf/net/split-pdf-pages/)

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
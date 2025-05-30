---
title: Menghapus lampiran dari PDF
linktitle: Menghapus lampiran dari PDF yang ada
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /id/net/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF dapat menghapus lampiran dari dokumen PDF Anda. Gunakan API PDF C# untuk menghapus lampiran dalam file PDF menggunakan pustaka Aspose.PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Removing attachment from PDF",
    "alternativeHeadline": "Remove Attachments Efficiently from PDF Files",
    "abstract": "Aspose.PDF kini mencakup fitur kuat yang memungkinkan pengguna untuk dengan mudah menghapus lampiran dari dokumen PDF mereka menggunakan API PDF C#. Fungsionalitas ini menyederhanakan manajemen PDF dengan memungkinkan pengguna untuk menghapus file yang disematkan dari dokumen mereka, memastikan pengalaman PDF yang lebih bersih dan lebih teratur.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Removing attachment from PDF, Aspose.PDF, delete attachments, PDF API, C# PDF library, EmbeddedFiles collection, document.Save method, PDF manipulation, attachments management, Aspose.PDF for .NET",
    "wordcount": "229",
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
    "url": "/net/removing-attachment-from-an-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/removing-attachment-from-an-existing-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat menghapus lampiran dari dokumen PDF Anda. Gunakan API PDF C# untuk menghapus lampiran dalam file PDF menggunakan pustaka Aspose.PDF."
}
</script>

Aspose.PDF dapat menghapus lampiran dari file PDF. Lampiran dokumen PDF disimpan dalam koleksi EmbeddedFiles dari objek Document.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

Untuk menghapus semua lampiran yang terkait dengan file PDF:

1. Panggil metode [Delete](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection/methods/delete) dari koleksi [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection).
1. Simpan file yang diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) dari objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

Potongan kode berikut menunjukkan cara menghapus lampiran dari dokumen PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteAllAttachments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DeleteAllAttachments.pdf"))
    {
        // Delete all attachments
        document.EmbeddedFiles.Delete();

        // Save PDF document
        document.Save(dataDir + "DeleteAllAttachments_out.pdf");
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
---
title: Menambahkan Lampiran pada Dokumen PDF
linktitle: Menambahkan Lampiran pada Dokumen PDF
type: docs
weight: 10
url: /net/add-attachment-to-pdf-document/
description: Halaman ini menjelaskan cara menambahkan lampiran pada file PDF dengan library Aspose.PDF untuk .NET
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/adding-to-a-pdf-document/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Menambahkan Lampiran pada Dokumen PDF",
    "alternativeHeadline": "Cara menambahkan lampiran pada PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen PDF",
    "keywords": "pdf, c#, lampiran dalam pdf",
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
    "url": "/net/add-attachment-to-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-attachment-to-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Halaman ini menjelaskan cara menambahkan lampiran pada file PDF dengan library Aspose.PDF untuk .NET"
}
</script>
Lampiran dapat mengandung berbagai informasi dan dapat berupa berbagai jenis file. Artikel ini menjelaskan cara menambahkan lampiran ke file PDF.

Potongan kode berikut juga berfungsi dengan antarmuka grafis [Aspose.Drawing](/pdf/net/drawing/) yang baru.

1. Buat proyek C# baru.
1. Tambahkan referensi ke Aspose.PDF DLL.
1. Buat objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Buat objek [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification) dengan file yang Anda tambahkan, dan deskripsi file.
1. Tambahkan objek [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification) ke koleksi [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) dari objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document), dengan metode Add koleksi tersebut.

Koleksi [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) berisi semua lampiran dalam file PDF.
Koleksi [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) berisi semua lampiran dalam file PDF.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "AddAttachment.pdf");

// Siapkan file baru untuk ditambahkan sebagai lampiran
FileSpecification fileSpecification = new FileSpecification(dataDir + "test.txt", "File teks contoh");

// Tambahkan lampiran ke koleksi lampiran dokumen
pdfDocument.EmbeddedFiles.Add(fileSpecification);

// Simpan dokumen yang telah diperbarui
pdfDocument.Save(dataDir + "AddllAnnotations_out.pdf");
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



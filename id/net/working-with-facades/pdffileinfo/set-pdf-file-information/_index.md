---
title: Atur Informasi File PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /id/net/set-pdf-file-information/
description: Bagian ini menjelaskan cara mengatur Informasi File PDF dengan Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Set PDF File Information",
    "alternativeHeadline": "Set Custom Metadata for PDF Files Effortlessly",
    "abstract": "Tingkatkan manajemen file PDF Anda dengan fungsionalitas baru di Aspose.PDF for .NET yang memungkinkan Anda dengan mudah mengatur dan memperbarui informasi spesifik file seperti Penulis, Judul, dan Kata Kunci. Manfaatkan kelas PdfFileInfo untuk secara efisien memodifikasi PDF Anda, menambahkan metadata berharga untuk meningkatkan organisasi dan kemampuan pencarian. Permudah alur kerja Anda dengan menyimpan pembaruan ini secara mulus menggunakan metode SaveNewInfo",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "251",
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
    "url": "/net/set-pdf-file-information/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/set-pdf-file-information/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga dapat menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

[Kelas PdfFileInfo](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileinfo) memungkinkan Anda untuk mengatur informasi spesifik file dari file PDF. Anda perlu membuat objek dari [Kelas PdfFileInfo](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileinfo) dan kemudian mengatur berbagai properti spesifik file seperti Penulis, Judul, Kata Kunci, dan Pencipta, dll. Akhirnya, simpan file PDF yang diperbarui menggunakan metode [SaveNewInfo](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades.pdffileinfo/savenewinfo/methods/1) dari objek [PdfFileInfo](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileinfo).

Cuplikan kode berikut menunjukkan kepada Anda cara mengatur informasi file PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPdfInfo()
{
    // Define the directory for input and output files
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create PdfFileInfo object to work with PDF metadata
    using (var fileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "sample.pdf"))
    {
        // Set PDF information
        fileInfo.Author = "Aspose";
        fileInfo.Title = "Hello World!";
        fileInfo.Keywords = "Peace and Development";
        fileInfo.Creator = "Aspose";
        
        // Save the PDF with updated information
        fileInfo.SaveNewInfo(dataDir + "SetFileInfo_out.pdf");
    }
}
```

## Atur Info Meta

Metode [SetMetaInfo](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileinfo/methods/setmetainfo) memungkinkan Anda untuk menambahkan informasi apa pun. Dalam contoh kami, kami menambahkan sebuah field. Periksa cuplikan kode berikut: 

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetMetaInfo()
{
    // Define the directory for input and output files
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of the PdfFileInfo object
    using (var fileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "sample.pdf"))
    {
        // Set a new custom attribute as meta info
        fileInfo.SetMetaInfo("Reviewer", "Aspose.PDF user");

        // Save the updated file
        fileInfo.SaveNewInfo(dataDir + "SetMetaInfo_out.pdf");
    }
}
```
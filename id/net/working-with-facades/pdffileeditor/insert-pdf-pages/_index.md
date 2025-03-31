---
title: Sisipkan Halaman PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /id/net/insert-pdf-pages/
description: Bagian ini menjelaskan cara menyisipkan halaman PDF dengan Aspose.PDF Facades menggunakan kelas PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Insert PDF pages",
    "alternativeHeadline": "Insert Specific PDF Pages into Existing Documents",
    "abstract": "Optimalkan manajemen PDF Anda dengan fitur baru yang memungkinkan pengguna untuk menyisipkan halaman tertentu dari satu PDF ke PDF lainnya menggunakan kelas PdfFileEditor. Fungsionalitas ini mendukung penyisipan halaman berbasis rentang dan berbasis array, meningkatkan efisiensi alur kerja dengan menggabungkan dokumen secara mulus melalui jalur file atau aliran.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "751",
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
    "url": "/net/insert-pdf-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/insert-pdf-pages/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Sisipkan Halaman PDF Antara Dua Nomor Menggunakan Jalur File

Rentang halaman tertentu dapat disisipkan dari satu PDF ke PDF lainnya menggunakan metode [Insert](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor). Untuk melakukan itu, Anda memerlukan file PDF input di mana Anda ingin menyisipkan halaman, file port dari mana halaman perlu diambil untuk penyisipan, lokasi di mana halaman akan disisipkan, dan rentang halaman dari file port yang harus disisipkan dalam file PDF input. Rentang ini ditentukan dengan parameter halaman awal dan halaman akhir. Akhirnya, file PDF output disimpan dengan rentang halaman yang ditentukan disisipkan dalam file input. Potongan kode berikut menunjukkan cara menyisipkan halaman PDF antara dua nomor menggunakan aliran file.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertPdfPagesBetweenTwoNumbersUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Insert pages
    pdfEditor.Insert(
        dataDir + "MultiplePages.pdf", 1, 
        dataDir + "InsertPages.pdf", 2, 5, 
        dataDir + "InsertPagesBetweenNumbers_out.pdf");
}
```

## Sisipkan Array Halaman PDF Menggunakan Jalur File

Jika Anda ingin menyisipkan beberapa halaman tertentu ke dalam file PDF lainnya, maka Anda dapat menggunakan overload dari metode [Insert](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) yang memerlukan array integer dari halaman. Dalam array ini, Anda dapat menentukan halaman tertentu mana yang ingin Anda sisipkan dalam file PDF input. Untuk melakukan itu, Anda memerlukan file PDF input di mana Anda ingin menyisipkan halaman, file port dari mana halaman perlu diambil untuk penyisipan, lokasi di mana halaman akan disisipkan, dan array integer dari halaman dari file port yang harus disisipkan dalam file PDF input. Array ini berisi daftar halaman tertentu yang Anda minati untuk disisipkan dalam file PDF input. Akhirnya, file PDF output disimpan dengan array halaman yang ditentukan disisipkan dalam file input. Potongan kode berikut menunjukkan cara menyisipkan array halaman PDF menggunakan jalur file.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertArrayOfPdfPagesUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    var pagesToInsert = new int[] { 2, 3 };
    // Insert pages
    pdfEditor.Insert(
        dataDir + "MultiplePages.pdf", 1, 
        dataDir + "InsertPages.pdf", pagesToInsert, 
        dataDir + "InsertArrayOfPages_out.pdf");
}
```

## Sisipkan Halaman PDF Antara Dua Nomor Menggunakan Aliran

Jika Anda ingin menyisipkan rentang halaman menggunakan aliran, Anda hanya perlu menggunakan overload yang sesuai dari metode [Insert](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdffileeditor). Untuk melakukan itu, Anda memerlukan aliran PDF input di mana Anda ingin menyisipkan halaman, aliran port dari mana halaman perlu diambil untuk penyisipan, lokasi di mana halaman akan disisipkan, dan rentang halaman dari aliran port yang harus disisipkan dalam aliran PDF input. Rentang ini ditentukan dengan parameter halaman awal dan halaman akhir. Akhirnya, aliran PDF output disimpan dengan rentang halaman yang ditentukan disisipkan dalam aliran input. Potongan kode berikut menunjukkan cara menyisipkan halaman PDF antara dua nomor menggunakan aliran.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertPdfPagesBetweenTwoNumbersUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (var portStream = new FileStream(dataDir + "InsertPages.pdf", FileMode.Open))
        {
            using (var outputStream = new FileStream(dataDir + "InsertPagesBetweenNumbersUsingStreams_out.pdf", FileMode.Create))
            {
                // Insert pages
                pdfEditor.Insert(inputStream, 1, portStream, 1, 4, outputStream);
            }
        }
    }
}
```

## Sisipkan Array Halaman PDF Menggunakan Aliran

Anda juga dapat menyisipkan array halaman ke dalam file PDF lainnya menggunakan aliran dengan bantuan overload yang sesuai dari metode Insert yang memerlukan array integer dari halaman. Dalam array ini, Anda dapat menentukan halaman tertentu mana yang ingin Anda sisipkan dalam aliran PDF input. Untuk melakukan itu, Anda memerlukan aliran PDF input di mana Anda ingin menyisipkan halaman, aliran port dari mana halaman perlu diambil untuk penyisipan, lokasi di mana halaman akan disisipkan, dan array integer dari halaman dari aliran port yang harus disisipkan dalam file PDF input. Array ini berisi daftar halaman tertentu yang Anda minati untuk disisipkan dalam aliran PDF input. Akhirnya, aliran PDF output disimpan dengan array halaman yang ditentukan disisipkan dalam file input. Potongan kode berikut menunjukkan cara menyisipkan array halaman PDF menggunakan aliran.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertArrayOfPdfPagesUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Pages to insert
    var pagesToInsert = new int[] { 2, 3 };
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (var portStream = new FileStream(dataDir + "InsertPages.pdf", FileMode.Open))
        {
            using (var outputStream = new FileStream(dataDir + "InsertPagesUsingStreams_out.pdf", FileMode.Create))
            {
                // Insert pages
                pdfEditor.Insert(inputStream, 1, portStream, pagesToInsert, outputStream);
            }
        }
    }
}
```
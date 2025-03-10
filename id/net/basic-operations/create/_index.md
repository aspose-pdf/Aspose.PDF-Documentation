---
title: Buat dokumen PDF secara programatis
linktitle: Buat PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /id/net/create-document/
description: Halaman ini menjelaskan cara membuat dokumen PDF dari awal dengan pustaka Aspose.PDF.
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Create PDF document programmatically",
    "alternativeHeadline": "Programmatic PDF Creation Made Easy with C#",
    "abstract": "Fitur baru dalam Aspose.PDF for .NET memungkinkan pengembang untuk membuat dokumen PDF secara programatis menggunakan C# dan VB.NET, menyederhanakan proses untuk berbagai aplikasi .NET seperti WinForms dan ASP.NET. Dengan metode sederhana untuk menambahkan halaman dan teks, pengguna dapat dengan mudah menghasilkan file PDF kustom dari awal, meningkatkan fungsionalitas aplikasi dan pengalaman pengguna mereka.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "307",
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
    "url": "/net/create-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-document/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas sederhana dan mudah tetapi juga dapat menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

Aspose.PDF for .NET API memungkinkan Anda untuk membuat dan membaca file PDF menggunakan C# dan VB.NET. API ini dapat digunakan dalam berbagai aplikasi .NET termasuk WinForms, ASP.NET, dan beberapa lainnya. Dalam artikel ini, kami akan menunjukkan cara menggunakan Aspose.PDF for .NET API untuk dengan mudah menghasilkan dan membaca file PDF dalam aplikasi .NET.

## Cara Membuat File PDF menggunakan C#

Untuk membuat file PDF menggunakan C#, langkah-langkah berikut dapat digunakan.

1. Buat objek dari kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Tambahkan objek [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) ke koleksi [Pages](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/pages) dari objek Document.
1. Tambahkan [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) ke koleksi [Paragraphs](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) dari halaman.
1. Simpan dokumen PDF yang dihasilkan.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void HelloWorld()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Add text to new page
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
        // Save PDF document
        document.Save(dataDir + "HelloWorld_out.pdf");
    }
}
```

Dalam hal ini, kami membuat dokumen PDF satu halaman dengan ukuran halaman A4, orientasi potret. Halaman kami akan berisi "Hello, World" di bagian kiri atas halaman.
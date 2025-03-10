---
title: Contoh Hello World menggunakan bahasa C#
linktitle: Contoh Hello World
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /id/net/hello-world-example/
description: Contoh ini menunjukkan cara membuat dokumen PDF sederhana dengan teks Hello World menggunakan Aspose.PDF
aliases:
    - /net/hello-world/
lastmod: "2022-02-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Example of Hello World using C# language",
    "alternativeHeadline": "Aspose.PDF C# example",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "302",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "http://docs.aspose.com/pdf/net/hello-world-example/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "http://docs.aspose.com/pdf/net/hello-world-example/"
    },
    "dateModified": "2024-11-26",
    "description": "Contoh ini menunjukkan cara membuat dokumen PDF sederhana dengan teks Hello World menggunakan Aspose.PDF",
    "articleBody": "A \"Hello World\" example is traditionally used to introduce features of a programming language or software with a simple use case.\nAspose.PDF for .NET is a feature rich PDF API that allows the developers to embed PDF document creation, manipulation & conversion capabilities in their .NET applications. It supports working with many popular file formats including PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX and image file formats. In this article, we are creating a PDF document containing text \"Hello World!\". After installing Aspose.PDF for .NET in your environment, you can execute below code sample to see how Aspose.PDF API works.\nBelow code snippet follows these steps:\n1. // Create PDF document\n2. Add a Page to document object\n3. Create a TextFragment\n4. Add TextFragment to Paragraph collection of the page\n5. Save resultant PDF document\nFollowing code snippet is a Hello World program to exhibit working of Aspose.PDF for .NET API."
}
</script>

Contoh "Hello World" secara tradisional digunakan untuk memperkenalkan fitur dari bahasa pemrograman atau perangkat lunak dengan kasus penggunaan yang sederhana.

Aspose.PDF for .NET adalah API PDF yang kaya fitur yang memungkinkan pengembang untuk menyematkan kemampuan pembuatan, manipulasi & konversi dokumen PDF dalam aplikasi .NET mereka. Ini mendukung bekerja dengan banyak format file populer termasuk PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX dan format file gambar. Dalam artikel ini, kami membuat dokumen PDF yang berisi teks "Hello World!". Setelah menginstal Aspose.PDF for .NET di lingkungan Anda, Anda dapat mengeksekusi contoh kode di bawah ini untuk melihat bagaimana API Aspose.PDF bekerja.

Potongan kode berikut juga bekerja dengan [Aspose.PDF.Drawing](/pdf/net/drawing/) pustaka.

Potongan kode di bawah ini mengikuti langkah-langkah ini:

1. Buat objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Tambahkan sebuah [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) ke objek dokumen.
1. Buat objek [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment).
1. Tambahkan TextFragment ke koleksi [Paragraph](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) dari halaman.
1. [Simpan](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) dokumen PDF yang dihasilkan.

Potongan kode berikut adalah program Hello World untuk menunjukkan cara kerja API Aspose.PDF for .NET.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void HelloWorld()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

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
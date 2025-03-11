---
title: ASP.NET tanpa menggunakan Visual Studio
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /id/net/asp-net-without-using-visual-studio/
description: Pelajari cara menggunakan Aspose.PDF for .NET dalam proyek ASP.NET tanpa bergantung pada Visual Studio. Ikuti panduan praktis ini.
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "ASP.NET without using Visual Studio",
    "alternativeHeadline": "Create ASP.NET Applications Without Visual Studio",
    "abstract": "Temukan cara untuk membuat aplikasi ASP.NET tanpa bergantung pada Visual Studio menggunakan Aspose.PDF for .NET. Pendekatan inovatif ini memungkinkan pengembang untuk menulis kode HTML dan C# atau VB.NET dalam satu file .aspx, menyederhanakan proses pembuatan dokumen PDF langsung dalam halaman ASP.NET. Maksimalkan efisiensi pengembangan Anda dengan integrasi yang mulus ini",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "263",
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
    "url": "/net/asp-net-without-using-visual-studio/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/asp-net-without-using-visual-studio/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga dapat mengatasi tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

{{% alert color="primary" %}}

[Aspose.PDF for .NET](/pdf/id/net/) dapat digunakan untuk mengembangkan halaman atau aplikasi ASP.NET tanpa menggunakan Visual Studio. Dalam contoh ini, kita akan menulis HTML dan kode C# atau VB.NET dalam satu file .aspx; ini biasanya dikenal sebagai Instant ASP.NET.

{{% /alert %}}

## Detail implementasi

{{% alert color="primary" %}}

Buat aplikasi web contoh dan salin Aspose.PDF.dll ke dalam direktori bernama "Bin" di direktori situs web Anda ( *jika folder bin tidak ada, buat satu* ). Kemudian buat halaman .aspx Anda dan salin kode berikut ke dalamnya.
Contoh ini menunjukkan cara menggunakan [Aspose.PDF for .NET](/pdf/id/net/) dengan kode inline dalam halaman ASP.NET untuk membuat dokumen PDF sederhana dengan beberapa teks contoh di dalamnya.
{{% /alert %}}

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
<%@ Page Language ="C#" %>
<%@ Import Namespace="System" %>
<%@ Import Namespace="System.IO" %>
<%@ Import Namespace="System.Data" %>
<%@ Import Namespace="Aspose.PDF" %>

<html>
    <head>
        <title> using Aspose.PDF for .NET with Inline ASP.NET</title>
    </head>
    <body>
        <h3>creation of simple PDF document while using Aspose.PDF for .NET with Inline ASP.NET</h3>
<%
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    // Set license
    Aspose.Pdf.License lic = new Aspose.Pdf.License();
    lic.SetLicense("Aspose.Total.lic");

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        Aspose.Pdf.Page page = document.Pages.Add();
        // Add text to new page
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
        // Save PDF document
        document.Save(dataDir + "HelloWorld_out.pdf");
    }
%>

    </body>
</html>
```
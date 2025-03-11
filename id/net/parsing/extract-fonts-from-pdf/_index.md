---
title: Ekstrak Font dari PDF C#
linktitle: Ekstrak Font dari PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /id/net/extract-fonts-from-pdf/
description: Gunakan pustaka Aspose.PDF untuk .NET untuk mengekstrak semua font yang disematkan dari dokumen PDF Anda.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Fonts from PDF C#",
    "alternativeHeadline": "Effortlessly Extract All Fonts from PDF Documents",
    "abstract": "Buka kekuatan dokumen PDF Anda dengan fungsionalitas pustaka Aspose.PDF for .NET yang memungkinkan Anda untuk dengan mudah mengekstrak semua font yang disematkan. Dengan menggunakan metode FontUtilities.GetAllFonts(), pengembang dapat dengan mudah mengakses dan mencantumkan font dalam file PDF mana pun, meningkatkan analisis dokumen dan kemampuan kustomisasi.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "156",
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
    "url": "/net/extract-fonts-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-fonts-from-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga dapat menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

Jika Anda ingin mendapatkan semua font dari dokumen PDF, Anda dapat menggunakan metode FontUtilities.GetAllFonts() yang disediakan dalam kelas Document. Silakan periksa cuplikan kode berikut untuk mendapatkan semua font dari dokumen PDF yang ada:

Cuplikan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/). 

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractFonts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractFonts.pdf"))
    {
        Aspose.Pdf.Text.Font[] fonts = document.FontUtilities.GetAllFonts();
        foreach (Aspose.Pdf.Text.Font font in fonts)
        {
            Console.WriteLine(font.FontName);
        }
    }
}
```
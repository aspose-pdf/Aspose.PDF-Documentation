---
title: Extract Fonts from PDF C#
linktitle: Extract Fonts from PDF
type: docs
weight: 30
url: /net/extract-fonts-from-pdf/
description: Use the Aspose.PDF for. NET library to extract all embedded fonts from your PDF document.
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
    "abstract": "Unlock the power of your PDF documents with the Aspose.PDF for .NET library functionality that allows you to effortlessly extract all embedded fonts. Utilizing the FontUtilities.GetAllFonts() method, developers can easily access and list fonts within any PDF file, enhancing document analysis and customization capabilities",
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
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

In case you want to get all fonts from a PDF document, you can use FontUtilities.GetAllFonts() method provided in Document class. Please check following code snippet in order to get all fonts from an existing PDF document:

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractFonts()
{
    // The path to the documents directory.
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open document
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

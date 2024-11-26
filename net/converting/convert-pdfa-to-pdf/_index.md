---
title: Convert PDF/A to PDF format 
linktitle: Convert PDF/A to PDF format
type: docs
weight: 110
url: /net/convert-pdfa-to-pdf/
lastmod: "2021-11-01"
description: This topic show you how to Aspose.PDF allows to convert PDF/A file to PDF document with .NET library. 
sitemap:
    changefreq: "monthly"
    priority: 0.8
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF/A to PDF format",
    "alternativeHeadline": "Remove PDF/A Compliance for Enhanced Document Flexibility in C#",
    "abstract": "Aspose.PDF now provides a feature to seamlessly convert PDF/A files to standard PDF documents using its .NET library. This functionality allows users to remove PDF/A compliance restrictions, enabling easier editing and modification of PDF content without the limitations imposed by PDF/A standards",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "259",
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
    "url": "/net/convert-pdfa-to-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdfa-to-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

## Convert PDF/A document to PDF

Convert PDF/A document to PDF means removing <abbr title="Portable Document Format Archive">PDF/A</abbr> restriction from the original document. 
Class [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) has method [RemovePdfaCompliance(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/removepdfacompliance) to remove the PDF compliance information from input/source file.

```csharp
public static void ConvertPDFAtoPDF()
{
    // For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    Document document = new Document(dataDir + "PDFAToPDF.pdf");
    // Remove PDF/A compliance information
    document.RemovePdfaCompliance();
    // Save updated document
    document.Save(dataDir + "PDFAToPDF_out.pdf");
}
```

This info also removes if you make any changes in the document (e.g. add pages). In the following example, the output document loses PDF/A compliance after the page adding.

```csharp
public static void ConvertPDFAtoPDFAdvanced()
{
    // For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    Document document = new Document(dataDir + "PDFAToPDF.pdf");
    // Adding a new (empty) page removes PDF/A compliance information.
    document.Pages.Add();
    // Save updated document
    document.Save(dataDir + "PDFAToPDF_out.pdf");
}
```

---
title: Create PDF document programmatically
linktitle: Create PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /net/create-document/
description: This page describes how to create PDF document from scratch with Aspose.PDF library.
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Create PDF document programmatically",
    "alternativeHeadline": "Programmatic PDF Creation Made Easy with C#",
    "abstract": "The new feature in Aspose.PDF for .NET allows developers to programmatically create PDF documents using C# and VB.NET, streamlining the process for various .NET applications like WinForms and ASP.NET. With simple methods to add pages and text, users can effortlessly generate custom PDF files from scratch, enhancing their application functionality and user experience",
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
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

Aspose.PDF for .NET API lets you create and read PDF files using C# and VB.NET. The API can be used in a variety of .NET applications including WinForms, ASP.NET, and several others. In this article, we are going to show how to use Aspose.PDF for .NET API to easily generate and read PDF files in .NET applications.

## How to Create PDF File using C#

To create a PDF file using C#, the following steps can be used.

1. Create an object of [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) class.
1. Add a [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) object to the [Pages](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/pages) collection of the Document object.
1. Add [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) to [Paragraphs](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) collection of the page.
1. Save the resultant PDF document.

The next code snippet also works with [Aspose.Drawing](/pdf/net/drawing/) library.

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

In this case, we create a PDF one-page document with A4 page size, portrait orientation. Our page will contain a "Hello, World" in the upper left part of the page.

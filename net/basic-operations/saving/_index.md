---
title: Save PDF document programmatically
linktitle: Save PDF
type: docs
weight: 30
url: /net/save-pdf-document/
description: Learn how to save PDF file in C# Aspose.PDF for .NET PDF library. Save PDF document to file system, to stream, and in Web applications.
aliases:
    - /net/saving/
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Save PDF document programmatically",
    "alternativeHeadline": "Programmatic PDF Saving with C#",
    "abstract": "Discover how developers programmatically save PDF documents with ease using Aspose.PDF for .NET. This feature supports saving PDFs to the file system, streams, and directly within web applications, accommodating varied use cases while ensuring compliance with PDF/A and PDF/X standards for long-term archiving and graphics exchange. Optimize your PDF handling capabilities with this robust saving mechanism",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "471",
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
                "telephone": "\u002B1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "\u002B44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "\u002B61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/save-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/save-pdf-document/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

The next code snippet also works with [Aspose.Drawing](/pdf/net/drawing/) library.

## Save PDF document to file system

You can save the created or manipulated PDF document to file system using `Save` method of `Document` class.
When you do not provide the format type (options), then the document is saved in Aspose.PDF v.1.7 (*.pdf) format.

```csharp
public static void SaveDocument()
{
    var originalFileName = dataDir + "SimpleResume.pdf";
    var modifiedFileName = dataDir + "SimpleResumeModified.pdf";

    var document = new Document(originalFileName);
    // make some manipation, i.g add new empty page
    document.Pages.Add();
    document.Save(modifiedFileName);
}
```

## Save PDF document to stream

You can also save the created or manipulated PDF document to stream by using overloads of `Save` methods.

```csharp
public static void SaveDocumentStream()
{
    var originalFileName = dataDir + "SimpleResume.pdf";
    var modifiedFileName = dataDir + "SimpleResumeModified.pdf";

    var document = new Document(originalFileName);
    // make some manipation, i.g add new empty page
    document.Pages.Add();
    document.Save(System.IO.File.OpenWrite(modifiedFileName));
}
```

## Save PDF document in Web applications

To save documents in Web applications, you can use the ways proposed above. In addition, the `Document` class has overloaded method `Save` for using with the [HttpResponse](https://docs.microsoft.com/en-us/dotnet/api/system.web.httpresponse?view=netframework-4.8) class.

```csharp
var originalFileName = dataDir + "SimpleResume.pdf";
var document = new Document(originalFileName);
// make some manipulation, i.g add a new empty page
document.Pages.Add();
document.Save(Response, originalFileName, ContentDisposition.Attachment, new PdfSaveOptions());
```

For more detailed explanation please follow to [Showcase](/pdf/net/showcases/) section.

## Save PDF/A or PDF/X format

PDF/A is an ISO-standardized version of the Portable Document Format (PDF) for use in archiving and long-term preservation of electronic documents.
PDF/A differs from PDF in that it prohibits features not suitable for long-term archiving, such as font linking (as opposed to font embedding) and encryption. ISO requirements for PDF/A viewers include color management guidelines, embedded font support, and a user interface for reading embedded annotations.

PDF/X is a subset of the PDF ISO standard. The purpose of PDF/X is to facilitate graphics exchange, and it therefore has a series of printing-related requirements which do not apply to standard PDF files.

In both cases, the `Save` method is used to store the documents, while the documents must be prepared using the `Convert` method.

```csharp
public static void SaveDocumentAsPDFx()
{
    var document = new Document("..\\..\\..\\Samples\\SimpleResume.pdf");
    document.Pages.Add();
    document.Convert(new PdfFormatConversionOptions(PdfFormat.PDF_X_3));
    document.Save("..\\..\\..\\Samples\\SimpleResume_X3.pdf");
}
```

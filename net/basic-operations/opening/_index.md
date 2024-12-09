---
title: Open PDF document programmatically
linktitle: Open PDF
type: docs
weight: 20
url: /net/open-pdf-document/
description: Learn how to open a PDF file in C# Aspose.PDF for .NET PDF library. You can open existing PDF, document from stream, and encrypted PDF document.
aliases:
    - /net/opening-a-pdf-document/
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Open PDF document programmatically",
    "alternativeHeadline": "Programmatically Open and Access Various PDF Documents with C#",
    "abstract": "Discover opening PDF documents with the Aspose.PDF for .NET library. This feature allows developers to seamlessly access existing PDFs, load documents from streams, and handle encrypted files with ease, enhancing workflow efficiency and expanding the capabilities of PDF manipulation in C#",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "238",
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
    "url": "/net/open-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/open-pdf-document/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

## Open existing PDF document

There are several ways to open a document. The easiest is to specify a file name.

```csharp
public static void OpenDocument()
{
    var fileName = @"C:\tmp\tourguidev2_gb_tags.pdf";
    using (var document = new Document(fileName))
    {
        Console.WriteLine($"Pages {document.Pages.Count}");
    }
}
```

## Open existing PDF document from stream

```csharp
public static void OpenDocumentStream()
{
    const string fileName = "SJPR0033_Folder_Utland_16sid_ENG_web3.pdf";
    var remoteUri = "https://www.sj.se/content/dam/SJ/pdf/Engelska/";
    // Create a new WebClient instance.
    var webClient = new WebClient();
    // Concatenate the domain with the Web resource filename.
    var strWebResource = remoteUri + fileName;
    Console.WriteLine("Downloading File \"{0}\" from \"{1}\" .......\n\n", fileName, strWebResource);

    var stream = new MemoryStream();
    webClient.OpenRead(strWebResource)?.CopyTo(stream);

    using (var document = new Document(stream))
    {
        Console.WriteLine($"Pages {document.Pages.Count}");
    }
}
```

## Open encrypted PDF document

```csharp
public static void OpenDocumentWithPassword()
{
    const string fileName = @"C:\tmp\DocSite.pdf";
    const string password = "Aspose2020";
    try
    {
        using (var document = new Document(fileName, password))
        {
            Console.WriteLine($"Pages {document.Pages.Count}");
        }
    }
    catch (InvalidPasswordException e)
    {
        Console.WriteLine(e);
    }
}
```

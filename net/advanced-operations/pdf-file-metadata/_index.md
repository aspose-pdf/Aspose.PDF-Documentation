---
title: Working with PDF File Metadata | C#
linktitle: PDF File Metadata
type: docs
weight: 140
url: /net/pdf-file-metadata/
description: This section explains how to get PDF file information, how to get XMP Metadata from a PDF file, set PDF File Information.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with PDF File Metadata | C#",
    "alternativeHeadline": "How to get PDF File Metadata",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, pdf file metadata",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
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
    "url": "/net/pdf-file-metadata/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-file-metadata/"
    },
    "dateModified": "2022-02-04",
    "description": "This section explains how to get PDF file information, how to get XMP Metadata from a PDF file, set PDF File Information."
}
</script>

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

## Get PDF File Information

In order to get file specific information of a PDF file, you first need to get the [DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo) object using [Info](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/info) property of the [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) object. Once the [DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo) object is retrieved, you can get the values of the individual properties. The following code snippet shows you how to get PDF file information.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Open document
Document pdfDocument = new Document(dataDir + "GetFileInfo.pdf");
// Get document information
DocumentInfo docInfo = pdfDocument.Info;
// Show document information
Console.WriteLine("Author: {0}", docInfo.Author);
Console.WriteLine("Creation Date: {0}", docInfo.CreationDate);
Console.WriteLine("Keywords: {0}", docInfo.Keywords);
Console.WriteLine("Modify Date: {0}", docInfo.ModDate);
Console.WriteLine("Subject: {0}", docInfo.Subject);
Console.WriteLine("Title: {0}", docInfo.Title);
```

## Set PDF File Information

Aspose.PDF for .NET allows you to set file-specific information for a PDF, information like author, creation date, subject, and title. To set this information:

1. Create a [DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo) object.
1. Set the values of the properties.
1. Save the updated document using the Document class’ Save method.

{{% alert color="primary" %}}

Please note that you cannot set values against the *Application* and *Producer* fields, because Aspose Ltd. and Aspose.PDF for .NET x.x.x will be displayed against these fields.

{{% /alert %}}

The following code snippet shows you how to set PDF file information.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Open document
Document pdfDocument = new Document(dataDir + "SetFileInfo.pdf");

// Specify document information
DocumentInfo docInfo = new DocumentInfo(pdfDocument);

docInfo.Author = "Aspose";
docInfo.CreationDate = DateTime.Now;
docInfo.Keywords = "Aspose.Pdf, DOM, API";
docInfo.ModDate = DateTime.Now;
docInfo.Subject = "PDF Information";
docInfo.Title = "Setting PDF Document Information";

dataDir = dataDir + "SetFileInfo_out.pdf";
// Save output document
pdfDocument.Save(dataDir);
```

## Get XMP Metadata from PDF File

Aspose.PDF allows you to access a PDF file's XMP metadata. To get a PDF file's metadata:

1. Create a [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) object and open the input PDF file.
1. Get the file's metadata using the [Metadata](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/metadata) property.

The following code snippet shows you how to get metadata from the PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Open document
Document pdfDocument = new Document(dataDir + "GetXMPMetadata.pdf");

// Get properties
Console.WriteLine(pdfDocument.Metadata["xmp:CreateDate"]);
Console.WriteLine(pdfDocument.Metadata["xmp:Nickname"]);
Console.WriteLine(pdfDocument.Metadata["xmp:CustomProperty"]);
```

## Set XMP Metadata in a PDF File

Aspose.PDF allows you to set metadata in a PDF file. To set metadata:

1. Create a [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) object.
1. Set metadata values using the [Metadata](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/metadata) property.
1. Save the updated document using the [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method of the [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) object.

The following code snippet shows you how to set metadata in a PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Open document
Document pdfDocument = new Document(dataDir + "SetXMPMetadata.pdf");

// Set properties
pdfDocument.Metadata["xmp:CreateDate"] = DateTime.Now;
pdfDocument.Metadata["xmp:Nickname"] = "Nickname";
pdfDocument.Metadata["xmp:CustomProperty"] = "Custom Value";

dataDir = dataDir + "SetXMPMetadata_out.pdf";
// Save document
pdfDocument.Save(dataDir);
```

## Insert Metadata with Prefix

Some developers need to create a new metadata namespace with a prefix. The following code snippet shows how to insert metadata with prefix.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Open document
Document pdfDocument = new Document(dataDir + "SetXMPMetadata.pdf");
pdfDocument.Metadata.RegisterNamespaceUri("xmp", "http:// Ns.adobe.com/xap/1.0/"); // Xmlns prefix was removed
pdfDocument.Metadata["xmp:ModifyDate"] = DateTime.Now;

dataDir = dataDir + "SetPrefixMetadata_out.pdf";
// Save document
pdfDocument.Save(dataDir);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>

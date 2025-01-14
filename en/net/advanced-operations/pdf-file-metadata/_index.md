---
title: Working with PDF File Metadata in C#
linktitle: PDF File Metadata
type: docs
weight: 200
url: /net/pdf-file-metadata/
description: Explore how to extract and manage PDF metadata, such as author and title, in .NET using Aspose.PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with PDF File Metadata in C#",
    "alternativeHeadline": "Extracting and Managing PDF Metadata in C#",
    "abstract": "Unlock the power of PDF file management with our new feature for C# developers, enabling seamless access to PDF file metadata. Gain insights into file properties, extract XMP metadata, and easily update document information, streamlining your document handling process. Experience enhanced functionality for maintaining and manipulating PDF metadata efficiently",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF file metadata, C# PDF manipulation, get PDF file information, set PDF file information, XMP metadata, Aspose.PDF for .NET, document properties, PDF metadata management",
    "wordcount": "834",
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
    "url": "/net/pdf-file-metadata/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-file-metadata/"
    },
    "dateModified": "2024-11-25",
    "description": "This section explains how to get PDF file information, how to get XMP Metadata from a PDF file, set PDF File Information."
}
</script>

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

## Get PDF File Information

In order to get file specific information of a PDF file, you first need to get the [DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo) object using [Info](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/info) property of the [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) object. Once the [DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo) object is retrieved, you can get the values of the individual properties. The following code snippet shows you how to get PDF file information.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void GetPDFFileInformation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetFileInfo.pdf"))
    {
        // Get document information
        var docInfo = document.Info;

        // Display document information
        Console.WriteLine("Author: {0}", docInfo.Author);
        Console.WriteLine("Creation Date: {0}", docInfo.CreationDate);
        Console.WriteLine("Keywords: {0}", docInfo.Keywords);
        Console.WriteLine("Modify Date: {0}", docInfo.ModDate);
        Console.WriteLine("Subject: {0}", docInfo.Subject);
        Console.WriteLine("Title: {0}", docInfo.Title);
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void GetPDFFileInformation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetFileInfo.pdf"))
    {
        // Get document information
        var docInfo = document.Info;
        // Display document information
        Console.WriteLine("Author: {0}", docInfo.Author);
        Console.WriteLine("Creation Date: {0}", docInfo.CreationDate);
        Console.WriteLine("Keywords: {0}", docInfo.Keywords);
        Console.WriteLine("Modify Date: {0}", docInfo.ModDate);
        Console.WriteLine("Subject: {0}", docInfo.Subject);
        Console.WriteLine("Title: {0}", docInfo.Title);
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## Set PDF File Information

Aspose.PDF for .NET allows you to set file-specific information for a PDF, information like author, creation date, subject, and title. To set this information:

1. Create a [DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo) object.
1. Set the values of the properties.
1. Save the updated document using the Document class’ Save method.

{{% alert color="primary" %}}

Please note that you cannot set values against the *Application* and *Producer* fields, because Aspose Ltd. and Aspose.PDF for .NET x.x.x will be displayed against these fields.

{{% /alert %}}

The following code snippet shows you how to set PDF file information.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void SetFileInformation()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetFileInfo.pdf"))
    {
        // Specify document information
        var docInfo = new Aspose.Pdf.DocumentInfo(document);

        docInfo.Author = "Aspose";
        docInfo.CreationDate = DateTime.Now;
        docInfo.Keywords = "Aspose.Pdf, DOM, API";
        docInfo.ModDate = DateTime.Now;
        docInfo.Subject = "PDF Information";
        docInfo.Title = "Setting PDF Document Information";

        // Save PDF document
        document.Save(dataDir + "SetFileInfo_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void SetFileInformation()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetFileInfo.pdf"))
    {
        // Specify document information
        var docInfo = new Aspose.Pdf.DocumentInfo(document);

        docInfo.Author = "Aspose";
        docInfo.CreationDate = DateTime.Now;
        docInfo.Keywords = "Aspose.Pdf, DOM, API";
        docInfo.ModDate = DateTime.Now;
        docInfo.Subject = "PDF Information";
        docInfo.Title = "Setting PDF Document Information";

        // Save PDF document
        document.Save(dataDir + "SetFileInfo_out.pdf");
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## Get XMP Metadata from PDF File

Aspose.PDF allows you to access a PDF file's XMP metadata. To get a PDF file's metadata:

1. Create a [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) object and open the input PDF file.
1. Get the file's metadata using the [Metadata](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/metadata) property.

The following code snippet shows you how to get metadata from the PDF file.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void GetXMPMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetXMPMetadata.pdf"))
    {
        // Get and display properties
        Console.WriteLine($"Create Date: {document.Metadata["xmp:CreateDate"]}");
        Console.WriteLine($"Nickname: {document.Metadata["xmp:Nickname"]}");
        Console.WriteLine($"Custom Property: {document.Metadata["xmp:CustomProperty"]}");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void GetXMPMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetXMPMetadata.pdf"))
    {
        // Get and display properties
        Console.WriteLine($"Create Date: {document.Metadata["xmp:CreateDate"]}");
        Console.WriteLine($"Nickname: {document.Metadata["xmp:Nickname"]}");
        Console.WriteLine($"Custom Property: {document.Metadata["xmp:CustomProperty"]}");
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## Set XMP Metadata in a PDF File

Aspose.PDF allows you to set metadata in a PDF file. To set metadata:

1. Create a [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) object.
1. Set metadata values using the [Metadata](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/metadata) property.
1. Save the updated document using the [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method of the [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) object.

The following code snippet shows you how to set metadata in a PDF file.

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void SetXMPMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetXMPMetadata.pdf"))
    {
        // Set properties
        document.Metadata["xmp:CreateDate"] = DateTime.Now.ToString("o");
        document.Metadata["xmp:Nickname"] = "Nickname";
        document.Metadata["xmp:CustomProperty"] = "Custom Value";

        // Save PDF document
        document.Save(dataDir + "SetXMPMetadata_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void SetXMPMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetXMPMetadata.pdf"))
    {
        // Set properties
        document.Metadata["xmp:CreateDate"] = DateTime.Now.ToString("o");
        document.Metadata["xmp:Nickname"] = "Nickname";
        document.Metadata["xmp:CustomProperty"] = "Custom Value";

        // Save PDF document
        document.Save(dataDir + "SetXMPMetadata_out.pdf");
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## Insert Metadata with Prefix

Some developers need to create a new metadata namespace with a prefix. The following code snippet shows how to insert metadata with prefix.

{{< tabs tabID="5" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrefixMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetXMPMetadata.pdf"))
    {
        // Register a namespace URI for the 'xmp' prefix
        document.Metadata.RegisterNamespaceUri("xmp", "http://ns.adobe.com/xap/1.0/");

        // Set the metadata property using the registered prefix
        document.Metadata["xmp:ModifyDate"] = DateTime.Now.ToString("o"); // ISO 8601 format for datetime

        // Save PDF document
        document.Save(dataDir + "SetPrefixMetadata_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrefixMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetXMPMetadata.pdf"))
    {
        // Register a namespace URI for the 'xmp' prefix
        document.Metadata.RegisterNamespaceUri("xmp", "http://ns.adobe.com/xap/1.0/");

        // Set the metadata property using the registered prefix
        document.Metadata["xmp:ModifyDate"] = DateTime.Now.ToString("o"); // ISO 8601 format for datetime

        // Save PDF document
        document.Save(dataDir + "SetPrefixMetadata_out.pdf");
    }
}
```
{{< /tab >}}
{{< /tabs >}}
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

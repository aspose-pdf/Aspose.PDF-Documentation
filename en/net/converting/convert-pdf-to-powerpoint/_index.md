---
title: Convert PDF to PowerPoint in .NET
linktitle: Convert PDF to PowerPoint
type: docs
weight: 30
url: /net/convert-pdf-to-powerpoint/
lastmod: "2021-11-01"
description: Aspose.PDF allows you to convert PDF to PPT (PowerPoint) format using .NET. One way there is a possibility to convert PDF to PPTX with Slides as Images.
lastmod: "2021-10-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to PowerPoint in .NET",
    "alternativeHeadline": "Convert PDF Documents to PowerPoint Presentations Efficiently in C#",
    "abstract": "Aspose.PDF for .NET introduces a powerful feature enabling seamless conversion of PDF documents to PowerPoint (PPTX) format, allowing each PDF page to transform into a distinct slide. With the option to render text as selectable or as images, users can easily customize their presentations while tracking conversion progress efficiently. Optimize your document workflow by leveraging this innovative functionality for enhanced productivity",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1174",
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
    "url": "/net/convert-pdf-to-powerpoint/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-powerpoint/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Overview

This article explains how to **convert PDF to PowerPoint using C#**. It covers these topics.

_Format_: **PPTX**
- [C# PDF to PPTX](#csharp-pdf-to-pptx)
- [C# Convert PDF to PPTX](#csharp-pdf-to-pptx)
- [C# How to convert PDF file to PPTX](#csharp-pdf-to-pptx)

_Format_: **PowerPoint**
- [C# PDF to PowerPoint](#csharp-pdf-to-powerpoint)
- [C# Convert PDF to PowerPoint](#csharp-pdf-to-powerpoint)
- [C# How to convert PDF file to PowerPoint](#csharp-pdf-to-powerpoint)

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

## C# PDF to PowerPoint and PPTX Conversion

**Aspose.PDF for .NET** lets you track the progress of PDF to PPTX conversion.

We have an API named Aspose.Slides which offers the feature to create as well as manipulate PPT/PPTX presentations. This API also provides the feature to convert PPT/PPTX files to PDF format. Recently we received requirements from many of our customers to support the capability of PDF transformation to PPTX format. Starting release of Aspose.PDF for .NET 10.3.0, we have introduced a feature to transform PDF documents to PPTX format. During this conversion, the individual pages of the PDF file are converted to separate slides in the PPTX file.

During PDF to <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr> conversion, the text is rendered as Text where you can select/update it. Please note that in order to convert PDF files to PPTX format, Aspose.PDF provides a class named [`PptxSaveOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions). An object of the PptxSaveOptions class is passed as a second argument to the [`Document.Save(..) method`](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). The following code snippet shows the process for converting PDF files into PPTX format.

## Simple conversion PDF to PowerPoint using C# and Aspose.PDF .NET

In order to convert PDF to PPTX, Aspose.PDF for .NET advice to use the following code steps.

<a name="csharp-pdf-to-powerpoint"><strong>Steps: Convert PDF to PowerPoint in C#</strong></a> | <a name="csharp-pdf-to-pptx"><strong>Steps: Convert PDF to PPTX in C#</strong></a>

1. Create an instance of [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) class.
2. Create an instance of [PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) class.
3. Use the **Save** method of the **Document** object to save the PDF as PPTX.

```csharp
private static void ConvertPDFToPPTX()
{
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    // Open the source PDF document
    var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Instantiate PptxSaveOptions object
    var saveOptions = new Aspose.Pdf.PptxSaveOptions();

    // Save the file in PPTX format
    document.Save(dataDir + "PDFToPPT_out.pptx", saveOptions);
}
```

## Convert PDF to PPTX with Slides as Images

{{% alert color="success" %}}
**Try to convert PDF to PowerPoint online**

Aspose.PDF for .NET presents you online free application ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to PPTX with Free App](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

In case if you need to convert a searchable PDF to PPTX as images instead of selectable text, Aspose.PDF provides such a feature via [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) class. To achieve this, set property [SlidesAsImages](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions/properties/slidesasimages) of [PptxSaveOptios](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) class to 'true' as shown in the following code sample.

```csharp
private static void ConvertPDFToPPTWithSlidesAsImages()
{
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    // Open the source PDF document
    var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Instantiate PptxSaveOptions object
    var saveOptions = new Aspose.Pdf.PptxSaveOptions
    {
        SlidesAsImages = true
    };

    // Save the file in PPTX format with slides as images
    document.Save(dataDir + "PDFToPPT_out_.pptx", saveOptions);
}
```

## Progress Detail of PPTX Conversion

Aspose.PDF for .NET lets you track the progress of PDF to PPTX conversion. The [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) class provides [CustomProgressHandler](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions/properties/customprogresshandler) property that can be specified to a custom method for tracking the progress of conversion as shown in the following code sample.

```csharp
 private static void ConvertPDFToPPTWithCustomProgressHandler()
 {
     var dataDir = RunExamples.GetDataDir_AsposePdf();
     // Open the source PDF document
     var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

     // Instantiate PptxSaveOptions object
     var saveOptions = new Aspose.Pdf.PptxSaveOptions();

     // Specify custom progress handler
     saveOptions.CustomProgressHandler = ShowProgressOnConsole;

     // Save the file in PPTX format with progress tracking
     document.Save(dataDir + "PDFToPPTWithProgressTracking_out_.pptx", saveOptions);
 }

 // Define the method to handle progress events and display them on the console
 private static void ShowProgressOnConsole(Aspose.Pdf.UnifiedSaveOptions.ProgressEventHandlerInfo eventInfo)
 {
     switch (eventInfo.EventType)
     {
         case ProgressEventType.TotalProgress:
             // Display overall progress of the conversion
             Console.WriteLine($"{DateTime.Now.TimeOfDay}  - Conversion progress: {eventInfo.Value}%.");
             break;

         case ProgressEventType.ResultPageCreated:
             // Display progress of the page layout creation
             Console.WriteLine($"{DateTime.Now.TimeOfDay}  - Result page {eventInfo.Value} of {eventInfo.MaxValue} layout created.");
             break;

         case ProgressEventType.ResultPageSaved:
             // Display progress of the page being exported
             Console.WriteLine($"{DateTime.Now.TimeOfDay}  - Result page {eventInfo.Value} of {eventInfo.MaxValue} exported.");
             break;

         case ProgressEventType.SourcePageAnalysed:
             // Display progress of the source page analysis
             Console.WriteLine($"{DateTime.Now.TimeOfDay}  - Source page {eventInfo.Value} of {eventInfo.MaxValue} analyzed.");
             break;

         default:
             break;
     }
 }
```

## See Also 

This article also covers these topics. The codes are same as above.

_Format_: **PowerPoint**
- [C# PDF to PowerPoint Code](#csharp-pdf-to-powerpoint)
- [C# PDF to PowerPoint API](#csharp-pdf-to-powerpoint)
- [C# PDF to PowerPoint Programmatically](#csharp-pdf-to-powerpoint)
- [C# PDF to PowerPoint Library](#csharp-pdf-to-powerpoint)
- [C# Save PDF as PowerPoint](#csharp-pdf-to-powerpoint)
- [C# Generate PowerPoint from PDF](#csharp-pdf-to-powerpoint)
- [C# Create PowerPoint from PDF](#csharp-pdf-to-powerpoint)
- [C# PDF to PowerPoint Converter](#csharp-pdf-to-powerpoint)

_Format_: **PPTX**
- [C# PDF to PPTX Code](#csharp-pdf-to-pptx)
- [C# PDF to PPTX API](#csharp-pdf-to-pptx)
- [C# PDF to PPTX Programmatically](#csharp-pdf-to-pptx)
- [C# PDF to PPTX Library](#csharp-pdf-to-pptx)
- [C# Save PDF as PPTX](#csharp-pdf-to-pptx)
- [C# Generate PPTX from PDF](#csharp-pdf-to-pptx)
- [C# Create PPTX from PDF](#csharp-pdf-to-pptx)
- [C# PDF to PPTX Converter](#csharp-pdf-to-pptx)

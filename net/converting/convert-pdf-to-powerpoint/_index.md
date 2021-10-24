---
title: Convert PDF to Microsoft PowerPoint using C#
linktitle: Convert PDF to PowerPoint
type: docs
weight: 30
url: /net/convert-pdf-to-powerpoint/
description: Aspose.PDF allows you to convert PDF to PowerPoint format using .NET. One way there is a possibility to convert PDF to PPTX with Slides as Images.
lastmod: "2021-10-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF for .NET** lets you track the progress of PDF to PPTX conversion.

We have an API named Aspose.Slides which offers the feature to create as well as manipulate PPT/PPTX presentations. This API also provides the feature to convert PPT/PPTX files to PDF format. Recently we received requirements from many of our customers to support the capability of PDF transformation to PPTX format. Starting release of Aspose.PDF for .NET 10.3.0, we have introduced a feature to transform PDF documents to PPTX format. During this conversion, the individual pages of the PDF file are converted to separate slides in the PPTX file.

During PDF to <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr> conversion, the text is rendered as Text where you can select/update it. Please note that in order to convert PDF files to PPTX format, Aspose.PDF provides a class named [`PptxSaveOptions`](https://apireference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions). An object of the PptxSaveOptions class is passed as a second argument to the [`Document.Save(..) method`](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/save). The following code snippet shows the process for converting PDF files into PPTX format.

## Simple conversion PDF to PowerPoint using C# and Aspose.PDF .NET

In order to convert PDF to PPTX, Aspose.PDF for .NET advice to use the following code steps.

1. Create an instance of [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) class
1. Create an instance of [PptxSaveOptions](https://apireference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) class
1. Use the Save method of the Document object to save the PDF as PPTX

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Load PDF document
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "input.pdf");
// Instantiate PptxSaveOptions instance
Aspose.Pdf.PptxSaveOptions pptx_save = new Aspose.Pdf.PptxSaveOptions();
// Save the output in PPTX format
doc.Save(dataDir + "PDFToPPT_out.pptx", pptx_save);
```

## Convert PDF to PPTX with Slides as Images

## Try to convert PDF to PowerPoint online

Aspose.PDF for .NET presents you online free application ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to PPTX with Free App](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)

In case if you need to convert a searchable PDF to PPTX as images instead of selectable text, Aspose.PDF provides such a feature via [Aspose.Pdf.PptxSaveOptions](https://apireference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) class. To achieve this, set property [SlidesAsImages](https://apireference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions/properties/slidesasimages) of [PptxSaveOptios](https://apireference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) class to 'true' as shown in the following code sample.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Load PDF document
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "input.pdf");
// Instantiate PptxSaveOptions instance
Aspose.Pdf.PptxSaveOptions pptx_save = new Aspose.Pdf.PptxSaveOptions();
// Save the output in PPTX format
pptx_save.SlidesAsImages = true;
doc.Save(dataDir + "PDFToPPT_out_.pptx", pptx_save);
```

## Progress Detail of PPTX Conversion

Aspose.PDF for .NET lets you track the progress of PDF to PPTX conversion. The [Aspose.Pdf.PptxSaveOptions](https://apireference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) class provides [CustomProgressHandler](https://apireference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions/properties/customprogresshandler) property that can be specified to a custom method for tracking the progress of conversion as shown in the following code sample.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Load PDF document
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "input.pdf");
// Instantiate PptxSaveOptions instance
Aspose.Pdf.PptxSaveOptions pptx_save = new Aspose.Pdf.PptxSaveOptions();

//Specify Custom Progress Handler
pptx_save.CustomProgressHandler = ShowProgressOnConsole;
// Save the output in PPTX format
doc.Save(dataDir + "PDFToPPTWithProgressTracking_out_.pptx", pptx_save);
```

Following is the custom method for displaying progress conversion.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
switch (eventInfo.EventType)
{
    case ProgressEventType.TotalProgress:
        Console.WriteLine(String.Format("{0}  - Conversion progress : {1}% .", DateTime.Now.TimeOfDay, eventInfo.Value.ToString()));
        break;
    case ProgressEventType.ResultPageCreated:
        Console.WriteLine(String.Format("{0}  - Result page's {1} of {2} layout created.", DateTime.Now.TimeOfDay, eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
        break;
    case ProgressEventType.ResultPageSaved:
        Console.WriteLine(String.Format("{0}  - Result page {1} of {2} exported.", DateTime.Now.TimeOfDay, eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
        break;
    case ProgressEventType.SourcePageAnalysed:
        Console.WriteLine(String.Format("{0}  - Source page {1} of {2} analyzed.", DateTime.Now.TimeOfDay, eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));

        break;
    default:
        break;
}
```

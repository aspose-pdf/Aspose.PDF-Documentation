---
title: Convert XPS to PDF
linktitle: Convert XPS to PDF
type: docs
weight: 330
url: /net/convert-xps-to-pdf/
lastmod: "2020-12-27"
description: Aspose.PDF for .NET allows you to convert XPS to PDF files with a class named XpsLoadOptions. Check code snippet to solve this task. 
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for .NET** support feature converting XPS files to PDF format. Check this article to resolve your tasks.

The XPS file type is primarily associated with the XML Paper Specification by Microsoft Corporation. The XML Paper Specification (XPS), formerly codenamed Metro and subsuming the Next Generation Print Path (NGPP) marketing concept, is Microsoft's initiative to integrate document creation and viewing into its Windows operating system.

{{% alert color="primary" %}}

The file format is basically a zipped XML file which is primarily used for distribution and storage. It's very difficult to edit and mostly implemented by Microsoft.

{{% /alert %}}

In order to convert XPS to PDF with Aspose.PDF for .NET, we have introduced a class named [XpsLoadOption](https://apireference.aspose.com/pdf/net/aspose.pdf/xpsloadoptions) which is used to initialize a [LoadOptions](https://apireference.aspose.com/pdf/net/aspose.pdf/loadoptions) object. Later, this object is passed as an argument during the Document object initialization and it helps the PDF rendering engine to determine the source document's input format.

{{% alert color="primary" %}}

In both XP and Windows 7, you should find an XPS Printer pre-installed if you look in the Control Panel and then Printers. To create these files you can use that printer for the output device. In Windows 7, you should be able to just double-click the file to open it in a XPS viewer. You may also download XPS viewer from Microsoft's website.

{{% /alert %}}

The following code snippet shows the process of converting XPS file into PDF format with C#.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Instantiate LoadOption object using XPS load option
Aspose.Pdf.LoadOptions options = new XpsLoadOptions();

// Create document object
Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "XPSToPDF.xps", options);

// Save the resultant PDF document
document.Save(dataDir + "XPSToPDF_out.pdf");
```

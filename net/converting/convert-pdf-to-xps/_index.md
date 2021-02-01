---
title: Convert PDF to XPS | C#
linktitle: Convert PDF to XPS
type: docs
weight: 160
url: /net/convert-pdf-to-xps/
lastmod: "2021-01-15"
description: This page describes the definition of an XPS document and how to use it. Convert PDF to XPS with Aspose.PDF for .NET, using XpsSaveOptions class. 
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for .NET** gives a possibility to convert PDF files to <abbr title="XML Paper Specification">XPS</abbr> format. Let try to use the presented code snippet for converting PDF files to XPS format with C#.

{{% alert color="primary" %}}

Try online. You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/pdf-to-xps](https://products.aspose.app/pdf/conversion/pdf-to-xps)

{{% /alert %}}

The XPS file type is primarily associated with the XML Paper Specification by Microsoft Corporation. The XML Paper Specification (XPS), formerly codenamed Metro and subsuming the Next Generation Print Path (NGPP) marketing concept, is Microsoft's initiative to integrate document creation and viewing into the Windows operating system.

To convert PDF files to XPS, Aspose.PDF has the class [XpsSaveOptions](https://apireference.aspose.com/net/pdf/aspose.pdf/xpssaveoptions) that is used as the second argument to the [Document.Save(..)](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) method to generate the XPS file.

The following code snippet shows the process of converting PDF file into XPS format.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Load PDF document
Document pdfDocument = new Document(dataDir + "input.pdf");

// Instantiate XPS Save options
Aspose.Pdf.XpsSaveOptions saveOptions = new Aspose.Pdf.XpsSaveOptions();
// Save the XPS document
pdfDocument.Save("PDFToXPS_out.xps", saveOptions)
```

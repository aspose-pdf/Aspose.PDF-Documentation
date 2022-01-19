---
title: Get XMP Metadata of PDF File
type: docs
weight: 30
url: /net/get-xmp-metadata-of-an-existing-pdf-file/
description: This section explains how to get XMP Metadata of an existing PDF with Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

In order to get XMP metadata from a PDF file, you need to create [PdfXmpMetadata](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) object and bind the PDF file using [BindPdf](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method. You can pass specific XMP metadata properties to the [PdfXmpMetadata](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) object to get their values. The following code snippet shows you how to get XMP metadata from a PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_WorkingDocuments();

// Create PdfXmpMetadata object
PdfXmpMetadata xmpMetaData = new PdfXmpMetadata();

// Bind pdf file to the object
xmpMetaData.BindPdf( dataDir + "input.pdf");

// Get XMP Meta Data properties
Console.WriteLine(": {0}", xmpMetaData[DefaultMetadataProperties.CreateDate].ToString());
Console.WriteLine(": {0}", xmpMetaData[DefaultMetadataProperties.MetadataDate].ToString());
Console.WriteLine(": {0}", xmpMetaData[DefaultMetadataProperties.CreatorTool].ToString());
Console.WriteLine(": {0}", xmpMetaData["customNamespace:UserPropertyName"].ToString());

Console.ReadLine();
```
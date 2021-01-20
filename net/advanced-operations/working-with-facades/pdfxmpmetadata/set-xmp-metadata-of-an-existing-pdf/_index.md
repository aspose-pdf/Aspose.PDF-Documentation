---
title: Set XMP Metadata of an existing PDF
type: docs
weight: 20
url: /net/set-xmp-metadata-of-an-existing-pdf/
description: This section explains how to set XMP Metadata of an existing PDF with Aspose.PDF Facades.
lastmod: "2021-01-20"
draft: false
---

In order to set XMP metadata in a PDF file, you need to create [PdfXmpMetadata](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) object and bind the PDF file using [BindPdf](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method. You can use [Add](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata/methods/add/index) method of the [PdfXmpMetadata](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) class to add different properties. Finally, call the [Save](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) method of the [PdfXmpMetadata](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) class. The following code snippet shows you how to add XMP metadata in a PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_WorkingDocuments();

// Create PdfXmpMetadata object
PdfXmpMetadata xmpMetaData = new PdfXmpMetadata();

// Bind pdf file to the object
xmpMetaData.BindPdf(dataDir+ "SetXMPMetadata.pdf");

// Add create date
xmpMetaData.Add(DefaultMetadataProperties.CreateDate, System.DateTime.Now.ToString());

// Change meta data date
xmpMetaData[DefaultMetadataProperties.MetadataDate] = System.DateTime.Now.ToString();

// Add creator tool
xmpMetaData.Add(DefaultMetadataProperties.CreatorTool, "Creator tool name");

// Remove modify date
xmpMetaData.Remove(DefaultMetadataProperties.ModifyDate);

// Add user defined property
// Step #1: register namespace prefix and URI
xmpMetaData.RegisterNamespaceURI("customNamespace", "http:// Www.customNameSpaces.com/ns/");
// Step #2: add user property with the prefix
xmpMetaData.Add("customNamespace:UserPropertyName", "UserPropertyValue");

// Change user defined property
xmpMetaData["customNamespace:UserPropertyName"] = "UserPropertyValue2";

// Save xmp meta data in the pdf file
xmpMetaData.Save(dataDir+ "SetXMPMetadata_out.pdf");

// Close the object
xmpMetaData.Close();
```
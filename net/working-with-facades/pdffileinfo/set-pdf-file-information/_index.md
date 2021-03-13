---
title: Set PDF File Information
type: docs
weight: 40
url: /net/set-pdf-file-information/
description: This section explains how to set PDF File Information with Aspose.PDF Facades.
lastmod: "2021-01-15"
draft: false
---


[PdfFileInfo](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) class allows you to set file specific information of a PDF file. You need to create an object of [PdfFileInfo](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) class and then set different file specific properties like Author, Title, Keyword, and Creator etc. Finally, save the updated PDF file using [SaveNewInfo](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdffileinfo/savenewinfo/methods/1) method of the [PdfFileInfo](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) object.

The following code snippet shows you how to set PDF file information.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_WorkingDocuments();
// Open document
PdfFileInfo fileInfo = new PdfFileInfo(dataDir+ "SetFileInfo.pdf");
// Set PDF information
fileInfo.Author = "Aspose";
fileInfo.Title = "Hello World!";
fileInfo.Keywords = "Peace and Development";
fileInfo.Creator = "Aspose";            
// Save updated file
fileInfo.SaveNewInfo(dataDir+ "SetFileInfo_out.pdf");
```
---
title: Get PDF file information
type: docs
weight: 50
url: /net/get-pdf-file-information/
description: This section explains how to get PDF File Information with Aspose.PDF Facades.
lastmod: "2021-01-15"
draft: false
---

In order to get file specific information of a PDF file, you need to create an object of [PdfFileInfo](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) class. After that, you can get values of the individual properties like Subject, Title, Keywords and Creator etc. 

The following code snippet shows you how to get PDF file information.
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_WorkingDocuments();
// Open document
PdfFileInfo fileInfo = new PdfFileInfo(dataDir+ "GetFileInfo.pdf");
// Get PDF information
Console.WriteLine("Subject: {0}", fileInfo.Subject);
Console.WriteLine("Title: {0}", fileInfo.Title);
Console.WriteLine("Keywords: {0}", fileInfo.Keywords);
Console.WriteLine("Creator: {0}", fileInfo.Creator);
Console.WriteLine("Creation Date: {0}", fileInfo.CreationDate);
Console.WriteLine("Modification Date: {0}", fileInfo.ModDate);
// Find whether is it valid PDF and it is encrypted as well
Console.WriteLine("Is Valid PDF: {0}", fileInfo.IsPdfFile);
Console.WriteLine("Is Encrypted: {0}", fileInfo.IsEncrypted);
```

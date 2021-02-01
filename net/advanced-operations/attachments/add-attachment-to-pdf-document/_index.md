---
title: Adding Attachment to a PDF document using Aspose.PDF for .NET
linktitle: Adding Attachment to a PDF document using Aspose.PDF for .NET
type: docs
weight: 30
url: /net/add-attachment-to-pdf-document/
description: This page describes how to add an attachment to a PDF file with C#.
aliases:
    - /net/adding-to-a-pdf-document/
lastmod: "2020-12-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Attachments can contain a wide variety of information and can be of a variety of file types. This article explains how to add an attachment to a PDF file.

1. Create a new C# project.
1. Add a reference to Aspose.PDF DLL.
1. Create a [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) object.
1. Create a [FileSpecification](https://apireference.aspose.com/pdf/net/aspose.pdf/filespecification) object with the file you are adding, and file description.
1. Add the [FileSpecification](https://apireference.aspose.com/pdf/net/aspose.pdf/filespecification) object to the [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) object’s [EmbeddedFiles](https://apireference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) collection, with the collection’s Add method.

The [EmbeddedFiles](https://apireference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) collection contains all the attachments in the PDF file. The following code snippet shows you how to add an attachment in a PDF document.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

// Open document
Document pdfDocument = new Document(dataDir + "AddAttachment.pdf");

// Setup new file to be added as attachment
FileSpecification fileSpecification = new FileSpecification(dataDir + "test.txt", "Sample text file");

// Add attachment to document's attachment collection
pdfDocument.EmbeddedFiles.Add(fileSpecification);

dataDir = dataDir + "AddAttachment_out.pdf";

// Save new output
pdfDocument.Save(dataDir);
```

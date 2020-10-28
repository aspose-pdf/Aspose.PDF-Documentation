---
title: Merge document
type: docs
weight: 50
url: /net/merge-document/
---

This article shows how to merge multiple PDF files into a single PDF document using Aspose.PDF for .NET. The example is written in C# but the API can be used in other .NET programming languages as well such as VB.NET. PDF files are merged such that the first one is joined at the end of the other document. 

# Merge PDF Files using C#
>You can merge PDF files using Aspose.PDF and get the results online at this link: [products.aspose.app/pdf/merger](https://products.aspose.app/pdf/merger)

To concatenate two PDF files:

1. Create two [Document](https://apireference.aspose.com/net/pdf/aspose.pdf/document)  objects, each containing one of the input PDF files.
1. Then call the [PageCollection](https://apireference.aspose.com/net/pdf/aspose.pdf/pagecollection) collection’s Add method for the Document object you want to add the other PDF file to.
1. Pass the PageCollection collection of the second Document object to the first PageCollection collection’s Add method.
1. Finally, save the output PDF file using the [Save](https://apireference.aspose.com/net/pdf/aspose.pdf.document/save/methods/4) method.

The following code snippet shows how to concatenate PDF files.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// Open first document
Document pdfDocument1 = new Document(dataDir + "Concat1.pdf");
// Open second document
Document pdfDocument2 = new Document(dataDir + "Concat2.pdf");

// Add pages of second document to the first
pdfDocument1.Pages.Add(pdfDocument2.Pages);

dataDir = dataDir + "ConcatenatePdfFiles_out.pdf";
// Save concatenated output file
pdfDocument1.Save(dataDir);
```
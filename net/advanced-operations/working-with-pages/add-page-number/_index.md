---
title: Add Page Number to PDF with C#
linktitle: Add Page Number
type: docs
weight: 100
url: /net/add-page-number/
description: Aspose.PDF for .NET allows you to add Page Number Stamp to your PDF file using PageNumber Stamp class.
lastmod: "2020-12-22"
aliases:
    - /pdf/net/get-and-set-page-properties/
sitemap:
    changefreq: "weekly"
    priority: 0.7
--- 

All the documents must have page numbers in it. The page number makes it easier for the reader to locate different parts of the document.
**Aspose.PDF for .NET** allows you to add page numbers with PageNumberStamp.

You can use [PageNumberStamp](https://apireference.aspose.com/pdf/net/aspose.pdf/pagenumberstamp) class to add a page number stamp in a PDF file. [PageNumber Stamp](https://apireference.aspose.com/pdf/net/aspose.pdf/pagenumberstamp) class provides properties necessary to create a page number based stamp like format, margins, alignments, starting number etc. In order to add page number stamp, you need to create a [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) object and a [PageNumberStamp](https://apireference.aspose.com/pdf/net/aspose.pdf/pagenumberstamp) object using required properties. After that, you can call [AddStamp](https://apireference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) method of the [Page](https://apireference.aspose.com/pdf/net/aspose.pdf/page) to add the stamp in the PDF. You can also set the font attributes of the page number stamp. The following code snippet shows you how to add page numbers in a PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Open document
Document pdfDocument = new Document(dataDir+ "PageNumberStamp.pdf");

// Create page number stamp
PageNumberStamp pageNumberStamp = new PageNumberStamp();
// Whether the stamp is background
pageNumberStamp.Background = false;
pageNumberStamp.Format = "Page # of " + pdfDocument.Pages.Count;
pageNumberStamp.BottomMargin = 10;
pageNumberStamp.HorizontalAlignment = HorizontalAlignment.Center;
pageNumberStamp.StartingNumber = 1;
// Set text properties
pageNumberStamp.TextState.Font = FontRepository.FindFont("Arial");
pageNumberStamp.TextState.FontSize = 14.0F;
pageNumberStamp.TextState.FontStyle = FontStyles.Bold;
pageNumberStamp.TextState.FontStyle = FontStyles.Italic;
pageNumberStamp.TextState.ForegroundColor = Color.Aqua;

// Add stamp to particular page
pdfDocument.Pages[1].AddStamp(pageNumberStamp);

dataDir = dataDir + "PageNumberStamp_out.pdf";
// Save output document
pdfDocument.Save(dataDir);
```

## Add Bates Numbers

**Bates numbering** (also known as Bates stamping) is used in the legal, medical, and business fields to place identifying numbers and/or date/time-marks on images and documents as they are scanned or processed, for example, during the discovery stage of preparations for trial or identifying business receipts. This process provides identification, protection, and automatic consecutive numbering of the images.

Aspose.PDF allows you to add a header and footer to all pages of a PDF document. Headers and footers can contain the date, automatic pagination, Bates numbers for legal documents, title, or author name. You can add headers and footers to one or more PDF files.

You can use different headers and footers in the same PDF file. For example, you can add one header for odd-numbered pages that displays the page number on the right, and another header for even-numbered pages with the page number on the left. When adding a Bates numbering, you can specify the number of digits, the start number, and the prefix or postfix to add to each Bates.

**TODO:** Insert example

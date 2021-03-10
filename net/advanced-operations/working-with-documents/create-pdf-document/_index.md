---
title: Create PDF Document using Aspose.PDF for .NET
linktitle: Create PDF Document
type: docs
weight: 10
url: /net/formatting-pdf-document/
description: Create and format the PDF Document with Aspose.PDF for .NET. Use the next code snippet to resolve your tasks.
lastmod: "2021-03-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Create Document

Aspose.PDF for .NET API lets you create and read PDF files using C# and VB.NET. The API can be used in a variety of .NET applications including WinForms, ASP.NET, and several others. In this article, we are going to show how to use Aspose.PDF for .NET API to easily generate and read PDF files in .NET applications.

### How to Create PDF File using C# language

To create a PDF file using C#, the following steps can be used.

1. Create an object of [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) class
1. Add a [Page](https://apireference.aspose.com/pdf/net/aspose.pdf/page) object to the [Pages](https://apireference.aspose.com/pdf/net/aspose.pdf/document/properties/pages) collection of the Document object
1. Add [TextFragment](https://apireference.aspose.com/pdf/net/aspose.pdf.text/textfragment) to [Paragraphs](https://apireference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) collection of the page
1. Save the resultant PDF document

```csharp
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

// Initialize document object
Document document = new Document();
// Add page
Page page = document.Pages.Add();
// Add text to new page
page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
// Save updated PDF
document.Save(dataDir + "HelloWorld_out.pdf");
```

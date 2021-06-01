---
title: Create Tagged PDF | C#
linktitle: Create Tagged PDF 
type: docs
weight: 10
lastmod: "2021-04-25"
url: /net/create-tagged-pdf/
description: This article explains how to create structure's elements for Tagged PDF document programmatically using Aspose.PDF for .NET.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Creating a Tagged PDF means adding (or creating) certain elements to the document that will enable the document to be validated in accordance with PDF/UA requirements. These elements are called often Structure Elements.

## Creating Tagged PDF (Simple Scenario)

In order to create structure elements in a Tagged PDF Document, Aspose.PDF offers methods to create structure element using [ITaggedContent](https://apireference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent) interface. Following code snippet shows how to create Tagged PDF which contain 2 elements: header and paragraph.

```csharp
private static void CreateTaggedPdfDocument01()
{
    // Create PDF Document
    var document = new Document();

    // Get Content for work with TaggedPdf
    ITaggedContent taggedContent = document.TaggedContent;
    var rootElement = taggedContent.RootElement;
    // Set Title and Language for Document
    taggedContent.SetTitle("Tagged Pdf Document");
    taggedContent.SetLanguage("en-US");

    // 
    HeaderElement mainHeader = taggedContent.CreateHeaderElement();
    mainHeader.SetText("Main Header");

    ParagraphElement paragraphElement = taggedContent.CreateParagraphElement();
    paragraphElement.SetText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. " +
    "Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. " +
    "Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet" +
    "nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus." +
    "Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat" +
    "sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper" +
    "pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus" +
    "ac iaculis eget, tempus et magna. Sed non consectetur elit. Sed vulputate, quam sed lacinia luctus," +
    "ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");

    rootElement.AppendChild(mainHeader);
    rootElement.AppendChild(paragraphElement);

    // Save Tagged Pdf Document
    document.Save("C:\\Samples\\TaggedPDF\\Sample1.pdf");
}
```

We will get a following document after creation:

![Tagged PDF document with 2 elements - Header and Paragraph](taggedpdf-01.png)

## Creating Tagged PDF with nested elements (Creating Structure Elements Tree)

In some cases, we need to create more complex sturcutre, eg. place quotes in paragraph. 
In order to create structure elements tree we should use [AppendChild](https://apireference.aspose.com/pdf/net/aspose.pdf.logicalstructure/element/methods/appendchild) method.
Following code snippet shows how to create structure elements tree of Tagged PDF Document:

```csharp
private static void CreateTaggedPdfDocument02()
{
    // Create Pdf Document
    var document = new Document();

    // Get Content for work with TaggedPdf
    ITaggedContent taggedContent = document.TaggedContent;
    var rootElement = taggedContent.RootElement;
    // Set Title and Language for Document
    taggedContent.SetTitle("Tagged Pdf Document");
    taggedContent.SetLanguage("en-US");

    HeaderElement header1 = taggedContent.CreateHeaderElement(1);
    header1.SetText("Header Level 1");

    ParagraphElement paragraphWithQuotes = taggedContent.CreateParagraphElement();
    paragraphWithQuotes.StructureTextState.Font = FontRepository.FindFont("Calibri");
    paragraphWithQuotes.StructureTextState.MarginInfo = new MarginInfo(10, 5, 10, 5);

    SpanElement spanElement1 = taggedContent.CreateSpanElement();
    spanElement1.SetText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. ");
    QuoteElement quoteElement = taggedContent.CreateQuoteElement();
    quoteElement.SetText("Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa.");
    quoteElement.StructureTextState.FontStyle = FontStyles.Bold | FontStyles.Italic;
    SpanElement spanElement2 = taggedContent.CreateSpanElement();
    spanElement2.SetText(" Sed non consectetur elit.");

    paragraphWithQuotes.AppendChild(spanElement1);
    paragraphWithQuotes.AppendChild(quoteElement);
    paragraphWithQuotes.AppendChild(spanElement2);

    rootElement.AppendChild(header1);
    rootElement.AppendChild(paragraphWithQuotes);

    // Save Tagged Pdf Document
    document.Save("C:\\Samples\\TaggedPDF\\Sample2.pdf");
}
```

We will get a following document after creation:
![Tagged PDF document with nested elements - span and quotes](taggedpdf-02.png)

## Styling Text Structure

In order to style text structure in a Tagged PDF Document, Aspose.PDF offers [Font](https://apireference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate/properties/font), [FontSize](https://apireference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate/properties/fontsize), [FontStyle](https://apireference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate/properties/fontstyle) and [ForegroundColor](https://apireference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate/properties/foregroundcolor) properties of [StructureTextState](https://apireference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate) Class. Following code snippet shows how to style text structure in a Tagged PDF Document:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Create Pdf Document
Document document = new Document();

// Get Content for work with TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// Set Title and Language for Document
taggedContent.SetTitle("Tagged Pdf Document");
taggedContent.SetLanguage("en-US");

ParagraphElement p = taggedContent.CreateParagraphElement();
taggedContent.RootElement.AppendChild(p);

// Under Development
p.StructureTextState.FontSize = 18F;
p.StructureTextState.ForegroundColor = Color.Red;
p.StructureTextState.FontStyle = FontStyles.Italic;

p.SetText("Red italic text.");

// Save Tagged Pdf Document
document.Save(dataDir + "StyleTextStructure.pdf");
```

## Illustrating Structure Elements

In order to illustrate structure elements in a Tagged PDF Document, Aspose.PDF offers [IllustrationElement](https://apireference.aspose.com/pdf/net/aspose.pdf.logicalstructure/illustrationelement) class. Following code snippet shows how to illustrate structure elements in a Tagged PDF Document:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Create Pdf Document
Document document = new Document();

// Get Content for work with TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// Set Title and Language for Document
taggedContent.SetTitle("Tagged Pdf Document");
taggedContent.SetLanguage("en-US");

// Under Development
IllustrationElement figure1 = taggedContent.CreateFigureElement();
taggedContent.RootElement.AppendChild(figure1);
figure1.AlternativeText = "Figure One";
figure1.Title = "Image 1";
figure1.SetTag("Fig1");
figure1.SetImage("image.png");

// Save Tagged Pdf Document
document.Save(dataDir + "IllustrationStructureElements.pdf");

```

## Validate Tagged PDF

Aspose.PDF for .NET provides the ability to validate PDF/UA Tagged PDF Document. Validation of PDF/UA standard supports:

- Checks for XObjects
- Checks for Actions
- Checks for Optional Content
- Checks for Embedded Files
- Checks for Acroform Fields(Validate Natural Language and Alternate Name and Digital Signatures)
- Checks for XFA Form Fields
- Checks for Security settings
- Checks for Navigation
- Checks for Annotations

The code snippet below shows how to validate the Tagged PDF Document. Corresponding problems will be displayed in the XML log report.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string inputFileName = dataDir + "StructureElements.pdf";
string outputLogName = dataDir + "ua-20.xml";

using (var document = new Aspose.Pdf.Document(inputFileName))
{
    bool isValid = document.Validate(outputLogName, Aspose.Pdf.PdfFormat.PDF_UA_1);

}
```

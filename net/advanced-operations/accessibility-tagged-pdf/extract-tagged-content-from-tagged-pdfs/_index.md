---
title: Extract Tagged Content from PDF | C#
linktitle: Extract Tagged Content
type: docs
weight: 20
url: /net/extract-tagged-content-from-tagged-pdfs/
description: This article explains how to extract tagged content PDF document using Aspose.PDF for .NET
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

In this article you will learn how to to extract tagged content PDF document using C#.

## Getting Tagged PDF Content

In order to get content of PDF Document with Tagged Text, Aspose.PDF offers [TaggedContent](https://apireference.aspose.com/pdf/net/aspose.pdf/document/properties/taggedcontent) property of [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) class.

Following code snippet shows how to get content of a PDF document with Tagged Text:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Create Pdf Document
Document document = new Document();

// Get Content for work with TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

//
// Work with Tagged Pdf content
//

// Set Title and Language for Document
taggedContent.SetTitle("Simple Tagged Pdf Document");
taggedContent.SetLanguage("en-US");

// Save Tagged Pdf Document
document.Save(dataDir + "TaggedPDFContent.pdf");
```

## Getting Root Structure

In order to get the root structure of Tagged PDF Document, Aspose.PDF offers [StructTreeRootElement](https://apireference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/properties/structtreerootelement) property of [ITaggedContent](https://apireference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent) interface and [StructureElement](https://apireference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement). Following code snippet shows how to get the root structure of Tagged PDF Document:

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

// Properties StructTreeRootElement and RootElement are used for access to
// StructTreeRoot object of pdf document and to root structure element (Document structure element).
StructTreeRootElement structTreeRootElement = taggedContent.StructTreeRootElement;
StructureElement rootElement = taggedContent.RootElement;
```

## Accessing Child Elements

In order to access child elements of a Tagged PDF Document, Aspose.PDF offers [ElementList](https://apireference.aspose.com/pdf/net/aspose.pdf.logicalstructure/elementlist) class. Following code snippet shows how to access child elements of a Tagged PDF Document:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Open Pdf Document
Document document = new Document(dataDir + "StructureElementsTree.pdf");

// Get Content for work with TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// Access to root element(s)
ElementList elementList = taggedContent.StructTreeRootElement.ChildElements;
foreach (Element element in elementList)
{
    if (element is StructureElement)
    {
        StructureElement structureElement = element as StructureElement;

        // Get properties
        string title = structureElement.Title;
        string language = structureElement.Language;
        string actualText = structureElement.ActualText;
        string expansionText = structureElement.ExpansionText;
        string alternativeText = structureElement.AlternativeText;
    }
}

// Access to child elements of first element in root element
elementList = taggedContent.RootElement.ChildElements[1].ChildElements;
foreach (Element element in elementList)
{
    if (element is StructureElement)
    {
        StructureElement structureElement = element as StructureElement;

        // Set properties
        structureElement.Title = "title";
        structureElement.Language = "fr-FR";
        structureElement.ActualText = "actual text";
        structureElement.ExpansionText = "exp";
        structureElement.AlternativeText = "alt";
    }
}

// Save Tagged Pdf Document
document.Save(dataDir + "AccessChildElements.pdf");
```

## Tagging Images in Existing PDF

In order to tag images in existing PDF document, Aspose.PDF offers [FindElements](https://apireference.aspose.com/pdf/net/aspose.pdf.logicalstructure/element/methods/findelements/_1) method of [StructureElement](https://apireference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement) class. You can add alternative text for figures using [AlternativeText](https://apireference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement/properties/alternativetext) property of [FigureElement](https://apireference.aspose.com/pdf/net/aspose.pdf.logicalstructure/figureelement) class.

Following code snippet shows how to tag images in existing PDF document:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string inFile = dataDir + "TH.pdf";
string outFile = dataDir + "TH_out.pdf";
string logFile = dataDir + "TH_out.xml";

// Open document
Document document = new Document(inFile);

// Gets tagged content and root structure element
ITaggedContent taggedContent = document.TaggedContent;
StructureElement rootElement = taggedContent.RootElement;

// Set title for tagged pdf document
taggedContent.SetTitle("Document with images");

foreach (FigureElement figureElement in rootElement.FindElements<FigureElement>(true))
{
    // Set Alternative Text  for Figure
    figureElement.AlternativeText = "Figure alternative text (technique 2)";


    // Create and Set BBox Attribute
    StructureAttribute bboxAttribute = new StructureAttribute(AttributeKey.BBox);
    bboxAttribute.SetRectangleValue(new Rectangle(0.0, 0.0, 100.0, 100.0));

    StructureAttributes figureLayoutAttributes = figureElement.Attributes.GetAttributes(AttributeOwnerStandard.Layout);
    figureLayoutAttributes.SetAttribute(bboxAttribute);
}

// Move Span Element into Paragraph (find wrong span and paragraph in first TD)
TableElement tableElement = rootElement.FindElements<TableElement>(true)[0];
SpanElement spanElement = tableElement.FindElements<SpanElement>(true)[0];
TableTDElement firstTdElement = tableElement.FindElements<TableTDElement>(true)[0];
ParagraphElement paragraph = firstTdElement.FindElements<ParagraphElement>(true)[0];

// Move Span Element into Paragraph
spanElement.ChangeParentElement(paragraph);


// Save document
document.Save(outFile);



// Checking PDF/UA Compliance for out document
document = new Document(outFile);

bool isPdfUaCompliance = document.Validate(logFile, PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("PDF/UA compliance: {0}", isPdfUaCompliance));
```

---
title: Create Tagged PDF 
linktitle: Create Tagged PDF 
type: docs
weight: 10
lastmod: "2025-02-17"
url: /java/create-tagged-pdf-documents/
description: This article explains how to create structure's elements for Tagged PDF document programmatically using Aspose.PDF for Java.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Creating and manipulating structure elements in a Tagged PDF
Abstract: The article provides a comprehensive guide on creating and manipulating structure elements in a Tagged PDF document using the Aspose.PDF library in Java. It covers several key functionalities, including creating individual structure elements, building a hierarchical structure element tree, styling text structures, illustrating structure elements, and incorporating tagged images and text into PDFs. The document emphasizes the use of the `ITaggedContent` interface to achieve these tasks, showcasing various code snippets for practical implementation. Users can create and style text block-level and inline-level structure elements, add illustrations with specific attributes, and manage tagged images for enhanced document accessibility and organization. The article also highlights methods under development for future enhancements, such as list and table elements, thereby outlining the current capabilities and potential expansions of the Aspose.PDF library for creating robust Tagged PDF documents.
SoftwareApplication: java
---

## Creating Structure Elements

In order to create structure elements in a Tagged PDF Document, Aspose.PDF offers methods to create structure element using [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent) Interface. Following code snippet shows how to create structure elements of Tagged PDF:

```java
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-Java
// The path to the documents directory.
String path = "pathTodir";

// Create Pdf Document
Document document = new Document();

// Get Content for work with TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Set Title and Language for Documnet
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// Create Grouping Elements
PartElement partElement = taggedContent.createPartElement();
ArtElement artElement = taggedContent.createArtElement();
SectElement sectElement = taggedContent.createSectElement();
DivElement divElement = taggedContent.createDivElement();
BlockQuoteElement blockQuoteElement = taggedContent.createBlockQuoteElement();
CaptionElement captionElement = taggedContent.createCaptionElement();
TOCElement tocElement = taggedContent.createTOCElement();
TOCIElement tociElement = taggedContent.createTOCIElement();
IndexElement indexElement = taggedContent.createIndexElement();
NonStructElement nonStructElement = taggedContent.createNonStructElement();
PrivateElement privateElement = taggedContent.createPrivateElement();

// Create Text Block-Level Structure Elements
ParagraphElement paragraphElement = taggedContent.createParagraphElement();
HeaderElement headerElement = taggedContent.createHeaderElement();
HeaderElement h1Element = taggedContent.createHeaderElement(1);

// Create Text Inline-Level Structure Elements
SpanElement spanElement = taggedContent.createSpanElement();
QuoteElement quoteElement = taggedContent.createQuoteElement();
NoteElement noteElement = taggedContent.createNoteElement();

// Create Illustration Structure Elements
FigureElement figureElement = taggedContent.createFigureElement();
FormulaElement formulaElement = taggedContent.createFormulaElement();

// Methods are under development
ListElement listElement = taggedContent.createListElement();
TableElement tableElement = taggedContent.createTableElement();
ReferenceElement referenceElement = taggedContent.createReferenceElement();
BibEntryElement bibEntryElement = taggedContent.createBibEntryElement();
CodeElement codeElement = taggedContent.createCodeElement();
LinkElement linkElement = taggedContent.createLinkElement();
AnnotElement annotElement = taggedContent.createAnnotElement();
RubyElement rubyElement = taggedContent.createRubyElement();
WarichuElement warichuElement = taggedContent.createWarichuElement();
FormElement formElement = taggedContent.createFormElement();

// Save Tagged Pdf Document
document.save(path + "StructureElements.pdf");
```

## Creating Structure Elements Tree

In order to create structure elements tree in a Tagged PDF Document, Aspose.PDF offers methods to create a structure element tree using [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent) Interface. Following code snippet shows how to create structure elements tree of Tagged PDF Document:

```java
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-Java
// The path to the documents directory.
String path = "pathTodir";
// Create Pdf Document
Document document = new Document();

// Get Content for work with TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Set Title and Language for Documnet
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// Get root structure element (Document)
StructureElement rootElement = taggedContent.getRootElement();

// Create Logical Structure
SectElement sect1 = taggedContent.createSectElement();
rootElement.appendChild(sect1);

SectElement sect2 = taggedContent.createSectElement();
rootElement.appendChild(sect2);

DivElement div11 = taggedContent.createDivElement();
sect1.appendChild(div11);

DivElement div12 = taggedContent.createDivElement();
sect1.appendChild(div12);

ArtElement art21 = taggedContent.createArtElement();
sect2.appendChild(art21);

ArtElement art22 = taggedContent.createArtElement();
sect2.appendChild(art22);

DivElement div211 = taggedContent.createDivElement();
art21.appendChild(div211);

DivElement div212 = taggedContent.createDivElement();
art21.appendChild(div212);

DivElement div221 = taggedContent.createDivElement();
art22.appendChild(div221);

DivElement div222 = taggedContent.createDivElement();
art22.appendChild(div222);

SectElement sect3 = taggedContent.createSectElement();
rootElement.appendChild(sect3);

DivElement div31 = taggedContent.createDivElement();
sect3.appendChild(div31);

// Save Tagged Pdf Document
document.save(path + "StructureElementsTree.pdf");
```

## Styling Text Structure

In order to style text structure in a Tagged PDF Document, Aspose.PDF offers **setFont()**, **setFontSize()**, **setFontStyle()** and **setForegroundColor()** properties of [StructureTextState](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.class-use/StructureTextState) Class. Following code snippet shows how to style text structure in a Tagged PDF Document:

```java
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-Java
// The path to the documents directory.
String path = "pathTodir";
// Create Pdf Document
Document document = new Document();

// Get Content for work with TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Set Title and Language for Documnet
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

ParagraphElement p = taggedContent.createParagraphElement();
taggedContent.getRootElement().appendChild(p);

// Under Development
p.getStructureTextState().setFontSize(18F);
p.getStructureTextState().setForegroundColor(Color.getRed());
p.getStructureTextState().setFontStyle(FontStyles.Italic);

p.setText("Red italic text.");

// Save Tagged Pdf Document
document.save(path + "StyleTextStructure.pdf");
```

## Illustrating Structure Elements

In order to illustrate structure elements in a Tagged PDF Document, Aspose.PDF offers [IllustrationElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.class-use/IllustrationElement) Class. Following code snippet shows how to illustrate structure elements in a Tagged PDF Document:

```java
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-Java
// The path to the documents directory.
String path = "pathTodir";
// Create Pdf Document
Document document = new Document();

// Get Content for work with TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Set Title and Language for Documnet
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// Under Development
IllustrationElement figure1 = taggedContent.createFigureElement();
taggedContent.getRootElement().appendChild(figure1);
figure1.setActualText("Figure One");
figure1.setTitle("Image 1");
figure1.setTag("Fig1");
figure1.setImage("image.png");

// Save Tagged Pdf Document
document.save(path + "IllustrationStructureElements.pdf");
```

## **Create PDF with Tagged Image**

In order to create PDF with Tagged Image, Aspose.PDF offers [createFigureElement()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent#createFigureElement--) method of [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent) Interface. The following code snippet shows the functionality.

```java
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-Java
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("CreatePDFwithTaggedImage");
taggedContent.setLanguage("en-US");

IllustrationElement figure1 = taggedContent.createFigureElement();
taggedContent.getRootElement().appendChild(figure1);
figure1.setAlternativeText("Aspose Logo");
figure1.setTitle("Image 1");
figure1.setTag("Fig");
// Add image with resolution 300 DPI (by default)
figure1.setImage("aspose-logo.jpg");
// Save PDF Document
document.save("PDFwithTaggedImage.pdf");
```

## Create PDF with Tagged Text

In order to create PDF with Tagged Text, Aspose.PDF offers [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent) Interface. The following code snippet shows the functionality.

```java
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-Java
// The path to the documents directory.
String dataDir = Utils.getDataDir() + "TaggedPDFs\\";
// Create Pdf Document
Document document = new Document();

// Get Content for work with TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Set Title and Language for Documnet
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// Create Text Block-Level Structure Elements
HeaderElement headerElement = taggedContent.createHeaderElement();
headerElement.setActualText("Heading 1");
ParagraphElement paragraphElement1 = taggedContent.createParagraphElement();
paragraphElement1.setActualText("test1");
ParagraphElement paragraphElement2 = taggedContent.createParagraphElement();
paragraphElement2.setActualText("test 2");
ParagraphElement paragraphElement3 = taggedContent.createParagraphElement();
paragraphElement3.setActualText("test 3");
ParagraphElement paragraphElement4 = taggedContent.createParagraphElement();
paragraphElement4.setActualText("test 4");
ParagraphElement paragraphElement5 = taggedContent.createParagraphElement();
paragraphElement5.setActualText("test 5");
ParagraphElement paragraphElement6 = taggedContent.createParagraphElement();
paragraphElement6.setActualText("test 6");
ParagraphElement paragraphElement7 = taggedContent.createParagraphElement();
paragraphElement7.setActualText("test 7");

// Save PDF Document
document.save( dataDir + "PDFwithTaggedText.pdf");
```

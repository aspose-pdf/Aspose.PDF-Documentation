---
title: Extract Tagged Content from PDF 
linktitle: Extract Tagged Content
type: docs
weight: 20
url: /java/extract-tagged-content-from-tagged-pdfs/
description: This article explains how to extract tagged content PDF document using Aspose.PDF for Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Guide on handling Tagged PDF content using the Aspose.PDF library in Java
Abstract: This article provides a comprehensive guide on handling Tagged PDF content using the Aspose.PDF library in Java. It explains how to retrieve content from a PDF document with tagged text by utilizing the `getTaggedContent()` method of the `Document` class. The article includes a practical code snippet demonstrating the process of setting a document's title and language and saving the tagged PDF content. Additionally, it describes how to access the root structure of a Tagged PDF Document through the `getStructTreeRootElement()` and `getStructureElement()` methods of the `ITaggedContent` interface. Furthermore, the article illustrates how to access and manipulate children elements within a Tagged PDF using the `ElementList` class, providing examples of getting and setting properties such as title, language, and various text attributes. Each section is accompanied by example code snippets to aid in understanding and implementation.
SoftwareApplication: java
---

## Getting Tagged PDF Content

In order to get content of PDF Document with Tagged Text, Aspose.PDF offers [getTaggedContent()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getTaggedContent--) method of [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) Class. Following code snippet shows how to get content of a PDF document with Tagged Text:

```java
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-Java
// The path to the documents directory.
String path = "pathTodir";

// Create Pdf Document
Document document = new Document();

// Get Content for work with TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

//
// Work with Tagged Pdf content
//

// Set Title and Language for Documnet
taggedContent.setTitle("Simple Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// Save Tagged Pdf Document
document.save(path + "TaggedPDFContent.pdf");
```

## Getting Root Structure

In order to get the root structure of Tagged PDF Document, Aspose.PDF offers [getStructTreeRootElement]()(https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent#getStructTreeRootElement--) and **getStructureElement()** methods of [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent) Interface. Following code snippet shows how to get the root structure of Tagged PDF Document:

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

// Properties StructTreeRootElement and RootElement are used for access to
// StructTreeRoot object of pdf document and to root structure element (Document structure element).
StructTreeRootElement structTreeRootElement = taggedContent.getStructTreeRootElement();
StructureElement rootElement = taggedContent.getRootElement();
```

## Accessing Children Elements

In order to access children elements of a Tagged PDF Document, Aspose.PDF offers **ElementList** Class. Following code snippet shows how to access children elements of a Tagged PDF Document:

```java
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-Java
String path = "pathTodir";
// Open Pdf Document
Document document = new Document( path +"StructureElements.pdf");

// Get Content for work with TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Access to root element(s)
ElementList elementList = taggedContent.getStructTreeRootElement().getChildElements();
for (Element element : elementList)
{
    if (element instanceof StructureElement)
    {
        StructureElement structureElement =  (StructureElement)element;

        // Get properties
        String title = structureElement.getTitle();
        String language = structureElement.getLanguage();
        String actualText = structureElement.getActualText();
        String expansionText = structureElement.getExpansionText();
        String alternativeText = structureElement.getAlternativeText();
    }
}

// Access to children elements of first element in root element
elementList = taggedContent.getRootElement().getChildElements().get_Item(1).getChildElements();
for (Element element : elementList)
{
    if (element instanceof StructureElement)
    {
        StructureElement structureElement = (StructureElement)element;

        // Set properties
        structureElement.setTitle("title");
        structureElement.setLanguage("fr-FR");
        structureElement.setActualText("actual text");
        structureElement.setExpansionText("exp");
        structureElement.setAlternativeText("alt");
    }
}

// Save Tagged Pdf Document
document.save( path +"AccessChildrenElements.pdf");
```

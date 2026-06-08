---
title: Extract Tagged Content from PDFs in Java
linktitle: Extract Tagged Content
type: docs
weight: 20
url: /java/extract-tagged-content-from-tagged-pdfs/
description: Learn how to inspect tagged PDF content in Java with Aspose.PDF, including tagged content access, root structure access, and child structure elements.
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
Use these APIs when you need to inspect the logical structure tree of a tagged PDF and examine or update structure element metadata.

## Get tagged content

1. Create a new PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Get the document's [ITaggedContent](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.tagged/itaggedcontent/).
1. Set the tagged [ITaggedContent](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.tagged/itaggedcontent/) title and language.
1. Save the tagged PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

```java
public static void getTaggedContent(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Simple Tagged Pdf Document");
        taggedContent.setLanguage("en-US");
        document.save(outputFile.toString());
    }
}
```

## Access the root structure

1. Create a new PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Get the document's [ITaggedContent](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.tagged/itaggedcontent/).
1. Set the tagged [ITaggedContent](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.tagged/itaggedcontent/) title and language.
1. Read the [StructTreeRootElement](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.tagged.logicalstructure/structtreerootelement/) and the root [StructureElement](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.tagged.logicalstructure.elements/structureelement/).
1. Save the tagged PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

```java
public static void getRootStructure(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        System.out.println("StructTreeRootElement: " + taggedContent.getStructTreeRootElement());
        System.out.println("RootElement: " + taggedContent.getRootElement());

        document.save(outputFile.toString());
    }
}
```

## Access child elements

This example iterates through child structure elements, prints their properties, and updates the first child branch.

1. Open the tagged PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Get the document's [ITaggedContent](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.tagged/itaggedcontent/).
1. Read the child [ElementList](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.tagged.logicalstructure/elementlist/) from the [StructTreeRootElement](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.tagged.logicalstructure/structtreerootelement/).
1. Iterate through the child [StructureElement](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.tagged.logicalstructure.elements/structureelement/) items and print their structure properties.
1. Get the first child [Element](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.tagged.logicalstructure.elements/element/) from the root [StructureElement](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.tagged.logicalstructure.elements/structureelement/).
1. Update the child [StructureElement](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.tagged.logicalstructure.elements/structureelement/) items with title, language, actual text, expansion text, and alternative text.
1. Save the updated tagged PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

```java
public static void accessChildElements(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ITaggedContent taggedContent = document.getTaggedContent();

        ElementList elementList = taggedContent.getStructTreeRootElement().getChildElements();
        for (Object element : elementList) {
            if (element instanceof StructureElement structureElement) {
                System.out.println("StructureElement properties - "
                        + "title: " + structureElement.getTitle()
                        + ", language: " + structureElement.getLanguage()
                        + ", actual_text: " + structureElement.getActualText()
                        + ", expansion_text: " + structureElement.getExpansionText()
                        + ", alternative_text: " + structureElement.getAlternativeText());
            }
        }

        Element firstChild = taggedContent.getRootElement().getChildElements().get_Item(1);
        for (Object element : firstChild.getChildElements()) {
            if (element instanceof StructureElement structureElement) {
                structureElement.setTitle("title");
                structureElement.setLanguage("fr-FR");
                structureElement.setActualText("actual text");
                structureElement.setExpansionText("exp");
                structureElement.setAlternativeText("alt");
            }
        }

        document.save(outputFile.toString());
    }
}
```

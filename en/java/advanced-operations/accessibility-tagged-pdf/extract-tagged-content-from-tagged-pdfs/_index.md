---
title: Extract Tagged Content from PDFs in Java
linktitle: Extract Tagged Content
type: docs
weight: 20
url: /java/extract-tagged-content-from-tagged-pdfs/
description: Learn how to inspect tagged PDF content in Java with Aspose.PDF, including tagged content access, root structure access, and child structure elements.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
Use these APIs when you need to inspect the logical structure tree of a tagged PDF and examine or update structure element metadata.

## Get tagged content metadata

Use this example when you need access to the tagged content container and want to define basic document metadata such as title and language.

1. Create a new PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Get the [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf/itaggedcontent/) object from the document.
1. Set the tagged content metadata and save the output file.

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

## Get the root structure of a tagged PDF

This example shows how to inspect the root objects that represent the structure tree of a tagged PDF.

1. Create a new PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) and get its tagged content.
1. Set the required document metadata.
1. Read and print the structure tree root and logical root element, then save the file.

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

## Access and update child structure elements

Use this example when you need to iterate through child elements in the structure tree, inspect their properties, and update selected metadata.

1. Open the source tagged PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Read the child elements from the structure tree root and print the available properties.
1. Access the child elements of the first root child, update their metadata, and save the document.

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

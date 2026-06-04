---
title: Extract Tagged Content from PDFs in Java
linktitle: Extract Tagged Content
type: docs
weight: 20
url: /java/extract-tagged-content-from-tagged-pdfs/
description: Learn how to inspect tagged PDF content in Java with Aspose.PDF, including tagged content access, root structure access, and child structure elements.
lastmod: "2026-06-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
Use these APIs when you need to inspect the logical structure tree of a tagged PDF and examine or update structure element metadata.

## Get tagged content

1. Create a new PDF document.
1. Get the document's tagged content.
1. Set the tagged document title and language.
1. Save the tagged PDF document.

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

1. Create a new PDF document.
1. Get the document's tagged content.
1. Set the tagged document title and language.
1. Read the structure tree root element and the root structure element.
1. Save the tagged PDF document.

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

1. Open the tagged PDF document.
1. Get the document's tagged content.
1. Read the child elements from the structure tree root.
1. Iterate through the child elements and print their structure properties.
1. Get the first child element from the root structure.
1. Update the child structure elements with title, language, actual text, expansion text, and alternative text.
1. Save the updated tagged PDF document.

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

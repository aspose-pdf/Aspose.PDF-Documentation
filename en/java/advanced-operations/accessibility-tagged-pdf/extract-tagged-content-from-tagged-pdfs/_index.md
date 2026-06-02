---
title: Extract Tagged Content from PDFs in Java
linktitle: Extract Tagged Content
type: docs
weight: 20
url: /java/extract-tagged-content-from-tagged-pdfs/
description: Learn how to inspect tagged PDF content in Java with Aspose.PDF, including tagged content access, root structure access, and child structure elements.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
Use these APIs when you need to inspect the logical structure tree of a tagged PDF and examine or update structure element metadata.

## Get tagged content

1. Open the PDF document used in this example.
2. Use the Aspose.PDF API calls shown here to get tagged content.
3. Read the returned values or continue with your next processing step.

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

1. Open or create the PDF document used in this example.
2. Use the Aspose.PDF API calls shown in the snippet to access the root structure.
3. Save the document or inspect the result, depending on the scenario.

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

1. Open or create the PDF document used in this example.
2. Use the Aspose.PDF API calls shown in the snippet to access child elements.
3. Save the document or inspect the result, depending on the scenario.

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

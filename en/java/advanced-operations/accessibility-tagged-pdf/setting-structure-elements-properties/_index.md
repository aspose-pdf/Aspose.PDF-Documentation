---
title: Set Tagged PDF Structure Element Properties in Java
linktitle: Setting Structure Elements Properties
type: docs
weight: 30
url: /java/setting-structure-elements-properties/
description: Learn how to set tagged PDF structure element properties in Java with Aspose.PDF, including title, language, actual text, alternative text, expansion text, links, notes, and tag names.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
This page covers common property-setting patterns for tagged PDF structure elements in Java.

## Set core structure element properties

1. Create a new PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Get the document's [ITaggedContent](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.tagged/itaggedcontent/).
1. Set the tagged [ITaggedContent](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.tagged/itaggedcontent/) title and language.
1. Get the root [StructureElement](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.tagged.logicalstructure.elements/structureelement/) and create a [SectElement](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.tagged.logicalstructure.elements.grouping/sectelement/).
1. Append the [SectElement](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.tagged.logicalstructure.elements.grouping/sectelement/) to the root [StructureElement](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.tagged.logicalstructure.elements/structureelement/).
1. Create a level 1 [HeaderElement](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/headerelement/) and add it to the [SectElement](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.tagged.logicalstructure.elements.grouping/sectelement/).
1. Set the [HeaderElement](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/headerelement/) text.
1. Set the [HeaderElement](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/headerelement/) title, language, alternative text, expansion text, and actual text.
1. Save the tagged PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

```java
public static void setProperties(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        StructureElement rootElement = taggedContent.getRootElement();
        SectElement sectionElement = taggedContent.createSectElement();
        rootElement.appendChild(sectionElement, true);

        HeaderElement headerElement = taggedContent.createHeaderElement(1);
        sectionElement.appendChild(headerElement, true);
        headerElement.setText("The Header");

        headerElement.setTitle("Title");
        headerElement.setLanguage("en-US");
        headerElement.setAlternativeText("Alternative Text");
        headerElement.setExpansionText("Expansion Text");
        headerElement.setActualText("Actual Text");

        document.save(outputFile.toString());
    }
}
```

## Set block and inline text elements

`TaggedPdfSetPropertiesExamples.java` includes examples for:

- creating paragraph text elements
- creating header levels 1 through 6
- combining paragraphs with nested span elements
- assigning custom tag names to paragraphs and spans

## Work with links, figures, notes, and language

The same example class also shows how to:

- create `LinkElement` instances with `WebHyperlink`
- add a `FigureElement` inside a link and set alternative text
- create `NoteElement` instances and assign IDs
- assign document and paragraph language values for multilingual content

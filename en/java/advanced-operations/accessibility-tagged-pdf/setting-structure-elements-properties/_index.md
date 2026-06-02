---
title: Set Tagged PDF Structure Element Properties in Java
linktitle: Setting Structure Elements Properties
type: docs
weight: 30
url: /java/setting-structure-elements-properties/
description: Learn how to set tagged PDF structure element properties in Java with Aspose.PDF, including title, language, actual text, alternative text, expansion text, links, notes, and tag names.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
This page covers common property-setting patterns for tagged PDF structure elements in Java.

## Set core structure element properties

1. Load the PDF document or object that will be updated.
2. Apply the settings shown in the example to set core structure element properties.
3. Save the document if the change should persist.

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

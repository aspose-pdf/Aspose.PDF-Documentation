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

## Set common structure element properties

Use this example when a tagged structure element should expose accessibility metadata such as title, language, actual text, and alternative text.

1. Create a new tagged PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) and initialize the tagged content metadata.
1. Create a section and header element in the structure tree.
1. Set the header properties and save the document.

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

## Set text elements

Use this example when you need to add a simple paragraph element to the tagged structure tree.

1. Create a new tagged PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create a [ParagraphElement](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.logicalstructure/paragraphelement/) and set its text.
1. Append the paragraph to the root element and save the document.

```java
public static void setTextElements(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        ParagraphElement paragraphElement = taggedContent.createParagraphElement();
        paragraphElement.setText("Paragraph.");
        taggedContent.getRootElement().appendChild(paragraphElement, true);

        document.save(outputFile.toString());
    }
}
```

## Set text block elements

This example creates multiple block-level structure elements, including headings of several levels and a paragraph.

1. Create a new tagged PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Add header elements for the required levels and then create a paragraph element.
1. Append the block elements to the root structure and save the document.

```java
public static void setTextBlockElements(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        for (int level = 1; level <= 6; level++) {
            HeaderElement header = taggedContent.createHeaderElement(level);
            header.setText("H" + level + ". Header of Level " + level);
            taggedContent.getRootElement().appendChild(header, true);
        }

        ParagraphElement p = taggedContent.createParagraphElement();
        p.setText("P. Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                + "Aenean nec lectus ac sem faucibus imperdiet.");
        taggedContent.getRootElement().appendChild(p, true);

        document.save(outputFile.toString());
    }
}
```

## Set inline elements

Use this example when block structure elements should contain nested inline spans.

1. Create a new tagged PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Build header elements and append span children to them.
1. Create a paragraph with multiple spans and save the document.

```java
public static void setInlineElements(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        for (int level = 1; level <= 6; level++) {
            HeaderElement header = taggedContent.createHeaderElement(level);
            taggedContent.getRootElement().appendChild(header, true);

            SpanElement span1 = taggedContent.createSpanElement();
            span1.setText("H" + level + ". ");
            header.appendChild(span1, true);

            SpanElement span2 = taggedContent.createSpanElement();
            span2.setText("Level " + level + " Header");
            header.appendChild(span2, true);
        }

        ParagraphElement paragraphElement = taggedContent.createParagraphElement();
        paragraphElement.setText("P. ");
        taggedContent.getRootElement().appendChild(paragraphElement, true);

        for (int index = 1; index <= 10; index++) {
            SpanElement span = taggedContent.createSpanElement();
            span.setText("Span " + index + ". ");
            paragraphElement.appendChild(span, true);
        }

        document.save(outputFile.toString());
    }
}
```

## Set custom tag names

This example assigns custom tag names to paragraph and span elements in the tagged structure.

1. Create a new tagged PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) and add a section element.
1. Create paragraphs and spans, then set custom tag names for each element.
1. Append the elements to the section and save the document.

```java
public static void setTagName(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        SectElement sectionElement = taggedContent.createSectElement();
        taggedContent.getRootElement().appendChild(sectionElement, true);

        String[] paragraphTags = {"P1", "Para", "Para", "Paragraph"};
        String[] spanTags = {"SPAN", "Sp", "Sp", "TheSpan"};

        for (int index = 0; index < 4; index++) {
            ParagraphElement paragraph = taggedContent.createParagraphElement();
            paragraph.setText("P" + (index + 1) + ". ");
            paragraph.setTag(paragraphTags[index]);

            SpanElement span = taggedContent.createSpanElement();
            span.setText("Span " + (index + 1) + ".");
            span.setTag(spanTags[index]);

            paragraph.appendChild(span, true);
            sectionElement.appendChild(paragraph, true);
        }

        document.save(outputFile.toString());
    }
}
```

## Set link and figure elements

Use this example when tagged link elements should include alternate descriptions, hyperlinks, and figure content with layout attributes.

1. Create a new tagged PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) and add link elements inside paragraphs.
1. Configure hyperlink targets, alternate descriptions, and the linked figure element.
1. Set the required layout attribute and save the document.

```java
public static void setElements(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Link Elements Example");
        taggedContent.setLanguage("en-US");

        for (int index = 1; index <= 4; index++) {
            ParagraphElement paragraph = taggedContent.createParagraphElement();
            taggedContent.getRootElement().appendChild(paragraph, true);

            LinkElement link = taggedContent.createLinkElement();
            paragraph.appendChild(link, true);
            link.setHyperlink(new WebHyperlink("http://google.com"));
            link.setText(index == 4 ? "The multiline link: Google Google Google Google" : "Google");
            link.setAlternateDescriptions("Link to Google");
        }

        ParagraphElement paragraph = taggedContent.createParagraphElement();
        taggedContent.getRootElement().appendChild(paragraph, true);

        LinkElement link = taggedContent.createLinkElement();
        paragraph.appendChild(link, true);
        link.setHyperlink(new WebHyperlink("http://google.com"));

        FigureElement figure = taggedContent.createFigureElement();
        figure.setImage(imageFile.toString(), 1200);
        figure.setAlternativeText("Google icon");

        StructureAttributes linkLayoutAttributes = link.getAttributes().getAttributes(AttributeOwnerStandard.Layout);
        StructureAttribute placementAttribute = new StructureAttribute(AttributeKey.Placement);
        placementAttribute.setNameValue(AttributeName.Placement_Block);
        linkLayoutAttributes.setAttribute(placementAttribute);

        link.appendChild(figure, true);
        link.setAlternateDescriptions("Link to Google");

        document.save(outputFile.toString());
    }
}
```

## Add paragraphs with inline link-related content

This example creates paragraph elements that combine plain text and nested span elements.

1. Create a new tagged PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create paragraph elements and add span children with custom text.
1. Append the paragraphs to the root element and save the document.

```java
public static void addLinkElement(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Text Elements Example");
        taggedContent.setLanguage("en-US");

        for (int paragraphIndex = 1; paragraphIndex <= 4; paragraphIndex++) {
            ParagraphElement paragraph = taggedContent.createParagraphElement();
            taggedContent.getRootElement().appendChild(paragraph, true);

            SpanElement span1 = taggedContent.createSpanElement();
            span1.setText("Span_" + paragraphIndex + "1");
            SpanElement span2 = taggedContent.createSpanElement();
            span2.setText(" and Span_" + paragraphIndex + "2.");

            paragraph.setText("Paragraph with ");
            paragraph.appendChild(span1, true);
            paragraph.appendChild(span2, true);
        }

        document.save(outputFile.toString());
    }
}
```

## Set note elements

Use this example when note structure elements should be created with automatic or explicit IDs.

1. Create a new tagged PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) and add a paragraph element.
1. Create note elements and set their text and IDs as needed.
1. Append the notes to the paragraph and save the document.

```java
public static void setNoteElement(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Sample of Note Elements");
        taggedContent.setLanguage("en-US");

        ParagraphElement paragraph = taggedContent.createParagraphElement();
        taggedContent.getRootElement().appendChild(paragraph, true);

        NoteElement note1 = taggedContent.createNoteElement();
        paragraph.appendChild(note1, true);
        note1.setText("Note with auto generate ID. ");

        NoteElement note2 = taggedContent.createNoteElement();
        paragraph.appendChild(note2, true);
        note2.setText("Note with ID = 'note_002'. ");
        note2.setId("note_002");

        NoteElement note3 = taggedContent.createNoteElement();
        paragraph.appendChild(note3, true);
        note3.setText("Note with ID = 'note_003'. ");
        note3.setId("note_003");

        document.save(outputFile.toString());
    }
}
```

## Set language and title for multilingual content

This example assigns document-level metadata and then creates paragraphs with different language values.

1. Create a new tagged PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) and set the document title and language.
1. Add a header element and create paragraphs for each localized phrase.
1. Save the multilingual tagged document.

```java
public static void setLanguageAndTitle(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Example Tagged Document");
        taggedContent.setLanguage("en-US");

        HeaderElement header = taggedContent.createHeaderElement(1);
        header.setText("Phrase on different languages");
        taggedContent.getRootElement().appendChild(header, true);

        addParagraph(taggedContent, "Hello, World!", "en-US");
        addParagraph(taggedContent, "Hallo Welt!", "de-DE");
        addParagraph(taggedContent, "Bonjour le monde!", "fr-FR");
        addParagraph(taggedContent, "Hola Mundo!", "es-ES");

        document.save(outputFile.toString());
    }
}
```

## Add a paragraph helper for tagged content

This helper method creates a paragraph, assigns its language, and appends it to the root structure.

1. Create a [ParagraphElement](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.logicalstructure/paragraphelement/).
1. Set the text and language for the element.
1. Append the paragraph to the tagged content root element.

```java
private static void addParagraph(ITaggedContent taggedContent, String text, String language) {
    ParagraphElement paragraph = taggedContent.createParagraphElement();
    paragraph.setText(text);
    paragraph.setLanguage(language);
    taggedContent.getRootElement().appendChild(paragraph, true);
}
```

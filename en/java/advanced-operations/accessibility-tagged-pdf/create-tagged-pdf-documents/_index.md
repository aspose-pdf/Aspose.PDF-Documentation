---
title: Create Tagged PDF in Java
linktitle: Create Tagged PDF
type: docs
weight: 10
url: /java/create-tagged-pdf/
description: Learn how to create tagged PDF documents in Java with Aspose.PDF, including PDF/UA structure elements, accessible form fields, TOC pages, and automatic tagging.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
Creating a tagged PDF means adding structure elements that make the document easier to validate against PDF/UA accessibility requirements and easier for assistive technologies to interpret.

## Create a simple tagged PDF

This example creates a tagged PDF with a header and a paragraph.

1. Initialize the PDF document and any resources required by this example.
2. Build and configure the Aspose.PDF objects needed to create a simple tagged PDF.
3. Save the output document or generated file.

```java
public static void createTaggedPdfDocumentSimple(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        StructureElement rootElement = taggedContent.getRootElement();

        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        HeaderElement mainHeader = taggedContent.createHeaderElement();
        mainHeader.setText("Main Header");

        ParagraphElement paragraphElement = taggedContent.createParagraphElement();
        paragraphElement.setText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                + "Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. "
                + "Cras pellentesque libero semper, gravida magna sed, luctus leo.");

        rootElement.appendChild(mainHeader, true);
        rootElement.appendChild(paragraphElement, true);
        document.save(outputFile.toString());
    }
}
```

## Create an advanced tagged PDF

The advanced example builds a heading plus a paragraph that mixes spans and a quote element.

1. Initialize the PDF document and any resources required by this example.
2. Build and configure the Aspose.PDF objects needed to create an advanced tagged PDF.
3. Save the output document or generated file.

```java
public static void createTaggedPdfDocumentAdv(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        StructureElement rootElement = taggedContent.getRootElement();

        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        HeaderElement header1 = taggedContent.createHeaderElement(1);
        header1.setText("Header Level 1");

        ParagraphElement paragraphWithQuotes = taggedContent.createParagraphElement();
        paragraphWithQuotes.getStructureTextState().setFont(FontRepository.findFont("Arial"));

        SpanElement spanElement1 = taggedContent.createSpanElement();
        spanElement1.setText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. ");

        QuoteElement quoteElement = taggedContent.createQuoteElement();
        quoteElement.setText("Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus.");

        SpanElement spanElement2 = taggedContent.createSpanElement();
        spanElement2.setText(" Sed non consectetur elit.");

        paragraphWithQuotes.appendChild(spanElement1, true);
        paragraphWithQuotes.appendChild(quoteElement, true);
        paragraphWithQuotes.appendChild(spanElement2, true);

        rootElement.appendChild(header1, true);
        rootElement.appendChild(paragraphWithQuotes, true);
        document.save(outputFile.toString());
    }
}
```

## Additional tagged-PDF creation scenarios

`TaggedPdfCreateExamples.java` also covers:

- styling tagged text with structure text state
- creating figure elements with alternative text and explicit positioning
- validating tagged PDFs against `PdfFormat.PDF_UA_1`
- adjusting the position of text structure elements
- converting an existing PDF to PDF/UA with automatic tagging
- creating tagged form fields
- creating tagged PDFs with table-of-contents pages

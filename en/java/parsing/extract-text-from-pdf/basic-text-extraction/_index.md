---
title: Basic Text Extraction using Java
linktitle: Basic Text Extraction
type: docs
weight: 10
url: /java/basic-text-extraction/
description: Learn how to extract text from PDF documents in Java with Aspose.PDF from all pages, from a specific page, or by paragraph structure.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
Basic text extraction is the starting point for reading PDF content in Java. Aspose.PDF provides two common approaches:

- Use `TextAbsorber` when you need a plain text result from a document or page.
- Use `ParagraphAbsorber` when you need to preserve page, section, paragraph, line, and fragment grouping.

PDF pages do not store text like a word-processing document, so the extracted order depends on the page content stream and layout. For region-specific extraction, geometry details, multi-column layouts, annotations, highlighted text, or superscript and subscript detection, use the related extraction articles in this section.

## Extract text from all pages

Use `TextAbsorber` to collect a flat text stream from the whole document and write it to a file. This is the simplest option when you only need the readable text content and do not need paragraph boundaries or coordinates.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create a [TextAbsorber](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/textabsorber/).
1. Visit all [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) objects in the document.
1. Write the extracted text to the output file.

```java
public static void extractTextFromAllPages(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber textAbsorber = new TextAbsorber();
        document.getPages().accept(textAbsorber);
        Files.writeString(outputFile, textAbsorber.getText());
    }
}
```

## Extract text from a specific page

Apply the absorber only to the page you need. Page numbers in the `Document` pages collection are 1-based, so `get_Item(1)` reads the first page.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create a [TextAbsorber](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/textabsorber/).
1. Visit the target [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/).
1. Write the extracted text to the output file.

```java
public static void extractTextFromPage(Path inputFile, Path outputFile, int pageNumber) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber textAbsorber = new TextAbsorber();
        document.getPages().get_Item(pageNumber).accept(textAbsorber);
        Files.writeString(outputFile, textAbsorber.getText());
    }
}
```

## Extract text by paragraph structure

Use `ParagraphAbsorber` when you need structural grouping instead of a single plain text stream. It returns page markups with sections, paragraphs, lines, and `TextFragment` objects, which is useful when the output must preserve logical blocks of text.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create a [ParagraphAbsorber](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/paragraphabsorber/) and visit the document.
1. Iterate through the page markups, sections, paragraphs, lines, and [TextFragment](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/textfragment/) objects.
1. Build the output text with page, section, and paragraph information.
1. Write the extracted paragraph text to the output file.

```java
public static void extractParagraphsFromPdf(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        ParagraphAbsorber absorber = new ParagraphAbsorber();
        absorber.visit(document);

        StringBuilder text = new StringBuilder();
        for (PageMarkup pageMarkup : absorber.getPageMarkups()) {
            int sectionIndex = 1;
            for (MarkupSection section : pageMarkup.getSections()) {
                int paragraphIndex = 1;
                for (MarkupParagraph paragraph : section.getParagraphs()) {
                    StringBuilder paragraphText = new StringBuilder();
                    for (List<TextFragment> line : paragraph.getLines()) {
                        for (TextFragment fragment : line) {
                            paragraphText.append(fragment.getText());
                        }
                        paragraphText.append("\r\n");
                    }
                    text.append("Page ").append(pageMarkup.getNumber())
                            .append(", Section ").append(sectionIndex)
                            .append(", Paragraph ").append(paragraphIndex)
                            .append(":\n");
                    text.append(paragraphText).append("\n");
                    paragraphIndex++;
                }
                sectionIndex++;
            }
        }

        Files.writeString(outputFile, text.toString());
    }
}
```

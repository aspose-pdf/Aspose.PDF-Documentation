---
title: Basic Text Extraction using Java
linktitle: Basic Text Extraction
type: docs
weight: 10
url: /java/basic-text-extraction/
description: Learn how to extract text from PDF documents in Java with Aspose.PDF from all pages, from a specific page, or by paragraph structure.
lastmod: "2026-06-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Extract text from all pages

Use `TextAbsorber` to capture text from the whole document and write it to a file.

1. Open the source PDF document.
1. Create a `TextAbsorber`.
1. Visit all pages in the document.
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

Apply the absorber only to the page you need.

1. Open the source PDF document.
1. Create a `TextAbsorber`.
1. Visit the target page.
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

Use `ParagraphAbsorber` when you need page, section, and paragraph grouping instead of a flat text stream.

1. Open the source PDF document.
1. Create a `ParagraphAbsorber` and visit the document.
1. Iterate through the page markups, sections, paragraphs, lines, and text fragments.
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

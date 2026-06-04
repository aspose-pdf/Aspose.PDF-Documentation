---
title: Region-Based Extraction using Java
linktitle: Region-Based Extraction
type: docs
weight: 20
url: /java/region-based-extraction/
description: Learn how to extract text from a specific page region or inspect paragraph geometry in PDF documents with Aspose.PDF for Java.
lastmod: "2026-06-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Extract text from a rectangular page region

Use `TextSearchOptions` with a `Rectangle` to restrict extraction to a defined area on a page.

1. Open the source PDF document.
1. Create a `TextAbsorber`.
1. Create text search options for the target rectangle and limit extraction to page bounds.
1. Apply the search options to the absorber.
1. Visit the target page and write the extracted text to the output file.

```java
public static void extractTextFromRegion(Path inputFile, Path outputFile, int pageNumber, Rectangle rectangle)
        throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber absorber = new TextAbsorber();
        TextSearchOptions options = new TextSearchOptions(rectangle);
        options.setLimitToPageBounds(true);
        absorber.setTextSearchOptions(options);
        document.getPages().get_Item(pageNumber).accept(absorber);
        Files.writeString(outputFile, absorber.getText());
    }
}
```

## Extract paragraphs with geometry information

Use `ParagraphAbsorber` to inspect section rectangles and paragraph polygons together with the extracted text.

1. Open the source PDF document.
1. Create a `ParagraphAbsorber` and visit the target page.
1. Get the page markup from the absorber results.
1. Iterate through the sections and paragraphs and read their geometry information.
1. Build the output text with rectangles, polygons, and extracted paragraph text.
1. Write the extracted details to the output file.

```java
public static void extractParagraphsWithGeometry(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        ParagraphAbsorber absorber = new ParagraphAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        PageMarkup pageMarkup = absorber.getPageMarkups().get(0);
        StringBuilder text = new StringBuilder();
        int sectionIndex = 1;
        for (MarkupSection section : pageMarkup.getSections()) {
            text.append("Section ").append(sectionIndex)
                    .append(": rectangle = ").append(section.getRectangle()).append("\n");
            int paragraphIndex = 1;
            for (MarkupParagraph paragraph : section.getParagraphs()) {
                text.append("  Paragraph ").append(paragraphIndex)
                        .append(": polygon = ").append(Arrays.toString(paragraph.getPoints())).append("\n");
                StringBuilder paragraphText = new StringBuilder();
                for (List<TextFragment> line : paragraph.getLines()) {
                    for (TextFragment fragment : line) {
                        paragraphText.append(fragment.getText());
                    }
                    paragraphText.append("\r\n");
                }
                text.append("    Text: ").append(paragraphText).append("\n\n");
                paragraphIndex++;
            }
            sectionIndex++;
        }

        Files.writeString(outputFile, text.toString());
    }
}
```

---
title: Format PDF Text in Java
linktitle: Text Formatting inside PDF
type: docs
weight: 70
url: /java/text-formatting-inside-pdf/
description: Learn how to format text inside PDF documents in Java using spacing, notes, lists, multi-column layout, and styling options.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Format and style text inside PDF files with Java
Abstract: This article explains how to format text in PDF documents using Aspose.PDF for Java. It covers line spacing, character spacing, bullet and numbered lists, footnotes and endnotes, inline paragraph content, multi-column layout, forced page breaks, and custom tab stops.
---
Aspose.PDF for Java provides formatting features at the text state, paragraph, and page layout levels.

## Specify line spacing

1. Open or create the PDF document used in this example.
2. Use the Aspose.PDF API calls shown in the snippet to specify line spacing.
3. Save the document or inspect the result, depending on the scenario.

```java
public static void specifyLineSpacingSimpleCase(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("Lorem ipsum text");
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setLineSpacing(16);
        page.getParagraphs().add(textFragment);

        document.save(outputFile.toString());
    }
}
```

## Character spacing, lists, and notes

The example class also includes:

- `characterSpacingUsingTextFragment`
- `characterSpacingUsingTextParagraph`
- `createBulletListHtmlVersion`
- `createNumberedListHtmlVersion`
- `createBulletListLatexVersion`
- `createNumberedListLatexVersion`
- `createBulletList`
- `createNumberedList`
- `addFootnote`
- `addFootnoteCustomTextStyle`
- `addFootnoteCustomText`
- `addFootnoteWithCustomLineStyle`
- `addFootnoteWithImageAndTable`
- `addEndnote`
- `addEndnoteCustomText`

## Multi-column layout, forced page breaks, and tab stops

The same source file also demonstrates:

- `forceNewPage`
- `usingInlineParagraphProperty`
- `createMultiColumnPdf`
- `customTabStops`

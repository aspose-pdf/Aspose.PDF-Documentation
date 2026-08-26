---
title: Improving Text Extraction from Multi-Column PDFs
linktitle: Text Extraction from Multi-Column PDFs
type: docs
weight: 30
url: /java/text-extraction-from-multi-column-pdf/
description: Learn techniques for improving text extraction from multi-column PDF layouts with Aspose.PDF for Java.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
Multi-column layouts often require extra processing to improve reading order and extraction quality.

## Extract text after reducing font size

This technique updates the text fragment font sizes, saves the adjusted document to memory, and then extracts text from the transformed result.

1. Open the source PDF in a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instance.
1. Create a [TextFragmentAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragmentabsorber/) and visit all document pages to collect [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) objects.
1. Iterate through the fragments and reduce each font size by the requested ratio so dense column layout can be normalized before extraction.
1. Save the adjusted [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) to an in-memory byte stream.
1. Reopen a second [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) from that memory buffer.
1. Create a [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/), visit all pages of the transformed document, and write the extracted text to the output file.

```java
public static void extractTextReduceFont(Path inputFile, Path outputFile, double reduceRatio) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber fragmentAbsorber = new TextFragmentAbsorber();
        document.getPages().accept(fragmentAbsorber);
        for (TextFragment fragment : fragmentAbsorber.getTextFragments()) {
            fragment.getTextState().setFontSize((float) (fragment.getTextState().getFontSize() * reduceRatio));
        }

        ByteArrayOutputStream stream = new ByteArrayOutputStream();
        document.save(stream);
        try (Document document2 = new Document(new ByteArrayInputStream(stream.toByteArray()))) {
            TextAbsorber textAbsorber = new TextAbsorber();
            document2.getPages().accept(textAbsorber);
            Files.writeString(outputFile, textAbsorber.getText());
        }
    }
}
```

## Extract text with a scale factor

Use `TextExtractionOptions` in pure formatting mode and tune the scale factor for column-heavy layouts.

1. Open the source PDF in a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instance.
1. Create a [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) for full-document extraction.
1. Create [TextExtractionOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/textextractionoptions/) in pure formatting mode so layout-sensitive extraction behavior is used.
1. Set the scale factor and apply the extraction options to the absorber before visiting the pages.
1. Visit all document pages and write the extracted text to the output file.

```java
public static void extractTextScaleFactor(Path inputFile, Path outputFile, double scaleFactor) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber textAbsorber = new TextAbsorber();
        TextExtractionOptions extractionOptions =
                new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
        extractionOptions.setScaleFactor(scaleFactor);
        textAbsorber.setExtractionOptions(extractionOptions);
        document.getPages().accept(textAbsorber);
        Files.writeString(outputFile, textAbsorber.getText());
    }
}
```

---
title: Search and Extract PDF Text in Java
linktitle: Search and Get Text
type: docs
weight: 60
url: /java/search-and-get-text-from-pdf/
description: Learn how to search, inspect, and extract text from PDF documents in Java.
lastmod: "2026-06-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Search PDF text and inspect extracted fragments in Java
Abstract: This article explains how to search and extract text from PDF documents using Aspose.PDF for Java. It covers TextAbsorber and TextFragmentAbsorber, including region-based extraction, page-specific searches, regex and phrase matching, hyperlink insertion, styled-text inspection, and fragment highlighting.
---
Aspose.PDF for Java provides multiple search models depending on whether you need raw extracted text or detailed fragment-level metadata.

## Search text with `TextAbsorber`

1. Open the source PDF document.
1. Configure the text search options required by the example.
1. Process the matched results returned by the search.

```java
public static void textAbsorberSearch(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextExtractionOptions textExtractionOptions = new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
        TextSearchOptions textSearchOptions = new TextSearchOptions(new Rectangle(0, 0, 842, 250, true));
        TextAbsorber absorber = new TextAbsorber(textExtractionOptions, textSearchOptions);

        document.getPages().accept(absorber);
        System.out.println("Text fragments found: " + absorber.getText());
    }
}
```

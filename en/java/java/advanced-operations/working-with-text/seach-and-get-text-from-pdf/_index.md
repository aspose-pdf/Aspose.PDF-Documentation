---
title: Search and Extract PDF Text in Java
linktitle: Search and Get Text
type: docs
weight: 60
url: /java/search-and-get-text-from-pdf/
description: Learn how to search, inspect, and extract text from PDF documents in Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Search PDF text and inspect extracted fragments in Java
Abstract: This article explains how to search and extract text from PDF documents using Aspose.PDF for Java. It covers TextAbsorber and TextFragmentAbsorber, including region-based extraction, page-specific searches, regex and phrase matching, hyperlink insertion, styled-text inspection, and fragment highlighting.
---
Aspose.PDF for Java supports raw text extraction and fragment-level search with coordinates, styles, and regex matching.

## Extract text from all pages with TextAbsorber

Use this example when you need plain extracted text from a selected document region across all pages.

1. Open the source PDF document.
1. Create `TextExtractionOptions` and region-based `TextSearchOptions`.
1. Run `TextAbsorber` on all pages and output the extracted text.

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

## Extract text from one page with TextAbsorber

Use this example when plain text extraction should be limited to one page.

1. Open the source PDF document.
1. Configure text extraction and search options with the target region.
1. Run `TextAbsorber` on the selected page and output the result.

```java
public static void textAbsorberSearchPage(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextExtractionOptions textExtractionOptions = new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
        TextSearchOptions textSearchOptions = new TextSearchOptions(new Rectangle(0, 0, 842, 250, true));
        TextAbsorber absorber = new TextAbsorber(textExtractionOptions, textSearchOptions);

        document.getPages().get_Item(2).accept(absorber);
        System.out.println("Text fragments found: " + absorber.getText());
    }
}
```

## Inspect all text fragments in the document

Use this example when you need text content together with font, position, and color metadata.

1. Open the source PDF document.
1. Run `TextFragmentAbsorber` across all pages.
1. Iterate through the fragments and output their metadata.

```java
public static void textFragmentAbsorberSearch(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        document.getPages().accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            System.out.println("Text: " + fragment.getText());
            System.out.println("Position: " + fragment.getPosition());
            System.out.println("XIndent: " + fragment.getPosition().getXIndent());
            System.out.println("YIndent: " + fragment.getPosition().getYIndent());
            System.out.println("Font - Name: " + fragment.getTextState().getFont().getFontName());
            System.out.println("Font - IsAccessible: " + fragment.getTextState().getFont().isAccessible());
            System.out.println("Font - IsEmbedded: " + fragment.getTextState().getFont().isEmbedded());
            System.out.println("Font - IsSubset: " + fragment.getTextState().getFont().isSubset());
            System.out.println("Font Size: " + fragment.getTextState().getFontSize());
            System.out.println("Foreground Color: " + fragment.getTextState().getForegroundColor());
        }
    }
}
```

## Search one phrase on a specific page

Use this example when a target word should be found on a selected page only.

1. Open the source PDF document.
1. Create `TextFragmentAbsorber` with the target phrase.
1. Visit the chosen page and output the matching fragment positions.

```java
public static void textFragmentAbsorberSearchPage(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("whale");
        document.getPages().get_Item(2).accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            System.out.println("Text: " + fragment.getText());
            System.out.println("Position: " + fragment.getPosition());
        }
    }
}
```

## Continue a sequential search across pages

Use this example when you want to reuse one absorber while moving from one page search to the next.

1. Open the source PDF document and create a reusable absorber.
1. Search the first page and inspect the results.
1. Continue searching additional pages and review the updated matches.

```java
public static void textFragmentAbsorberSequentialSearch(Path inputFile) {
    Document document = new Document(inputFile.toString());
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    absorber.setPhrase("whale");

    document.getPages().get_Item(1).accept(absorber);
    for (TextFragment fragment : absorber.getTextFragments()) {
        System.out.println("Text: " + fragment.getText());
        System.out.println("Page: " + fragment.getPage().getNumber());
        System.out.println("Position: " + fragment.getPosition());
    }

    System.out.println("--");

    document.getPages().get_Item(2).accept(absorber);
    absorber.visit(document);

    for (TextFragment fragment : absorber.getTextFragments()) {
        System.out.println("Text: " + fragment.getText());
        System.out.println("Page: " + fragment.getPage().getNumber());
        System.out.println("Position: " + fragment.getPosition());
    }
}
```

## Search a phrase inside a selected rectangle

Use this example when phrase matching should be limited to a region on one page.

1. Open the source PDF document.
1. Create `TextFragmentAbsorber` with the target phrase and rectangle-based `TextSearchOptions`.
1. Visit the page and output the matched fragment positions.

```java
public static void textFragmentAbsorberSearchPhrase(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(
                "elephant", new TextSearchOptions(new Rectangle(0, 0, 842, 250, true)));

        document.getPages().get_Item(2).accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            System.out.println("Text: " + fragment.getText());
            System.out.println("Position: " + fragment.getPosition());
        }
    }
}
```

## Search text by regular expression

Use this example when matches should be found by a regex pattern instead of a fixed phrase.

1. Open the source PDF document.
1. Create a regex-enabled `TextFragmentAbsorber`.
1. Visit the target page and output the matching fragments.

```java
public static void textFragmentAbsorberSearchRegex(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(
                Pattern.compile("\\d+\\.\\d+"), new TextSearchOptions(true));

        document.getPages().get_Item(2).accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            System.out.println("Text: " + fragment.getText());
            System.out.println("Position: " + fragment.getPosition());
        }
    }
}
```

## Search a list of phrases by regex patterns

Use this example when several target phrases should be found in one pass.

1. Open the source PDF document.
1. Create an array of regex patterns and pass it to `TextFragmentAbsorber`.
1. Visit the document and inspect the grouped regex results.

```java
public static void textFragmentAbsorberSearchListOfPhrases(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Pattern[] patterns = new Pattern[] {
                Pattern.compile("whale"),
                Pattern.compile("elephant")
        };
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(patterns, new TextSearchOptions(true));
        document.getPages().accept(absorber);

        for (TextFragmentCollection fragments : absorber.getRegexResults().values()) {
            for (TextFragment fragment : fragments) {
                System.out.println("Text: " + fragment.getText());
                System.out.println("Position: " + fragment.getPosition());
            }
        }
    }
}
```

## Find text and turn it into hyperlinks

Use this example when matched words should be highlighted and converted into clickable links.

1. Open the source PDF document.
1. Search the target words with regex search enabled.
1. Update the text style, attach hyperlinks, and save the modified PDF.

```java
public static void textFragmentAbsorberSearchAndAddHyperlink(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("whale|elephant");
        absorber.setTextSearchOptions(new TextSearchOptions(true));
        absorber.visit(document.getPages().get_Item(1));

        for (TextFragment fragment : absorber.getTextFragments()) {
            fragment.getTextState().setForegroundColor(Color.getBlue());
            fragment.getTextState().setUnderline(true);
            fragment.setHyperlink(new WebHyperlink("https://en.wikipedia.org/wiki/" + fragment.getText()));
        }

        document.save(inputFile.toString().replace("in.pdf", "out.pdf"));
    }
}
```

## Search text by style characteristics

Use this example when you need to inspect fragments based on formatting such as bold or invisible text.

1. Open the source PDF document.
1. Run `TextFragmentAbsorber` on the target page.
1. Check each fragment style and output the matching entries.

```java
public static void textFragmentAbsorberSearchStyledText(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.setTextSearchOptions(new TextSearchOptions(true));
        absorber.visit(document.getPages().get_Item(1));

        for (TextFragment fragment : absorber.getTextFragments()) {
            if (fragment.getTextState().getFontStyle() == FontStyles.Bold) {
                System.out.println("Bold: " + fragment.getText());
            }
            if (fragment.getTextState().isInvisible()) {
                System.out.println("Invisible: " + fragment.getText());
            }
        }
    }
}
```

## Highlight search results in rendered page previews

Use this example when text matches should be correlated with rendered page images for visual inspection.

1. Create a PNG device with the required resolution.
1. Search each page with `TextFragmentAbsorber` and render the page to an image stream.
1. Write the page preview images and output fragment coordinates for inspection.

```java
public static void textFragmentAbsorberSearchAndHighlight(Path inputFile) throws Exception {
    int resolution = 150;
    PngDevice pngDevice = new PngDevice(new Resolution(resolution, resolution));

    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(Pattern.compile("[\\S]+"));
        absorber.setTextSearchOptions(new TextSearchOptions(true));

        for (int pageNumber = 1; pageNumber <= document.getPages().size(); pageNumber++) {
            Page page = document.getPages().get_Item(pageNumber);
            page.accept(absorber);

            try (ByteArrayOutputStream stream = new ByteArrayOutputStream()) {
                pngDevice.process(page, stream);
                Path output = Path.of(inputFile.toString().replace("_in.pdf", page.getNumber() + "_out.png"));
                Files.write(output, stream.toByteArray());
            }

            for (TextFragment textFragment : absorber.getTextFragments()) {
                Rectangle pageRect = page.getPageRect(true);
                System.out.println("TextFragment = " + textFragment.getText()
                        + " Page URY = " + pageRect.getURY()
                        + " TextFragment URY = " + textFragment.getRectangle().getURY());
            }
        }
    }
}
```

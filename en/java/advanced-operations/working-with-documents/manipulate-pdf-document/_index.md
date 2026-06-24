---
title: Manipulate PDF Documents in Java
linktitle: Manipulate PDF Document
type: docs
weight: 20
url: /java/manipulate-pdf-document/
description: Learn how to validate, structure, and modify PDF documents in Java, including TOC management and PDF/A checks.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Validate, restructure, and flatten PDF documents with Java
Abstract: This article explains how to manipulate PDF documents using Aspose.PDF for Java. It covers validating PDF/A compliance, adding and customizing a table of contents, hiding or customizing TOC page numbers, assigning an expiry script, and flattening interactive form fields.
---
Aspose.PDF for Java includes document-structure operations that go beyond simple page editing.

## Validate PDF/A-1a compliance

Use this example when you need to check whether a document meets the PDF/A-1a archival standard.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Run validation against the required [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) target.
1. Save the validation report to the specified output path.

```java
public static void validatePdfaStandardA1a(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.validate(outputFile.toString(), PdfFormat.PDF_A_1A);
    }
}
```

## Validate PDF/A-1b compliance

This variation validates the same source document against the PDF/A-1b conformance level.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Call the validation method with the [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) value for PDF/A-1b.
1. Write the validation result to the output report file.

```java
public static void validatePdfaStandardA1b(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.validate(outputFile.toString(), PdfFormat.PDF_A_1B);
    }
}
```

## Add a table of contents

Use this approach when the document should include a generated TOC page with links to content pages.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Insert a new TOC [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) and configure its [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/).
1. Create [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) entries that point to the destination pages.
1. Save the updated document.

```java
public static void addTableOfContents(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page tocPage = document.getPages().insert(1);
        TocInfo tocInfo = new TocInfo();
        TextFragment title = new TextFragment("Table Of Contents");
        title.getTextState().setFontSize(20);
        title.getTextState().setFontStyle(FontStyles.Bold);
        tocInfo.setTitle(title);
        tocPage.setTocInfo(tocInfo);

        String[] titles = {"First page", "Second page"};
        for (int index = 0; index < titles.length && index + 2 <= document.getPages().size(); index++) {
            Heading heading = new Heading(1);
            TextSegment segment = new TextSegment(titles[index]);
            heading.setTocPage(tocPage);
            heading.getSegments().add(segment);
            Page destinationPage = document.getPages().get_Item(index + 2);
            heading.setDestinationPage(destinationPage);
            heading.setTop(destinationPage.getRect().getHeight());
            tocPage.getParagraphs().add(heading);
        }

        document.save(outputFile.toString());
    }
}
```

## Customize TOC levels and formatting

This example shows how to assign different visual settings to multiple table-of-contents levels.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Add a TOC [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) and configure the [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/) format array.
1. Create sample [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) entries with different levels.
1. Save the document with the formatted TOC.

```java
public static void setTocLevels(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page tocPage = document.getPages().add();
        TocInfo tocInfo = new TocInfo();
        tocInfo.setLineDash(TabLeaderType.Solid);
        TextFragment title = new TextFragment("Table Of Contents");
        title.getTextState().setFontSize(30);
        tocInfo.setTitle(title);
        tocPage.setTocInfo(tocInfo);

        tocInfo.setFormatArrayLength(4);
        tocInfo.getFormatArray()[0].getMargin().setLeft(0);
        tocInfo.getFormatArray()[0].getMargin().setRight(30);
        tocInfo.getFormatArray()[0].setLineDash(TabLeaderType.Dot);
        tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        tocInfo.getFormatArray()[1].getMargin().setLeft(10);
        tocInfo.getFormatArray()[1].getMargin().setRight(30);
        tocInfo.getFormatArray()[1].setLineDash(3);
        tocInfo.getFormatArray()[1].getTextState().setFontSize(10);
        tocInfo.getFormatArray()[2].getMargin().setLeft(20);
        tocInfo.getFormatArray()[2].getMargin().setRight(30);
        tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
        tocInfo.getFormatArray()[3].setLineDash(TabLeaderType.Solid);
        tocInfo.getFormatArray()[3].getMargin().setLeft(30);
        tocInfo.getFormatArray()[3].getMargin().setRight(30);
        tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

        try (Page page = document.getPages().add()) {
            for (int level = 1; level < 5; level++) {
                Heading heading = new Heading(level);
                heading.setAutoSequence(true);
                heading.setTocPage(tocPage);
                heading.getTextState().setFont(FontRepository.findFont("Arial"));
                heading.getSegments().add(new TextSegment("Sample Heading" + level));
                heading.setInList(true);
                page.getParagraphs().add(heading);
            }
        }

        document.save(outputFile.toString());
    }
}
```

## Hide page numbers in the TOC

Use this example when the table of contents should show entry titles without page numbers.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Add a TOC [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) and disable page numbers in [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/).
1. Create the required [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) entry and add it to the content page.
1. Save the updated document.

```java
public static void hidePageNumbersInToc(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page;
        Heading heading;
        try (Page tocPage = document.getPages().add()) {
            TocInfo tocInfo = new TocInfo();
            TextFragment title = new TextFragment("Table Of Contents");
            title.getTextState().setFontSize(20);
            title.getTextState().setFontStyle(FontStyles.Bold);
            tocInfo.setTitle(title);
            tocInfo.setShowPageNumbers(false);
            tocPage.setTocInfo(tocInfo);

            tocInfo.setFormatArrayLength(4);
            tocInfo.getFormatArray()[0].getMargin().setRight(0);
            tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
            tocInfo.getFormatArray()[1].getMargin().setLeft(30);
            tocInfo.getFormatArray()[1].getTextState().setUnderline(true);
            tocInfo.getFormatArray()[1].getTextState().setFontSize(10);
            tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
            tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

            page = document.getPages().add();
            heading = new Heading(1);
            heading.setTocPage(tocPage);
        }
        heading.setAutoSequence(true);
        heading.setInList(true);
        heading.getSegments().add(new TextSegment("this is heading of level 1"));
        page.getParagraphs().add(heading);

        document.save(outputFile.toString());
    }
}
```

## Customize TOC page number prefixes

This example adds a custom prefix to the page numbers displayed in the generated table of contents.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Insert a TOC [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) and set the desired page number prefix in [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/).
1. Create [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) entries that point to each page.
1. Save the updated document.

```java
public static void customizePageNumbersInToc(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page tocPage = document.getPages().insert(1);
        TocInfo tocInfo = new TocInfo();
        TextFragment title = new TextFragment("Table Of Contents");
        title.getTextState().setFontSize(20);
        title.getTextState().setFontStyle(FontStyles.Bold);
        tocInfo.setTitle(title);
        tocInfo.setPageNumbersPrefix("P");
        tocPage.setTocInfo(tocInfo);

        for (int index = 1; index <= document.getPages().size(); index++) {
            Page page = document.getPages().get_Item(index);
            Heading heading = new Heading(1);
            heading.setTocPage(tocPage);
            heading.setDestinationPage(page);
            heading.setTop(page.getRect().getHeight());
            heading.getSegments().add(new TextSegment("Page " + index));
            tocPage.getParagraphs().add(heading);
        }

        document.save(outputFile.toString());
    }
}
```

## Add a PDF expiry script

Use this approach when the document should run JavaScript on open and show an expiry warning after a specific date.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) and add any required content.
1. Create a [JavascriptAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/javascriptaction/) with the expiry logic.
1. Assign the script as the document open action and save the output file.

```java
public static void setPdfExpiryDate(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        try (Page page = document.getPages().add()) {
            page.getParagraphs().add(new TextFragment("Hello World..."));
        }
        JavascriptAction script = new JavascriptAction(
                "var year=2017;"
                        + "var month=5;"
                        + "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
                        + "expiry = new Date(year, month);"
                        + "if (today.getTime() > expiry.getTime())"
                        + "app.alert('The file is expired. You need a new one.');");
        document.setOpenAction(script);
        document.save(outputFile.toString());
    }
}
```

## Flatten a fillable PDF form

This example converts interactive form fields into static page content so the resulting document is no longer editable as a form.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Check whether the document contains form widgets.
1. Flatten each [Field](https://reference.aspose.com/pdf/java/com.aspose.pdf/field/) represented by a [WidgetAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/widgetannotation/).
1. Save the flattened document.

```java
public static void flattenFillablePdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getForm() != null && document.getForm().size() > 0) {
            for (WidgetAnnotation annotation : document.getForm()) {
                if (annotation instanceof Field field) {
                    field.flatten();
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```

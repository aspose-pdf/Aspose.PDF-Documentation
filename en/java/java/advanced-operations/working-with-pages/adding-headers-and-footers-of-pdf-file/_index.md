---
title: Add PDF Headers and Footers in Java
linktitle: Adding Header and Footer to PDF
type: docs
weight: 50
url: /java/add-headers-and-footers-of-pdf-file/
description: Learn how to add headers and footers to PDF files in Java using text, images, and structured content.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add headers and footers to PDF files with Java
Abstract: This article shows how to add headers and footers to PDF documents using Aspose.PDF for Java. It covers text, page numbering, HTML, image, table, and LaTeX-based header and footer content.
---
Aspose.PDF for Java lets you assign `HeaderFooter` objects to each page and populate them with different content types.

## Add text headers and footers

Use this example when you need simple text content at the top and bottom of each page.

1. Create [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) objects and add text fragments.
1. Configure margins for the header and footer.
1. Apply them to each page of the source PDF and save the result.

```java
public static void addHeaderAndFooterAsText(Path inputFile, Path outputFile) {
    HeaderFooter header = new HeaderFooter();
    header.getParagraphs().add(new TextFragment("Demo header"));

    HeaderFooter footer = new HeaderFooter();
    footer.getParagraphs().add(new TextFragment("Demo footer"));

    MarginInfo margin = new MarginInfo();
    margin.setLeft(50);
    margin.setTop(20);
    header.setMargin(margin);
    footer.setMargin(margin);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## Add headers and footers with page numbering

Use this example when the header or footer should show the current page number and total page count.

1. Create [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) objects with page numbering placeholders.
1. Configure margins for both objects.
1. Apply them to each page and save the updated PDF.

```java
public static void usingHeaderAndFooterForPageNumbering(Path inputFile, Path outputFile) {
    HeaderFooter header = new HeaderFooter();
    header.getParagraphs().add(new TextFragment("Page $p from $P"));

    HeaderFooter footer = new HeaderFooter();
    footer.getParagraphs().add(new TextFragment("Page $p / $P"));

    MarginInfo margin = new MarginInfo();
    margin.setLeft(50);
    margin.setTop(20);
    header.setMargin(margin);
    footer.setMargin(margin);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## Add HTML headers and footers

Use this example when header and footer content should include inline HTML formatting.

1. Create [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) objects and add [HtmlFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlfragment/) content.
1. Configure margins for placement.
1. Assign the header and footer to each page and save the document.

```java
public static void addHeaderAndFooterAsHtml(Path inputFile, Path outputFile) {
    HeaderFooter header = new HeaderFooter();
    header.getParagraphs().add(new HtmlFragment("This is an HTML <strong>Header</strong>"));

    HeaderFooter footer = new HeaderFooter();
    footer.getParagraphs().add(new HtmlFragment("Powered by <i>Aspose.PDF</i>"));

    MarginInfo margin = new MarginInfo();
    margin.setLeft(50);
    margin.setTop(20);
    header.setMargin(margin);
    footer.setMargin(margin);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## Add image headers and footers

Use this example when the header and footer should display an image on every page.

1. Create [Image](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) objects and add them to header and footer containers.
1. Configure margins and assign the containers to each page.
1. Save the updated PDF.

```java
public static void addHeaderAndFooterAsImage(Path inputFile, Path imageFile, Path outputFile) {
    Image headerImage = new Image();
    headerImage.setFile(imageFile.toString());
    HeaderFooter header = new HeaderFooter();
    header.getParagraphs().add(headerImage);

    Image footerImage = new Image();
    footerImage.setFile(imageFile.toString());
    HeaderFooter footer = new HeaderFooter();
    footer.getParagraphs().add(footerImage);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            MarginInfo margin = new MarginInfo();
            margin.setLeft(50);
            header.setMargin(margin);
            footer.setMargin(margin);
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## Add table-based headers and footers

Use this example when header and footer content should use table layout and text styling.

1. Create the required text styles and table objects.
1. Add the tables to [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) containers.
1. Apply the header and footer to each page and save the document.

```java
public static void addHeaderAndFooterAsTable(Path inputFile, Path outputFile) {
    TextState textStateHeader = new TextState();
    textStateHeader.setFont(FontRepository.findFont("Arial"));
    textStateHeader.setFontSize(12);
    textStateHeader.setHorizontalAlignment(HorizontalAlignment.Center);

    TextState textStateFooter = new TextState();
    textStateFooter.setFont(FontRepository.findFont("Arial"));
    textStateFooter.setFontSize(12);
    textStateFooter.setHorizontalAlignment(HorizontalAlignment.Left);

    HeaderFooter header = new HeaderFooter();
    HeaderFooter footer = new HeaderFooter();

    Table tableHeader = new Table();
    tableHeader.setColumnWidths(String.valueOf(594 - header.getMargin().getLeft() - header.getMargin().getRight()));
    tableHeader.getRows().add().getCells().add("This is a Table Header", textStateHeader);

    Table table = new Table();
    table.setColumnWidths(String.valueOf(594 - footer.getMargin().getLeft() - footer.getMargin().getRight()));
    table.getRows().add().getCells().add("Powered by Aspose.PDF", textStateFooter);

    header.getParagraphs().add(tableHeader);
    footer.getParagraphs().add(table);
    footer.getMargin().setLeft(150);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## Add LaTeX headers and footers

Use this example when the header and footer should render TeX or LaTeX content.

1. Open the source PDF and determine the total page count.
1. Create [TeXFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/texfragment/) content for the header and footer of each page.
1. Assign the content and save the document.

```java
public static void addHeaderAndFooterAsLatex(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        int pageCount = document.getPages().size();
        for (int i = 1; i <= pageCount; i++) {
            HeaderFooter header = new HeaderFooter();
            header.getParagraphs().add(new TeXFragment("This is a LaTeX Header. \\today\\", true));

            HeaderFooter footer = new HeaderFooter();
            footer.getParagraphs().add(new TeXFragment("\\copyright\\ 2025 My Company -- Page \\thepage\\ is " + pageCount, true));

            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

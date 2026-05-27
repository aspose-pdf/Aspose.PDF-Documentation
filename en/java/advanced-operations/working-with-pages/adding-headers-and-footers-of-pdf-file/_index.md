---
title: Add PDF Headers and Footers in Java
linktitle: Adding Header and Footer to PDF
type: docs
weight: 50
url: /java/add-headers-and-footers-of-pdf-file/
description: Learn how to add headers and footers to PDF files in Java using text, images, and structured content.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add headers and footers to PDF files with Java
Abstract: This article shows how to add headers and footers to PDF documents using Aspose.PDF for Java. It covers text, page numbering, HTML, image, table, and LaTeX-based header and footer content.
---
Aspose.PDF for Java lets you assign `HeaderFooter` objects to each page and populate them with different content types.

## Add text headers and footers

```java
public static void addHeaderAndFooterAsText(Path inputFile, Path outputFile) {
    HeaderFooter header = new HeaderFooter();
    header.getParagraphs().add(new TextFragment("Demo header"));

    HeaderFooter footer = new HeaderFooter();
    footer.getParagraphs().add(new TextFragment("Demo footer"));

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## Use headers and footers for page numbering

`usingHeaderAndFooterForPageNumbering` uses page number placeholders such as `$p` and `$P`.

## Other header and footer content types

The example class also includes:

- `addHeaderAndFooterAsHtml`
- `addHeaderAndFooterAsImage`
- `addHeaderAndFooterAsTable`
- `addHeaderAndFooterAsLatex`

---
title: Manipulate PDF Documents in Java
linktitle: Manipulate PDF Document
type: docs
weight: 20
url: /java/manipulate-pdf-document/
description: Learn how to validate, structure, and modify PDF documents in Java, including TOC management and PDF/A checks.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Validate, restructure, and flatten PDF documents with Java
Abstract: This article explains how to manipulate PDF documents using Aspose.PDF for Java. It covers validating PDF/A compliance, adding and customizing a table of contents, hiding or customizing TOC page numbers, assigning an expiry script, and flattening interactive form fields.
---
Aspose.PDF for Java includes document-structure operations that go beyond simple page editing.

## Validate PDF/A compliance

The example class validates documents against both PDF/A-1a and PDF/A-1b:

```java
public static void validatePdfaStandardA1a(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.validate(outputFile.toString(), PdfFormat.PDF_A_1A);
    }
}
```

## Add a table of contents

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
        document.save(outputFile.toString());
    }
}
```

The related examples also show how to:

- Format multiple TOC levels with different leader styles in `setTocLevels`.
- Hide page numbers with `hidePageNumbersInToc`.
- Add a page-number prefix with `customizePageNumbersInToc`.

## Add an expiry script

`setPdfExpiryDate` attaches a `JavascriptAction` to the document open event so the viewer can warn when the file is considered expired.

## Flatten a fillable PDF

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

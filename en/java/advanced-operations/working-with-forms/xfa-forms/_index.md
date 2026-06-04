---
title: Working with XFA Forms
linktitle: XFA Forms
type: docs
weight: 20
url: /java/xfa-forms/
description: Learn how to convert XFA forms to standard AcroForms in PDF documents using Aspose.PDF for Java.
lastmod: "2026-06-04"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Convert XFA-based PDF forms to standard AcroForms with Java
Abstract: This article explains how to work with XFA-based forms using Aspose.PDF for Java. It covers converting a dynamic XFA form to a standard AcroForm and handling XFA documents that require the ignore-needs-rendering option before conversion.
---
XFA forms can be converted to standard AcroForms so they can be processed with the regular PDF form APIs.

## Convert a dynamic XFA form to an AcroForm

1. Open the source PDF document.
1. Set the properties required by the example.
1. Save the updated PDF document.

```java
public static void convertDynamicXfaToAcroform(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getForm().setType(FormType.Standard);
        document.save(outputFile.toString());
    }
}
```

## Convert an XFA form with `ignoreNeedsRendering`

1. Open the source PDF document.
1. Set the properties required by the example.
1. Save the updated PDF document.

```java
public static void convertXfaFormWithIgnoreNeedsRendering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        if (!document.getForm().getNeedsRendering() && document.getForm().hasXfa()) {
            document.getForm().setIgnoreNeedsRendering(true);
        }
        document.getForm().setType(FormType.Standard);
        document.save(outputFile.toString());
    }
}
```

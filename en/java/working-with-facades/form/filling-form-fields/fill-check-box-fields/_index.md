---
title: Fill Check Box Fields
type: docs
weight: 20
url: /java/fill-check-box-fields/
description: Learn how to fill check box fields in a PDF form with Java using the Form facade in Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Set check box field values in a PDF form with Java
Abstract: This article shows how to bind a PDF form, set check box fields by name, and save the updated document with the Form facade in Aspose.PDF for Java.
---
Use `FormExamples.fillCheckBoxFields(...)` to set check box values in a form.

```java
public static void fillCheckBoxFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("subscribe_newsletter", "Yes");
        form.fillField("accept_terms", "Yes");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

---
title: Flatten All Fields
type: docs
weight: 10
url: /java/flatten-all-fields/
description: Learn how to flatten all PDF form fields in Java using the Form facade in Aspose.PDF.
lastmod: "2026-06-03"
TechArticle: true
AlternativeHeadline: Convert all interactive form fields to static content in Java
Abstract: This article shows how to bind a PDF form, flatten every form field, and save the updated document with the Form facade in Aspose.PDF for Java.
---
Use `FormExamples.flattenAllFields(...)` when you need to convert all interactive fields into static page content.

```java
public static void flattenAllFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.flattenAllFields();
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

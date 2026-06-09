---
title: Rename Form Fields
type: docs
weight: 30
url: /java/rename-form-fields/
description: Learn how to rename PDF form fields in Java using the Form facade in Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Rename form fields in a PDF document with Java
Abstract: This article shows how to bind a PDF form, rename existing fields, and save the updated document with the Form facade in Aspose.PDF for Java.
---
Use `FormExamples.renameFormFields(...)` to rename fields in an interactive PDF form.

```java
public static void renameFormFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.renameField("First Name", "NewFirstName");
        form.renameField("Last Name", "NewLastName");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

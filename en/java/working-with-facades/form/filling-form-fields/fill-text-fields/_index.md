---
title: Fill Text Fields
linktitle: Fill Text Fields
type: docs
weight: 10
url: /java/fill-text-fields/
description: Learn how to fill text fields in a PDF form with Java using the Form facade in Aspose.PDF.
lastmod: "2026-05-28"
TechArticle: true
AlternativeHeadline: Populate text form fields in a PDF with Java
Abstract: This article shows how to bind a PDF form, set text field values by name, and save the updated document with the Form facade in Aspose.PDF for Java.
---
Use `FormExamples.fillTextFields(...)` to populate text-based form fields.

```java
public static void fillTextFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("name", "John Doe");
        form.fillField("address", "123 Main St, Anytown, USA");
        form.fillField("email", "john.doe@example.com");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

---
title: Get Field Values
linktitle: Get Field Values
type: docs
weight: 50
url: /java/get-field-values/
description: Learn how to read PDF form field names and values in Java using the Form facade in Aspose.PDF.
lastmod: "2026-05-28"
TechArticle: true
AlternativeHeadline: Read field values from a PDF form in Java
Abstract: This article shows how to bind a PDF form, enumerate field names, and print each field value with the Form facade in Aspose.PDF for Java.
---
Use `FormExamples.inspectFormFields(...)` to inspect field names and their current values.

```java
public static void inspectFormFields(Path inputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        System.out.println("Field names: " + Arrays.toString(form.getFieldNames()));
        for (String fieldName : form.getFieldNames()) {
            System.out.println(fieldName + " = " + form.getField(fieldName));
        }
    } finally {
        form.close();
    }
}
```

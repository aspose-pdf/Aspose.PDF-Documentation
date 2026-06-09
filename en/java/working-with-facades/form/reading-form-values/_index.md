---
title: Reading Form Values
type: docs
weight: 60
url: /java/reading-form-values/
description: Learn how to inspect PDF form field names and values in Java using the Form facade in Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Read PDF form field names and values in Java
Abstract: This section covers the Java form-reading workflows implemented in the current Form facade example set for Aspose.PDF for Java. The repository provides a general field inspection example and uses explicit scope notes for specialized pages that do not yet have matching Java samples.
---
The Java `FormExamples` class demonstrates the main form-processing workflows exposed by the Facades API.

## Get Field Values

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

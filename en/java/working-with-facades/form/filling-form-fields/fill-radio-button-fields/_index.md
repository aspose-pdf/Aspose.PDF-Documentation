---
title: Fill Radio Button Fields
type: docs
weight: 30
url: /java/fill-radio-button-fields/
description: Learn how to select a radio button value in a PDF form with Java using the Form facade in Aspose.PDF.
lastmod: "2026-06-03"
TechArticle: true
AlternativeHeadline: Select a radio button field option in Java
Abstract: This article shows how to bind a PDF form, select a radio button option by index, and save the updated document with the Form facade in Aspose.PDF for Java.
---
Use `FormExamples.fillRadioButtonFields(...)` to select a radio button option.

```java
public static void fillRadioButtonFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("gender", 0);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

---
title: Fill Barcode Fields
type: docs
weight: 50
url: /java/fill-barcode-fields/
description: Learn how to fill a barcode form field in Java using the Form facade in Aspose.PDF.
lastmod: "2026-06-03"
TechArticle: true
AlternativeHeadline: Populate a barcode field in a PDF form with Java
Abstract: This article shows how to bind a PDF form, set a barcode field value, and save the updated document with the Form facade in Aspose.PDF for Java.
---
Use `FormExamples.fillBarcodeFields(...)` to populate a barcode field in a PDF form.

```java
public static void fillBarcodeFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillBarcodeField("product_barcode", "123456789012");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

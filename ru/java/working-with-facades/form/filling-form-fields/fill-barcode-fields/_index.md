---
title: Заполните поля штрих-кода
linktitle: Заполните поля штрих-кода
type: docs
weight: 50
url: /java/fill-barcode-fields/
description: Узнайте, как заполнить поле формы штрих-кода в Java, используя фасад формы в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Заполнение поля штрих-кода в форме PDF с помощью Java
Abstract: This article shows how to bind a PDF form, set a barcode field value, and save the updated document with the Form facade in Aspose.PDF for Java.
---
Используйте `FormExamples.fillBarcodeFields(...)`, чтобы заполнить поле штрих-кода в форме PDF.

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

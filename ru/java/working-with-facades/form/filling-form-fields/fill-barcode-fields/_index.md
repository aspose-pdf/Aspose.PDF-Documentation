---
title: Заполнить поля штрих‑кода
linktitle: Заполнить поля штрих‑кода
type: docs
weight: 50
url: /ru/java/fill-barcode-fields/
description: Узнайте, как заполнить поле формы штрих‑кода на Java, используя фасад Form в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Заполните поле штрих‑кода в PDF‑форме с помощью Java
Abstract: В этой статье показано, как привязать PDF‑форму, установить значение поля штрих‑кода и сохранить обновлённый документ с использованием фасада Form в Aspose.PDF for Java.
---
Использовать `FormExamples.fillBarcodeFields(...)` заполнить поле штрих‑кода в форме PDF.

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



---
title: Заполнить текстовые поля
linktitle: Заполнить текстовые поля
type: docs
weight: 10
url: /ru/java/fill-text-fields/
description: Узнайте, как заполнять текстовые поля в PDF-форме с помощью Java, используя фасад Form в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Заполните текстовые поля формы в PDF с помощью Java
Abstract: В этой статье показано, как привязать PDF-форму, установить значения текстовых полей по имени и сохранить обновленный документ, используя фасад Form в Aspose.PDF for Java.
---
Использовать `FormExamples.fillTextFields(...)` для заполнения текстовых полей формы.

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



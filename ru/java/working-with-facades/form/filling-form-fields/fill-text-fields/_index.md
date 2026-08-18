---
title: Заполните текстовые поля
linktitle: Заполните текстовые поля
type: docs
weight: 10
url: /java/fill-text-fields/
description: Узнайте, как заполнять текстовые поля в форме PDF с помощью Java, используя фасад формы в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Заполнение полей текстовой формы в PDF-файле с помощью Java
Abstract: В этой статье показано, как привязать форму PDF, установить значения текстового поля по имени и сохранить обновленный документ с фасадом формы в Aspose.PDF для Java.
---
Используйте `FormExamples.fillTextFields(...)` для заполнения текстовых полей формы.

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

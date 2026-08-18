---
title: Создать кнопку отправки
linktitle: Создать кнопку отправки
type: docs
weight: 60
url: /java/create-submit-button/
description: Узнайте, как добавить кнопку отправки в PDF-документ на Java с помощью фасада FormEditor в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Создайте кнопку отправки PDF в Java
Abstract: В этой статье показано, как связать существующий PDF-файл, добавить поле кнопки отправки с целевым URL-адресом и сохранить измененный документ с помощью фасада FormEditor в Aspose.PDF для Java.
---
Используйте `FormEditorExamples.createSubmitButton(...)`, чтобы создать кнопку, которая отправляет данные формы.

## Создайте кнопку отправки

1. Привяжите исходный PDF-файл к фасаду `FormEditor`.
2. Вызовите `addSubmitBtn(...)`, указав имя кнопки, страницу, метку, целевой URL-адрес и прямоугольник.
3. Сохраните обновленный документ.

```java
public static void createSubmitButton(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addSubmitBtn("submitbutton", 1, "Submit", "http://localhost/testing/show", 100, 450, 150, 475);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```

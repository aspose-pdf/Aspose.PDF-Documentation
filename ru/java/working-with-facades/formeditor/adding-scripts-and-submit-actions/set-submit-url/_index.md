---
title: Установить URL-адрес отправки
linktitle: Установить URL-адрес отправки
type: docs
weight: 30
url: /java/set-submit-url/
description: Узнайте, как установить URL-адрес отправки для кнопки формы PDF в Java с помощью фасада FormEditor в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Настройка URL-адреса отправки формы PDF в Java
Abstract: В этой статье показано, как связать существующий PDF-файл, установить URL-адрес отправки и флаг отправки для поля кнопки, а также сохранить обновленный документ с помощью фасада FormEditor в Aspose.PDF для Java.
---
## Установите URL-адрес отправки

1. Привяжите исходный PDF-файл к фасаду `FormEditor`.
2. Позвоните `setSubmitUrl(...)` для поля кнопки.
3. Примените флаг отправки для формата отправки.
4. Сохраните обновленный документ.

```java
public static void setSubmitUrl(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setSubmitUrl("Script_Demo_Button", "http://www.example.com/submit");
        editor.setSubmitFlag("Script_Demo_Button", SubmitFormFlag.Xfdf);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```

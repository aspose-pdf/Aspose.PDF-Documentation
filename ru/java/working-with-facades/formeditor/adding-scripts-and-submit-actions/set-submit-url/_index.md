---
title: Установить URL-адрес отправки
linktitle: Установить URL-адрес отправки
type: docs
weight: 30
url: /ru/java/set-submit-url/
description: Узнайте, как задать URL отправки для кнопки формы PDF в Java, используя фасад FormEditor в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Настройте URL отправки формы PDF в Java
Abstract: В этой статье показано, как привязать существующий PDF, задать URL отправки и флаг отправки для поля кнопки, а также сохранить обновлённый документ, используя фасад FormEditor в Aspose.PDF for Java.
---
## Задать URL отправки

1. Привяжите исходный PDF к `FormEditor` фасад.
2. Вызов `setSubmitUrl(...)` для поля кнопки.
3. Примените флаг отправки для формата отправки.
4. Сохраните обновлённый документ.

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


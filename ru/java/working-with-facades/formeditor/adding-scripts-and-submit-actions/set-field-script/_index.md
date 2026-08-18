---
title: Установить сценарий поля
linktitle: Установить сценарий поля
type: docs
weight: 20
url: /java/set-field-script/
description: Узнайте, как назначить или обновить действие JavaScript в поле формы PDF в Java с помощью фасада FormEditor в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Установите действие JavaScript в поле формы PDF в Java
Abstract: В этой статье показано, как связать существующий PDF-файл, добавить исходный сценарий, заменить его обновленным сценарием и сохранить измененный документ с помощью фасада FormEditor в Aspose.PDF для Java.
---
## Установите сценарий поля

1. Привяжите исходный PDF-файл к фасаду `FormEditor`.
2. Добавьте в поле начальное действие JavaScript.
3. Замените его обновленным текстом сценария.
4. Сохраните обновленный документ.

```java
public static void setFieldScript(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addFieldScript("Script_Demo_Button", "app.alert('Script 1 has been executed');");
        editor.setFieldScript("Script_Demo_Button", "app.alert('Script 2 has been executed');");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```

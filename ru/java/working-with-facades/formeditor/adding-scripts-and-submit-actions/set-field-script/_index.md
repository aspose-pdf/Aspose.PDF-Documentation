---
title: Установить скрипт поля
linktitle: Установить скрипт поля
type: docs
weight: 20
url: /ru/java/set-field-script/
description: Узнайте, как назначать или обновлять действие JavaScript для поля формы PDF на Java, используя фасад FormEditor в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Установить действие JavaScript для поля формы PDF на Java
Abstract: В этой статье показано, как привязать существующий PDF, добавить начальный скрипт, заменить его обновлённым скриптом и сохранить изменённый документ, используя фасад FormEditor в Aspose.PDF for Java.
---
## Установите скрипт поля

1. Привяжите исходный PDF к `FormEditor` фасад.
2. Добавьте начальное действие JavaScript к полю.
3. Замените его обновлённым текстом скрипта.
4. Сохраните обновлённый документ.

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



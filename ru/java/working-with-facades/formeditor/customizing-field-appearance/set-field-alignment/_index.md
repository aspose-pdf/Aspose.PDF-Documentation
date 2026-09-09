---
title: Установить выравнивание поля
linktitle: Установить выравнивание поля
type: docs
weight: 20
url: /ru/java/set-field-alignment/
description: Узнайте, как установить горизонтальное выравнивание текста для поля формы PDF в Java, используя фасад FormEditor в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Установить выравнивание поля формы PDF в Java
Abstract: В этой статье показано, как привязать существующий PDF, установить горизонтальное выравнивание поля и сохранить обновленный документ, используя фасад FormEditor в Aspose.PDF для Java.
---
## Установите горизонтальное выравнивание поля

1. Привяжите исходный PDF к `FormEditor` фасад.
2. Вызовите `setFieldAlignment(...)` для целевого поля и желаемой константы выравнивания.
3. Сохраните обновлённый документ.

```java
public static void setFieldAlignment(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldAlignment("First Name", FormFieldFacade.ALIGN_CENTER);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```



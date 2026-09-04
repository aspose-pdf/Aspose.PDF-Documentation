---
title: Установить внешний вид поля
linktitle: Установить внешний вид поля
type: docs
weight: 40
url: /ru/java/set-field-appearance/
description: Узнайте, как изменить флаги визуального отображения поля формы PDF в Java с использованием фасада FormEditor в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Изменить флаги отображения поля формы PDF в Java
Abstract: В этой статье показано, как привязать существующий PDF, применить флаг отображения к полю и сохранить обновлённый документ, используя фасад FormEditor в Aspose.PDF for Java.
---
## Установите флаги отображения поля

1. Привяжите исходный PDF к `FormEditor` фасад.
2. Вызовите `setFieldAppearance(...)` для целевого поля и выбранного флага аннотации.
3. Сохраните обновлённый документ.

```java
public static void setFieldAppearance(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldAppearance("First Name", AnnotationFlags.Hidden);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```



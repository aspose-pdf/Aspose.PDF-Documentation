---
title: Установка ограничения поля
linktitle: Установка ограничения поля
type: docs
weight: 50
url: /ru/java/set-field-limit/
description: Узнайте, как установить максимальное ограничение количества символов для поля PDF‑формы в Java, используя фасад FormEditor в Aspose.PDF.
lastmod: "2026-09-17"
TechArticle: true
AlternativeHeadline: Установить ограничение количества символов для поля PDF‑формы в Java
Abstract: В этой статье показано, как привязать существующий PDF, установить максимальное ограничение количества символов поля и сохранить обновлённый документ, используя фасад FormEditor в Aspose.PDF for Java.
---
## Установка ограничения количества символов поля

1. Привяжите исходный PDF к фасаду `FormEditor`.
2. Вызовите `setFieldLimit(...)` для целевого поля и максимального количества символов.
3. Сохраните обновлённый документ.

```java
public static void setFieldLimit(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldLimit("First Name", 15);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```



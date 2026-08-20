---
title: Однострочный в многосрочный
linktitle: Однострочный в многосрочный
type: docs
weight: 60
url: /ru/java/single-to-multiple/
description: Узнайте, как преобразовать однострочное текстовое поле в многострочное поле в PDF‑документе на Java с использованием фасада FormEditor в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Преобразовать однострочное поле PDF в многострочное на Java
Abstract: В этой статье показано, как привязать существующий PDF, преобразовать однострочное поле в многострочное и сохранить обновлённый документ с использованием фасада FormEditor в Aspose.PDF for Java.
---
## Преобразуйте однострочное поле в несколько строк

1. Привяжите исходный PDF к `FormEditor` фасад.
2. Вызовите `single2Multiple(...)` для имени целевого поля.
3. Сохраните обновлённый документ.

```java
public static void singleToMultiple(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.single2Multiple("City");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```



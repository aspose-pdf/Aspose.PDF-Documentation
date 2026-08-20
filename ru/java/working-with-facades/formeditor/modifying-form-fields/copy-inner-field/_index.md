---
title: Копировать внутреннее поле
linktitle: Копировать внутреннее поле
type: docs
weight: 70
url: /ru/java/copy-inner-field/
description: Узнайте, как скопировать поле формы в новое положение внутри того же PDF‑документа на Java, используя фасад FormEditor в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Скопировать поле формы PDF внутри того же документа на Java
Abstract: В этой статье показано, как привязать существующий PDF, дублировать поле на другую страницу и позицию, и сохранить обновлённый документ, используя фасад FormEditor в Aspose.PDF for Java.
---
## Скопировать поле внутри того же PDF

1. Привяжите исходный PDF к `FormEditor` фасад.
2. Вызовите `copyInnerField(...)` с именем исходного поля, новым именем поля, страницей и координатами.
3. Сохраните обновлённый документ.

```java
public static void copyInnerField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.copyInnerField("First Name", "First Name Copy", 2, 200, 600);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```



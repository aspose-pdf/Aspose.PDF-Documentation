---
title: Копировать внешнее поле
linktitle: Копировать внешнее поле
type: docs
weight: 80
url: /ru/java/copy-outer-field/
description: Узнайте, как копировать поле формы из одного PDF‑документа в другой на Java с использованием фасада FormEditor в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Копировать поле формы PDF между документами на Java
Abstract: В этой статье показано, как создать целевой PDF, привязать его к фасаду FormEditor, скопировать поле из другого документа и сохранить результат, используя Aspose.PDF for Java.
---
## Скопировать поле из другого PDF

1. Создайте целевой PDF как минимум с одной страницей.
2. Привяжите целевой PDF к `FormEditor` фасад.
3. Вызовите `copyOuterField(...)` с путем к исходному документу, именем поля, целевой страницей и координатами.
4. Сохраните обновлённый целевой документ.

```java
public static void copyOuterField(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        document.getPages().add();
        document.save(outputFile.toString());
    }

    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(outputFile.toString());
        editor.copyOuterField(inputFile.toString(), "First Name", 1, 200, 600);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```



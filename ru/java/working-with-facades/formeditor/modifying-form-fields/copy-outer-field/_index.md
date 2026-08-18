---
title: Копировать внешнее поле
linktitle: Копировать внешнее поле
type: docs
weight: 80
url: /java/copy-outer-field/
description: Узнайте, как скопировать поле формы из одного PDF-документа в другой на Java с помощью фасада FormEditor в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Скопируйте поле формы PDF между документами в Java
Abstract: В этой статье показано, как создать целевой PDF-файл, привязать его к фасаду FormEditor, скопировать поле из другого документа и сохранить результат с помощью Aspose.PDF для Java.
---
## Копирование поля из другого PDF-файла

1. Создайте целевой PDF-файл хотя бы с одной страницей.
2. Привяжите целевой PDF-файл к фасаду `FormEditor`.
3. Вызовите `copyOuterField(...)`, указав путь к исходному документу, имя поля, целевую страницу и координаты.
4. Сохраните обновленный целевой документ.

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

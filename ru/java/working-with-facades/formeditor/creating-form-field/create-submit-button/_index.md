---
title: Создать кнопку отправки
linktitle: Создать кнопку отправки
type: docs
weight: 60
url: /ru/java/create-submit-button/
description: Узнайте, как добавить кнопку отправки в PDF-документ на Java с помощью фасада FormEditor в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Создать кнопку отправки PDF на Java
Abstract: В этой статье показано, как привязать существующий PDF, добавить поле кнопки отправки с целевым URL и сохранить изменённый документ, используя фасад FormEditor в Aspose.PDF for Java.
---
Использовать `FormEditorExamples.createSubmitButton(...)` создать кнопку, которая отправляет данные формы.

## Создайте кнопку отправки

1. Привяжите исходный PDF к `FormEditor` фасад.
2. Вызов `addSubmitBtn(...)` с именем кнопки, страницей, ярлыком, целевым URL и прямоугольником.
3. Сохраните обновлённый документ.

```java
public static void createSubmitButton(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addSubmitBtn("submitbutton", 1, "Submit", "http://localhost/testing/show", 100, 450, 150, 475);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```


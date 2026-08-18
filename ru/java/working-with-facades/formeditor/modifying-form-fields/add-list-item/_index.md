---
title: Добавить элемент списка
linktitle: Добавить элемент списка
type: docs
weight: 10
url: /java/add-list-item/
description: Узнайте, как добавлять элементы в поле списка в PDF-документе на Java с помощью фасада FormEditor в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Добавьте элемент списка в поле формы PDF в Java
Abstract: В этой статье показано, как связать существующий PDF-файл, добавить новый элемент в поле списка и сохранить обновленный документ с помощью фасада FormEditor в Aspose.PDF для Java.
---
## Добавьте элемент в поле списка

1. Привяжите исходный PDF-файл к фасаду `FormEditor`.
2. Вызовите `addListItem(...)` для целевого поля и новой пары отображение/значение.
3. Сохраните обновленный документ.

```java
public static void addListItem(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addListItem("Country", new String[] {"New Zealand", "New Zealand"});
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```

---
title: Удалить элемент списка
linktitle: Удалить элемент списка
type: docs
weight: 20
url: /java/del-list-item/
description: Узнайте, как удалить элемент из поля списка в PDF-документе на Java с помощью фасада FormEditor в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Удаление элемента списка из поля формы PDF в Java
Abstract: В этой статье показано, как связать существующий PDF-файл, удалить определенный элемент из поля списка и сохранить обновленный документ с помощью фасада FormEditor в Aspose.PDF для Java.
---
## Удаление элемента из поля списка

1. Привяжите исходный PDF-файл к фасаду `FormEditor`.
2. Вызовите `delListItem(...)`, чтобы узнать целевое поле и элемент, который нужно удалить.
3. Сохраните обновленный документ.

```java
public static void deleteListItem(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.delListItem("Country", "UK");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```

---
title: Удалить элемент списка
linktitle: Удалить элемент списка
type: docs
weight: 20
url: /ru/java/del-list-item/
description: Узнайте, как удалить элемент из поля списка в PDF-документе на Java, используя фасад FormEditor в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Удалить элемент списка из поля формы PDF на Java
Abstract: В этой статье показано, как привязать существующий PDF, удалить конкретный элемент из поля списка и сохранить обновлённый документ, используя фасад FormEditor в Aspose.PDF for Java.
---
## Удалите элемент из поля списка

1. Привяжите исходный PDF к `FormEditor` фасад.
2. Вызов `delListItem(...)` для целевого поля и элемента, который нужно удалить.
3. Сохраните обновлённый документ.

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


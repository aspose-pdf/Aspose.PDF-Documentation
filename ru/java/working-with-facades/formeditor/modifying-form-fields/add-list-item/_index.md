---
title: Добавить элемент списка
linktitle: Добавить элемент списка
type: docs
weight: 10
url: /ru/java/add-list-item/
description: Узнайте, как добавить элементы в поле списка в PDF‑документе на Java, используя фасад FormEditor в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Добавьте элемент списка в PDF‑поле формы на Java
Abstract: В этой статье показано, как привязать существующий PDF, добавить новый элемент в поле списка и сохранить обновлённый документ, используя фасад FormEditor в Aspose.PDF for Java.
---
## Добавьте элемент в поле списка

1. Привяжите исходный PDF к `FormEditor` фасад.
2. Вызов `addListItem(...)` для целевого поля и новой пары отображения/значения.
3. Сохраните обновлённый документ.

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


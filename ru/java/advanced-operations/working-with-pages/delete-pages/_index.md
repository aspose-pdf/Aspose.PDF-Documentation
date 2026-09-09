---
title: Удалить страницы PDF в Java
linktitle: Удаление страниц PDF
type: docs
weight: 80
url: /ru/java/delete-pages/
description: Узнайте, как удалять страницы из PDF‑файлов в Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удалить одну или несколько страниц PDF в Java
Abstract: В этой статье объясняется, как удалить страницы из PDF‑файлов с помощью Aspose.PDF for Java. Описывается удаление отдельной страницы и удаление нескольких страниц одновременно через API коллекции страниц.
---
Используйте коллекцию страниц документа, когда необходимо удалить одну или несколько страниц из PDF.

## Удалите одну страницу

Используйте этот пример, когда нужно удалить одну страницу по её индексу.

1. Откройте исходный PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Удалите целевую страницу из коллекции страниц.
1. Сохраните обновлённый документ.

```java
public static void deletePage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().delete(2);
        document.save(outputFile.toString());
    }
}
```

## Удалите несколько страниц

Используйте этот пример, когда несколько страниц должны быть удалены за одну операцию.

1. Откройте исходный PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Передайте индексы страниц, которые нужно удалить из коллекции страниц.
1. Сохраните изменённый PDF.

```java
public static void deleteBunchPages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().delete(new Integer[]{2, 3, 4});
        document.save(outputFile.toString());
    }
}
```



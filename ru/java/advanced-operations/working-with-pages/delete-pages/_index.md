---
title: Удалить PDF-страницы в Java
linktitle: Удаление страниц PDF
type: docs
weight: 80
url: /java/delete-pages/
description: Узнайте, как удалять страницы из файлов PDF в Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удалить одну или несколько страниц PDF в Java
Abstract: В этой статье объясняется, как удалить страницы из файлов PDF с помощью Aspose.PDF для Java. Он охватывает удаление одной страницы и одновременное удаление нескольких страниц через API коллекции страниц.
---
Используйте коллекцию страниц документа, когда вам нужно удалить одну или несколько страниц из PDF-файла.

## Удалите одну страницу

Используйте этот пример, когда вам нужно удалить одну страницу по ее индексу.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Удалите целевую страницу из коллекции страниц.
1. Сохраните обновленный документ.

```java
public static void deletePage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().delete(2);
        document.save(outputFile.toString());
    }
}
```

## Удалите несколько страниц

Используйте этот пример, когда необходимо удалить несколько страниц за одну операцию.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Передайте индексы страниц, которые необходимо удалить из коллекции страниц.
1. Сохраните измененный PDF-файл.

```java
public static void deleteBunchPages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().delete(new Integer[]{2, 3, 4});
        document.save(outputFile.toString());
    }
}
```

---
title: Удаление нумерации Бейтса из PDF на Java
linktitle: Удаление нумерации Бейтса
type: docs
weight: 100
url: /ru/java/remove-bates-numbering/
description: Удалить нумерацию Бейтса со всех страниц PDF в Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удаление нумерации Бейтса из PDF на Java
Abstract: Удалить нумерацию Бейтса со всех страниц PDF в Java.
---
Удалить нумерацию Бейтса со всех страниц PDF в Java.

## Удаление нумерации Бейтса

Используйте этот подход, когда необходимо удалить существующие артефакты нумерации Бейтса из документа.

1. Откройте исходный PDF в объекте [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Вызовите вспомогательный метод коллекции страниц, который удаляет нумерацию Бейтса.
1. Сохраните очищенный выходной файл.

```java
public static void deleteBatesNumbering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageCollectionExtensions.deleteBatesNumbering(document.getPages());
        document.save(outputFile.toString());
    }
}
```

## См. также

- [Добавление нумерации Бейтса](/pdf/ru/java/add-bates-numbering/)
- [Работа с PDF-артефактами](/pdf/ru/java/artifacts/)

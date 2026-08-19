---
title: Удалить таблицы из существующих PDF‑документов
linktitle: Удалить таблицы
description: Узнайте, как удалить одну или несколько таблиц из существующих PDF‑документов на Java.
lastmod: "2026-08-19"
type: docs
weight: 50
url: /ru/java/removing-tables/
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удалить одну или несколько таблиц из PDF‑файлов с помощью Java
Abstract: Эта статья объясняет, как удалять таблицы из существующих PDF‑документов с использованием Aspose.PDF for Java. В ней представляется TableAbsorber для обнаружения таблиц и демонстрируется, как удалить одну таблицу или удалить все найденные таблицы со страницы.
---
Использовать `TableAbsorber` когда нужно удалить одну или несколько обнаруженных таблиц из существующего PDF.

## Удалите одну обнаруженную таблицу

Используйте этот пример, когда должна быть удалена только первая найденная таблица на странице.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Перейдите на целевую страницу с [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/).
1. Удалите первую обнаруженную таблицу и сохраните документ.

```java
public static void removeOneTable(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));
        absorber.remove(absorber.getTableList().get(0));
        document.save(outputFile.toString());
    }
}
```

## Удалите все обнаруженные таблицы со страницы

Используйте этот пример, когда каждую найденную таблицу на странице следует удалить.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Перейдите на целевую страницу с [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) и скопировать обнаруженные таблицы в список.
1. Удалите каждую обнаруженную таблицу и сохранить обновлённый PDF.

```java
public static void removeAllTables(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));
        List<AbsorbedTable> tables = new ArrayList<>(absorber.getTableList());
        for (AbsorbedTable table : tables) {
            absorber.remove(table);
        }
        document.save(outputFile.toString());
    }
}
```


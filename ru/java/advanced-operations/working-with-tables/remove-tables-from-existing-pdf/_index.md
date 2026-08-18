---
title: Удаление таблиц из существующих PDF-документов
linktitle: Удалить таблицы
description: Узнайте, как удалить одну или несколько таблиц из существующих PDF-документов в Java.
lastmod: "2026-06-09"
type: docs
weight: 50
url: /java/removing-tables/
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удалить одну или несколько таблиц из файлов PDF с помощью Java
Abstract: В этой статье объясняется, как удалить таблицы из существующих PDF-документов с помощью Aspose.PDF для Java. В нем представлен TableAbsorber для поиска таблиц и показано, как удалить одну таблицу или удалить все обнаруженные таблицы со страницы.
---
Используйте `TableAbsorber`, когда вам нужно удалить одну или несколько обнаруженных таблиц из существующего PDF-файла.

## Удалите одну обнаруженную таблицу

Используйте этот пример, когда необходимо удалить только первую совпавшую таблицу на странице.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Посетите целевую страницу с помощью [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/).
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

Используйте этот пример, когда необходимо удалить каждую совпадающую таблицу на странице.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Посетите целевую страницу с помощью [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) и скопируйте обнаруженные таблицы в список.
1. Удалите каждую обнаруженную таблицу и сохраните обновленный PDF-файл.

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

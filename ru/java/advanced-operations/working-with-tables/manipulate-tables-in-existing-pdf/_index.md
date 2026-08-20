---
title: Манипулирование таблицами в существующих PDF-документах
linktitle: Манипулирование таблицами
type: docs
weight: 40
url: /ru/java/manipulating-tables/
description: Узнайте, как проверять и изменять таблицы в существующих PDF-документах с помощью Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Проверка и изменение существующих PDF-таблиц с Java
Abstract: В этой статье объясняется, как манипулировать таблицами, уже присутствующими в PDF-документах, используя Aspose.PDF for Java. Описывается поиск таблиц с помощью TableAbsorber, обновление текста внутри ячейки и замена обнаруженной таблицы новым объектом Table.
---
Использовать `TableAbsorber` когда вам нужно найти существующие таблицы и обновить их содержание.

## Заменить текст внутри ячейки таблицы

Используйте этот пример, когда текст в обнаруженной ячейке должен быть обновлён без перестройки всей таблицы.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и перейдите к странице с [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/).
1. Проверьте, что целевая таблица и фрагменты текста ячеек существуют.
1. Замените текст в ячейке и сохраните обновлённый документ.

```java
public static void replaceCells(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        if (absorber.getTableList().isEmpty()) {
            throw new IllegalStateException("No tables were found on page 1.");
        }
        if (absorber.getTableList().get(0).getRowList().get(0).getCellList().get(0).getTextFragments().size() == 0) {
            throw new IllegalStateException("The target cell has no text fragments.");
        }

        absorber.getTableList().get(0).getRowList().get(0).getCellList().get(0)
                .getTextFragments().get_Item(1).setText("New Value");
        document.save(outputFile.toString());
    }
}
```

## Заменить обнаруженную таблицу новой таблицей

Используйте этот пример, когда оригинальную таблицу следует полностью заменить вновь созданной.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и обнаруживать таблицы на странице.
1. Создайте новый [Таблица](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) с желаемой структурой.
1. Замените поглощённую таблицу и сохраните полученный PDF.

```java
public static void replaceTable(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        if (absorber.getTableList().isEmpty()) {
            throw new IllegalStateException("No tables were found on page 1.");
        }

        AbsorbedTable oldTable = absorber.getTableList().get(0);
        Table newTable = new Table();
        newTable.setColumnWidths("100 100 100");
        newTable.setDefaultCellBorder(new BorderInfo(BorderSide.All, 1.0f));

        Row row = newTable.getRows().add();
        row.getCells().add("Col 1");
        row.getCells().add("Col 2");
        row.getCells().add("Col 3");
        row = newTable.getRows().add();
        row.getCells().add("Col 12");
        row.getCells().add("Col 22");
        row.getCells().add("Col 32");

        absorber.replace(document.getPages().get_Item(1), oldTable, newTable);
        document.save(outputFile.toString());
    }
}
```



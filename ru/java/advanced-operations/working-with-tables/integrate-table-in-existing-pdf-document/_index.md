---
title: Интеграция таблиц PDF с источниками данных на Java
linktitle: Интегрировать таблицу
type: docs
weight: 30
url: /ru/java/integrate-table/
description: Узнайте, как интегрировать таблицы PDF со структурированными источниками данных, такими как CSV‑файлы, на Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Создавайте таблицы PDF из структурированных данных с помощью Java
Abstract: В этой статье объясняется, как интегрировать таблицы PDF с внешними данными, используя Aspose.PDF for Java. Описывается чтение CSV‑данных, выбор конкретных столбцов, построение стилизованного объекта Table из разобранных строк и вывод результата в документ PDF.
---
Пример на Java создает таблицы PDF из CSV‑данных без использования внешних библиотек dataframe.

## Создайте таблицу из строк CSV

Используйте этот пример, когда выбранные столбцы CSV необходимо преобразовать в стилизованную таблицу PDF.

1. Создайте [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) и настроить её границы.
1. Определите необходимые индексы столбцов из строки заголовка CSV.
1. Добавьте строку заголовка и запрошенное количество строк данных, затем верните таблицу.

```java
public static Table createTableFromCsv(List<String[]> rows, int maxRows) {
    Table table = new Table();
    table.setBorder(new BorderInfo(BorderSide.All, 1, Color.getLightGray()));
    table.setDefaultCellBorder(new BorderInfo(BorderSide.Bottom, 1, Color.getLightGray()));

    String[] header = rows.get(0);
    int[] selectedColumns = findColumns(header, "city", "country", "population", "iso3");

    Row headerRow = table.getRows().add();
    headerRow.setRowBroken(false);
    for (int columnIndex : selectedColumns) {
        Cell cell = headerRow.getCells().add(header[columnIndex]);
        cell.setBackgroundColor(Color.getLightGray());
    }

    int limit = Math.min(maxRows, rows.size() - 1);
    for (int rowIndex = 1; rowIndex <= limit; rowIndex++) {
        Row row = table.getRows().add();
        String[] rowData = rows.get(rowIndex);
        for (int columnIndex : selectedColumns) {
            row.getCells().add(columnIndex < rowData.length ? rowData[columnIndex] : "");
        }
    }

    return table;
}
```

## Создайте PDF из данных CSV

Используйте этот пример, когда CSV‑ввод должен быть отрендерен как таблица PDF‑документа.

1. Прочитайте строки CSV из входного файла.
1. Предпросмотрите подмножество разобранных строк в консоли.
1. Создайте PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/), добавьте сгенерированную таблицу, и сохраните выходной файл.

```java
public static void createPdfFromCsv(Path inputFile, Path outputFile, int maxRows) throws Exception {
    List<String[]> rows = readCsv(inputFile);
    for (int i = 0; i < Math.min(20, rows.size()); i++) {
        System.out.println(String.join(" | ", rows.get(i)));
    }

    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(createTableFromCsv(rows, maxRows));
        document.save(outputFile.toString());
    }
}
```

## Найдите индексы столбцов CSV по имени

Используйте этот помощник, когда необходимо найти определённые именованные столбцы в строке заголовка CSV.

1. Итерируйтесь по запрошенным именам столбцов.
1. Ищите в строке заголовка соответствующие индексы.
1. Верните собранные позиции столбцов.

```java
private static int[] findColumns(String[] header, String... names) {
    int[] indexes = new int[names.length];
    for (int i = 0; i < names.length; i++) {
        indexes[i] = 0;
        for (int j = 0; j < header.length; j++) {
            if (names[i].equals(header[j])) {
                indexes[i] = j;
                break;
            }
        }
    }
    return indexes;
}
```

## Читайте строки CSV из файла

Используйте этот вспомогательный элемент, когда источник CSV должен быть загружен в память перед генерацией таблицы.

1. Читайте все строки из входного файла.
1. Разделите каждую строку с помощью вспомогательного средства CSV‑парсера.
1. Верните собранные значения строк.

```java
private static List<String[]> readCsv(Path inputFile) throws Exception {
    List<String[]> rows = new ArrayList<>();
    for (String line : Files.readAllLines(inputFile)) {
        rows.add(splitCsvLine(line));
    }
    return rows;
}
```

## Разбейте одну строку CSV на значения

Используйте этот вспомогательный метод, когда строка CSV может содержать заключённые в кавычки значения и экранированные символы кавычек.

1. Итерируйте по символам в строке.
1. Отслеживайте, находится ли парсер в данный момент внутри текста в кавычках.
1. Сформируйте окончательный список значений и верните его в виде массива.

```java
private static String[] splitCsvLine(String line) {
    List<String> values = new ArrayList<>();
    StringBuilder current = new StringBuilder();
    boolean inQuotes = false;
    for (int i = 0; i < line.length(); i++) {
        char ch = line.charAt(i);
        if (ch == '"') {
            if (inQuotes && i + 1 < line.length() && line.charAt(i + 1) == '"') {
                current.append('"');
                i++;
            } else {
                inQuotes = !inQuotes;
            }
        } else if (ch == ',' && !inQuotes) {
            values.add(current.toString());
            current.setLength(0);
        } else {
            current.append(ch);
        }
    }
    values.add(current.toString());
    return values.toArray(String[]::new);
}
```



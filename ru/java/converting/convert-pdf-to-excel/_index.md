---
title: Преобразование PDF в Excel на Java
linktitle: Преобразование PDF в Excel
type: docs
weight: 20
url: /ru/java/convert-pdf-to-excel/
lastmod: "2026-09-16"
description: Узнайте, как конвертировать файлы PDF в Excel на Java с помощью Aspose.PDF, включая вывод в формате XML Spreadsheet 2003, XLSX, XLSM, CSV и ODS.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как конвертировать PDF в Excel на Java
Abstract: В этой статье объясняется, как конвертировать PDF‑файлы в форматы, совместимые с Excel, с помощью Aspose.PDF for Java. Рассматриваются вывод в XML Spreadsheet 2003, XLSX, XLSM, CSV и ODS, а также варианты вставки пустых столбцов и минимизации количества листов.
---
Aspose.PDF for Java может экспортировать содержимое PDF в несколько форматов электронных таблиц с различными вариантами макета. Используйте [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/), чтобы выбрать формат целевой книги и настроить распределение содержимого страницы по листам и столбцам.

## Преобразование PDF в Excel 2003 XML

Используйте этот пример, когда содержимое PDF должно быть экспортировано в формат электронной таблицы Excel 2003 XML.

1. Откройте исходный PDF в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) и установите формат `XMLSpreadSheet2003`.
1. Вызовите `document.save(outputFile.toString(), saveOptions)`, при этом загруженный PDF сериализуется в XML‑схеме Excel 2003.
1. Сохраните преобразованный выходной файл.

```java
public static void convertPdfToExcelSpreadSheet2003(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Преобразование PDF в XLSX

Используйте этот пример, когда содержимое PDF должно быть преобразовано в формат Excel 2007+ XLSX.

1. Откройте исходный PDF в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) и установите формат `XLSX`.
1. Вызовите `document.save(outputFile.toString(), saveOptions)`, при этом макет PDF экспортируется как рабочая книга Office Open XML.
1. Сохраните файл выходной таблицы.

```java
public static void convertPdfToExcel2007(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Преобразование PDF в XLSX с настройкой столбцов

Используйте этот пример, когда необходимо настроить обработку столбцов при конвертации PDF в Excel.

1. Откройте исходный PDF в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) для вывода в `XLSX`.
1. Включите `setInsertBlankColumnAtFirst(true)`, когда нужен дополнительный ведущий столбец для улучшения макета листа, полученного из PDF.
1. Вызовите `document.save(outputFile.toString(), saveOptions)` и запишите преобразованный файл XLSX.

```java
public static void convertPdfToExcel2007ControlColumn(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        saveOptions.setInsertBlankColumnAtFirst(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Преобразование PDF в один лист Excel

Используйте этот пример, когда все страницы PDF следует экспортировать в один лист.

1. Откройте исходный PDF в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) для экспорта в `XLSX`.
1. Включите `setMinimizeTheNumberOfWorksheets(true)`, при этом несколько страниц PDF объединяются в меньшее количество листов.
1. Вызовите `document.save(outputFile.toString(), saveOptions)` и сохраните файл вывода XLSX.

```java
public static void convertPdfToExcel2007SingleExcelWorksheet(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        saveOptions.setMinimizeTheNumberOfWorksheets(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Преобразование PDF в XLSM

Используйте этот пример, когда вывод PDF должен быть сохранён как рабочая книга Excel с поддержкой макросов.

1. Откройте исходный PDF в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) и установите формат `XLSM`.
1. Вызовите `document.save(outputFile.toString(), saveOptions)`, при этом содержимое PDF экспортируется в контейнер рабочей книги с поддержкой макросов.
1. Сохраните файл XLSM.

```java
public static void convertPdfToExcel2007Macro(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSM);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Преобразование PDF в CSV

Используйте этот пример, когда табличный контент PDF должен быть экспортирован в CSV.

1. Откройте исходный PDF в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) и установите формат `CSV`.
1. Вызовите `document.save(outputFile.toString(), saveOptions)`, при этом содержимое PDF преобразуется в плоский текст, разделённый запятыми.
1. Сохраните сгенерированный CSV‑файл.

```java
public static void convertPdfToExcel2007Csv(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.CSV);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Преобразование PDF в ODS

Используйте этот пример, когда содержимое PDF должно быть экспортировано в формат электронных таблиц OpenDocument.

1. Откройте исходный PDF в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) и установите формат `ODS`.
1. Вызовите `document.save(outputFile.toString(), saveOptions)`, при этом PDF экспортируется в формат электронных таблиц OpenDocument.
1. Сохраните преобразованный файл ODS.

```java
public static void convertPdfToOds(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.ODS);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

---
title: Конвертировать PDF в Excel на Java
linktitle: Конвертировать PDF в Excel
type: docs
weight: 20
url: /java/convert-pdf-to-excel/
lastmod: "2026-06-16"
description: Узнайте, как конвертировать PDF-файлы в Excel на Java с помощью Aspose.PDF, включая выходные данные XML Spreadsheet 2003, XLSX, XLSM, CSV и ODS.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как конвертировать PDF в Excel в Java
Abstract: В этой статье объясняется, как конвертировать PDF-файлы в форматы, совместимые с Excel, с помощью Aspose.PDF для Java. Он охватывает выходные данные XML Spreadsheet 2003, XLSX, XLSM, CSV и ODS, а также варианты вставки пустых столбцов и минимизации количества рабочих листов.
---
Aspose.PDF для Java может экспортировать содержимое PDF в несколько форматов электронных таблиц с различными вариантами макета. Используйте [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/), чтобы выбрать целевой формат книги и управлять тем, как содержимое страницы отображается на листах и ​​столбцах.

## Конвертировать PDF в XML Excel 2003

Используйте этот пример, когда содержимое PDF необходимо экспортировать в формат электронной таблицы Excel 2003 XML.

1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) и установите его формат `XMLSpreadSheet2003`.
1. Вызовите `document.save(outputFile.toString(), saveOptions)`, чтобы загруженный PDF-файл был сериализован в XML-схеме Excel 2003.
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

## Конвертировать PDF в XLSX

Используйте этот пример, когда содержимое PDF необходимо преобразовать в формат Excel 2007+ XLSX.

1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) и установите его формат `XLSX`.
1. Вызовите `document.save(outputFile.toString(), saveOptions)`, чтобы макет PDF был экспортирован как книга Office Open XML.
1. Сохраните выходной файл электронной таблицы.

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

## Конвертируйте PDF в XLSX с управлением столбцами

Используйте этот пример, когда необходимо настроить обработку столбцов во время преобразования PDF в Excel.

1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) для вывода `XLSX`.
1. Включите `setInsertBlankColumnAtFirst(true)`, если необходим дополнительный начальный столбец для улучшения макета листа, созданного из PDF-файла.
1. Позвоните `document.save(outputFile.toString(), saveOptions)` и запишите преобразованный файл XLSX.

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

Используйте этот пример, когда все страницы PDF необходимо экспортировать на один лист.

1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) для экспорта `XLSX`.
1. Включите `setMinimizeTheNumberOfWorksheets(true)`, чтобы несколько страниц PDF были объединены в меньшее количество листов.
1. Вызовите `document.save(outputFile.toString(), saveOptions)` и сохраните выходной файл XLSX.

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

## Конвертировать PDF в XLSM

Используйте этот пример, когда выходные данные PDF необходимо сохранить как книгу Excel с поддержкой макросов.

1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) и установите формат `XLSM`.
1. Вызовите `document.save(outputFile.toString(), saveOptions)`, чтобы содержимое PDF было экспортировано в контейнер книги с поддержкой макросов.
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

## Конвертировать PDF в CSV

Используйте этот пример, когда табличное содержимое PDF необходимо экспортировать в формате CSV.

1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) и установите формат `CSV`.
1. Вызовите `document.save(outputFile.toString(), saveOptions)`, чтобы содержимое PDF было преобразовано в текстовый вывод, разделенный запятыми.
1. Сохраните созданный файл CSV.

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

## Конвертировать PDF в ODS

Используйте этот пример, когда содержимое PDF необходимо экспортировать в формат электронной таблицы OpenDocument.

1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) и установите формат `ODS`.
1. Позвоните `document.save(outputFile.toString(), saveOptions)`, чтобы PDF-файл был экспортирован в формат электронной таблицы OpenDocument.
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

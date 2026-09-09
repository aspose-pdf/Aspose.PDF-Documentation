---
title: Преобразовать PDF в Excel в Java
linktitle: Преобразовать PDF в Excel
type: docs
weight: 20
url: /ru/java/convert-pdf-to-excel/
lastmod: "2026-08-19"
description: Узнайте, как преобразовать файлы PDF в Excel на Java с Aspose.PDF, включая вывод XML Spreadsheet 2003, XLSX, XLSM, CSV и ODS.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как преобразовать PDF в Excel на Java
Abstract: В этой статье объясняется, как преобразовать файлы PDF в форматы, совместимые с Excel, с помощью Aspose.PDF for Java. Описываются вывод в XML Spreadsheet 2003, XLSX, XLSM, CSV и ODS, а также варианты вставки пустых столбцов и минимизации количества листов.
---
Aspose.PDF for Java может экспортировать содержимое PDF в несколько форматов электронных таблиц с различными параметрами макета. Используйте [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) выбрать формат целевой книги и контролировать, как содержимое страницы распределяется по листам и столбцам.

## Конвертируйте PDF в Excel 2003 XML

Используйте этот пример, когда содержимое PDF должно быть экспортировано в формат электронных таблиц Excel 2003 XML.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) и установить его формат на `XMLSpreadSheet2003`.
1. Вызовите `document.save(outputFile.toString(), saveOptions)` Поэтому загруженный PDF сериализуется в схеме XML Excel 2003.
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

## Конвертируйте PDF в XLSX

Используйте этот пример, когда содержимое PDF должно быть конвертировано в формат Excel 2007+ XLSX.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) и установить его формат на `XLSX`.
1. Вызовите `document.save(outputFile.toString(), saveOptions)` поэтому макет PDF экспортируется как рабочая книга Office Open XML.
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

## Конвертируйте PDF в XLSX с управлением столбцами

Используйте этот пример, когда нужно скорректировать обработку столбцов при преобразовании PDF в Excel.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) для `XLSX` вывод.
1. Включите `setInsertBlankColumnAtFirst(true)` когда нужен дополнительный ведущий столбец для улучшения макета листа, полученного из PDF.
1. Вызовите `document.save(outputFile.toString(), saveOptions)` и записать преобразованный файл XLSX.

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

## Конвертируйте PDF в один лист Excel

Используйте этот пример, когда все страницы PDF должны быть экспортированы в один лист.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) для `XLSX` экспорт.
1. Включите `setMinimizeTheNumberOfWorksheets(true)` поэтому несколько страниц PDF объединяются в меньшее количество листов.
1. Вызовите `document.save(outputFile.toString(), saveOptions)` и сохранить файл вывода XLSX.

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

## Конвертируйте PDF в XLSM

Используйте этот пример, когда вывод PDF должен быть сохранён как книга Excel с поддержкой макросов.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) и установите формат `XLSM`.
1. Вызовите `document.save(outputFile.toString(), saveOptions)` поэтому содержимое PDF экспортируется в контейнер рабочей книги, поддерживающей макросы.
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

## Конвертируйте PDF в CSV

Используйте этот пример, когда табличный контент PDF должен быть экспортирован в CSV.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) и установите формат `CSV`.
1. Вызовите `document.save(outputFile.toString(), saveOptions)` поэтому содержимое PDF преобразуется в плоский текст, разделённый запятыми.
1. Сохраните сгенерированный файл CSV.

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

## Конвертируйте PDF в ODS

Используйте этот пример, когда содержимое PDF должно быть экспортировано в формат электронных таблиц OpenDocument.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) и установите формат `ODS`.
1. Вызовите `document.save(outputFile.toString(), saveOptions)` поэтому PDF экспортируется в формате электронных таблиц OpenDocument.
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



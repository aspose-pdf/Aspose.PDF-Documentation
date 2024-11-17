---
title: Convert PDF to Excel 
linktitle: Convert PDF to Excel
type: docs
weight: 20
url: /ru/java/convert-pdf-to-excel/
lastmod: "2021-11-19"
description: Aspose.PDF for Java allows you to convert PDF to Excel format using java. During this, the individual pages of the PDF file are converted to Excel worksheets.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF для Java API позволяет рендерить ваши PDF файлы в форматы файлов Excel [XLS](https://docs.fileformat.com/spreadsheet/xls/) и [XLSX](https://docs.fileformat.com/spreadsheet/xlsx/). У нас уже есть другой API, известный как [Aspose.Cells для Java](https://products.aspose.com/cells/java), который предоставляет возможность создавать и изменять существующие рабочие книги Excel. Он также предоставляет возможность преобразовывать рабочие книги Excel в формат PDF.

{{% alert color="primary" %}}

**Попробуйте преобразовать PDF в Excel онлайн**

Aspose.PDF for Java представляет вам бесплатное онлайн-приложение ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в Excel с бесплатным приложением](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## Конвертация PDF в Excel XLS

Чтобы преобразовать файлы PDF в формат XLS, Aspose.PDF имеет класс под названием [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions). Объект класса [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) передается в качестве второго аргумента методу Document.Save(..).

Преобразование файла PDF в формат XLSX является частью библиотеки Aspose.PDF для Java версии 18.6. Для того чтобы преобразовать файлы PDF в формат XLSX, вам нужно установить формат как XLSX с использованием метода setFormat() класса [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions).

Следующий фрагмент кода показывает, как преобразовать файл PDF в формат xls и .xlsx:

```java
package com.aspose.pdf.examples;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertPDFtoXLSX {

    private ConvertPDFtoXLSX() {

    }

    // Путь к каталогу с документами.
    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {

        ConvertPDFtoExcelSimple();
        ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst();
        ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets();
        ConvertPDFtoExcelAdvanced_SaveXLSX();
    }

    public static void ConvertPDFtoExcelSimple() {
        // Загрузить PDF документ
        Document pdfDocument = new Document(_dataDir + "input.pdf");

        // Создать объект параметров сохранения Excel
        ExcelSaveOptions excelsave = new ExcelSaveOptions();

        // Сохранить выходной файл в формате XLS
        pdfDocument.save("PDFToXLS_out.xls", excelsave);
    }
}
```


## Преобразование PDF в XLS с управлением колонками

При преобразовании PDF в формат XLS в выходной файл добавляется пустой столбец в качестве первого столбца. В классе [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) используется опция InsertBlankColumnAtFirst для управления этим столбцом. Значение по умолчанию — true.

```java
    public static void ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst() {
        // Загрузить PDF документ
        Document pdfDocument = new Document(_dataDir + "input.pdf");
        // Создать объект ExcelSave Option
        ExcelSaveOptions excelsave = new ExcelSaveOptions();
        excelsave.setInsertBlankColumnAtFirst(false);
        // Сохранить выходной файл в формате XLS
        pdfDocument.save("PDFToXLS_out.xls", excelsave);
    }
```

## Преобразование PDF в один лист Excel

При экспорте PDF файла с большим количеством страниц в XLS каждая страница экспортируется на отдельный лист в Excel файле.
 Это связано с тем, что свойство MinimizeTheNumberOfWorksheets по умолчанию установлено в значение false. Чтобы гарантировать, что все страницы экспортируются в один лист в выходном Excel файле, установите свойство MinimizeTheNumberOfWorksheets в true.

```java
    public static void ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets() {
        // Загрузка PDF документа
        Document pdfDocument = new Document(_dataDir + "input.pdf");

        // Создание объекта ExcelSave Option
        ExcelSaveOptions excelsave = new ExcelSaveOptions();
        excelsave.setMinimizeTheNumberOfWorksheets(true);

        // Сохранение результата в формате XLS
        pdfDocument.save("PDFToXLS_out.xls", excelsave);
    }
```

## Преобразование в формат XLSX

По умолчанию Aspose.PDF использует XML Spreadsheet 2003 для хранения данных. Для преобразования файлов PDF в формат XLSX, Aspose.PDF имеет класс под названием ExcelSaveOptions с Format. Объект класса [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) передается в качестве второго аргумента методу Document.Save(..).

```java
    public static void ConvertPDFtoExcelAdvanced_SaveXLSX() {
        // Загрузить PDF документ
        Document pdfDocument = new Document(_dataDir + "input.pdf");

        // Создать объект параметров сохранения Excel
        ExcelSaveOptions excelSave = new ExcelSaveOptions();
        excelSave.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);

        // Сохранить вывод в формате XLS
        pdfDocument.save("PDFToXLS_out.xlsx", excelSave);
    }
```
---
title: Конвертировать PDF в Microsoft Excel 
linktitle: Конвертировать PDF в Excel
type: docs
weight: 20
url: /php-java/convert-pdf-to-excel/
lastmod: "2024-05-20"
keywords: конвертировать PDF в Excel с использованием PHP, конвертировать PDF в XLS с использованием PHP, конвертировать PDF в XLSX с использованием PHP, экспортировать таблицу из PDF в Excel в PHP.
description: Aspose.PDF для PHP позволяет конвертировать PDF в формат Excel с использованием PHP. При этом отдельные страницы PDF файла конвертируются в листы Excel.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF для PHP API позволяет преобразовывать ваши PDF файлы в форматы Excel [XLS](https://docs.fileformat.com/spreadsheet/xls/) и [XLSX](https://docs.fileformat.com/spreadsheet/xlsx/). У нас уже есть другой API, известный как [Aspose.Cells for PHP via Java](https://products.aspose.com/cells/php-java), который предоставляет возможность создавать и изменять существующие книги Excel. Он также предоставляет возможность преобразовывать книги Excel в формат PDF.

{{% alert color="primary" %}}

**Попробуйте конвертировать PDF в Excel онлайн**

Aspose.PDF для PHP представляет вам бесплатное онлайн-приложение ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в Excel с бесплатным приложением](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## Конвертация PDF в Excel XLS

Чтобы конвертировать файлы PDF в формат XLS, Aspose.PDF имеет класс под названием [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions). Объект класса [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) передается в качестве второго аргумента в метод Document.Save(..).

Конвертация PDF файла в формат XLSX является частью библиотеки Aspose.PDF для PHP версии 18.6. Чтобы конвертировать файлы PDF в формат XLSX, необходимо установить формат как XLSX с помощью метода setFormat() класса [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions).

Следующие фрагменты кода показывают, как конвертировать PDF файл в формат XLS и XLSX:

```php
// Загрузите входной PDF-документ, используя класс Document.
$document = new Document($inputFile);

// Создайте экземпляр класса ExcelSaveOptions, чтобы задать параметры сохранения.
$saveOption = new ExcelSaveOptions();

// Установите выходной формат в XLS.
// $saveOption->setFormat(ExcelSaveOptions_ExcelFormat::$XMLSpreadSheet2003);

// Установите выходной формат в XLSX.
    $excelSaveOptions_ExcelFormat = new ExcelSaveOptions_ExcelFormat();
    $saveOption->setFormat($excelSaveOptions_ExcelFormat->XLSX);

// Сохраните PDF-документ как файл Excel, используя указанные параметры сохранения.
$document->save($outputFile, $saveOption);
```
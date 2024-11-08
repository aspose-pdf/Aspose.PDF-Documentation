---
title: Конвертация PDF в Excel в .NET
linktitle: Конвертация PDF в Excel
type: docs
weight: 20
url: /ru/net/convert-pdf-to-excel/
lastmod: "2021-11-01"
keywords: конвертация PDF в Excel с использованием c#, конвертация PDF в XLS с использованием csharp, конвертация PDF в XLSX с использованием csharp, экспорт таблицы из PDF в Excel на csharp.
description: Библиотека Aspose.PDF для .NET позволяет конвертировать PDF в формат Excel с использованием C#. Эти форматы включают XLS, XLSX, XML 2003 Spreadsheet, CSV, ODS.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Обзор

В данной статье объясняется, как **конвертировать PDF в форматы Excel с использованием C#**. Она охватывает следующие темы.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

_Формат_: **XLS**

- [C# PDF в XLS](#csharp-pdf-to-xls)
- [C# Конвертировать PDF в XLS](#csharp-pdf-to-xls)
- [C# Как конвертировать файл PDF в XLS](#csharp-pdf-to-xls)

_Формат_: **XLSX**

- [C# PDF в XLSX](#csharp-pdf-to-xlsx)
- [C# Конвертировать PDF в XLSX](#csharp-pdf-to-xlsx)
- [C# Как конвертировать файл PDF в XLSX](#csharp-pdf-to-xlsx)
- [C# Как конвертировать PDF файл в XLSX](#csharp-pdf-to-xlsx)

_Формат_: **Excel**

- [C# PDF в Excel](#csharp-pdf-to-xlsx)
- [C# PDF в Excel XLS](#csharp-pdf-to-xls)
- [C# PDF в Excel XLSX](#csharp-pdf-to-xlsx)

_Формат_: **Один лист Excel**

- [C# Конвертировать PDF в XLS с одним листом](#csharp-pdf-to-excel-single)
- [C# Конвертировать PDF в XLSX с одним листом](#csharp-pdf-to-excel-single)

_Формат_: **XML Spreadsheet 2003**

- [C# PDF в XML Excel](#csharp-pdf-to-excel-xml-2003)
- [C# Конвертировать PDF в XML электронную таблицу Excel](#csharp-pdf-to-excel-xml-2003)

_Формат_: **CSV**

- [C# PDF в CSV](#csharp-pdf-to-csv)
- [C# Конвертировать PDF в CSV](#csharp-pdf-to-csv)
- [C# Как конвертировать PDF файл в CSV](#csharp-pdf-to-csv)

_Формат_: **ODS**

- [C# PDF в ODS](#csharp-pdf-to-ods)
- [C# Конвертировать PDF в ODS](#csharp-pdf-to-ods)
- [C# Как конвертировать PDF файл в ODS](#csharp-pdf-to-ods)

## C# Конвертация PDF в Excel

**Aspose.PDF for .NET** поддерживает возможность конвертации PDF файлов в форматы Excel 2007, CSV и SpeadsheetML.
**Aspose.PDF для .NET** поддерживает функцию конвертации PDF-файлов в форматы Excel 2007, CSV и SpeadsheetML.

Aspose.PDF для .NET — это компонент для манипуляции с PDF-файлами, мы представили функцию, которая рендерит PDF-файл в рабочую книгу Excel (файлы XLSX). Во время этой конвертации отдельные страницы PDF-файла конвертируются в листы Excel.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в Excel онлайн**

Aspose.PDF для .NET предлагает вам бесплатное онлайн-приложение ["PDF в XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), где вы можете изучить функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в Excel с помощью бесплатного приложения](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

Для конвертации PDF-файлов в формат <abbr title="Microsoft Excel Open XML Spreadsheet">XLSX</abbr>, Aspose.PDF имеет класс под названием [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions).
Для конвертации файлов PDF в формат <abbr title="Microsoft Excel Open XML Spreadsheet">XLSX</abbr>, Aspose.PDF имеет класс под названием [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions).

Следующий фрагмент кода показывает процесс преобразования файла PDF в формат XLS или XLSX с помощью Aspose.PDF для .NET.

<a name="csharp-pdf-to-xls"><strong>Шаги: Конвертация PDF в XLS на C#</strong></a>

1. Создайте экземпляр объекта **Document** с исходным документом PDF.
2. Создайте экземпляр **ExcelSaveOptions**.
3. Сохраните в формате **XLS**, указав **.xls расширение**, вызвав метод **Document.Save()** и передав ему **ExcelSaveOptions**

<a name="csharp-pdf-to-xlsx"><strong>Шаги: Конвертация PDF в XLSX на C#</strong></a>

1. Создайте экземпляр объекта **Document** с исходным документом PDF.
2. Создайте экземпляр **ExcelSaveOptions**.
3. Сохраните в формате **XLSX**, указав **.xlsx расширение**, вызвав метод **Document.Save()** и передав ему **ExcelSaveOptions**

```csharp
```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Загружаем PDF документ
Document pdfDocument = new Document(dataDir + "input.pdf");

// Создаем объект параметров сохранения в Excel
Aspose.Pdf.ExcelSaveOptions excelsave = new ExcelSaveOptions();

// Сохраняем результат в формате XLS
pdfDocument.Save("PDFToXLS_out.xlsx", excelsave);
```

## Конвертация PDF в XLS с контролем колонок

При конвертации PDF в формат XLS в выходной файл добавляется пустая колонка как первая колонка. В классе ExcelSaveOptions используется опция InsertBlankColumnAtFirst для контроля этой колонки. Значение по умолчанию `false`, что означает, что пустые колонки не будут вставлены.

```csharp
public static void ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst()
{
    // Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    // Загружаем PDF документ
    Document pdfDocument = new Document(_dataDir + "input.pdf");
    // Создаем объект параметров сохранения в Excel
    Aspose.Pdf.ExcelSaveOptions excelsave = new ExcelSaveOptions {InsertBlankColumnAtFirst = false};
    // Сохраняем результат в формате XLS
    pdfDocument.Save("PDFToXLS_out.xlsx", excelsave);
}
```
## Конвертация PDF в один лист Excel

При экспорте файла PDF с большим количеством страниц в XLS каждая страница экспортируется в отдельный лист файла Excel. Это связано с тем, что свойство MinimizeTheNumberOfWorksheets по умолчанию установлено в значение false. Чтобы все страницы были экспортированы в один лист в выходном файле Excel, установите свойство MinimizeTheNumberOfWorksheets в значение true.

<a name="csharp-pdf-to-excel-single"><strong>Шаги: Конвертация PDF в XLS или XLSX один лист на C#</strong></a>

1. Создайте экземпляр объекта **Document** с исходным документом PDF.
2. Создайте экземпляр **ExcelSaveOptions** с **MinimizeTheNumberOfWorksheets = true**.
3. Сохраните в формате **XLS** или **XLSX** с одним листом, вызвав метод **Document.Save()** и передав ему **ExcelSaveOptions**.

```csharp
public static void ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets()
{
    // Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    // Загрузите документ PDF
    Document pdfDocument = new Document(_dataDir + "input.pdf");

    // Создайте объект ExcelSave Option
    Aspose.Pdf.ExcelSaveOptions excelsave = new ExcelSaveOptions {MinimizeTheNumberOfWorksheets = true};
    // Сохраните результат в формате XLS
    pdfDocument.Save("PDFToXLS_out.xlsx", excelsave);
}
```
## Конвертация в другие форматы таблиц

### Конвертация в формат XML Spreadsheet 2003

Начиная с версии 20.8, Aspose.PDF использует формат файла Microsoft Excel Open XML Spreadsheet 2007 в качестве стандартного для хранения данных. Для конвертации PDF файлов в формат XML Spreadsheet 2003, Aspose.PDF предоставляет класс [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions) с свойством [Format](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions/properties/format). Объект класса [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions) передается в качестве второго аргумента методу [Document.Save(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index).

Приведенный ниже фрагмент кода показывает процесс конвертации PDF файла в формат XLS Excel 2003 XML.

<a name="csharp-pdf-to-excel-xml-2003"><strong>Шаги: Конвертация PDF в формат Excel 2003 XML на C#</strong></a>

1. Создайте экземпляр объекта **Document** с исходным PDF документом.
2.
2.
3. Сохраните в формате **XLS - Excel 2003 XML Format**, вызвав метод **Document.Save()** и передав ему **ExcelSaveOptions**.

```csharp
public static void ConvertPDFtoExcelAdvanced_SaveXLS2003()
{
    // Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET

    // Загрузите PDF документ
    Document pdfDocument = new Document(_dataDir + "input.pdf");

    // Создайте объект настроек сохранения Excel
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003 };

    // Сохраните результат в формате XLS
    pdfDocument.Save("PDFToXLS_out.xls", excelSave);
}
```

### Конвертировать в CSV

Конвертация в формат CSV производится таким же образом, как описано выше. Все, что вам нужно - это установить соответствующий формат.

<a name="csharp-pdf-to-csv"><strong>Шаги: Конвертация PDF в CSV на C#</strong></a>

1. Создайте экземпляр объекта **Document** с исходным PDF документом.
2.
2.
3. Сохраните в формате **CSV**, вызвав метод **Document.Save()** и передав ему **ExcelSaveOptions**.


```csharp
 // Создайте объект ExcelSave Options
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.CSV };
```

### Конвертировать в ODS

<a name="csharp-pdf-to-ods"><strong>Шаги: Конвертация PDF в ODS в C#</strong></a>

1. Создайте экземпляр объекта **Document** с исходным PDF-документом.
2. Создайте экземпляр **ExcelSaveOptions** с **Format = ExcelSaveOptions.ExcelFormat.ODS**
3. Сохраните в формате **ODS**, вызвав метод **Document.Save()** и передав ему **ExcelSaveOptions**.


Конвертация в формат ODS выполняется так же, как и во всех других форматах.

```csharp
 // Создайте объект ExcelSave Options
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.ODS };
```

## Смотрите также 

В этой статье также рассматриваются следующие темы. Коды такие же, как выше.

_Формат_: **Excel**
- [C# PDF в Excel код](#csharp-pdf-to-xlsx)
- [C# API для PDF в Excel](#csharp-pdf-to-xlsx)
- [API C# для конвертации PDF в Excel](#csharp-pdf-to-xlsx)
- [Программное преобразование PDF в Excel на C#](#csharp-pdf-to-xlsx)
- [Библиотека C# для работы с PDF и Excel](#csharp-pdf-to-xlsx)
- [Сохранение PDF в формате Excel на C#](#csharp-pdf-to-xlsx)
- [Генерация Excel из PDF на C#](#csharp-pdf-to-xlsx)
- [Создание Excel из PDF на C#](#csharp-pdf-to-xlsx)
- [Конвертер PDF в Excel на C#](#csharp-pdf-to-xlsx)

_Format_: **XLS**
- [Код C# для конвертации PDF в XLS](#csharp-pdf-to-xls)
- [API C# для конвертации PDF в XLS](#csharp-pdf-to-xls)
- [Программное преобразование PDF в XLS на C#](#csharp-pdf-to-xls)
- [Библиотека C# для работы с PDF и XLS](#csharp-pdf-to-xls)
- [Сохранение PDF в формате XLS на C#](#csharp-pdf-to-xls)
- [Генерация XLS из PDF на C#](#csharp-pdf-to-xls)
- [Создание XLS из PDF на C#](#csharp-pdf-to-xls)
- [Конвертер PDF в XLS на C#](#csharp-pdf-to-xls)

_Format_: **XLSX**
- [Код C# для конвертации PDF в XLSX](#csharp-pdf-to-xlsx)
- [API C# для конвертации PDF в XLSX](#csharp-pdf-to-xlsx)
- [Программное преобразование PDF в XLSX на C#](#csharp-pdf-to-xlsx)
- [Библиотека C# для работы с PDF и XLSX](#csharp-pdf-to-xlsx)
- [Сохранение PDF в формате XLSX на C#](#csharp-pdf-to-xlsx)
- [Генерация XLSX из PDF на C#](#csharp-pdf-to-xlsx)
- [C# Генерация XLSX из PDF](#csharp-pdf-to-xlsx)
- [C# Создание XLSX из PDF](#csharp-pdf-to-xlsx)
- [C# Конвертер PDF в XLSX](#csharp-pdf-to-xlsx)

_Format_: **CSV**
- [C# Код для преобразования PDF в CSV](#csharp-pdf-to-csv)
- [C# API для преобразования PDF в CSV](#csharp-pdf-to-csv)
- [C# Программное преобразование PDF в CSV](#csharp-pdf-to-csv)
- [C# Библиотека для преобразования PDF в CSV](#csharp-pdf-to-csv)
- [C# Сохранение PDF как CSV](#csharp-pdf-to-csv)
- [C# Генерация CSV из PDF](#csharp-pdf-to-csv)
- [C# Создание CSV из PDF](#csharp-pdf-to-csv)
- [C# Конвертер PDF в CSV](#csharp-pdf-to-csv)

_Format_: **ODS**
- [C# Код для преобразования PDF в ODS](#csharp-pdf-to-ods)
- [C# API для преобразования PDF в ODS](#csharp-pdf-to-ods)
- [C# Программное преобразование PDF в ODS](#csharp-pdf-to-ods)
- [C# Библиотека для преобразования PDF в ODS](#csharp-pdf-to-ods)
- [C# Сохранение PDF как ODS](#csharp-pdf-to-ods)
- [C# Генерация ODS из PDF](#csharp-pdf-to-ods)
- [C# Создание ODS из PDF](#csharp-pdf-to-ods)
- [C# Конвертер PDF в ODS](#csharp-pdf-to-ods)

---
title: Конвертация PDF в Excel в .NET
linktitle: Конвертация PDF в Excel
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ru/net/convert-pdf-to-excel/
lastmod: "2021-11-01"
description: Библиотека Aspose.PDF for .NET позволяет конвертировать PDF в формат Excel с использованием C#. Эти форматы включают XLS, XLSX, XML 2003 Spreadsheet, CSV, ODS.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to Excel in .NET",
    "alternativeHeadline": "Convert PDF Files to Excel Formats with C#",
    "abstract": "Откройте для себя мощную возможность Aspose.PDF for .NET без усилий конвертировать PDF документы в различные форматы Excel, включая XLS, XLSX, CSV и ODS, используя C#. Эта функция не только позволяет преобразовывать отдельные страницы PDF в отдельные листы Excel, но также предлагает варианты для объединенных листов, предоставляя пользователям гибкость в управлении своими данными PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1409",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/convert-pdf-to-excel/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-excel/"
    },
    "dateModified": "2025-04-04",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но также справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

## Обзор

Эта статья объясняет, как **конвертировать PDF в форматы Excel с использованием C#**. Она охватывает следующие темы.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

- [Конвертация PDF в XLS](#csharp-pdf-to-xls)
- [Конвертация PDF в XLSX](#csharp-pdf-to-xlsx)
- [Конвертация PDF в Excel](#csharp-pdf-to-xlsx)
- [Конвертация PDF в XLS с одним листом](#csharp-pdf-to-excel-single)
- [Конвертация PDF в XLSX с одним листом](#csharp-pdf-to-excel-single)
- [Конвертация PDF в XML Excel](#csharp-pdf-to-excel-xml-2003)
- [Конвертация PDF в CSV](#csharp-pdf-to-csv)
- [Конвертация PDF в ODS](#csharp-pdf-to-ods)
- [Конвертация PDF в XLSM](#csharp-pdf-to-xlsm)

## Конвертации C# PDF в Excel

**Aspose.PDF for .NET** поддерживает функцию конвертации PDF файлов в форматы Excel 2007, CSV и SpeadsheetML.

Aspose.PDF for .NET является компонентом для манипуляции PDF, мы внедрили функцию, которая преобразует PDF файл в рабочую книгу Excel (файлы XLSX). В процессе этой конвертации отдельные страницы PDF файла преобразуются в листы Excel.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в Excel онлайн**

Aspose.PDF for .NET предлагает вам онлайн бесплатное приложение ["PDF в XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в Excel с бесплатным приложением](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

Для конвертации PDF файлов в формат <abbr title="Microsoft Excel Open XML Spreadsheet">XLSX</abbr> Aspose.PDF имеет класс [ExcelSaveOptions](https://reference.aspose.com/pdf/ru/net/aspose.pdf/excelsaveoptions). Объект класса ExcelSaveOptions передается в качестве второго аргумента в конструктор Document.Save(..).

Следующий фрагмент кода показывает процесс конвертации PDF файла в формат XLS или XLSX с помощью Aspose.PDF for .NET.

<a name="csharp-pdf-to-xls" id="cshart-pdf-to-xls"><strong>Конвертация PDF в XLS</strong></a>

1. Создайте экземпляр объекта **Document** с исходным PDF документом.
2. Создайте экземпляр **ExcelSaveOptions**.
3. Сохраните его в формате **XLS**, указав **.xls расширение**, вызвав метод **Document.Save()** и передав ему **ExcelSaveOptions**.

<a name="csharp-pdf-to-xlsx" id="cshart-pdf-to-xlsx"><strong>Конвертация PDF в XLSX</strong></a>

1. Создайте экземпляр объекта **Document** с исходным PDF документом.
2. Создайте экземпляр **ExcelSaveOptions**.
3. Сохраните его в формате **XLSX**, указав **.xlsx расширение**, вызвав метод **Document.Save()** и передав ему **ExcelSaveOptions**.

```csharp
  // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertPDFtoExcel()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Open PDF document
     using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
     {
         // Instantiate ExcelSaveOptions object
         var saveOptions = new Aspose.Pdf.ExcelSaveOptions();

         // Save the file in XLSX format
         document.Save(dataDir + "PDFToXLS_out.xlsx", saveOptions);
     }
 }
```

## Конвертация PDF в XLS с контролем столбца

При конвертации PDF в формат XLS в выходной файл добавляется пустой столбец в качестве первого столбца. Опция InsertBlankColumnAtFirst класса ExcelSaveOptions используется для управления этим столбцом. Значение по умолчанию - `false`, что означает, что пустые столбцы не будут вставлены.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            InsertBlankColumnAtFirst = false
        };

        // Save the file in XLSX format
        document.Save(dataDir + "PDFToXLS_out.xlsx", saveOptions);
    }
}
```

## Конвертация PDF в один лист Excel

При экспорте PDF файла с большим количеством страниц в XLS каждая страница экспортируется на отдельный лист в файле Excel. Это происходит потому, что свойство MinimizeTheNumberOfWorksheets по умолчанию установлено в false. Чтобы убедиться, что все страницы экспортируются на один единственный лист в выходном Excel файле, установите свойство MinimizeTheNumberOfWorksheets в true.

<a name="csharp-pdf-to-excel-single" id="cshart-pdf-to-excel-single"><strong>Конвертация PDF в XLS или XLSX с одним листом</strong></a>

1. Создайте экземпляр объекта **Document** с исходным PDF документом.
2. Создайте экземпляр **ExcelSaveOptions** с **MinimizeTheNumberOfWorksheets = true**.
3. Сохраните его в формате **XLS** или **XLSX**, имея один лист, вызвав метод **Document.Save()** и передав ему **ExcelSaveOptions**.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            MinimizeTheNumberOfWorksheets = true
        };

        // Save the file in XLSX format
        document.Save(dataDir + "PDFToXLS_out.xlsx", saveOptions);
    }
}
```

## Конвертация в другие форматы таблиц

### Конвертация в формат XML Spreadsheet 2003

Начиная с версии 20.8 Aspose.PDF использует формат файла Microsoft Excel Open XML Spreadsheet 2007 по умолчанию для хранения данных. Чтобы конвертировать PDF файлы в формат XML Spreadsheet 2003, Aspose.PDF имеет класс [ExcelSaveOptions](https://reference.aspose.com/pdf/ru/net/aspose.pdf/excelsaveoptions) с [Format](https://reference.aspose.com/pdf/ru/net/aspose.pdf/excelsaveoptions/properties/format). Объект класса [ExcelSaveOptions](https://reference.aspose.com/pdf/ru/net/aspose.pdf/excelsaveoptions) передается в качестве второго аргумента в метод [Document.Save(..)](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document/methods/save/index).

Следующий фрагмент кода показывает процесс конвертации PDF файла в формат XLS Excel 2003 XML.

<a name="csharp-pdf-to-excel-xml-2003" id="cshart-pdf-to-excel-xml-2003"><strong>Конвертация PDF в формат Excel 2003 XML</strong></a>

1. Создайте экземпляр объекта **Document** с исходным PDF документом.
2. Создайте экземпляр **ExcelSaveOptions** с **Format = ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003**.
3. Сохраните его в формате **XLS - Excel 2003 XML Format**, вызвав метод **Document.Save()** и передав ему **ExcelSaveOptions**.

```csharp
  // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertPDFtoExcelAdvanced_SaveXLS2003()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Open PDF document
     using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
     {
         // Instantiate ExcelSaveOptions object
         var saveOptions = new Aspose.Pdf.ExcelSaveOptions
         {
             Format = Aspose.Pdf.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
         };

         // Save the file in XLS format
         document.Save(dataDir + "PDFToXLS_out.xls", saveOptions);
     }
 }
```

### Конвертация в CSV

Конвертация в формат CSV выполняется так же, как и выше. Все, что вам нужно - установить соответствующий формат.

<a name="csharp-pdf-to-csv"  id="cshart-pdf-to-csv"><strong>Конвертация PDF в CSV</strong></a>

1. Создайте экземпляр объекта **Document** с исходным PDF документом.
2. Создайте экземпляр **ExcelSaveOptions** с **Format = ExcelSaveOptions.ExcelFormat.CSV**.
3. Сохраните его в формате **CSV**, вызвав метод **Document.Save()** и передав ему **ExcelSaveOptions**.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToCSV()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            Format = Aspose.Pdf.ExcelSaveOptions.ExcelFormat.CSV
        };
        
        // Save the file in CSV format
        document.Save(dataDir + "PDFToXLS_out.csv", saveOptions);
    }
}
```

### Конвертация в ODS

<a name="csharp-pdf-to-ods"  id="cshart-pdf-to-ods"><strong>Конвертация PDF в ODS</strong></a>

1. Создайте экземпляр объекта **Document** с исходным PDF документом.
2. Создайте экземпляр **ExcelSaveOptions** с **Format = ExcelSaveOptions.ExcelFormat.ODS**.
3. Сохраните его в формате **ODS**, вызвав метод **Document.Save()** и передав ему **ExcelSaveOptions**.

Конвертация в формат ODS выполняется так же, как и все другие форматы.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToODS()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            Format = Aspose.Pdf.ExcelSaveOptions.ExcelFormat.ODS
        };

        // Save the file in ODS format
        document.Save(dataDir + "PDFToODS_out.ods", saveOptions);
    }
}
```

### Конвертация в XLSM

<a name="csharp-pdf-to-xlsm" id="cshart-pdf-to-xlsm"><strong>Конвертация PDF в XLSM</strong></a>

1. Создайте экземпляр объекта **Document** с исходным PDF документом.
2. Создайте экземпляр **ExcelSaveOptions** с **Format = ExcelSaveOptions.ExcelFormat.XLSM**.
3. Сохраните его в формате **XLSM**, вызвав метод **Document.Save()** и передав ему **ExcelSaveOptions**.

Конвертация в формат XLSM выполняется так же, как и все другие форматы.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToXLSM()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            Format = Aspose.Pdf.ExcelSaveOptions.ExcelFormat.XLSM
        };

        // Save the file in XLSM format
        document.Save(dataDir + "PDFToODS_out.xlsm", saveOptions);
    }
}
```
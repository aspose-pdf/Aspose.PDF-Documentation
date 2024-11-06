---
title: Convert PDF to Excel in C++
linktitle: Convert PDF to Excel
type: docs
weight: 20
url: ru/cpp/convert-pdf-to-excel/
lastmod: "2021-11-19"
description: Aspose.PDF для C++ позволяет конвертировать PDF в формат Excel с использованием C++. Во время этого отдельные страницы PDF файла конвертируются в листы Excel.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Overview

В этой статье объясняется, как **конвертировать PDF в форматы Excel с использованием C++**. Она охватывает следующие темы.

_Формат_: **XLS**
- [C++ PDF в XLS](#cpp-pdf-to-xls)
- [C++ Конвертация PDF в XLS](#cpp-pdf-to-xls)
- [C++ Как конвертировать PDF файл в XLS](#cpp-pdf-to-xls)

_Формат_: **XLSX**
- [C++ PDF в XLSX](#cpp-pdf-to-xlsx)
- [C++ Конвертация PDF в XLSX](#cpp-pdf-to-xlsx)
- [C++ Как конвертировать PDF файл в XLSX](#cpp-pdf-to-xlsx)

_Формат_: **Microsoft Excel XLS формат**
- [C++ PDF в Excel](#cpp-pdf-to-excel-xls)
- [C++ Конвертация PDF в Excel](#cpp-pdf-to-excel-xls)
- [C++ Как конвертировать PDF файл в Excel](#cpp-pdf-to-excel-xls)

_Формат_: **Microsoft Excel XLSX формат**
- [C++ PDF в Excel](#cpp-pdf-to-excel-xlsx)
- [C++ Конвертация PDF в Excel](#cpp-pdf-to-excel-xlsx)
- [C++ Как конвертировать файл PDF в Excel](#cpp-pdf-to-excel-xlsx)

Другие темы, рассмотренные в этой статье
- [См. также](#see-also)

## Конвертация PDF в Excel с помощью C++

**Aspose.PDF для C++** поддерживает функцию конвертации файлов PDF в форматы Excel.

Aspose.PDF для C++ — это компонент для работы с PDF, в котором мы внедрили функцию преобразования файла PDF в книгу Excel (файлы XLS). В процессе этой конвертации отдельные страницы PDF файла преобразуются в листы Excel.

Для того чтобы конвертировать файлы PDF в формат <abbr title="Microsoft Excel Spreadsheet">XLS</abbr>, в Aspose.PDF имеется класс под названием ExcelSaveOptions. Объект класса ExcelSaveOptions передается в качестве второго аргумента в конструктор Document.Save(..).

Следующий фрагмент кода демонстрирует процесс конвертации файла PDF в формат XLS с помощью Aspose.PDF для C++.

<a name="cpp-pdf-to-xls" id="cpp-pdf-to-xls"><strong>Шаги: Конвертация PDF в XLS на C++</strong></a> | <a name="cpp-pdf-to-excel-xls" id="cpp-pdf-to-excel-xls"><strong>Шаги: Конвертация PDF в формат Excel XLS на C++</strong></a>

1. Создайте экземпляр объекта [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) с исходным PDF-документом.
2. Сохраните его в формате _XLS_, вызвав метод **Document->Save()**.

```cpp
void ConvertPDFtoExcel()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Conversion\\");

    // Строка для имени файла
    String infilename("sample.pdf");
    String outfilename("PDFToExcel.xls");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
    // Сохранить результат в формате XLS
    document->Save(_dataDir + outfilename, SaveFormat::Excel);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message();
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Преобразование PDF в XLS с контролем столбца

При преобразовании PDF в формат XLS в выходной файл добавляется пустой столбец в качестве первого столбца. The in ExcelSaveOptions class' InsertBlankColumnAtFirst option is used to control this column. Its default value is true.

```cpp
void ConvertPDFtoExcel_Advanced_InsertBlankColumnAtFirst()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for file name
    String infilename("sample.pdf");
    String outfilename("PDFToExcel.xls");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instantiate ExcelSave Option object
    auto excelSave = MakeObject<ExcelSaveOptions>();

    // The in ExcelSaveOptions class' InsertBlankColumnAtFirst option is used to control this column. Its default value is true.
    excelSave->set_InsertBlankColumnAtFirst(false);

    // Save the output in XLS format
    document->Save(outfilename, excelSave);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Конвертировать PDF в один лист Excel

При экспорте PDF-файла с большим количеством страниц в XLS каждая страница экспортируется на отдельный лист в файле Excel. Это связано с тем, что свойство MinimizeTheNumberOfWorksheets по умолчанию установлено в значение false. Чтобы обеспечить экспорт всех страниц в один лист в выходном Excel файле, установите свойство MinimizeTheNumberOfWorksheets в значение true.

```cpp
void ConvertPDFtoExcel_Advanced_MinimizeTheNumberOfWorksheets()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Conversion\\");

    // Строка для имени файла
    String infilename("sample.pdf");
    String outfilename("PDFToExcel.xls");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Создать объект параметров сохранения Excel
    auto excelSave = MakeObject<ExcelSaveOptions>();

    excelSave->set_MinimizeTheNumberOfWorksheets(true);

    // Сохранить выходной файл в формате XLS
    document->Save(outfilename, excelSave);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Конвертация в формат XLSX

По умолчанию Aspose.PDF использует XML Spreadsheet 2003 для хранения данных. Для конвертации файлов PDF в формат XLSX, Aspose.PDF имеет класс под названием [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.excel_save_options) с 'Format'. Объект класса [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.excel_save_options) передается в качестве второго аргумента методу [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa).

Следующий фрагмент кода показывает процесс конвертации файла PDF в формат XLSX.

<a name="cpp-pdf-to-xlsx" id="cpp-pdf-to-xlsx"><strong>Шаги: Конвертация PDF в XLSX на C++</strong></a> | <a name="cpp-pdf-to-excel-xlsx" id="cpp-pdf-to-excel-xlsx"><strong>Шаги: Конвертация PDF в формат Excel XLSX на C++</strong></a>

1. Создайте экземпляр объекта [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) с исходным PDF документом.
2. Создайте экземпляр [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.excel_save_options).
3. Установите формат как _ExcelSaveOptions::ExcelFormat::XLSX_.
4. Сохраните в формате _XLSX_, вызвав метод **Document->Save()** и передав ему экземпляр _ExcelSaveOptions_.

```cpp
void ConvertPDFtoExcel_Advanced_SaveXLSX()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Conversion\\");

    // Строка для имени файла
    String infilename("sample.pdf");
    String outfilename("PDFToExcel.xls");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Создать объект параметров сохранения Excel
    auto excelSave = MakeObject<ExcelSaveOptions>();

    excelSave->set_Format(ExcelSaveOptions::ExcelFormat::XLSX);

    // Сохраните выходные данные в формате XLS
    document->Save(outfilename, excelSave);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="success" %}}

**Попробуйте конвертировать PDF в Excel онлайн**
Aspose.PDF for C++ представляет вам бесплатное онлайн-приложение ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Convertion PDF to Excel with Free App](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## См. также

Эта статья также охватывает следующие темы. Коды такие же, как и выше.

_Формат_: **Формат Microsoft Excel XLS**
- [C++ PDF в Excel XLS Код](#cpp-pdf-to-excel-xls)
- [C++ PDF в Excel XLS Программно](#cpp-pdf-to-excel-xls)
- [C++ PDF в Excel XLS Библиотека](#cpp-pdf-to-excel-xls)
- [C++ Сохранить PDF как Excel XLS](#cpp-pdf-to-excel-xls)
- [C++ Генерация Excel XLS из PDF](#cpp-pdf-to-excel-xls)
- [C++ Создать Excel XLS из PDF](#cpp-pdf-to-excel-xls)
- [C++ Конвертер PDF в Excel XLS](#cpp-pdf-to-excel-xls)

_Формат_: **Формат Microsoft Excel XLSX**
- [C++ PDF в Excel XLSX Код](#cpp-pdf-to-excel-xlsx)

- [C++ PDF в Excel XLSX Программно](#cpp-pdf-to-excel-xlsx)

- [C++ PDF to Excel XLSX Library](#cpp-pdf-to-excel-xlsx)
- [C++ Сохранить PDF как Excel XLSX](#cpp-pdf-to-excel-xlsx)
- [C++ Создать Excel XLSX из PDF](#cpp-pdf-to-excel-xlsx)
- [C++ Создать Excel XLSX из PDF](#cpp-pdf-to-excel-xlsx)
- [C++ PDF в конвертер Excel XLSX](#cpp-pdf-to-excel-xlsx)

_Формат_: **XLS**
- [C++ Код для PDF в XLS](#cpp-pdf-to-xls)
- [C++ Программное преобразование PDF в XLS](#cpp-pdf-to-xls)
- [C++ Библиотека для PDF в XLS](#cpp-pdf-to-xls)
- [C++ Сохранить PDF как XLS](#cpp-pdf-to-xls)
- [C++ Генерировать XLS из PDF](#cpp-pdf-to-xls)
- [C++ Создать XLS из PDF](#cpp-pdf-to-xls)
- [C++ PDF в конвертер XLS](#cpp-pdf-to-xls)

_Формат_: **XLSX**
- [C++ Код для PDF в XLSX](#cpp-pdf-to-xlsx)
- [C++ Программное преобразование PDF в XLSX](#cpp-pdf-to-xlsx)
- [C++ Библиотека для PDF в XLSX](#cpp-pdf-to-xlsx)
- [C++ Сохранить PDF как XLSX](#cpp-pdf-to-xlsx)
- [C++ Генерировать XLSX из PDF](#cpp-pdf-to-xlsx)
- [C++ Создать XLSX из PDF](#cpp-pdf-to-xlsx)
- [C++ PDF в конвертер XLSX](#cpp-pdf-to-xlsx)
```
---
title: Преобразование PDF в Excel на Python
linktitle: Преобразование PDF в Excel
type: docs
weight: 20
url: /ru/python-net/convert-pdf-to-excel/
lastmod: "2022-12-23"
description: Библиотека Aspose.PDF for Python позволяет преобразовывать PDF в формат Excel с использованием Python. Эти форматы включают XLS, XLSX, XML 2003 Spreadsheet, CSV, ODS.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Обзор

Эта статья объясняет, как **преобразовать PDF в форматы Excel с использованием Python**. Она охватывает следующие темы.

_Формат_: **XLS**

- [Python PDF в XLS](#python-pdf-to-xls)
- [Python Преобразование PDF в XLS](#python-pdf-to-xls)
- [Python Как преобразовать PDF файл в XLS](#python-pdf-to-xls)

_Формат_: **XLSX**

- [Python PDF в XLSX](#python-pdf-to-xlsx)
- [Python Преобразование PDF в XLSX](#python-pdf-to-xlsx)
- [Python Как преобразовать PDF файл в XLSX](#python-pdf-to-xlsx)

_Формат_: **Excel**

- [Python PDF to Excel](#python-pdf-to-xlsx)
- [Python PDF to Excel XLS](#python-pdf-to-xls)
- [Python PDF to Excel XLSX](#python-pdf-to-xlsx)

_Формат_: **CSV**

- [Python PDF в CSV](#python-pdf-to-csv)
- [Python Конвертировать PDF в CSV](#python-pdf-to-csv)
- [Python Как конвертировать PDF файл в CSV](#python-pdf-to-csv)

_Формат_: **ODS**

- [Python PDF в ODS](#python-pdf-to-ods)
- [Python Конвертировать PDF в ODS](#python-pdf-to-ods)
- [Python Как конвертировать PDF файл в ODS](#python-pdf-to-ods)

## Конвертация PDF в EXCEL с помощью Python

**Aspose.PDF for Python via .NET** поддерживает возможность конвертации PDF файлов в форматы Excel и CSV.

Aspose.PDF for Python via .NET — это компонент для работы с PDF, мы внедрили функцию, которая преобразует PDF файл в рабочую книгу Excel (файлы XLSX). Во время этой конвертации отдельные страницы PDF файла преобразуются в листы Excel.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в Excel онлайн**

Aspose.PDF предлагает вам бесплатное онлайн-приложение ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Преобразование PDF в Excel с бесплатным приложением](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

Следующий фрагмент кода показывает процесс преобразования PDF файла в формат XLS или XLSX с использованием Aspose.PDF для Python через .NET.

<a name="python-pdf-to-xls"><strong>Шаги: Конвертация PDF в XLS на Python</strong></a>

1. Создайте экземпляр объекта [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) с исходным PDF документом.
2. Создайте экземпляр [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
3. Сохраните в формате **XLS**, указав **расширение .xls** с помощью вызова метода [Document.Save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) и передачи ему [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xls.xls"
    # Открыть PDF документ
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003

    # Сохранить файл в формате MS Excel
    document.save(output_pdf, save_option)
```


<a name="python-pdf-to-xlsx"><strong>Шаги: Преобразование PDF в XLSX на Python</strong></a>

1. Создайте экземпляр объекта [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) с исходным PDF-документом.
2. Создайте экземпляр [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
3. Сохраните его в формате **XLSX**, указав **расширение .xlsx**, вызвав метод [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) и передав ему [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_xlsx.xlsx"
    # Открыть PDF-документ
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()

    # Сохранить файл в формате MS Excel
    document.save(output_pdf, save_option)
```

## Преобразование PDF в XLS с управлением колонкой

При преобразовании PDF в формат XLS в выходной файл добавляется пустая колонка в качестве первой колонки.
 В классе 'ExcelSaveOptions' опция InsertBlankColumnAtFirst используется для управления этим столбцом. Значение по умолчанию — true.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xlsx_with_control_column.xls"
    # Открыть PDF документ
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003
    save_option.insert_blank_column_at_first = True

    # Сохранить файл в формате MS Excel
    document.save(output_pdf, save_option)
```

## Конвертировать PDF в один лист Excel

При экспорте PDF файла с большим количеством страниц в XLS, каждая страница экспортируется на отдельный лист в файле Excel. Это происходит потому, что свойство MinimizeTheNumberOfWorksheets по умолчанию установлено в false. Чтобы все страницы были экспортированы на один лист в выходном файле Excel, установите свойство MinimizeTheNumberOfWorksheets в true.

<a name="python-pdf-to-excel-single"><strong>Шаги: Конвертировать PDF в один лист XLS или XLSX в Python</strong></a>
1. Создайте экземпляр объекта [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) с исходным PDF-документом.
2. Создайте экземпляр [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) с **MinimizeTheNumberOfWorksheets = true**.
3. Сохраните его в формате **XLS** или **XLSX** с одним листом, вызвав метод [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) и передав ему [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "many_pages.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xlsx_single_excel_worksheet.xls"
    # Открыть PDF-документ
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003
    save_option.minimize_the_number_of_worksheets = True

    # Сохранить файл в формате MS Excel
    document.save(output_pdf, save_option)

```


## Конвертация в другие форматы электронных таблиц

### Конвертация в CSV

Конвертация в формат CSV выполняется так же, как и выше. Все, что нужно - установить соответствующий формат.

<a name="python-pdf-to-csv"><strong>Шаги: Конвертация PDF в CSV на Python</strong></a>

1. Создайте экземпляр объекта [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) с исходным PDF-документом.
2. Создайте экземпляр [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) с **Format = ExcelSaveOptions.ExcelFormat.CSV**
3. Сохраните его в формате **CSV**, вызвав метод [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) и передав ему [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_csv.csv"
    # Открыть PDF-документ
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.CSV

    # Сохранить файл
    document.save(output_pdf, save_option)
```


### Преобразование в ODS

<a name="python-pdf-to-ods"><strong>Шаги: Преобразование PDF в ODS на Python</strong></a>

1. Создайте экземпляр объекта [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) с исходным PDF-документом.
2. Создайте экземпляр [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) с **Format = ExcelSaveOptions.ExcelFormat.ODS**
3. Сохраните в формате **ODS**, вызвав метод [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) и передав в него [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

Преобразование в формат ODS выполняется так же, как и во все остальные форматы.

```python

    import aspose.pdf as ap
    
    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_ods.ods"
    # Открыть PDF-документ
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.ODS

    # Сохранить файл
    document.save(output_pdf, save_option)
```


## См. также

Эта статья также охватывает следующие темы. Коды такие же, как и выше.

_Формат_: **Excel**
- [Python PDF в Excel Код](#python-pdf-to-xlsx)
- [Python PDF в Excel API](#python-pdf-to-xlsx)
- [Python PDF в Excel Программно](#python-pdf-to-xlsx)
- [Python PDF в Excel Библиотека](#python-pdf-to-xlsx)
- [Python Сохранить PDF как Excel](#python-pdf-to-xlsx)
- [Python Генерация Excel из PDF](#python-pdf-to-xlsx)
- [Python Создать Excel из PDF](#python-pdf-to-xlsx)
- [Python Конвертер PDF в Excel](#python-pdf-to-xlsx)

_Формат_: **XLS**
- [Python PDF в XLS Код](#python-pdf-to-xls)
- [Python PDF в XLS API](#python-pdf-to-xls)
- [Python PDF в XLS Программно](#python-pdf-to-xls)
- [Python PDF в XLS Библиотека](#python-pdf-to-xls)
- [Python Сохранить PDF как XLS](#python-pdf-to-xls)
- [Python Генерация XLS из PDF](#python-pdf-to-xls)
- [Python Создать XLS из PDF](#python-pdf-to-xls)
- [Python Конвертер PDF в XLS](#python-pdf-to-xls)

_Формат_: **XLSX**

- [Python PDF в XLSX Код](#python-pdf-to-xlsx)
- [Python PDF to XLSX API](#python-pdf-to-xlsx)
- [Python PDF to XLSX Programmatically](#python-pdf-to-xlsx)
- [Python PDF to XLSX Library](#python-pdf-to-xlsx)
- [Python Save PDF as XLSX](#python-pdf-to-xlsx)
- [Python Generate XLSX from PDF](#python-pdf-to-xlsx)
- [Python Create XLSX from PDF](#python-pdf-to-xlsx)
- [Python PDF to XLSX Converter](#python-pdf-to-xlsx)

_Формат_: **CSV**
- [Python PDF to CSV Code](#python-pdf-to-csv)
- [Python PDF to CSV API](#python-pdf-to-csv)
- [Python PDF to CSV Programmatically](#python-pdf-to-csv)
- [Python PDF to CSV Library](#python-pdf-to-csv)
- [Python Save PDF as CSV](#python-pdf-to-csv)
- [Python Generate CSV from PDF](#python-pdf-to-csv)
- [Python Create CSV from PDF](#python-pdf-to-csv)
- [Python PDF to CSV Converter](#python-pdf-to-csv)

_Формат_: **ODS**
- [Python PDF to ODS Code](#python-pdf-to-ods)
- [Python PDF to ODS API](#python-pdf-to-ods)
- [Python PDF to ODS Programmatically](#python-pdf-to-ods)
- [Python PDF to ODS Library](#python-pdf-to-ods)

- [Python Save PDF as ODS](#python-pdf-to-ods)
- [Python Генерация ODS из PDF](#python-pdf-to-ods)
- [Python Создание ODS из PDF](#python-pdf-to-ods)
- [Python Конвертер PDF в ODS](#python-pdf-to-ods)
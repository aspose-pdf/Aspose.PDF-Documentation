---
title: Преобразование PDF в Excel на Python
linktitle: Преобразование PDF в Excel
type: docs
weight: 20
url: ru/python-java/convert-pdf-to-excel/
lastmod: "2022-12-23"
keywords: преобразование PDF в Excel с использованием python, преобразование PDF в XLS с использованием python, преобразование PDF в XLSX с использованием python, экспорт таблицы из PDF в Excel на python.
description: Библиотека Aspose.PDF для Python позволяет преобразовывать PDF в формат Excel с использованием Python. Эти форматы включают XLS, XLSX, XML 2003 Spreadsheet, CSV, ODS.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Обзор

Эта статья объясняет, как **преобразовывать PDF в форматы Excel с использованием Python**. Она охватывает следующие темы.

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
- [Python PDF to CSV](#python-pdf-to-csv)
- [Python Convert PDF to CSV](#python-pdf-to-csv)
- [Python How to convert PDF file to CSV](#python-pdf-to-csv)

_Формат_: **ODS**
- [Python PDF to ODS](#python-pdf-to-ods)
- [Python Convert PDF to ODS](#python-pdf-to-ods)
- [Python How to convert PDF file to ODS](#python-pdf-to-ods)

## Конвертация PDF в EXCEL с помощью Python

**Aspose.PDF для Python через .NET** поддерживает возможность конвертации PDF файлов в форматы Excel и CSV.

Aspose.PDF для Python через Java - это компонент для работы с PDF, и мы внедрили функцию, которая преобразует PDF файл в книгу Excel (XLSX файлы). Во время этого преобразования отдельные страницы PDF файла преобразуются в листы Excel.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в Excel онлайн**

Aspose.PDF предлагает вам бесплатное онлайн-приложение ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в Excel с бесплатным приложением](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

Следующий фрагмент кода показывает процесс преобразования PDF файла в формат XLS или XLSX с использованием Aspose.PDF для Python через Java.

<a name="python-pdf-to-xls"><strong>Шаги: Преобразование PDF в XLS на Python</strong></a>

1. Создайте экземпляр объекта [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) с исходным PDF документом.
2. Создайте экземпляр [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).
3. Сохраните его в формате **XLS**, указав **расширение .xls**, вызвав метод [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) и передав ему [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).

```python

from asposepdf import Api

# инициализация лицензии
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

# конвертация из массива байтов
documentName = "testdata/source.pdf"
with open(documentName, "rb") as file:
    byte_array = file.read()
doc = Api.Document(byte_array)
documentOutName = "testout/result1.xls"
doc.save(documentOutName, Api.SaveFormat.Excel)

# конвертация из файла
documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result2.xls"
doc.save(documentOutName, Api.SaveFormat.Excel)

# конвертация из массива байтов
documentName = "testdata/source.pdf"
with open(documentName, "rb") as file:
    byte_array = file.read()
doc = Api.Document(byte_array)
documentOutName = "testout/result3.xls"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
doc.save(documentOutName, Api.SaveFormat.Excel)

# конвертация из файла
documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result4.xls"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
doc.save(documentOutName, Api.SaveFormat.Excel)
```


<a name="python-pdf-to-xlsx"><strong>Шаги: Конвертация PDF в XLSX на Python</strong></a>

1. Создайте экземпляр объекта [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) с исходным PDF документом.
2. Создайте экземпляр [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).
3. Сохраните его в формате **XLSX**, указав **расширение .xlsx**, вызвав метод [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) и передав ему [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).

```python

from asposepdf import Api

documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result.xlsx"
doc.save(documentOutName, save_option)
```

## Конвертация PDF в XLS с контролем столбца

При конвертации PDF в формат XLS в выходной файл добавляется пустой столбец в качестве первого столбца.
 The in 'ExcelSaveOptions class' параметр InsertBlankColumnAtFirst используется для управления этим столбцом. Значение по умолчанию — true.

```python

from asposepdf import Api

documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result.xlsx"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
save_option._insertBlankColumnAtFirst = True
doc.save(documentOutName, save_option)

```

## Конвертация PDF в один лист Excel

При экспорте PDF-файла с большим количеством страниц в XLS каждая страница экспортируется на отдельный лист в файле Excel. Это происходит потому, что свойство MinimizeTheNumberOfWorksheets по умолчанию установлено в false. Чтобы все страницы экспортировались на один лист в выходном файле Excel, установите свойство MinimizeTheNumberOfWorksheets в true.

<a name="python-pdf-to-excel-single"><strong>Шаги: Конвертация PDF в один лист XLS или XLSX в Python</strong></a>
1. Создайте экземпляр объекта [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) с исходным PDF-документом.
2. Создайте экземпляр [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/) с **MinimizeTheNumberOfWorksheets = True**.
3. Сохраните его в формате **XLS** или **XLSX** с одним листом, вызвав метод [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) и передав ему [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).

```python

from asposepdf import Api

documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result.xls"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
save_option._minimizeTheNumberOfWorksheets = True
# Сохраните файл в формате MS Excel
doc.save(documentOutName, save_option)

```

## Конвертация в другие форматы электронных таблиц

### Конвертация в CSV

Преобразование в формат CSV выполняется так же, как и выше. Все, что вам нужно - установить соответствующий формат.

<a name="python-pdf-to-csv"><strong>Шаги: Конвертация PDF в CSV в Python</strong></a>

1. Создайте экземпляр объекта [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) с исходным PDF документом.
2. Создайте экземпляр [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/) с **Format = ExcelSaveOptions.ExcelFormat.CSV**
3. Сохраните в формате **CSV**, вызвав метод [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) и передав ему [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).

```python

from asposepdf import Api

documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result.csv"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.CSV
doc.save(documentOutName, save_option)
```


### Преобразование в ODS

<a name="python-pdf-to-ods"><strong>Шаги: Преобразование PDF в ODS на Python</strong></a>

1. Создайте экземпляр объекта [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) с исходным PDF-документом.
2. Создайте экземпляр [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/) с **Format = ExcelSaveOptions.ExcelFormat.ODS**
3. Сохраните его в формате **ODS**, вызвав метод [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) и передав ему [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).

Преобразование в формат ODS выполняется так же, как и все другие форматы.

```python

from asposepdf import Api

documentName = "../../testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "../../testout/result1.ods"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.ODS
doc.save(documentOutName, save_option)
```


## См. Также

Эта статья также охватывает следующие темы. Коды такие же, как выше.

_Формат_: **Excel**
- [Python PDF в Excel Код](#python-pdf-to-xlsx)
- [Python PDF в Excel API](#python-pdf-to-xlsx)
- [Python PDF в Excel Программно](#python-pdf-to-xlsx)
- [Python PDF в Excel Библиотека](#python-pdf-to-xlsx)
- [Python Сохранить PDF как Excel](#python-pdf-to-xlsx)
- [Python Генерация Excel из PDF](#python-pdf-to-xlsx)
- [Python Создать Excel из PDF](#python-pdf-to-xlsx)
- [Python PDF в Excel Конвертер](#python-pdf-to-xlsx)

_Формат_: **XLS**
- [Python PDF в XLS Код](#python-pdf-to-xls)
- [Python PDF в XLS API](#python-pdf-to-xls)
- [Python PDF в XLS Программно](#python-pdf-to-xls)
- [Python PDF в XLS Библиотека](#python-pdf-to-xls)
- [Python Сохранить PDF как XLS](#python-pdf-to-xls)
- [Python Генерация XLS из PDF](#python-pdf-to-xls)
- [Python Создать XLS из PDF](#python-pdf-to-xls)
- [Python PDF в XLS Конвертер](#python-pdf-to-xls)

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
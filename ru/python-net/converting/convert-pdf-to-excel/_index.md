---
title: Конвертировать PDF в Excel с помощью Python
linktitle: Конвертировать PDF в Excel
type: docs
weight: 20
url: /ru/python-net/convert-pdf-to-excel/
lastmod: "2026-04-14"
description: Узнайте, как конвертировать PDF в Excel на Python, включая XLS, XLSX, CSV, ODS, вывод в один лист и обработку столбцов с помощью Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Конвертировать PDF в Excel, XLSX, CSV и ODS на Python
Abstract: Эта статья показывает, как конвертировать файлы PDF в форматы электронных таблиц с использованием Aspose.PDF for Python via .NET. Она охватывает вывод в форматы XLS, XLSX, XLSM, CSV и ODS, а также параметры для управления пустыми столбцами и уменьшения количества создаваемых листов.
---

## Конвертировать PDF в Excel с помощью Python

**Aspose.PDF for Python via .NET** поддерживает конвертирование PDF‑файлов в Excel и другие форматы электронных таблиц из кода Python.

Используйте эту страницу, когда нужно конвертировать PDF в XLS, XLSX, CSV или ODS для извлечения таблиц, повторного использования отчётов, сортировки, фильтрации или последующего анализа. При конвертации PDF в Excel отдельные страницы PDF могут быть отображены как листы Excel.

Первый пример преобразует PDF‑файл в формат Spreadsheet 2003 XML. В последующих разделах показаны форматы XLSX, XLSM, CSV, ODS и вывод в виде одного листа.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в Excel онлайн**

Aspose.PDF представляет вам онлайн‑приложение ["PDF в XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), где вы можете попытаться исследовать работу функциональности и качества.

[![Aspose.PDF Конвертация PDF в Excel с приложением](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

Следующий фрагмент кода показывает процесс преобразования PDF‑файла в формат XLS или XLSX с помощью Aspose.PDF for Python via .NET.

Шаги: Преобразовать файл PDF в формат Excel (XML Spreadsheet 2003)

1. Загрузите PDF‑документ.
1. Настройте параметры сохранения Excel, используя [ПараметрыСохраненияExcel](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. Сохраните преобразованный файл.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_spread_sheet2003(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Преобразовать PDF в XLSX с помощью Python

Шаги: Преобразовать файл PDF в формат XLSX (Excel 2007+)

1. Загрузите PDF‑документ.
1. Настройте параметры сохранения Excel, используя [ПараметрыСохраненияExcel](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. Сохраните преобразованный файл.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XLSX
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Конвертировать PDF в XLSX с управлением столбцами

При конвертации PDF в формат Excel в выходной файл может быть добавлена пустая колонка в качестве первой колонки. Используйте `insert_blank_column_at_first` вариант `ExcelSaveOptions` класс для управления этим поведением. Его значение по умолчанию — `true`.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007_control_column(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XLSX
    save_options.insert_blank_column_at_first = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Преобразовать PDF в один лист Excel

Aspose.PDF for Python via .NET показывает, как преобразовать PDF в файл Excel (.xlsx) с включённой опцией 'minimize_the_number_of_worksheets'.

Шаги: Конвертировать PDF в XLS или XLSX в один лист в Python

1. Загрузите PDF‑документ.
1. Настройте параметры сохранения Excel, используя [ПараметрыСохраненияExcel](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. Опция 'minimize_the_number_of_worksheets' уменьшает количество листов Excel, объединяя страницы PDF в меньшее число листов (например, один лист для всего документа, если это возможно).
1. Сохраните преобразованный файл.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007_single_excel_worksheet(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XLSX
    save_options.minimize_the_number_of_worksheets = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Преобразовать PDF в Excel 2007 с поддержкой макросов (XLSM)

Этот пример на Python показывает, как преобразовать файл PDF в файл Excel в формате XLSM (рабочая книга Excel с поддержкой макросов).

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007_macro(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XLSM
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Преобразовать в другие форматы электронных таблиц

### Преобразовать PDF в CSV

Функция 'convert_pdf_to_excel_2007_csv' выполняет ту же операцию, что и ранее, но на этот раз целевой формат — CSV (Comma-Separated Values), а не XLSM.

Шаги: конвертировать PDF в CSV в Python

1. Создайте экземпляр [Документ](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) объект с исходным PDF документом.
1. Создайте экземпляр [ПараметрыСохраненияExcel](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) с **ExcelSaveOptions.ExcelFormat.CSV**
1. Сохраните его в формате **CSV**, вызвав [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)* метод и его передачу [ПараметрыСохраненияExcel](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007_csv(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.CSV
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Преобразовать PDF в ODS

Шаги: Конвертировать PDF в ODS в Python

1. Создайте экземпляр [Документ](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) объект с исходным PDF документом.
1. Создайте экземпляр [ПараметрыСохраненияExcel](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) с **ExcelSaveOptions.ExcelFormat.ODS**
1. Сохраните его в формате **ODS**, вызвав [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) метод и передача его [ПараметрыСохраненияExcel](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

Конвертация в формат ODS выполняется так же, как и все остальные форматы.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_ods(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.ODS
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Связанные преобразования

- [Конвертировать PDF в Word](/pdf/ru/python-net/convert-pdf-to-word/) если ваш приоритет — редактируемый поток текста, а не структура таблицы.
- [Преобразовать PDF в HTML](/pdf/ru/python-net/convert-pdf-to-html/) когда вам нужен вывод, удобный для браузера.
- [Преобразовать PDF в другие форматы](/pdf/ru/python-net/convert-pdf-to-other-files/) для EPUB, Markdown, текста, XPS и связанных процессов экспорта.

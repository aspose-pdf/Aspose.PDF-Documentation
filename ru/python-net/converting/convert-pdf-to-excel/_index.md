---
title: Конвертировать PDF в Excel с помощью Python
linktitle: Конвертировать PDF в Excel
type: docs
weight: 20
url: /python-net/convert-pdf-to-excel/
lastmod: "2026-04-14"
description: Узнайте, как конвертировать PDF-файлы в Excel в Python с помощью Aspose.PDF for Python via .NET, включая XLS, XLSX, CSV, ODS и вывод в виде одного листа.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Как конвертировать PDF в Excel в Python
Abstract: В этой статье представлен всесторонний руководитель по конвертации PDF‑файлов в различные форматы Excel с использованием Python, конкретно с библиотекой Aspose.PDF for Python via .NET. Описываются процессы преобразования в форматы XLS, XLSX, CSV и ODS. Документ объясняет шаги, необходимые для конвертации PDF в XLS и XLSX, выделяя создание экземпляров Document и ExcelSaveOptions, а также использование метода Document.Save() для указания выходных форматов. В статье также рассматриваются такие возможности, как контроль вставки пустых столбцов и уменьшение количества листов во время конвертации. Кроме того, приводятся примеры преобразования PDF в отдельные листы Excel и другие форматы, такие как CSV и ODS, подчёркивая гибкость и функциональность Aspose.PDF. Также упоминается онлайн‑инструмент для конвертации PDF в XLSX, позволяющий пользователям оценить качество преобразования. В заключении статьи приведён список связанных тем и фрагменты кода, помогающие лучше понять и реализовать эти конвертации программно.
---

## Конвертировать PDF в Excel (Spreadsheet 2003 XML)

**Aspose.PDF for Python via .NET** поддерживает возможность конвертации PDF‑файлов в форматы Excel и CSV.

Aspose.PDF for Python via .NET — это компонент для работы с PDF, мы внедрили функцию, которая преобразует PDF‑файл в рабочую книгу Excel (файлы XLSX). Во время этого преобразования отдельные страницы PDF‑файла конвертируются в листы Excel.

Используйте эту страницу, когда вам необходимо извлекать содержимое PDF, ориентированное на таблицы или в виде отчётов, в форматы таблиц для сортировки, фильтрации или последующего анализа.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в Excel онлайн**

Aspose.PDF представляет вам онлайн‑приложение ["PDF в XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), где вы можете попытаться исследовать его функциональность и качество работы.

[![Aspose.PDF Преобразование PDF в Excel с приложением](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

Следующий фрагмент кода демонстрирует процесс преобразования PDF‑файла в формат XLS или XLSX с помощью Aspose.PDF for Python via .NET.

Шаги: Преобразовать PDF‑файл в формат Excel (XML Spreadsheet 2003)

1. Загрузите PDF‑документ.
1. Настройте параметры сохранения Excel с помощью [ПараметрыСохраненияExcel](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. Сохранить преобразованный файл.

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

## Конвертировать PDF в Excel 2007+ (XLSX)

Шаги: Конвертировать PDF‑файл в формат XLSX (Excel 2007+)

1. Загрузите PDF‑документ.
1. Настройте параметры сохранения Excel с помощью [ПараметрыСохраненияExcel](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. Сохранить преобразованный файл.

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

## Конвертировать PDF в XLS с контролем столбца

При конвертации PDF в формат XLS в выходной файл добавляется пустой столбец в качестве первого столбца. Опция 'insert_blank_column_at_first' в классе 'ExcelSaveOptions' используется для управления этим столбцом. Ее значение по умолчанию — true.

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

Aspose.PDF for Python via .NET демонстрирует, как конвертировать PDF в файл Excel (.xlsx), с включённым параметром ’minimize_the_number_of_worksheets’.

Шаги: Преобразовать PDF в XLS или XLSX в один лист с помощью Python

1. Загрузите PDF‑документ.
1. Настройте параметры сохранения Excel с помощью [ПараметрыСохраненияExcel](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. Опция 'minimize_the_number_of_worksheets' уменьшает количество листов Excel, объединяя страницы PDF в меньшее число листов (например, один лист для всего документа, если это возможно).
1. Сохранить преобразованный файл.

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

### Конвертировать PDF в CSV

Функция 'convert_pdf_to_excel_2007_csv' выполняет ту же операцию, что и раньше, но на этот раз целевой формат — CSV (значения, разделённые запятыми) вместо XLSM.

Шаги: Конвертировать PDF в CSV в Python

1. Создать экземпляр [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) объект с исходным PDF документом.
1. Создать экземпляр [ПараметрыСохраненияExcel](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) с **ExcelSaveOptions.ExcelFormat.CSV**
1. Сохраните его в формате **CSV**, вызвав [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)* метод и его передача [ПараметрыСохраненияExcel](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

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

### Конвертировать PDF в ODS

Шаги: Преобразовать PDF в ODS в Python

1. Создать экземпляр [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) объект с исходным PDF документом.
1. Создать экземпляр [ПараметрыСохраненияExcel](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) с **ExcelSaveOptions.ExcelFormat.ODS**
1. Сохраните его в формат **ODS**, вызывая [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) метод и передача его [ПараметрыСохраненияExcel](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

Преобразование в формат ODS происходит так же, как и все остальные форматы.

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

- [Конвертировать PDF в Word](/pdf/ru/python-net/convert-pdf-to-word/) если ваш приоритет — редактируемый поток текста, а не структура таблицы.
- [Преобразовать PDF в HTML](/pdf/ru/python-net/convert-pdf-to-html/) когда вам нужен вывод, пригодный для браузера.
- [Конвертировать PDF в другие форматы](/pdf/ru/python-net/convert-pdf-to-other-files/) для EPUB, Markdown, текста, XPS и связанных экспортных рабочих процессов.
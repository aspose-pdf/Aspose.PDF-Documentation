---
title: Конвертировать PDF в Excel с помощью Python
linktitle: Конвертировать PDF в Excel
type: docs
weight: 20
url: /ru/python-net/convert-pdf-to-excel/
lastmod: "2026-04-14"
description: Узнайте, как конвертировать PDF‑файлы в Excel в Python с помощью Aspose.PDF for Python via .NET, включая XLS, XLSX, CSV, ODS и вывод в виде одного листа.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как конвертировать PDF в Excel в Python
Abstract: Эта статья предоставляет исчерпывающее руководство по конвертации PDF‑файлов в различные форматы Excel с использованием Python, в частности с библиотекой Aspose.PDF for Python via .NET. В ней подробно описаны процессы преобразования в форматы XLS, XLSX, CSV и ODS. Документ объясняет шаги, необходимые для конвертации PDF в XLS и XLSX, выделяя создание экземпляров Document и ExcelSaveOptions, а также использование метода Document.Save() для указания форматов вывода. Статья также обсуждает такие возможности, как контроль вставки пустых столбцов и минимизация количества листов при конвертации. Кроме того, приводятся примеры преобразования PDF в отдельные листы Excel и в другие форматы, такие как CSV и ODS, подчеркивая гибкость и функциональность Aspose.PDF. Также упоминается онлайн‑инструмент для конвертации PDF в XLSX, позволяющий пользователям оценить качество преобразования. В заключении статья содержит список связанных тем и фрагменты кода, которые помогут лучше понять и реализовать эти конверсии программно.
---

## Конвертация PDF в EXCEL с помощью Python

**Aspose.PDF for Python via .NET** поддерживает возможность конвертации PDF‑файлов в форматы Excel и CSV.

Aspose.PDF for Python via .NET — это компонент для работы с PDF, мы внедрили функцию, которая преобразует PDF‑файл в рабочую книгу Excel (файлы XLSX). При этом преобразовании отдельные страницы PDF‑файла конвертируются в листы Excel.

Используйте эту страницу, когда вам нужно извлечь из PDF контент, ориентированный на таблицы или отчётный стиль, в форматы электронных таблиц для сортировки, фильтрации или последующего анализа.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в Excel онлайн**

Aspose.PDF представляет вам онлайн-приложение ["PDF в XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), где вы можете попытаться исследовать функциональность и качество, как это работает.

[![Aspose.PDF конвертация PDF в Excel с онлайн-приложением](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

Следующий фрагмент кода показывает процесс преобразования PDF‑файла в формат XLS или XLSX с помощью Aspose.PDF for Python via .NET.

Шаги: Конвертировать PDF‑файл в формат Excel (XML Spreadsheet 2003)

1. Загрузите PDF‑документ.
1. Настройте параметры сохранения Excel с помощью [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. Сохраните конвертированный файл.

```python
from os import path
import aspose.pdf as apdf

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

document = apdf.Document(path_infile)
save_options = apdf.ExcelSaveOptions()
save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003
document.save(path_outfile, save_options)

print(infile + " converted into " + outfile)
```

## Связанные преобразования

- [Преобразовать PDF в Word](/pdf/ru/python-net/convert-pdf-to-word/) если ваш приоритет — редактируемый поток текста, а не структура таблицы.
- [Конвертировать PDF в HTML](/pdf/ru/python-net/convert-pdf-to-html/) когда вам нужен вывод, совместимый с браузером.
- [Конвертировать PDF в другие форматы](/pdf/ru/python-net/convert-pdf-to-other-files/) для EPUB, Markdown, текста, XPS и связанных процессов экспорта.

Шаги: Конвертировать PDF‑файл в формат XLSX (Excel 2007+)

1. Загрузите PDF‑документ.
1. Настройте параметры сохранения Excel с помощью [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. Сохраните конвертированный файл.

```python
from os import path
import aspose.pdf as apdf

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

document = apdf.Document(path_infile)
save_options = apdf.ExcelSaveOptions()
save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XLSX
document.save(path_outfile, save_options)

print(infile + " converted into " + outfile)
```

## Преобразовать PDF в XLS с контролем столбца

При конвертировании PDF в формат XLS в выходной файл добавляется пустой столбец в качестве первого столбца. В классе 'ExcelSaveOptions' опция 'insert_blank_column_at_first' используется для управления этим столбцом. Ее значение по умолчанию — true.

```python
from os import path
import aspose.pdf as apdf

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

document = apdf.Document(path_infile)
save_options = apdf.ExcelSaveOptions()
save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XLSX
save_options.insert_blank_column_at_first = True
document.save(path_outfile, save_options)

print(infile + " converted into " + outfile)
```

## Конвертировать PDF в один лист Excel

Aspose.PDF for Python via .NET показывает, как преобразовать PDF в файл Excel (.xlsx) с включённой опцией 'minimize_the_number_of_worksheets'.

Шаги: Конвертировать PDF в XLS или XLSX в один рабочий лист в Python

1. Загрузите PDF‑документ.
1. Настройте параметры сохранения Excel с помощью [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. Опция 'minimize_the_number_of_worksheets' уменьшает количество листов Excel, объединяя страницы PDF в меньшее количество листов (например, один лист для всего документа, если это возможно).
1. Сохраните конвертированный файл.

```python
from os import path
import aspose.pdf as apdf

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

document = apdf.Document(path_infile)
save_options = apdf.ExcelSaveOptions()
save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XLSX
save_options.minimize_the_number_of_worksheets = True
document.save(path_outfile, save_options)

print(infile + " converted into " + outfile)
```

## Преобразовать PDF‑файл в файл Excel в формате XLSM

Этот пример на Python показывает, как преобразовать файл PDF в Excel‑файл формата XLSM (рабочая книга Excel с поддержкой макросов).

```python
from os import path
import aspose.pdf as apdf

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

document = apdf.Document(path_infile)
save_options = apdf.ExcelSaveOptions()
save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XLSM
document.save(path_outfile, save_options)
print(infile + " converted into " + outfile)
```

## Преобразовать в другие форматы электронных таблиц

### Конвертировать в CSV

Функция 'convert_pdf_to_excel_2007_csv' выполняет ту же операцию, что и ранее, но на этот раз целевой формат — CSV (значения, разделённые запятыми) вместо XLSM.

Шаги: Преобразовать PDF в CSV на Python

1. Создайте экземпляр [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) объект с исходным PDF-документом.
1. Создайте экземпляр [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) с **ExcelSaveOptions.ExcelFormat.CSV**
1. Сохраните его в формате **CSV**, вызвав [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)* метод и передача его [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

```python
from os import path
import aspose.pdf as apdf


def convert_pdf_to_excel_2007_csv(infile, outfile):
    path_infile = path.join(data_dir, infile)
    path_outfile = path.join(data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.CSV
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Конвертировать в ODS

Шаги: Конвертировать PDF в ODS в Python

1. Создайте экземпляр [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) объект с исходным PDF-документом.
1. Создайте экземпляр [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) с **ExcelSaveOptions.ExcelFormat.ODS**
1. Сохраните его в формат **ODS**, вызвав [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) метод и его передача [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

Преобразование в формат ODS выполняется так же, как и все остальные форматы.

```python
from os import path
import aspose.pdf as apdf

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

document = apdf.Document(path_infile)
save_options = apdf.ExcelSaveOptions()
save_options.format = apdf.ExcelSaveOptions.ExcelFormat.ODS
document.save(path_outfile, save_options)

print(infile + " converted into " + outfile)
```

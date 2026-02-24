---
title: Конвертировать PDF в Excel на Python
linktitle: Конвертировать PDF в Excel
type: docs
weight: 20
url: /ru/python-net/convert-pdf-to-excel/
lastmod: "2025-09-27"
description: Легко конвертировать PDF в электронные таблицы Excel с помощью Aspose.PDF for Python via .NET. Следуйте этому руководству для точного преобразования PDF в XLSX.
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как конвертировать PDF в Excel на Python
Abstract: Эта статья предоставляет всестороннее руководство по конвертации PDF‑файлов в различные форматы Excel с использованием Python, в частности с библиотекой Aspose.PDF for Python via .NET. Она подробно описывает процессы конвертации в форматы XLS, XLSX, CSV и ODS. Документ объясняет шаги, необходимые для преобразования PDF в XLS и XLSX, подчеркивая создание экземпляров Document и ExcelSaveOptions, а также использование метода Document.Save() для указания выходного формата. В статье также рассматриваются функции, такие как управление вставкой пустых колонок и минимизация количества листов при конвертации. Кроме того, приводятся примеры конвертации PDF в отдельные листы Excel и другие форматы, например CSV и ODS, подчёркивающие гибкость и функциональность Aspose.PDF. Упоминается онлайн‑инструмент для конвертации PDF в XLSX, позволяющий пользователям оценить качество преобразования. Статья завершается перечнем связанных тем и фрагментами кода для дальнейшего понимания и реализации этих конвертаций программно.
---

## Конвертация PDF в EXCEL с помощью Python

**Aspose.PDF for Python via .NET** поддерживает функцию конвертации PDF‑файлов в Excel и CSV форматы.

Aspose.PDF for Python via .NET является компонентом манипуляции PDF, мы добавили функцию, которая преобразует PDF‑файл в книгу Excel (файлы XLSX). При этом отдельные страницы PDF‑файла конвертируются в листы Excel.

{{% alert color="success" %}}
**Попробовать конвертировать PDF в Excel онлайн**

 Aspose.PDF предлагает вам бесплатное онлайн‑приложение ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), где вы можете протестировать его функциональность и качество.

[![Aspose.PDF Конвертация PDF в Excel с бесплатным приложением](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

Следующий фрагмент кода показывает процесс конвертации PDF‑файла в формат XLS или XLSX с помощью Aspose.PDF for Python via .NET.

Шаги: Конвертировать PDF‑файл в формат Excel (XML Spreadsheet 2003)

1. Загрузите PDF‑документ.
1. Настройте параметры сохранения Excel, используя [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
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

Шаги: Конвертировать PDF‑файл в формат XLSX (Excel 2007+)

1. Загрузите PDF‑документ.
1. Настройте параметры сохранения Excel, используя [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
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

## Конвертировать PDF в XLS с управлением колонкой

При конвертации PDF в формат XLS в выходной файл добавляется пустая колонка в качестве первой. В классе 'ExcelSaveOptions' параметр 'insert_blank_column_at_first' используется для управления этой колонкой. Его значение по умолчанию — true.

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

## Конвертировать PDF в единственный лист Excel

Aspose.PDF for Python via .NET показывает, как конвертировать PDF в файл Excel (.xlsx) с включённым параметром 'minimize_the_number_of_worksheets'.

Шаги: Конвертировать PDF в один лист XLS или XLSX в Python

1. Загрузите PDF‑документ.
1. Настройте параметры сохранения Excel, используя [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. Параметр 'minimize_the_number_of_worksheets' уменьшает количество листов Excel, объединяя страницы PDF в меньшее число листов (например, один лист для всего документа, если возможно).
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

## Конвертировать PDF‑файл в файл Excel в формате XLSM

Этот пример на Python показывает, как конвертировать PDF‑файл в файл Excel в формате XLSM (Excel Macro-Enabled Workbook).

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

## Конвертировать в другие форматы таблиц

### Конвертировать в CSV

Функция 'convert_pdf_to_excel_2007_csv' выполняет ту же операцию, что и ранее, но теперь целевой формат — CSV (значения, разделённые запятыми) вместо XLSM.

Шаги: Конвертировать PDF в CSV в Python

1. Создайте экземпляр объекта [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) с исходным PDF‑документом.
1. Создайте экземпляр [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) с **ExcelSaveOptions.ExcelFormat.CSV**
1. Сохраните его в формат **CSV**, вызвав метод [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)* и передав в него [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

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

1. Создайте экземпляр объекта [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) с исходным PDF‑документом.
1. Создайте экземпляр [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) с **ExcelSaveOptions.ExcelFormat.ODS**
1. Сохраните его в формат **ODS**, вызвав метод [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) и передав ему [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

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


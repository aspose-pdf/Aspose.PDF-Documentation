---
title: Интегрировать таблицу с источниками данных PDF
linktitle: Интегрировать таблицу
type: docs
weight: 30
url: /ru/python-net/integrate-table/
description: Узнайте, как интегрировать PDF‑таблицы с источниками данных, такими как базы данных и pandas DataFrames, на Python.
lastmod: "2026-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Интегрировать PDF‑таблицы с базами данных и DataFrames с помощью Python
Abstract: В этой статье объясняется, как интегрировать PDF‑таблицы с внешними источниками данных с использованием Aspose.PDF for Python via .NET. Узнайте, как создавать PDF‑таблицы из pandas DataFrames и других структурированных источников, вставлять их в документы и управлять потоками таблиц при рендеринге на несколько страниц PDF в Python.
---

## Создать PDF из DataFrame

Функция 'create_pdf_from_dataframe' принимает DataFrame и преобразует его в таблицу внутри нового PDF. Она создаёт новый PDF‑документ, добавляет страницу, генерирует таблицу из DataFrame (используя вспомогательный метод) и сохраняет результат по указанному пути к файлу. И это не только возможно, но и очень просто.

Используйте эту страницу, когда вам нужно создавать таблицы PDF из данных приложения, структурированных наборов данных или конвейеров отчётов в Python.

1. Инициализирует пустой PDF‑документ с помощью 'ap.Document()'.
1. Функция 'self.create_table_from_dataframe(df, max_rows)' преобразует DataFrame в объект таблицы Aspose.PDF.
1. Вставьте таблицу на страницу PDF. Добавляет сгенерированную таблицу в содержимое первой страницы (page.paragraphs.add(table)).
1. Сохраните PDF‑документ.

```python
from os import path
import sys

import pandas as pd
import aspose.pdf as ap
from config import set_license, initialize_data_dir

def create_pdf_from_dataframe(
    outfile: str, df: pd.DataFrame, max_rows: int = 20
) -> None:
    # Create new PDF document
    document = ap.Document()
    page = document.pages.add()

    table = create_table_from_dataframe(df, max_rows)

    # Add table object to first page of input document
    page.paragraphs.add(table)
    document.save(outfile)
```

## Создать таблицу из DataFrame

Этот код преобразует DataFrame в объект Table библиотеки Aspose.PDF. Он настраивает границы таблицы, добавляет строку заголовка с именами столбцов и заполняет таблицу первыми max_rows строками из DataFrame. Полученная Table затем можно добавить в PDF‑документ.

1. Создаёт пустой объект 'ap.Table()'.
1. Установить границу таблицы.
1. Установить границу ячейки по умолчанию.
1. Добавить строку заголовка.
1. Добавить строки данных.
1. Вернуть таблицу.

```python
from os import path
import sys

import pandas as pd
import aspose.pdf as ap
from config import set_license, initialize_data_dir

def create_table_from_dataframe(df: pd.DataFrame, max_rows: int = 20) -> ap.Table:
    """Create an Aspose.PDF table from a pandas DataFrame."""
    # Initializes a new instance of the Table
    table = ap.Table()
    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1, ap.Color.light_gray)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.BOTTOM, 1, ap.Color.light_gray
    )

    # Add header row with column names
    header_row = table.rows.add()
    header_row.is_row_broken = False  # Prevent header row from being split across pages
    for column_name in df.columns:
        cell = header_row.cells.add(str(column_name))
        cell.background_color = ap.Color.light_gray

    # Add data rows
    for row_data in df.head(max_rows).itertuples(index=False):
        row = table.rows.add()
        for value in row_data:
            row.cells.add(str(value))

    return table
```

## Связанные темы таблицы

- [Работа с таблицами в PDF с использованием Python](/pdf/ru/python-net/working-with-tables/)
- [Добавить таблицы в PDF с помощью Python](/pdf/ru/python-net/adding-tables/)
- [Извлекать таблицы из PDF‑документов](/pdf/ru/python-net/extracting-table/)
- [Манипулировать таблицами в существующих PDF](/pdf/ru/python-net/manipulating-tables/)
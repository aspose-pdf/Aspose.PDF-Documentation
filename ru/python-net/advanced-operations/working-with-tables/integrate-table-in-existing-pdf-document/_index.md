---
title: Интеграция таблицы с источниками данных PDF
linktitle: Интегрировать таблицу
type: docs
weight: 30
url: /ru/python-net/integrate-table/
description: В этой статье показано, как интегрировать таблицы PDF. Интегрировать таблицу с базой данных и определить, будет ли таблица разбиваться на текущей странице.
lastmod: "2025-09-17"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## Создать PDF из DataFrame

Функция 'create_pdf_from_dataframe' принимает DataFrame и преобразует его в таблицу в новом PDF. Она создаёт новый PDF‑документ, добавляет страницу, генерирует таблицу из DataFrame (используя вспомогательный метод) и сохраняет результат по указанному пути к файлу. И это не только возможно, но и очень просто.

1. Инициализирует пустой PDF‑документ с помощью 'ap.Document()'.
1. Функция 'self.create_table_from_dataframe(df, max_rows)' преобразует DataFrame в объект таблицы Aspose.PDF.
1. Вставляет таблицу в страницу PDF. Добавляет сгенерированную таблицу в содержимое первой страницы (page.paragraphs.add(table)).
1. Сохраняет PDF‑документ.

```python

from os import path
import pandas as pd
import aspose.pdf as ap

# Example DataFrame
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Paris", "London"]
})

max_rows = 3  # Number of rows to include in the table
path_outfile = "output.pdf"

# Define the function to create a table from DataFrame
def create_table_from_dataframe(df, max_rows):
    table = ap.Table()
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1, ap.Color.light_gray)
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.BOTTOM, 1, ap.Color.light_gray
    )
    # Add header row with column names
    header_row = table.rows.add()
    header_row.is_row_broken = False
    for column_name in df.columns:
        cell = header_row.cells.add(str(column_name))
        cell.background_color = ap.Color.light_gray
    # Add data rows
    for row_data in df.head(max_rows).itertuples(index=False):
        row = table.rows.add()
        for value in row_data:
            row.cells.add(str(value))
    return table

# Load source PDF document
document = ap.Document()
page = document.pages.add()

table = create_table_from_dataframe(df, max_rows)

# Add table object to first page of input document
page.paragraphs.add(table)
document.save(path_outfile)
```

## Создать таблицу из DataFrame

Этот код преобразует DataFrame в объект Table библиотеки Aspose.PDF. Он настраивает границы таблицы, добавляет строку заголовка с именами столбцов и заполняет таблицу первыми max_rows строками из DataFrame. Получившуюся таблицу затем можно добавить в PDF‑документ.

1. Создаёт пустой объект 'ap.Table()'.
1. Устанавливает границы таблицы.
1. Устанавливает границы ячеек по умолчанию.
1. Добавляет строку заголовка.
1. Добавляет строки данных.
1. Возвращает таблицу.

```python

    from os import path
    import pandas as pd
    import aspose.pdf as ap

    
    table = ap.Table()  # Initializes a new instance of the Table
    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1, ap.Color.light_gray)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.BOTTOM, 1, ap.Color.light_gray
    )

    # Add header row with column names
    header_row = table.rows.add()
    header_row.is_row_broken = (
        False  # Prevent header row from being split across pages
    )
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

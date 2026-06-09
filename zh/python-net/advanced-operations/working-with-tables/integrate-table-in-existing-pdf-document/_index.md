---
title: 在 Python 中将 PDF 表格与数据源集成
linktitle: 集成表格
type: docs
weight: 30
url: /zh/python-net/integrate-table/
description: 了解如何在 Python 中将 PDF 表格与数据库和 pandas DataFrame 等数据源集成。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 将 PDF 表格与数据库和 DataFrame 集成
Abstract: 本文阐述了如何使用 Aspose.PDF for Python via .NET 将 PDF 表格与外部数据源集成。了解如何从 pandas DataFrame 和其他结构化来源构建 PDF 表格，将其插入文档，并在 Python 中跨 PDF 页面渲染时控制表格流动。
---

## 从 DataFrame 创建 PDF

这 `create_pdf_from_dataframe` 函数构建一个新的 PDF 并插入一个由 pandas DataFrame 生成的表格。这种方法对于数据已经以表格形式存在的报告工作流非常有用。

该函数执行以下步骤：

1. 使用创建一个空的 PDF 文档 `ap.Document()`.
1. 向文档添加一个页面。
1. 通过调用将 DataFrame 转换为 Aspose.PDF 表格 `create_table_from_dataframe(df, max_rows)`.
1. 使用将表格添加到页面 `page.paragraphs.add(table)`.
1. 将 PDF 保存到输出路径。

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

## 从 DataFrame 创建表

这 `create_table_from_dataframe` 函数将 DataFrame 转换为 Aspose.PDF `Table` 可以添加到任何页面的对象。

它执行以下操作：

1. 创建一个空的 `ap.Table()` 实例。
1. 设置表格和单元格边框，以实现一致的格式。
1. 使用 DataFrame 列名添加标题行。
1. 从...添加数据行 `df.head(max_rows)`.
1. 返回填充好的表格对象。

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

## 相关表格主题

- [使用 Python 在 PDF 中处理表格](/pdf/zh/python-net/working-with-tables/)
- [使用 Python 向 PDF 添加表格](/pdf/zh/python-net/adding-tables/)
- [从 PDF 文档中提取表格](/pdf/zh/python-net/extracting-table/)
- [在现有 PDF 中操作表格](/pdf/zh/python-net/manipulating-tables/)
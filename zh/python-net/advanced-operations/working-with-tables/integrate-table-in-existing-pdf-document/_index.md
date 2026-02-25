---
title: 将表格与数据源 PDF 集成
linktitle: 集成表格
type: docs
weight: 30
url: /zh/python-net/integrate-table/
description: 本文展示了如何集成 PDF 表格。将表格与数据库集成，并确定表格是否会在当前页面拆分。
lastmod: "2025-09-17"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## 从 DataFrame 创建 PDF

函数 'create_pdf_from_dataframe' 接受一个 DataFrame 并将其转换为新 PDF 中的表格。它创建一个全新的 PDF 文档，添加页面，使用辅助方法从 DataFrame 生成表格，并将结果保存到指定的文件路径。并且这不仅可行，而且非常简单。

1. 使用 'ap.Document()' 初始化一个空的 PDF 文档。
1. 'self.create_table_from_dataframe(df, max_rows)' 函数将 DataFrame 转换为 Aspose.PDF 表格对象。
1. 将表格插入 PDF 页面。将生成的表格添加到第一页的内容中 (page.paragraphs.add(table))。
1. 保存 PDF 文档。

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

## 从 DataFrame 创建表格

此代码将 DataFrame 转换为 Aspose.PDF Table 对象。它设置表格边框，添加包含列名的标题行，并使用 DataFrame 前 max_rows 行填充表格。生成的表格随后可添加到 PDF 文档中。

1. 创建一个空的 'ap.Table()' 对象。
1. 设置表格边框。
1. 设置默认单元格边框。
1. 添加标题行。
1. 添加数据行。
1. 返回表格。

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

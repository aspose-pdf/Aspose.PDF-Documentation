---
title: 操作现有 PDF 文档中的表格
linktitle: 操作表格
type: docs
weight: 40
url: /zh/python-net/manipulating-tables/
description: 学习如何使用 Python 检查和修改现有 PDF 文档中的表格。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 检查并修改现有 PDF 表格
Abstract: 本文解释了如何使用 Aspose.PDF for Python via .NET 操作 PDF 文档中已存在的表格。了解如何使用 TableAbsorber 定位表格、访问特定的行和单元格、更新表格文本内容，并在 Python 中保存修改后的 PDF。
---

## 操作现有 PDF 中的表格

Aspose.PDF for Python via .NET 让您能够更新 PDF 文档中已存在的表格。您可以使用 [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) 类来查找页面上的表格，访问行和单元格，修改文本内容，并保存更新后的文件。

当您需要在不重新创建整个文档布局的情况下更新 PDF 中已有的表格内容时，请使用此页面。

## 在 PDF 表格单元格中查找并替换文本

此示例在第 1 页找到第一个表格，访问第一个单元格，替换其文本，并保存输出的 PDF。

1. 打开输入的 PDF。
1. 创建一个 TableAbsorber 并访问第 1 页。
1. 确保检测到至少一个表格。
1. 访问第一个表格的第一行中的第一个单元格。
1. 确保单元格包含文本片段，然后更新第一个片段。
1. 保存修改后的 PDF。

```python
import aspose.pdf as ap

def replace_cell_text(infile: str, outfile: str) -> None:
    """Replace text in the first cell of the first detected table."""
    # Open PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    if len(absorber.table_list) == 0:
        raise ValueError("No tables were found on page 1.")

    first_cell = absorber.table_list[0].row_list[0].cell_list[0]
    if len(first_cell.text_fragments) == 0:
        raise ValueError("The target cell has no text fragments.")

    # Change text of the first text fragment in the cell
    first_cell.text_fragments[0].text = "New Value"

    # Save PDF document
    document.save(outfile)
```

## 用新表替换现有表

您还可以用新创建的表替换检测到的表。当结构和内容都必须更改时，这种方法非常有用。

以下代码打开一个 PDF，查找第 1 页的第一张表格，创建一个替换表格，用新表格替换旧表格，并保存结果。

```python
import aspose.pdf as ap

def replace_table(infile: str, outfile: str) -> None:
    """Replace an entire table with a new one."""
    # Open PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    if len(absorber.table_list) == 0:
        raise ValueError("No tables were found on page 1.")

    # Get first table on the page
    old_table = absorber.table_list[0]

    # Create new table
    new_table = ap.Table()
    new_table.column_widths = "100 100 100"
    new_table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 1.0)

    row = new_table.rows.add()
    row.cells.add("Col 1")
    row.cells.add("Col 2")
    row.cells.add("Col 3")
    row = new_table.rows.add()
    row.cells.add("Col 12")
    row.cells.add("Col 22")
    row.cells.add("Col 32")

    # Replace the old table with the new one
    absorber.replace(document.pages[1], old_table, new_table)

    # Save PDF document
    document.save(outfile)
```

## 相关表格主题

- [使用 Python 在 PDF 中处理表格](/pdf/zh/python-net/working-with-tables/)
- [使用 Python 向 PDF 添加表格](/pdf/zh/python-net/adding-tables/)
- [从 PDF 文档中提取表格](/pdf/zh/python-net/extracting-table/)
- [从现有 PDF 中删除表格](/pdf/zh/python-net/removing-tables/)

---
title: 在现有 PDF 中操作表格
linktitle: 操作表格
type: docs
weight: 40
url: /zh/python-net/manipulating-tables/
description: 了解如何使用 Aspose.PDF for Python via .NET 在现有 PDF 中处理表格，从而实现文档修改的灵活性。
lastmod: "2025-09-27"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## 在现有 PDF 中操作表格

Aspose.PDF for Python 展示了如何在 PDF 文档中修改特定单元格的内容。它使用 TableAbsorber 类定位第一页上的表格，访问第一个表格的第一个单元格中的特定文本片段，更新其文本，并将修改后的 PDF 保存为新文件。

1. 使用 'ap.Document()' 打开 PDF 文件。
1. 创建 TableAbsorber 对象以检测 PDF 中的表格。
1. 调用 absorber.visit() 来查找首页上的所有表格。
1. 访问特定的文本片段：
- 获取第一个表格。
- 获取表格的第一行。
- 选择单元格中的第二个文本片段。
1. 修改文本。
1. 保存更新后的 PDF。
1. 打印已保存文件的确认信息。

```python

    import aspose.pdf as ap
    from os import path

    # Define file names and data directory
    data_dir = "."  # or specify your data directory
    infile = "input.pdf"   # replace with your input PDF file name
    outfile = "output.pdf" # replace with your desired output PDF file name

    # Open PDF document
    path_infile = path.join(data_dir, infile)
    path_outfile = path.join(data_dir, outfile)
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    # Get access to first table on page, their first cell and text fragments in it
    fragment = absorber.table_list[0].row_list[0].cell_list[0].text_fragments[1]

    # Change text of the first text fragment in the cell
    fragment.text = "hi world"

    # Save PDF document

    document.save(path_outfile)
    print(f"File saved at: {path_outfile}")
```

## 在 PDF 文档中用新表格替换旧表格

Aspose.PDF 允许在 PDF 中用新表格替换现有表格。代码片段打开 PDF，使用 TableAbsorber 在第一页识别第一个表格，创建具有自定义列宽和内容的新表格，然后用新表格替换原始表格。最后，它将更新后的 PDF 保存为新文件。

它演示了如何在不更改文档其余部分的情况下修改 PDF 中的表格结构和内容。

```python

    import aspose.pdf as ap
    from os import path

    # Open PDF document
    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    # Get first table on the page
    table = absorber.table_list[0]

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

    # Replace the table with new one
    absorber.replace(document.pages[1], table, new_table)

    # Save PDF document
    document.save(path_outfile)
    print(f"File saved at: {path_outfile}")
```

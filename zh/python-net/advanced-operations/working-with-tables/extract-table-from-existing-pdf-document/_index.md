---
title: 在 Python 中从 PDF 提取表格
linktitle: 提取表格
type: docs
weight: 20
url: /zh/python-net/extracting-table/
description: 了解如何在 Python 中从现有的 PDF 文档中提取表格数据。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 从 PDF 文件中提取表格数据
Abstract: 本文介绍如何使用 Aspose.PDF for Python via .NET 从 PDF 文档中提取表格。它展示了如何使用 `TableAbsorber` 按页检测表格，遍历行和单元格，并检索单元格文本以进行分析和下游数据处理。
---

## 从 PDF 中提取表格

从 PDF 中提取表格对于报告、数据迁移和分析工作流非常有用。使用 Aspose.PDF for Python via .NET，您可以高效地检测并读取现有 PDF 文档中的表格内容。

此代码片段打开一个现有的 PDF 文件，扫描每一页的表格，并提取单元格文本内容。它使用 `TableAbsorber` 检测表格，然后遍历行和单元格以打印提取的文本。

1. 将 PDF 加载到 ap.Document 对象中。
1. 遍历页面。
1. 创建一个 TableAbsorber 对象。
1. 遍历表格。
1. 遍历行和单元格。
1. 提取并打印单元格中的文本。

此示例读取 PDF，查找所有表格，并逐行打印单元格内容。

```python
import aspose.pdf as ap
from os import path
import sys

def extract(infile: str) -> None:
    """Extract and print all tables from a PDF file."""
    document = ap.Document(infile)
    for page in document.pages:
        absorber = ap.text.TableAbsorber()
        absorber.visit(page)
        for table in absorber.table_list:
            print("Table ----")
            for row in table.row_list:
                print("Row:")
                row_txt = ""
                for cell in row.cell_list:
                    cell_txt = ""
                    text_fragment_collection = cell.text_fragments
                    for fragment in text_fragment_collection:
                        for seg in fragment.segments:
                            cell_txt += seg.text
                    row_txt += " | "
                    row_txt += cell_txt
                print(row_txt)
```

## 相关表格主题

- [使用 Python 在 PDF 中处理表格](/pdf/zh/python-net/working-with-tables/)
- [使用 Python 向 PDF 添加表格](/pdf/zh/python-net/adding-tables/)
- [将 PDF 表格与数据源集成](/pdf/zh/python-net/integrate-table/)
- [从现有 PDF 中删除表格](/pdf/zh/python-net/removing-tables/)
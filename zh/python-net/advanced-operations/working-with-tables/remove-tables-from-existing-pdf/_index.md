---
title: 从现有 PDF 文档中删除表格
linktitle: 删除表格
description: 了解如何在 Python 中从现有 PDF 文档中删除一个或多个表格。
lastmod: "2026-06-08"
type: docs
weight: 50
url: /zh/python-net/removing-tables/
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 删除 PDF 文件中的一个或多个表格
Abstract: 本文说明了如何使用 Aspose.PDF for Python via .NET 从现有 PDF 文档中删除表格。它介绍了 `TableAbsorber` 用于定位表格，并演示了如何删除单个表格或从页面中删除所有检测到的表格。
---

## 从 PDF 文档中删除表格

Aspose.PDF for Python 允许您从 PDF 中移除表格。它打开现有的 PDF，检测首页上的第一个表格，用 `TableAbsorber`，使用删除该表 `remove()`，并将更新后的 PDF 保存到一个新文件。

当您需要清理大量表格的 PDF、删除过时的表格内容，或在重新分发前简化文档时，请使用此页面。

```python
import aspose.pdf as ap
from os import path
import sys

def remove_one_table(infile: str, outfile: str) -> None:
    # Load existing PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit first page with absorber
    absorber.visit(document.pages[1])
    # Get first table on the page
    table = absorber.table_list[0]
    # Remove the table
    absorber.remove(table)
    # Save PDF
    document.save(outfile)
```

## 从 PDF 文档中移除所有表格

使用我们的库，您可以从 PDF 的特定页面中移除所有表格。代码打开现有的 PDF，使用 TableAbsorber 检测第二页上的所有表格，遍历检测到的表格，逐一移除，然后将修改后的 PDF 保存为新文件。当您需要批量移除页面上的表格而保留 PDF 其余内容完整时，这非常有用。

```python
import aspose.pdf as ap
from os import path
import sys

def remove_all_tables(infile: str, outfile: str) -> None:
    # Load existing PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit first page with absorber
    absorber.visit(document.pages[1])
    #  Loop through the copy of collection and removing tables
    tables = list(absorber.table_list)
    for table in tables:
        absorber.remove(table)

    # Save document
    document.save(outfile)
```

## 相关表格主题

- [使用 Python 在 PDF 中处理表格](/pdf/zh/python-net/working-with-tables/)
- [使用 Python 向 PDF 添加表格](/pdf/zh/python-net/adding-tables/)
- [从 PDF 文档中提取表格](/pdf/zh/python-net/extracting-table/)
- [在现有 PDF 中操作表格](/pdf/zh/python-net/manipulating-tables/)
---
title: 添加列表项
type: docs
weight: 10
url: /zh/python-net/add-list-item/
description: 本示例演示了如何使用 Aspose.PDF for Python 在 PDF 文档中向列表框表单字段添加项目。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 向 PDF 列表框字段添加项目
Abstract: 本文展示了如何打开 PDF 文档，向名为 "Country" 的列表框字段追加项目，并保存更新后的文档。
---

PDF 中的列表框字段允许用户从预定义集合中选择一个或多个选项。使用 Aspose.PDF for Python，开发者可以以编程方式向这些字段添加新项目。The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 类提供了 ‘add_list_item’ 方法，用于向现有列表框字段追加项目。

1. 打开现有的 PDF 表单。
1. 创建一个 FormEditor 对象。
1. 将 PDF 绑定到 FormEditor。
1. 向列表框字段 "Country" 添加项目。
1. 保存更新后的文档。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_list_item(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Add list item to list box field
    form_editor.add_list_item("Country", ["New Zealand", "New Zealand"])
    # Save updated document
    form_editor.save(outfile)
```

---
title: 删除列表项
type: docs
weight: 40
url: /zh/python-net/del-list-item/
description:
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 从 PDF 列表框字段中移除项目
Abstract: 此示例演示如何使用 Aspose.PDF for Python 从 PDF 文档中的列表框表单字段中移除项目。代码打开现有 PDF，删除列表框字段中的特定项目，并保存更新后的文档。
---

PDF 中的列表框字段允许用户选择一个或多个预定义选项。使用 Aspose.PDF for Python，开发人员可以以编程方式从这些字段中移除项目。

本文说明如何删除名为“Country”的列表框字段中的 ‘UK’ 项，确保该字段仅包含所需的选项。

这 [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 该类提供 ‘del_list_item’ 方法，用于从列表框字段中移除特定项目。

1. 打开现有的 PDF 表单。
1. 创建一个 FormEditor 对象。
1. 将 PDF 文档绑定到 FormEditor。
1. 删除 "UK" 项从 "Country" 列表框字段。
1. 保存更新后的文档。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def del_list_item(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Delete list item from list box field
    form_editor.del_list_item("Country", "UK")
    # Save updated document
    form_editor.save(outfile)
```


---
title: 删除字段
type: docs
weight: 60
url: /zh/python-net/remove-field/
description: 此示例演示如何使用 'FormEditor' 类的 'remove_field' 方法从 PDF 表单中删除 'Country' 字段。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 从 PDF 文档中删除表单字段
Abstract: 此示例演示如何使用 Aspose.PDF for Python 从 PDF 文档中删除现有的表单字段。代码加载 PDF 文件，使用 FormEditor 类删除指定字段，并保存更新后的文档。
---

由于设计更改或工作流更新，PDF 表单可能包含不再需要的字段。使用 Aspose.PDF for Python，开发人员可以轻松地以编程方式删除特定的表单字段。

这 [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) Aspose.PDF 中的类提供了 'remove_field' 方法，允许开发人员按名称删除表单字段。

1. 加载 PDF 文档。
1. 创建一个 FormEditor 对象。
1. 将 PDF 绑定到 FormEditor。
1. 删除指定的表单字段。
1. 保存更新后的文档。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Remove field from document
    form_editor.remove_field("Country")
    # Save updated document
    form_editor.save(outfile)
```

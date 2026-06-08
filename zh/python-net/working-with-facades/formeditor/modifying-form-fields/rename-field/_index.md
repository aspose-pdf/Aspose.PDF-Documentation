---
title: 重命名字段
type: docs
weight: 70
url: /zh/python-net/rename-field/
description: 使用 Aspose.PDF for Python 重命名 PDF 文档中的现有表单字段。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 重命名 PDF 表单字段
Abstract: 本示例演示了如何使用 Aspose.PDF for Python 重命名 PDF 文档中的现有表单字段。代码打开一个输入 PDF，使用 FormEditor 类更改指定表单字段的名称，并保存更新后的文档。
---

PDF 表单通常依赖字段名称进行脚本编写、自动化和数据处理。使用 Aspose.PDF for Python，开发人员可以在不重新创建字段或更改表单布局的情况下重命名现有字段。

这 [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) class 提供了 'rename_field' 方法，允许开发人员在保留字段位置、值和外观的情况下更改现有字段的名称。

1. 加载现有的 PDF 表单。
1. 创建一个 FormEditor 实例。
1. 将 PDF 文档绑定到编辑器。
1. 重命名目标字段。
1. 保存更新后的 PDF。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def rename_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Rename field in document
    form_editor.rename_field("City", "Town")
    # Save updated document
    form_editor.save(outfile)
```


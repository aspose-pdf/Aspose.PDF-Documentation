---
title: 使用 XFA 表单
linktitle: XFA 表单
type: docs
weight: 20
url: /zh/python-net/xfa-forms/
description: Aspose.PDF for Python via .NET API 让您能够在 PDF 文档中使用 XFA 和 XFA AcroForm 字段。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 将 XFA 转换为 AcroForm

{{% alert color="primary" %}}

在线试用
您可以在此链接检查 Aspose.PDF 转换的质量并在线查看结果： [products.aspose.app/pdf/xfa/acroform](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

下面的代码片段演示如何将动态 XFA（XML Forms Architecture）表单转换为标准 AcroForm。

**关键步骤包括：**

1. 加载输入 PDF 文档。
1. 将表单类型更改为 STANDARD。
1. 将转换后的 PDF 保存到新文件。

此转换可在不同的 PDF 阅读器和应用程序之间实现更好的兼容性和一致的表单处理。

```python
import aspose.pdf as ap
import sys
from os import path

def convert_dynamic_xfa_to_acroform(infile: str, outfile: str):
    """Convert dynamic XFA form to standard AcroForm."""
    with ap.Document(infile) as document:
        document.form.type = ap.forms.FormType.STANDARD
        document.save(outfile)
```

## IgnoreNeedsRendering 的使用

本示例演示了如何使用 Aspose.PDF for Python 将动态 XFA 表单转换为标准 AcroForm。代码会检查输入的 PDF 是否包含 XFA 表单，并在必要时覆盖渲染。随后将表单类型设置为 STANDARD 并保存更新后的 PDF。

```python
import aspose.pdf as ap
import sys
from os import path

def convert_xfa_form_with_ignore_needs_rendering(infile: str, outfile: str):
    """Convert XFA form ignoring needs rendering flag."""
    with ap.Document(infile) as document:
        if not document.form.needs_rendering and document.form.has_xfa:
            document.form.ignore_needs_rendering = True
        document.form.type = ap.forms.FormType.STANDARD
        document.save(outfile)
```

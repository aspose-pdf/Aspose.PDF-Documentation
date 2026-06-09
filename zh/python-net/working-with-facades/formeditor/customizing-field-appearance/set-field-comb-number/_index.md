---
title: 设置字段组合号码
type: docs
weight: 70
url: /zh/python-net/set-field-comb-number/
description: 本示例演示如何使用 Aspose.PDF for Python 为 PDF 表单字段设置组合号码。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 为 PDF 表单字段设置组合号码
Abstract: 使用 Aspose.PDF for Python，开发人员可以以编程方式设置表单字段的盒子数量（组合号码），以强制固定长度输入。本文演示了为名为 "PIN" 的字段设置组合号码。
---

组合号码定义了字段内容如何被拆分为等间距的盒子，常用于 PIN 码、序列号或其他固定长度的输入字段。代码打开现有 PDF，为字段设置组合号码，并保存修改后的文档。

这 [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 该类提供了 'set_field_comb_number' 方法，用于定义表单字段中盒子（字符）的数量。

1. 打开现有的 PDF 表单。
1. 创建一个 FormEditor 对象。
1. 将名为 "PIN" 的字段的 comb number 设置为 5。
1. 保存更新后的文档。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_comb_number(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field comb number to 5
    form_editor.set_field_comb_number("PIN", 5)

    # Save updated document
    form_editor.save(outfile)
```

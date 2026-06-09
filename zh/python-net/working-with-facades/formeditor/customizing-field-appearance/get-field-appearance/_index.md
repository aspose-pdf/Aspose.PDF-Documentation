---
title: 获取字段外观
type: docs
weight: 20
url: /zh/python-net/get-field-appearance/
description: 这篇文章解释了如何打开 PDF，访问表单字段，检索其外观设置并显示它们。示例演示了检索名为 "Last Name" 的字段的外观。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 检索 PDF 表单字段外观
Abstract: 该示例演示了如何使用 Aspose.PDF for Python 检索 PDF 文档中表单字段的可视外观属性。代码打开现有的 PDF，访问特定的表单字段，并打印其外观详情，包括背景颜色、文字颜色、边框颜色和对齐方式。
---

PDF 文档中的表单字段具有背景颜色、文字颜色、边框颜色和对齐方式等可视属性。使用 Aspose.PDF for Python，开发者可以通过使用的方式以编程方式检查这些外观设置 [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 类。

1. 打开现有的 PDF 文档。
1. 创建一个 FormEditor 对象。
1. 检索特定字段的外观信息。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_field_appearance(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Get field appearance
    appearance = form_editor.get_field_appearance("Last Name")
    print("Field Appearance: " + str(appearance))
```

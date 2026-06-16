---
title: 获取文档权限
type: docs
weight: 10
url: /zh/python-net/get-document-privileges/
description: 了解如何使用 Aspose.PDF for Python 以编程方式检查 PDF 文档的权限。本教程演示如何使用 PdfFileInfo 类读取文档的安全设置，例如打印、复制或修改权限。
lastmod: "2026-06-08"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Python 检索 PDF 文档权限
Abstract: PDF 文档可能具有限制打印、复制、修改或填写表单等操作的安全限制。通过以编程方式访问这些权限，开发人员可以确定在 PDF 上允许的操作。此指南展示如何使用 PdfFileInfo 类检索 PDF 的文档权限并在 Python 中显示它们。
---

PDF 权限控制用户对文档可以执行和不能执行的操作。常见的权限包括：

- 打印文档
- 复制内容
- 修改批注或内容
- 填写表单字段
- 使用屏幕阅读器
- 组装或合并文档

使用 Aspose.PDF for Python，您可以通过编程方式使用 the 检查这些设置 [PdfFileInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) 类。这在自动化工作流中处理多个 PDF、验证合规性或在应用程序中控制文档处理时尤为有用。

1. 加载 PDF 文件。
1. 检索其文档权限。
1. 显示文档允许的操作。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_document_privileges(input_file_name):
    pdf_metadata = pdf_facades.PdfFileInfo(input_file_name)

    privileges = pdf_metadata.get_document_privilege()

    print("Document Privileges:")
    print(f"  Can Print: {privileges.allow_print}")
    print(f"  Can Degraded Print: {privileges.allow_degraded_printing}")
    print(f"  Can Copy: {privileges.allow_copy}")
    print(f"  Can Modify Contents: {privileges.allow_modify_contents}")
    print(f"  Can Modify Annotations: {privileges.allow_modify_annotations}")
    print(f"  Can Fill In: {privileges.allow_fill_in}")
    print(f"  Can Screen Readers: {privileges.allow_screen_readers}")
    print(f"  Can Assembly: {privileges.allow_assembly}")
```

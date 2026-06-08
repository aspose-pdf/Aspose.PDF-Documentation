---
title: 提取链接
type: docs
weight: 70
url: /zh/python-net/extract-links/
description: 此示例绑定一个输入 PDF，提取所有链接，并打印其坐标和 URI（如果可用）。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 PdfContentEditor 在 Python 中提取 PDF 链接
Abstract: 此示例演示如何使用 Aspose.PDF for Python via the Facades API 提取 PDF 文档中的所有链接。它展示了如何识别并检索嵌入在 PDF 中的网页链接或其他可操作链接。
---

PDF 通常包含交互元素，例如网页链接、文档链接和自定义操作。使用 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)，您可以以编程方式从 PDF 中提取所有链接注释。这使您能够检查或处理链接，例如验证 URL 或分析文档中的导航模式。

1. 创建一个 PdfContentEditor 实例。
1. 绑定输入的 PDF 文档。
1. 使用 'extract_link()' 提取所有链接。
1. 遍历已提取的链接。
1. 检查链接是否为 LinkAnnotation，以及其操作是否为 GoToURIAction。
1. 打印矩形坐标和 URI。
1. 如果未找到链接，则显示一条消息。

```python
import aspose.pdf.facades as pdf_facades
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as apd
import aspose.pdf as ap

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def extract_links(infile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Extract links from the document
    links = content_editor.extract_link()

    count = 0
    for link in links:
        count += 1
        print(f"Link {count}: {link.rect}")
        if is_assignable(link, ap.annotations.LinkAnnotation):
            annotation = cast(ap.annotations.LinkAnnotation, link)
            if is_assignable(annotation.action, ap.annotations.GoToURIAction):
                action = cast(ap.annotations.GoToURIAction, annotation.action)
                print(f"  URI: {action.uri}")

    if count == 0:
        print("No links found")
```

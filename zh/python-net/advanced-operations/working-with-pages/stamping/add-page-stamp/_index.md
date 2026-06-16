---
title: 在 Python 中向 PDF 添加页面印章
linktitle: 添加页面印章
type: docs
weight: 30
url: /zh/python-net/page-stamps-in-the-pdf-file/
description: 了解如何在 Python 中将 PDF 页面印章作为叠加层或背景添加。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 向 PDF 添加页面印章
Abstract: 本文介绍如何使用 Aspose.PDF for Python 向 PDF 文档添加页面印章。页面印章允许您在 PDF 的特定页面上覆盖或底层放置内容——如徽标、水印或批注。示例展示了如何打开现有 PDF，从另一个 PDF 页面创建 PdfPageStamp 对象，将其配置为背景印章，并将其应用于指定页面。随后将带印章的 PDF 保存为新文档。此技术在自动化 PDF 工作流中用于品牌化、水印或强调页面级内容。
---

Aspose.PDF for Python via .NET 展示了如何将页面印章（水印或叠加层）应用于 PDF 的特定页面 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). 页面印章可以是作为背景或前景层使用的已有 PDF 页面（参见 [`PdfPageStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf.pdfpagestamp/)）。这对于添加徽标、水印或其他重复的页面内容非常有用。

1. 使用以下方法打开 PDF 文档 `ap.Document()` (见 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. 创建一个 `PdfPageStamp` 使用 PDF 页面或文件作为印章的对象（参见 [`PdfPageStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf.pdfpagestamp/)).
1. 设置印章属性，例如， `background = True` 将其放置在内容后面。
1. 使用以下方法将印章添加到特定页面 `document.pages[page_number].add_stamp(page_stamp)` (见 [`Page.add_stamp()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) 和 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)).
1. 使用以下方式将修改后的 PDF 保存到指定的输出文件 [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python
import sys
import aspose.pdf as ap
from os import path

def add_page_stamp(input_file_name, page_stamp_name, output_file_name):
    # Open PDF document
    document = ap.Document(input_file_name)

    page_stamp = ap.PdfPageStamp(page_stamp_name, 1)
    page_stamp.background = True

    # Add stamp to particular page
    document.pages[1].add_stamp(page_stamp)

    document.save(output_file_name)
```

## 相关的盖章主题

- [在 Python 中对 PDF 页面加盖印章](/pdf/zh/python-net/stamping/)
- [在 Python 中为 PDF 添加页码](/pdf/zh/python-net/add-page-number/)
- [使用 Python 向 PDF 添加图像印章](/pdf/zh/python-net/image-stamps-in-pdf-page/)
- [在 Python 中向 PDF 添加文本印章](/pdf/zh/python-net/text-stamps-in-the-pdf-file/)
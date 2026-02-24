---
title: 使用 Python 在 PDF 中添加页面印章
linktitle: 添加页面印章
type: docs
weight: 30
url: /zh/python-net/page-stamps-in-the-pdf-file/
description: Aspose.PDF for Python via .NET 允许您向 PDF 文件添加页面印章。
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 向 PDF 添加页面印章
Abstract: 本文说明了如何使用 Aspose.PDF for Python 向 PDF 文档添加页面印章。页面印章允许您在 PDF 的特定页面上覆盖或下铺内容——如徽标、水印或批注。示例展示了如何打开已有的 PDF，使用另一个 PDF 页面创建 PdfPageStamp 对象，将其配置为背景印章，并将其应用于特定页面。随后将已加印章的 PDF 保存为新文档。此技术对于品牌标识、水印或在自动化 PDF 工作流中强调页面级内容非常有用。
---

Aspose.PDF for Python via .NET 展示了如何将页面印章（水印或覆盖层）应用于 PDF 中的特定页面 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)。页面印章可以是用作背景或前景层的现有 PDF 页面（参见 [`PdfPageStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf.pdfpagestamp/)）。这对于添加徽标、水印或其他重复的页面内容非常有用。

1. 使用 `ap.Document()` 打开 PDF 文档（参见 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)）。
1. 使用 PDF 页面或文件创建 `PdfPageStamp` 对象作为印章（参见 [`PdfPageStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf.pdfpagestamp/)）。
1. 设置印章属性，例如 `background = True` 以将其放置在内容后面。
1. 使用 `document.pages[page_number].add_stamp(page_stamp)` 将印章添加到特定页面（参见 [`Page.add_stamp()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) 和 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)）。
1. 使用 [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 将修改后的 PDF 保存到指定的输出文件。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_page_stamp(input_file_name, page_stamp_name, output_file_name):
    # Open PDF document
    document = ap.Document(input_file_name)

    page_stamp = ap.PdfPageStamp(page_stamp_name, 1)
    page_stamp.background = True

    # Add stamp to particular page
    document.pages[1].add_stamp(page_stamp)

    document.save(output_file_name)
```


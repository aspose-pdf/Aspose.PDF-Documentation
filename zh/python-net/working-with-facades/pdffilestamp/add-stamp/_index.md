---
title: 将印章添加到 PDF
type: docs
weight: 40
url: /zh/python-net/add-stamp/
description: 学习如何在 Python 中使用 PdfFileStamp 向 PDF 页面添加印章。
lastmod: "2026-06-08"
TechArticle: true
AlternativeHeadline: 在 Python 中向 PDF 添加文本印章
Abstract: 本文说明了如何使用 Aspose.PDF for Python via .NET 通过 PdfFileStamp 外观向 PDF 文档添加印章内容。它展示了如何创建印章、在页面上定位、控制旋转和不透明度，并保存更新后的 PDF。
---

Aspose.PDF for Python via .NET 提供了 [PdfFileStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) 用于向 PDF 页面添加重复内容的外观。除页眉、页脚和页码外，您还可以使用它在文档的每一页上放置基于文本的印章。

## 将印章添加到 PDF

在配置印章后，将输入 PDF 绑定到 `PdfFileStamp`, 添加印章，并保存输出文件。这将在整个文档中应用配置的印章。

```python
import sys
from os import path

import aspose.pdf.facades as pdf_facades

CURRENT_DIR = path.dirname(__file__)
EXAMPLES_DIR = path.abspath(path.join(CURRENT_DIR, "..", ".."))
if EXAMPLES_DIR not in sys.path:
    sys.path.insert(0, EXAMPLES_DIR)

from config import initialize_data_dir, set_license


def add_stamp_to_pdf(infile: str, image_file: str, outfile: str) -> None:
    """Add an image stamp to a PDF file."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

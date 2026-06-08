---
title: 添加文本注释
type: docs
weight: 50
url: /zh/python-net/add-text-annotation/
description: 使用 Aspose.PDF for Python via .NET 中的 PdfContentEditor 类向 PDF 文档添加文本批注。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中添加文本批注。
Abstract: 了解如何使用 Aspose.PDF for Python via .NET 中的 PdfContentEditor 类向 PDF 文档添加文本批注。此示例展示了如何在特定位置放置文本批注，定义其标题和内容，并保存更新后的 PDF 文件。
---

本文展示了如何使用 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) Aspose.PDF 中的类。

文本批注允许您将评论、注释或额外信息附加到 PDF 页面上的特定位置。这些批注可以以图标形式出现，并在用户查看文档时展开。

在此示例中：

- 将 PDF 文档加载到 PdfContentEditor 中。
- 在页面的特定位置添加文本注释。
- 该注释包括标题、内容、图标类型和可见性设置。
- 修改后的文档保存为新文件。

1. 创建一个 PdfContentEditor 对象。
1. 绑定输入 PDF 文档。
1. 定义注释位置。
1. 添加文本注释。
1. 保存更新后的 PDF。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_text_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add text annotation to page 1
    content_editor.create_text(
        apd.Rectangle(100, 400, 50, 50),
        "Text Annotation",
        "This is a text annotation",
        True,
        "Insert",
        1,
    )
    # Save updated document
    content_editor.save(outfile)
```

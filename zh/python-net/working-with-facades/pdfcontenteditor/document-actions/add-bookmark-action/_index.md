---
title: 添加书签操作
type: docs
weight: 10
url: /zh/python-net/add-bookmark-action/
description: 此示例绑定一个输入 PDF，创建一个标签为 "PdfContentEditor Bookmark" 的书签，该书签导航至第 1 页，并保存更新后的文档。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 在 PDF 中创建带导航操作的书签
Abstract: 此示例演示了如何使用 Aspose.PDF for Python via the Facades API 向 PDF 文档添加带有导航操作的书签。它展示了如何配置书签文本、外观以及将用户导向特定页面的操作。
---

书签提供了在 PDF 文档内快速导航的功能。使用 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)，您可以以程序方式创建书签并分配诸如导航至页面的操作。您还可以自定义书签的外观，包括颜色以及粗体或斜体等样式选项。

1. 创建 PdfContentEditor 对象。
1. 绑定输入 PDF。
1. 定义书签属性。
1. 分配书签操作。
1. 保存已更新的 Document。

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_bookmark_action(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add a bookmark action to navigate to page 1
    content_editor.create_bookmarks_action(
        "PdfContentEditor Bookmark",
        apd.Color.blue,
        True,
        False,
        "",
        "GoTo",
        "1",
    )
    # Save updated document
    content_editor.save(outfile)
```
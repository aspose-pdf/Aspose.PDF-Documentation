---
title: 获取 PDF 查看器首选项
type: docs
weight: 20
url: /zh/python-net/get-viewer-preferences/
description: 如何使用 Aspose.PDF for Python 以编程方式读取和修改 PDF 查看器首选项
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中使用 Aspose.PDF 管理 PDF 查看器首选项
Abstract: 本指南演示了如何使用 Aspose.PDF for Python 以编程方式读取和修改 PDF 查看器首选项。查看器首选项控制 PDF 在 PDF 查看器中打开时的显示方式，例如以大纲打开、隐藏工具栏或使用单页布局。
---

Aspose.PDF 提供了访问和更新 PDF 查看器首选项的工具。这些首选项定义了 PDF 文档在 PDF 阅读器中的初始布局和呈现行为。包括启用大纲视图、隐藏菜单栏或指定页面布局模式等选项。使用 PdfContentEditor，您可以检索现有的首选项、检查特定标志，并根据需要进行更新。

1. 定义 ViewerPreference 标志。
1. 初始化 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 并绑定 PDF。
1. 获取当前 Viewer Preferences。
1. 检查特定标志。
1. 显示当前首选项。

```python
import aspose.pdf.facades as pdf_facades
import sys
from enum import IntFlag
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_viewer_preferences(infile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Read current viewer preference flags
    viewer_preference = ViewerPreference(content_editor.get_viewer_preference())
    if viewer_preference & ViewerPreference.PAGE_MODE_USE_OUTLINES:
        print("PageModeUseOutlines is enabled")
    print(f"Current viewer preference: {viewer_preference}")
```

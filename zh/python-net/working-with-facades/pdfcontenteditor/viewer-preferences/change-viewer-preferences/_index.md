---
title: 更改 PDF 查看器首选项
type: docs
weight: 10
url: /zh/python-net/change-viewer-preferences/
description: 本模块演示如何使用 Aspose.PDF for Python 调整 PDF 文档的查看器设置。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 定制 PDF 查看器体验
Abstract: 通过以编程方式修改查看器首选项来控制 PDF 文档打开时的呈现方式。此功能允许您定制用户界面和布局，确保一致的查看体验。
---

PDF 文件内置了查看器首选项，可控制页面布局、工具栏可见性和窗口行为等方面。使用此脚本，您可以：

- 检查 PDF 的当前查看器首选项。
- 修改布局选项（例如，单页、单列、双列）。
- 切换 UI 元素，例如工具栏、菜单栏或标题显示。
- 保存 PDF 并使用更新的首选项，以实现受控的查看体验。

1. 定义 ViewerPreference 标志。
1. 获取当前 Viewer Preferences。
1. 修改首选项。
1. 应用更新的首选项。
1. 保存 PDF。

```python
import aspose.pdf.facades as pdf_facades
import sys
from enum import IntFlag
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Define ViewerPreference flags
class ViewerPreference(IntFlag):
    HIDE_TOOLBAR = 1
    HIDE_MENUBAR = 2
    HIDE_WINDOW_UI = 4
    FIT_WINDOW = 8
    CENTER_WINDOW = 16
    DISPLAY_DOC_TITLE = 32
    NON_FULL_SCREEN_PAGE_MODE_USE_NONE = 64
    NON_FULL_SCREEN_PAGE_MODE_USE_OUTLINES = 128
    NON_FULL_SCREEN_PAGE_MODE_USE_THUMBS = 256
    NON_FULL_SCREEN_PAGE_MODE_USE_OC = 512
    DIRECTION_L2R = 1024
    DISPLAY_DOC_TITLE_IN_TITLE_BAR = 2048
    PAGE_LAYOUT_SINGLE_PAGE = 4096
    PAGE_LAYOUT_ONE_COLUMN = 8192
    PAGE_LAYOUT_TWO_COLUMN_LEFT = 16384
    PAGE_LAYOUT_TWO_COLUMN_RIGHT = 32768
    PAGE_LAYOUT_TWO_PAGE_LEFT = 65536
    PAGE_LAYOUT_TWO_PAGE_RIGHT = 131072


def change_viewer_preferences(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    # Get current viewer preference and toggle single-page layout
    current_preference = ViewerPreference(content_editor.get_viewer_preference())
    updated_preference = current_preference | ViewerPreference.PAGE_LAYOUT_SINGLE_PAGE
    content_editor.change_viewer_preference(int(updated_preference))

    # Save updated document
    content_editor.save(outfile)
```

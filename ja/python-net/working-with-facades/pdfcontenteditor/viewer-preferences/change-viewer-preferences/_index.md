---
title: PDF ビューアーの環境設定の変更
type: docs
weight: 10
url: /ja/python-net/change-viewer-preferences/
description: このモジュールでは、Aspose.PDF for Python を使用して PDF ドキュメントのビューア設定を調整する方法を示します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python による PDF ビューアーエクスペリエンスのカスタマイズ
Abstract: ビューアの環境設定をプログラムで変更して、PDF 文書を開いたときの表示方法を制御します。この機能により、ユーザーインターフェイスとレイアウトをカスタマイズして、一貫した表示体験を実現できます。
---

PDF ファイルには、ページレイアウト、ツールバーの表示、ウィンドウの動作などを制御するビューア設定が組み込まれています。このスクリプトを使用すると、次のことが可能になります。

- PDF の現在のビューア設定を調べます。
- レイアウトオプションの変更 (例:1 ページ、1 列、2 列)。
- ツールバー、メニューバー、タイトル表示などの UI 要素を切り替えます。
- 表示を制御できるように、更新した環境設定で PDF を保存します。

1. ビューア設定フラグを定義します。
1. 現在のビューア設定を取得します。
1. プリファレンスを変更します。
1. 更新した設定を適用します。
1. PDF を保存します。

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

---
title: PDF ビューアーの環境設定を取得
type: docs
weight: 20
url: /ja/python-net/get-viewer-preferences/
description: Aspose.PDF for Python を使用して PDF ビューアのプリファレンスをプログラムで読み込んだり変更したりする方法
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python の Aspose.PDF を使って PDF ビューアーのプリファレンスを管理する
Abstract: このガイドでは、Aspose.PDF for Python を使用してプログラムで PDF ビューアの設定を読んだり変更したりする方法を示します。ビューア環境設定は、PDF ビューアで開いたときの PDF の表示方法（アウトラインで開く、ツールバーを非表示にする、1 ページレイアウトを使用するなど）を制御します。
---

Aspose.PDF には、PDF ビューアの環境設定にアクセスして更新するためのツールが用意されています。これらの環境設定は、PDF リーダーでの PDF ドキュメントの初期レイアウトと表示動作を定義します。これには、アウトライン表示の有効化、メニューバーの非表示、ページレイアウトモードの指定などのオプションが含まれます。PDFContentEditor を使用すると、既存の設定を取得したり、特定のフラグを確認したり、必要に応じて更新したりできます。

1. ビューア設定フラグを定義します。
1. [初期化] [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) そして PDF をバインドします。
1. 現在のビューア設定を取得します。
1. 特定のフラグを確認してください。
1. 現在の設定を表示します。

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

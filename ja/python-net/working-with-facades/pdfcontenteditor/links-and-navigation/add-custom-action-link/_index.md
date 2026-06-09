---
title: カスタムアクションリンクを追加
type: docs
weight: 20
url: /ja/python-net/add-custom-action-link/
description: この例では、入力 PDF をバインドし、最初のページにカスタムアクションリンクを追加し、変更された文書を保存します。わかりやすくするために空のアクションリストを使用していますが、実際の実装には実際のアクションを含めることもできます。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python の PDF コンテンツエディタを使用して PDF にカスタムアクションリンクを追加
Abstract: この例は、Facades API 経由で Aspose.PDF for Python を使用して PDF ドキュメントにカスタムアクションリンクを追加する方法を示しています。ページ上にクリック可能な領域を作成し、カスタムアクションを割り当てて、更新した文書を保存する方法を示しています。
---

カスタムアクションリンクを使用すると、スクリプトの実行、ページの移動、アプリケーション固有のコマンドの実行など、クリック時に特定のアクションをトリガーできるインタラクティブ領域を PDF に定義できます。を使用する [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)、ページ、四角形、色、およびアクションを指定して、カスタムアクションリンクを作成できます。

1. PDF コンテンツエディターのインスタンスを作成します。
1. 入力 PDF ドキュメントをバインドします。
1. クリック可能なリンクの長方形を定義します。
1. ページ番号とリンクの色を指定します。
1. カスタムアクションを割り当てます (この例では空白)。
1. 更新した PDF ドキュメントを保存します。

```python
import aspose.pdf.facades as pdf_facades
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as apd
import aspose.pdf as ap

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_custom_action_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add custom action link. Empty action list keeps the sample runnable
    # without requiring additional enum lookups.
    content_editor.create_custom_action_link(
        apd.Rectangle(200, 500, 260, 20),
        1,
        apd.Color.dark_red,
        [],
    )
    # Save updated document
    content_editor.save(outfile)
```

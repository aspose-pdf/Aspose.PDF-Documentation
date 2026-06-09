---
title: JavaScript リンクを追加
type: docs
weight: 30
url: /ja/python-net/add-javascript-link/
description: この例では、入力 PDF をバインドし、クリック時にアラートをトリガーする JavaScript リンクを追加し、変更された文書を保存します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python の PDFContentEditor を使用して PDF に JavaScript リンクを追加する
Abstract: この例は、ファサード API 経由で Aspose.PDF for Python を使用して PDF ドキュメントに JavaScript リンクを追加する方法を示しています。クリックすると JavaScript コードを実行するクリック可能な領域を作成し、更新された PDF を保存する方法を示しています。
---

PDF 内の JavaScript リンクにより、警告の表示、計算の実行、文書コンテンツの動的な変更などのインタラクティブな機能が可能になります。を使用する [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)ページ上にクリック可能な四角形を定義し、それをカスタム JavaScript コードに関連付けることができます。

1. PDF コンテンツエディターのインスタンスを作成します。
1. 入力 PDF ドキュメントをバインドします。
1. クリック可能な JavaScript リンクの四角形を定義します。
1. ページ番号とリンクの色を指定します。
1. クリック時に実行する JavaScript コードを割り当てます。
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


def add_javascript_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add JavaScript link action
    content_editor.create_java_script_link(
        "app.alert('PdfContentEditor JavaScript link');",
        apd.Rectangle(160, 560, 260, 20),
        1,
        apd.Color.orange,
    )
    # Save updated document
    content_editor.save(outfile)
```

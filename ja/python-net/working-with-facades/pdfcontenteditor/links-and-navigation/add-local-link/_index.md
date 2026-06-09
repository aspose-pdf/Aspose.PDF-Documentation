---
title: ローカルリンクを追加
type: docs
weight: 40
url: /ja/python-net/add-local-link/
description: 次の使用例は、入力 PDF を連結し、1 ページ目を指す赤色のローカルリンクを 1 ページ目に追加し、変更した文書を保存します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python の PDF コンテンツエディタを使用して PDF にローカルリンクを追加
Abstract: この例は、Facades API 経由で Aspose.PDF for Python を使用して PDF ドキュメントにローカルリンクを追加する方法を示しています。同じ PDF 内の別のページに移動して更新された文書を保存するクリック可能な領域を作成する方法を示しています。
---

PDF のローカルリンクを使用すると、同じ文書内のページ間をすばやく移動できます。を使用する [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)、あるページを別のページにリンクするクリック可能な長方形を定義できるため、ドキュメントの使いやすさとナビゲーションが向上します。

1. PDF コンテンツエディターのインスタンスを作成します。
1. 入力 PDF ドキュメントをバインドします。
1. クリック可能なローカルリンクの長方形を定義します。
1. ソースページと宛先ページを指定します。
1. リンクの色を設定します。
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


def add_local_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add a local link on page 1 to destination page 1
    content_editor.create_local_link(
        apd.Rectangle(120, 620, 220, 20),
        1,
        1,
        apd.Color.red,
    )
    # Save updated document
    content_editor.save(outfile)
```

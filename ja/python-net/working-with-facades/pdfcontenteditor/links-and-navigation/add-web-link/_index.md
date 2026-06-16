---
title: Web リンクを追加
type: docs
weight: 60
url: /ja/python-net/add-web-link/
description: この例では、入力 PDF をバインドし、Aspose の Python PDF 製品ページを指す青い Web リンク注釈を 1 ページ目に追加し、変更された文書を保存します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python の PDF コンテンツエディタを使用して PDF に Web リンクを追加する
Abstract: この例は、Facades API 経由で Aspose.PDF for Python を使用して PDF ドキュメントにウェブリンクを追加する方法を示しています。指定した URL を Web ブラウザーで開き、更新した文書を保存するためのクリック可能な領域をページ上に作成する方法を示しています。
---

PDF 内の Web リンクを使用すると、ユーザーはオンラインリソース、Web サイト、またはドキュメントに直接移動できます。を使用する [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)、PDF ページ上に長方形の領域を定義できます。この領域をクリックすると、デフォルトの Web ブラウザーで URL が開きます。

1. PDF コンテンツエディターのインスタンスを作成します。
1. 入力 PDF ドキュメントをバインドします。
1. クリック可能な Web リンクの四角形を定義します。
1. URL、ページ番号、リンクの色を指定します。
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


def add_web_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add a web link annotation to page 1
    content_editor.create_web_link(
        apd.Rectangle(100, 650, 200, 20),
        "https://products.aspose.com/pdf/python-net/",
        1,
        apd.Color.blue,
    )
    # Save updated document
    content_editor.save(outfile)
```

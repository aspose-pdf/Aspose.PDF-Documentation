---
title: アプリケーションリンクを追加
type: docs
weight: 10
url: /ja/python-net/add-application-link/
description: この例では、入力 PDF をバインドし、最初のページにアプリケーション起動リンクを追加し、変更された文書を保存します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python の PDFContentEditor を使用して PDF にアプリケーション起動リンクを追加する
Abstract: この例は、Facades API 経由で Aspose.PDF for Python を使用して PDF ドキュメントにアプリケーション起動リンクを追加する方法を示しています。クリックすると指定したアプリケーションが開くクリック可能な領域を作成し、更新された PDF を保存する方法を示します。
---

PDF には、外部アプリケーションを起動するリンクなどのインタラクティブな要素を含めることができます。を使用する [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)ページ上に長方形の領域を定義して、クリックすると特定の実行ファイルを開くことができます。

1. PDF コンテンツエディターのインスタンスを作成します。
1. 入力 PDF ドキュメントをバインドします。
1. クリック可能なリンクの四角形領域を定義します。
1. 起動するアプリケーションパスを指定します。
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


def add_application_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add application launch link
    content_editor.create_application_link(
        apd.Rectangle(180, 530, 260, 20),
        "notepad.exe",
        1,
        apd.Color.purple,
    )
    # Save updated document
    content_editor.save(outfile)
```

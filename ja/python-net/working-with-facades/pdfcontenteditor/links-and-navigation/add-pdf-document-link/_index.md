---
title: PDF ドキュメントリンクを追加
type: docs
weight: 50
url: /ja/python-net/add-pdf-document-link/
description: 次の使用例は、入力 PDF を連結し、別の PDF のページへの緑色のリンクを追加し、変更された文書を保存します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python の PDF コンテンツエディタを使用して PDF ドキュメントリンクを追加する
Abstract: この例は、Facades API 経由で Aspose.PDF for Python を使用して別の PDF ドキュメントへのリンクを追加する方法を示しています。クリック可能な領域を作成して別の PDF を開き、更新した文書を保存する方法を示しています。
---

PDF ドキュメントリンクを使用すると、ある PDF から別の PDF にシームレスに移動できます。を使用する [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)、別のPDFファイル内のページにリンクするクリック可能な長方形を定義して、ドキュメントをインタラクティブでつながりのあるものにすることができます。

1. PDF コンテンツエディターのインスタンスを作成します。
1. 入力 PDF ドキュメントをバインドします。
1. クリック可能なリンクの長方形を定義します。
1. リンクされた PDF ファイル、ソースページ、およびリンク先ページを指定します。
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


def add_pdf_document_link(infile, linked_pdf, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add link to another PDF document
    content_editor.create_pdf_document_link(
        apd.Rectangle(140, 590, 240, 20),
        linked_pdf,
        1,
        1,
        apd.Color.green,
    )
    # Save updated document
    content_editor.save(outfile)
```

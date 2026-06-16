---
title: ラバースタンプを追加
type: docs
weight: 10
url: /ja/python-net/add-rubber-stamp/
description: 次の使用例は、入力 PDF を連結し、最初の 4 ページに緑色の「承認済み」ラバースタンプを追加し、変更された文書を保存します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python の PDF コンテンツエディタを使用して PDF にラバースタンプ注釈を追加
Abstract: この例は、Facades API 経由で Aspose.PDF for Python を使用して PDF ドキュメントにラバースタンプの注釈を追加する方法を示しています。ラバースタンプを使用すると、承認、レビュー、またはカスタムラベルが付いたページに視覚的にマークを付けることができます。
---

ラバースタンプの注釈は、PDF で承認や審査状況、その他の注記を示すために一般的に使用されます。を使用する [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)、スタンプの四角形を定義したり、テキストやコメントを設定したり、色を選択したり、それをドキュメントの複数のページに適用したりできます。

1. PDF コンテンツエディターのインスタンスを作成します。
1. 入力 PDF ドキュメントをバインドします。
1. 1 ～ 4 ページを繰り返します。
1. カスタムテキスト、コメント、色を含むラバースタンプの注釈を追加します。
1. 更新した PDF ドキュメントを保存します。

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_rubber_stamp(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    for i in range(1, 5):
        content_editor.create_rubber_stamp(
            i,
            apd.Rectangle(120, 450, 180, 60),
            "Approved",
            "Approved by reviewer",
            apd.Color.green,
        )
    # Save updated document
    content_editor.save(outfile)
```

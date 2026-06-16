---
title: スタンプを ID で移動
type: docs
weight: 80
url: /ja/python-net/move-stamp-by-id-example/
description: この例では、ラバースタンプを 1 ページ目に追加し、その ID を使用して新しい位置に移動してから、更新された文書を保存します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python の PDF コンテンツエディタを使用して PDF 内のラバースタンプを ID で移動する
Abstract: この例は、Facades API 経由で Aspose.PDF for Python を使用して PDF 内の既存のラバースタンプアノテーションの位置を変更する方法を示しています。スタンプを作成し、その ID を使用してプログラムで移動する方法を示しています。
---

PDF にラバースタンプの注釈を追加した後、その位置を調整する必要がある場合があります。'move_stamp_by_id () 'メソッドを使用すると、スタンプを再作成しなくても、識別子に基づいてスタンプを再配置できます。これは、スタンプの配置を動的に調整する必要がある自動ワークフローで役立ちます。

1. を作成 [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) インスタンス。
1. 入力 PDF ドキュメントをバインドします。
1. ラバースタンプの注釈を追加します。
1. ID を使用してスタンプを移動します。
1. 更新した PDF ドキュメントを保存します。

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def move_stamp_by_id_example(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(300, 420, 180, 60),
        "Approved",
        "Move this stamp by ID",
        apd.Color.green,
    )

    # Move stamp by ID overload
    content_editor.move_stamp_by_id(1, 1, 240, 360)

    # Save updated document
    content_editor.save(outfile)
```    

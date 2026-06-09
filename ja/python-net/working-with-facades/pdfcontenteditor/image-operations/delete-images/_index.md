---
title: PDF から画像を削除
type: docs
weight: 20
url: /ja/python-net/delete-images/
description:
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python の PDF コンテンツエディターを使用して PDF ページから特定の画像を削除する
Abstract: この例は、Facades API 経由で Aspose.PDF for Python を使用して PDF ドキュメントから特定の画像を削除する方法を示しています。特定のページの画像をターゲットにして、更新した文書を保存する方法を示しています。
---

場合によっては、すべてのビジュアルを消去するのではなく、特定の画像のみを PDF から削除したい場合があります。で [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)ページ番号と画像インデックスを指定することで、選択した画像を削除できます。

このコードスニペットは、入力 PDF をバインドし、1 ページ目の 2 番目の画像を削除し、変更した PDF を保存します。他の画像はそのまま残ります。

1. PDF コンテンツエディターのインスタンスを作成します。
1. 入力 PDF ドキュメントをバインドします。
1. 指定されたページから特定の画像を削除します。
1. 更新した PDF ドキュメントを保存します。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_images(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Delete image on page 1
    content_editor.delete_image(1, [2])
    # Save updated document
    content_editor.save(outfile)
```

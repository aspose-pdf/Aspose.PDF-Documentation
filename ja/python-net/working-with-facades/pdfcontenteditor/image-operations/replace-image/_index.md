---
title: PDF 内の画像の置換
type: docs
weight: 30
url: /ja/python-net/replace-image/
description: 次の使用例は、入力 PDF を連結し、1 ページ目の最初の画像を新しい画像に置き換え、変更した文書を保存します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python の PDF コンテンツエディターを使用して PDF 内の画像を置き換える
Abstract: この例は、Facades API 経由で Aspose.PDF for Python を使用して PDF ドキュメント内の既存の画像を置き換える方法を示しています。ページ上の特定の画像をターゲットにして新しい画像に置き換え、更新された PDF を保存する方法を示しています。
---

PDF には、ロゴ、図、写真など、更新や置換が必要な画像が含まれていることがよくあります。と [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)ページ番号、画像インデックス、および新しい画像ファイルパスを指定することで、特定のページの特定の画像を置き換えることができます。

1. PDF コンテンツエディターのインスタンスを作成します。
1. 入力 PDF ドキュメントをバインドします。
1. 特定のページの特定の画像を置き換えます。
1. 更新した PDF ドキュメントを保存します。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_image(infile, image_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace image on page 1
    content_editor.replace_image(1, 1, image_file)
    # Save updated document
    content_editor.save(outfile)
```

---
title: スタンプをインデックスで移動
type: docs
weight: 90
url: /ja/python-net/move-stamp-by-index/
description: Aspose.PDF for Python を使用してページ上のインデックスを使用して PDF 内のラバースタンプの注釈の位置を変更する方法
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 索引ベースの位置を使用して PDF 内のラバースタンプを移動する
Abstract: この例は、Facades API 経由で Aspose.PDF for Python のページ上のインデックスを使用して PDF 内のラバースタンプの注釈の位置を変更する方法を示しています。複数のスタンプを作成し、移動操作に備えて準備することを強調しています。
---

PDF編集では、既存のラバースタンプの位置を調整する必要がある場合があります。このコードスニペットは、以下の方法を示しています。

- 同じページに複数のスタンプを追加
- インデックスを使って再配置の準備をする
- 必要に応じて、ページ、インデックス、および新しい座標を指定してスタンプを移動します

'move_stamp (ページ番号、スタンプインデックス、new_x、new_y) 'メソッドを使うと、スタンプを正確に再配置できます。

1. を作成 [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 対象。
1. PDF をエディターにバインドします。
1. ページに複数のラバースタンプを追加します。
1. 移動操作を実行する前に文書を保存してください。
1. 特定のスタンプをインデックス単位で移動します。
1. 更新した PDF を保存します。

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def move_stamp_by_index(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    content_editor.create_rubber_stamp(
        2,
        apd.Rectangle(200, 380, 180, 60),
        "Draft",
        "Draft stamp for ID-based operations",
        apd.Color.orange,
    )

    content_editor.create_rubber_stamp(
        2,
        apd.Rectangle(200, 480, 180, 60),
        "Draft",
        "Draft stamp for ID-based operations",
        apd.Color.orange,
    )
    content_editor.save(outfile)

    # Move first stamp on page 1 by index
    # content_editor.move_stamp(1, 1, 10, 10)
    # Save updated document
    content_editor.save(outfile)
```    

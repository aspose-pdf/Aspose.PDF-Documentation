---
title: IDでスタンプを管理
type: docs
weight: 95
url: /ja/python-net/manage-stamp-by-id/
description: Aspose.PDF for Python を使用して PDF 内のラバースタンプアノテーションを固有の ID で操作する方法
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python の PDF コンテンツエディタを使用して PDF 内のラバースタンプを ID 別に管理
Abstract: この例は、Facades API 経由で Aspose.PDF for Python を使用して、PDF 内のラバースタンプアノテーションを固有の ID で操作する方法を示しています。他のスタンプに影響を与えずに、特定のページの特定のスタンプを表示または非表示にすることができます。
---

複数のラバースタンプがあるPDFでは、IDに基づいて個々のスタンプを制御すると便利です。「hide_stamp_by_id ()」メソッドと「show_stamp_by_id ()」メソッドを使用すると、選択的に可視性を制御できます。この例では以下の方法を示しています。

- ユニークIDのスタンプを複数追加
- 特定のページのスタンプを非表示にする
- スタンプを別のページに表示する

ID ベースの操作を使用すると、ページ位置やその他の属性によってスタンプを追跡する必要がなくなります。

1. を作成 [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) インスタンス。
1. 入力 PDF ドキュメントをバインドします。
1. 特定のIDのラバースタンプを追加します。
1. ID とページ番号に基づいてスタンプの表示/非表示を切り替えます。
1. 更新した PDF ドキュメントを保存します。

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def manage_stamp_by_id(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    content_editor.create_rubber_stamp(
        1,
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

    # Apply ID-based stamp operations
    content_editor.hide_stamp_by_id(1, 1)
    content_editor.show_stamp_by_id(1, 2)

    # Save updated document
    content_editor.save(outfile)
```

---
title: ポップアップ注釈の追加
type: docs
weight: 40
url: /ja/python-net/add-popup-annotation/
description: この例では、PDF を読み込み、最初のページにポップアップ注釈を追加し、変更された文書を保存します。ポップアップはデフォルトで表示されるように設定されており、指定されたコメントテキストが表示されます。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF にポップアップアノテーションを追加する
Abstract: この例は、Facades API 経由で Aspose.PDF for Python を使用して PDF ドキュメントにポップアップアノテーションを挿入する方法を示しています。ポップアップ領域を定義する方法、注釈テキストを設定する方法、表示を制御する方法、更新した文書を保存する方法を説明します。
---

ポップアップ注釈は、PDF ファイルにコメント、説明、またはインタラクティブなメモを追加するのに役立ちます。を使用する [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)、場所、コンテンツ、表示、ページ番号を指定することで、ポップアップ注釈をプログラムで作成できます。

1. PDF コンテンツエディターオブジェクトを作成します。
1. 入力 PDF をバインドします。
1. ポップアップ注釈の四角形を定義します。
1. ポップアップ注釈を追加します。
1. 更新したドキュメントを保存します。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_popup_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add popup annotation to page 1
    content_editor.create_popup(
        apd.Rectangle(220, 520, 180, 80),
        "This is a popup annotation",
        True,
        1,
    )
    # Save updated document
    content_editor.save(outfile)
```

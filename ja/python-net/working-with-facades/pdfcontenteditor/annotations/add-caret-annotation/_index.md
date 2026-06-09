---
title: キャレット注釈を追加
type: docs
weight: 10
url: /ja/python-net/add-caret-annotation/
description: 次の使用例は、既存の PDF を読み込み、最初のページにキャレット注釈を追加して、変更した文書を保存します。注釈には赤いキャレット記号と説明のコメントテキストが含まれています。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF にキャレットアノテーションを追加する
Abstract: この例は、Facades API 経由で Aspose.PDF for Python を使用して PDF ドキュメントにキャレットアノテーションを追加する方法を示しています。このサンプルでは、PDF ファイルをバインドする方法、四角形を使用して注釈の配置を定義する方法、キャレットプロパティを設定する方法、および更新されたドキュメントを保存する方法を示しています。
---

キャレット注釈は通常、文書内のテキスト挿入や編集コメントを示すために使用されます。PDFContentEditor では、ページ番号、注釈の境界、コールアウト領域、シンボル、注記テキスト、および色を指定することで、キャレット注釈をプログラムで追加できます。

1. 作成 [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 対象。
1. 入力 PDF をバインドします。
1. キャレット注釈パラメータの定義:
  - 注釈を追加するページ番号
  - キャレット四角形 (注釈位置)
  - コールアウト長方形 (テキスト領域)
  - 記号 (「P」など)
  - 注釈テキスト
  - 注釈色
1. キャレット注釈を追加します。
1. 更新したドキュメントを保存します。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_caret_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add caret annotation to page 1
    content_editor.create_caret(
        1,
        apd.Rectangle(350, 400, 10, 10),
        apd.Rectangle(300, 380, 115, 15),
        "P",
        "This is a caret annotation",
        apd.Color.red,
    )
    # Save updated document
    content_editor.save(outfile)
```

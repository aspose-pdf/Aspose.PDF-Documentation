---
title: マークアップ注釈の追加
type: docs
weight: 30
url: /ja/python-net/add-markup-annotation/
description: この例では、入力 PDF をバインドし、最初のページに 4 つの異なるマークアップ注釈を追加し、更新された文書を保存します。アノテーションはそれぞれ異なるマークアップスタイルと色を示しています。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF にハイライト、下線、取り消し線、曲がりくねったマークアップの注釈を追加する
Abstract: この例は、Facades API 経由で Aspose.PDF for Python を使用して PDF ドキュメントに複数のマークアップ注釈 (ハイライト、下線、取り消し線、波打ち) を追加する方法を示しています。このサンプルでは、注釈領域を定義し、マークアップタイプを指定し、色を適用し、変更した文書を保存する方法を示しています。
---

マークアップ注釈は、PDF 内のテキストを強調したり確認したりするために使用されます。PDFContentEditor では、四角形の領域、コメントテキスト、マークアップタイプ、ページ番号、色を指定することで、さまざまなマークアップスタイルをプログラムで適用できます。

1. 作成 [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 対象。
1. 入力 PDF をバインドします。
1. 注釈長方形を定義します。
1. マークアップ注釈を追加します。
1. 更新したドキュメントを保存します。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_markup_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add markup annotation to page 1
    content_editor.create_markup(
        apd.Rectangle(120, 440, 200, 20),
        "This is a highlight annotation",
        0,
        1,
        apd.Color.yellow,
    )
    content_editor.create_markup(
        apd.Rectangle(110, 542, 200, 20),
        "This is a underline annotation",
        1,
        1,
        apd.Color.yellow,
    )
    content_editor.create_markup(
        apd.Rectangle(120, 568, 200, 20),
        "This is a strikeout annotation",
        2,
        1,
        apd.Color.orange_red,
    )
    content_editor.create_markup(
        apd.Rectangle(110, 598, 200, 20),
        "This is a squiggly annotation",
        3,
        1,
        apd.Color.dark_blue,
    )
    # Save updated document
    content_editor.save(outfile)
```

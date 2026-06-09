---
title: カーブ注釈を追加
type: docs
weight: 20
url: /ja/python-net/add-curve-annotation/
description: 次の使用例は、入力 PDF を連結し、最初のページに破線を描き、変更した文書を保存します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python の PDF コンテンツエディタを使用して PDF にカーブアノテーションを追加
Abstract: この例は、Facades API 経由で Aspose.PDF for Python を使用して PDF ドキュメントにカーブアノテーションを追加する方法を示しています。曲線の頂点、境界線のスタイル、注釈の境界、テキストコンテンツを定義し、更新された文書を保存する方法を示しています。
---

カーブ注釈は、PDF内の不規則なパスや形状を強調表示したり、視覚的に強調したり、重要な領域をマークしたりするために使用されます。を使用する [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)、頂点のシーケンス、境界線のスタイル、可視性、注釈長方形、説明文を指定して曲線を描くことができます。

1. PDF コンテンツエディターオブジェクトを作成します。
1. 入力 PDF をバインドします。
1. カーブのプロパティを設定します。
1. カーブアノテーションを描画します。
1. 更新したドキュメントを保存します。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_curve_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    line_info = pdf_facades.LineInfo()
    line_info.border_style = 1  # 1 - Dashed
    line_info.vertice_coordinate = [120, 520, 160, 560, 220, 540, 280, 580]
    line_info.visibility = True
    content_editor.draw_curve(
        line_info,
        1,
        apd.Rectangle(110, 510, 220, 100),
        "This is curve annotation",
    )

    # Save output PDF file
    content_editor.save(outfile)
```

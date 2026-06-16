---
title: ライン注釈を追加
type: docs
weight: 30
url: /ja/python-net/add-line-annotation/
description: この例では、入力 PDF をバインドし、四角い線の終端が付いた赤い線の注釈を描画し、変更した PDF を保存します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python の PDF コンテンツエディターを使用して PDF にラインアノテーションを追加
Abstract: この例は、Facades API 経由で Aspose.PDF for Python を使用して PDF ドキュメントに行アノテーションを追加する方法を示しています。線の始点と終点、四角形の境界、外観プロパティを定義し、更新された文書を保存する方法を説明します。
---

ライン注釈は、テキストを強調したり、関係を強調したり、PDF 内の特定の領域に注意を引いたりするのに便利です。と [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)、始点と終点、境界矩形、色、境界スタイル、および行末を指定することで、プログラムで線注釈を作成できます。

1. PDF コンテンツエディターオブジェクトを作成します。
1. 入力 PDF をバインドします。
1. ライン注釈プロパティを定義します。
1. Line アノテーションを追加します。
1. 更新したドキュメントを保存します。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_line_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    # Create LineAnnotation object
    rect = apd.Rectangle(100, 100, 200, 200)
    contents = "This is line annotation"
    content_editor.create_line(
        rect,
        contents,
        100,
        100,
        200,
        200,
        1,
        1,
        apd.Color.red,
        "Solid",
        [3, 2],
        ["Square"],
    )

    # Save output PDF file
    content_editor.save(outfile)
```

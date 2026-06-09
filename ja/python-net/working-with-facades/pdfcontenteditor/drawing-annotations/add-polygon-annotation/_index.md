---
title: ポリゴン注釈を追加
type: docs
weight: 40
url: /ja/python-net/add-polygon-annotation/
description: 次の使用例は、入力 PDF を連結し、最初のページに実線の多角形を描き、変更した文書に注釈を付けて保存します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python の PDF コンテンツエディターを使用して PDF にポリゴンアノテーションを追加
Abstract: この例は、Facades API 経由で Aspose.PDF for Python を使用して PDF ドキュメントにポリゴンアノテーションを追加する方法を示しています。ポリゴンの頂点、境界線のスタイル、注釈の境界、説明文を定義し、更新された文書を保存する方法を示しています。
---

ポリゴン注釈は、PDF内の不規則な領域や形状を強調表示したり、視覚的に強調したり、特定の領域をマークしたりするために使用されます。を使う [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)、頂点座標、境界線のスタイル、ページ番号、および注釈長方形を指定してポリゴンを作成できます。

1. PDF コンテンツエディターオブジェクトを作成します。
1. 入力 PDF をバインドします。
1. ポリゴンのプロパティを設定します。
1. ポリゴンアノテーションを追加します。
1. 更新したドキュメントを保存します。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_polygon_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    line_info = pdf_facades.LineInfo()
    line_info.border_style = 0  # 0 - Solid
    line_info.vertice_coordinate = [100, 200, 150, 260, 220, 220, 200, 160]
    content_editor.create_polygon(
        line_info,
        1,
        apd.Rectangle(90, 150, 150, 120),
        "This is polygon annotation",
    )

    # Save output PDF file
    content_editor.save(outfile)
```

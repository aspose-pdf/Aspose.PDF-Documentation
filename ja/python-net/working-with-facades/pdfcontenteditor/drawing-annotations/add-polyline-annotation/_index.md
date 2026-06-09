---
title: ポリライン注釈を追加
type: docs
weight: 50
url: /ja/python-net/add-polyline-annotation/
description: この例では、入力 PDF をバインドし、最初のページに実線のポリラインを作成し、変更した文書に注釈を付けて保存します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python の PDF コンテンツエディタを使用して PDF にポリライン注釈を追加
Abstract: この例は、Facades API 経由で Aspose.PDF for Python を使用して PDF ドキュメントにポリラインアノテーションを追加する方法を示しています。一連の頂点、境界線のスタイル、注釈長方形、テキストを定義し、更新された文書を保存する方法を示しています。
---

ポリライン注釈を使用すると、PDF 内の接続された一連の線分を強調表示できます。を使用する [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)、頂点の座標、境界線のスタイル、ページ番号、注釈の境界を指定してポリラインを描くことができます。これは、図や文書内の経路、傾向、つながりを視覚的に表すのに便利です。

1. PDF コンテンツエディターオブジェクトを作成します。
1. 入力 PDF をバインドします。
1. ポリラインのプロパティを設定します。
1. ポリライン注釈を追加します。
1. 更新したドキュメントを保存します。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_polyline_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    line_info = pdf_facades.LineInfo()
    line_info.border_style = 0  # 0 - Solid
    line_info.vertice_coordinate = [120, 420, 180, 460, 230, 430, 290, 470]
    content_editor.create_poly_line(
        line_info,
        1,
        apd.Rectangle(110, 410, 200, 90),
        "This is polyline annotation",
    )

    # Save output PDF file
    content_editor.save(outfile)
```

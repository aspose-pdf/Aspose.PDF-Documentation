---
title: PDF にページ区切りを追加
type: docs
weight: 20
url: /ja/python-net/add-page-breaks-in-pdf/
description: Python 用 Aspose.PDF を使用して PDF ドキュメントにページ区切りを挿入します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python でプログラムで PDF ページに改ページを追加する
Abstract: Aspose.PDF for Python を使用して PDF ドキュメントにページ区切りを挿入する方法を説明します。この例は、ページを指定した垂直位置で分割する方法を示しています。これにより、開発者はコンテンツを再編成したり、追加のページを動的に作成したりできます。
---

改ページは、長い PDF ページを複数のページに分割する必要がある場合や、文書全体でのコンテンツの配分方法を制御する必要がある場合に便利です。Aspose.PDF for Python を使用すると、開発者は PDF を手動で編集しなくても、特定の位置に改ページを挿入できます。

この記事では、の「add_page_break」メソッドの使用方法を説明します [PDF ファイルエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) クラスを使用して、選択したページの定義した垂直座標にページ区切りを挿入します。このメソッドは新しいページを作成し、ブレークポイントの下にあるコンテンツをそのページに移動します。

1. PDF ファイルエディターオブジェクトを作成します。
1. 改ページ位置を定義します。
1. ページ区切りを挿入します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Add Page Breaks in PDF
def add_page_breaks_in_pdf(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.add_page_break(
        infile,
        outfile,
        [
            pdf_facades.PdfFileEditor.PageBreak(1, 400),
        ],
    )
```

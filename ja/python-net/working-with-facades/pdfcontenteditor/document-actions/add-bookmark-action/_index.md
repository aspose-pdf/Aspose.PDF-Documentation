---
title: 「ブックマークを追加」アクション
type: docs
weight: 10
url: /ja/python-net/add-bookmark-action/
description: この例では、入力 PDF をバインドし、1 ページ目に移動する「PDFContentEditor Bookmark」というラベルの付いたブックマークを作成し、更新された文書を保存します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF にナビゲーションアクション付きのブックマークを作成する
Abstract: この例は、Facades API 経由で Aspose.PDF for Python を使用して、ナビゲーションアクションを含むブックマークを PDF ドキュメントに追加する方法を示しています。ブックマークのテキスト、外観、およびユーザーを特定のページに誘導するアクションを設定する方法を示しています。
---

ブックマークを使用すると、PDF 文書内をすばやく移動できます。を使用する [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)、プログラムでブックマークを作成し、ページへの移動などのアクションを割り当てることができます。色やスタイル (太字や斜体など) のオプションを含め、ブックマークの外観をカスタマイズすることもできます。

1. PDF コンテンツエディターオブジェクトを作成します。
1. 入力 PDF をバインドします。
1. ブックマークのプロパティを定義します。
1. ブックマークアクションを割り当てます。
1. 更新したドキュメントを保存します。

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_bookmark_action(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add a bookmark action to navigate to page 1
    content_editor.create_bookmarks_action(
        "PdfContentEditor Bookmark",
        apd.Color.blue,
        True,
        False,
        "",
        "GoTo",
        "1",
    )
    # Save updated document
    content_editor.save(outfile)
```
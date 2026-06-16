---
title: ムービー注釈を追加
type: docs
weight: 10
url: /ja/python-net/add-movie-annotation/
description: 次の使用例は、入力 PDF をバインドし、1 ページにムービー注釈を追加し、更新された PDF を保存します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python の PDF コンテンツエディターを使用して PDF にムービーアノテーションを追加
Abstract: この例は、Facades API 経由で Aspose.PDF for Python を使用して PDF ドキュメントにムービー (ビデオ) を埋め込む方法を示しています。PDF 内で動画を直接再生するクリック可能な注釈を追加する方法を示しています。
---

PDF のムービー注釈を使用すると、ビデオなどのマルチメディアコンテンツを文書に埋め込むことができます。を使用する [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)、ビデオが表示されるページ上の長方形を定義できます。クリックすると、PDF から動画を直接再生できるので、ドキュメントがよりインタラクティブで魅力的なものになります。

1. PDF コンテンツエディターのインスタンスを作成します。
1. 入力 PDF ドキュメントをバインドします。
1. ムービーアノテーションの長方形を定義します。
1. 埋め込むビデオファイルを指定します。
1. 注釈のページ番号を割り当てます。
1. 更新した PDF ドキュメントを保存します。

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_movie_annotation(infile, movie_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add movie annotation to page 1
    content_editor.create_movie(apd.Rectangle(80, 500, 220, 120), movie_file, 1)
    # Save updated document
    content_editor.save(outfile)
```

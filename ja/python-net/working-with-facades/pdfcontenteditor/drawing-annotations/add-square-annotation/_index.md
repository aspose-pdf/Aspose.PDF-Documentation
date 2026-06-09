---
title: 四角形の注釈を追加
type: docs
weight: 60
url: /ja/python-net/add-square-annotation/
description: 次の使用例は、入力 PDF を連結し、最初のページに塗りつぶされた青い四角形の注釈を追加し、変更された文書を保存します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python の PDF コンテンツエディターを使用して PDF に四角形の注釈を追加
Abstract: この例は、Facades API 経由で Aspose.PDF for Python を使用して PDF ドキュメントに四角形の注釈を追加する方法を示しています。注釈長方形、テキストコンテンツ、色、塗りつぶしオプションを定義し、更新した文書を保存する方法を示しています。
---

四角形の注釈は通常、関心のある領域を強調したり、重要なセクションをマークしたり、PDF文書に視覚的な手がかりを与えたりする場合に使用されます。使用方法 [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)、境界長方形、コンテンツテキスト、境界線の色、塗りつぶしオプション、ページ番号、境界線の幅を指定することで、正方形 (または円形) の注釈を作成できます。

1. PDF コンテンツエディターオブジェクトを作成します。
1. 入力 PDF をバインドします。
1. Square アノテーションを定義します。
1. Square アノテーションを追加します。
1. 更新したドキュメントを保存します。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_square_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    # Create SquareAnnotation object
    rect = apd.Rectangle(100, 300, 200, 400)
    contents = "This is square annotation"
    content_editor.create_square_circle(rect, contents, apd.Color.blue, True, 1, 3)

    # Save output PDF file
    content_editor.save(outfile)
```

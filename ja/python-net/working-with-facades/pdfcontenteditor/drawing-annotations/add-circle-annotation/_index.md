---
title: 円の注釈を追加
type: docs
weight: 10
url: /ja/python-net/add-circle-annotation/
description: 次の使用例は、入力 PDF を連結し、最初のページに円形の注釈を作成し、変更した文書を保存します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python の PDF コンテンツエディタを使用して PDF に円形の注釈を追加
Abstract: この例は、Facades API 経由で Aspose.PDF for Python を使用して PDF ドキュメントに円の注釈を追加する方法を示しています。アノテーションの境界を定義し、コンテンツテキストを設定し、色と外観を設定し、更新されたドキュメントを保存する方法を示します。
---

円形の注釈は、PDF 文書内の関心領域を強調表示するのに便利です。と [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)、円の境界を定義する長方形と、注釈テキスト、色、塗りつぶしオプション、ページ番号、境界線の幅を指定することで、円形を作成できます。

1. PDF コンテンツエディターオブジェクトを作成します。
1. 入力 PDF をバインドします。
1. 円の境界を定義します。
1. Circle アノテーションを追加します。
1. 更新したドキュメントを保存します。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_circle_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    # Create CircleAnnotation object
    rect = apd.Rectangle(300, 300, 400, 400)
    contents = "This is circle annotation"
    content_editor.create_square_circle(rect, contents, apd.Color.blue, False, 1, 3)

    # Save output PDF file
    content_editor.save(outfile)
```

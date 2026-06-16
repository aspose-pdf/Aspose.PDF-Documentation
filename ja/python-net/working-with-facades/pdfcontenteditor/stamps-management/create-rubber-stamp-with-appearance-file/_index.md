---
title: 外観ファイルを使用してラバースタンプを作成
type: docs
weight: 20
url: /ja/python-net/create-rubber-stamp-with-appearance-file/
description: この例では、入力 PDF をバインドし、イメージファイルをスタンプの外観として使用して 1 ページ目にラバースタンプを作成し、更新された PDF を保存します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDFコンテンツエディターを使用して外観をカスタマイズしたラバースタンプをPDFに作成
Abstract: この例は、Facades API 経由で Aspose.PDF for Python を使用して、カスタム外観 (画像) のラバースタンプ注釈を PDF ドキュメントに追加する方法を示しています。カスタムスタンプを使用すると、ロゴ、署名、またはブランドビジュアルをスタンプの一部として含めることができます。
---

ラバースタンプの注釈は、テキストだけでなく、画像ファイルを外観として使用してカスタマイズすることもできます。この方法は、PDF ページに会社のロゴ、署名スタンプ、その他の視覚的表示を追加する場合に便利です。

1. を作成 [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) インスタンス。
1. 入力 PDF ドキュメントをバインドします。
1. スタンプの長方形を定義します。
1. カスタムイメージファイルを使用して、ラバースタンプの外観を定義します。
1. スタンプのテキストと色を設定します。
1. 更新した PDF ドキュメントを保存します。

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_rubber_stamp_with_appearance_file(infile, image_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Create rubber stamp using appearance_file overload (image path)
    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(100, 400, 200, 60),
        "Stamp with custom appearance",
        apd.Color.dark_green,
        image_file,
    )
    # Save updated document
    content_editor.save(outfile)
```

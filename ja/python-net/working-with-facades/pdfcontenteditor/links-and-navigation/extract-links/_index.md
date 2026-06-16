---
title: リンクを抽出
type: docs
weight: 70
url: /ja/python-net/extract-links/
description: この例では、入力 PDF をバインドし、すべてのリンクを抽出し、それらの座標と URI (利用可能な場合) を出力します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python の PDF コンテンツエディターを使用して PDF からリンクを抽出する
Abstract: この例は、Facades API 経由で Aspose.PDF for Python を使用して PDF ドキュメントからすべてのリンクを抽出する方法を示しています。PDF に埋め込まれている Web リンクやその他の実行可能なリンクを識別して取得する方法を示しています。
---

PDF には、Web リンク、ドキュメントリンク、カスタムアクションなどのインタラクティブな要素が含まれていることがよくあります。を使用する [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)、PDF からすべてのリンク注釈をプログラムで抽出できます。これにより、URL を検証したり、文書内のナビゲーションパターンを分析したりするなど、リンクを検査または処理できます。

1. PDF コンテンツエディターのインスタンスを作成します。
1. 入力 PDF ドキュメントをバインドします。
1. 'extract_link () 'を使用してすべてのリンクを抽出します。
1. 抽出されたリンクを繰り返し処理します。
1. リンクがリンク注釈であるかどうか、およびそのアクションが GoTouriAction であるかどうかを確認します。
1. 長方形の座標と URI を出力します。
1. リンクが見つからない場合は、メッセージを表示します。

```python
import aspose.pdf.facades as pdf_facades
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as apd
import aspose.pdf as ap

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def extract_links(infile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Extract links from the document
    links = content_editor.extract_link()

    count = 0
    for link in links:
        count += 1
        print(f"Link {count}: {link.rect}")
        if is_assignable(link, ap.annotations.LinkAnnotation):
            annotation = cast(ap.annotations.LinkAnnotation, link)
            if is_assignable(annotation.action, ap.annotations.GoToURIAction):
                action = cast(ap.annotations.GoToURIAction, annotation.action)
                print(f"  URI: {action.uri}")

    if count == 0:
        print("No links found")
```

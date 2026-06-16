---
title: テキストをステートに置換
type: docs
weight: 50
url: /ja/python-net/replace-text-with-state/
description: この例では、出現する「ソフトウェア」がすべて「SOFTWARE」に置き換えられ、フォントサイズが 14 の青色でフォーマットされています。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python の PDFContentEditor を使用して PDF 内のテキストをカスタムフォーマットに置き換える
Abstract: この例は、Facades API 経由で Aspose.PDF for Python を使用してカスタムフォーマットを適用しながら PDF ドキュメント内のテキストを置き換える方法を示しています。置換時にテキストの色とフォントサイズを制御する方法を示しています。
---

PDF 内のテキストを更新する場合、置換後のコンテンツが目立つようにしたい場合があります。TextState オブジェクトを使用すると、色やフォントサイズなどのスタイルを定義し、それを置換されたすべてのテキストに適用できます。

1. を作成 [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)  インスタンス。
1. 入力 PDF ドキュメントをバインドします。
1. カスタムフォーマットで TextState を定義します。
1. 置換スコープを設定します。
1. 文書全体のテキストを置換します。
1. 更新した PDF ドキュメントを保存します。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_with_state(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.blue
    text_state.font_size = 14

    # Replace text with explicit text formatting
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text("software", "SOFTWARE", text_state)
    # Save updated document
    content_editor.save(outfile)
```

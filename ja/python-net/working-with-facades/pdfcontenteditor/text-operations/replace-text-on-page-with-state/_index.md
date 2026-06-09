---
title: ページ上のテキストを状態に置換
type: docs
weight: 20
url: /ja/python-net/replace-text-on-page-with-state/
description: この例では、1 ページ目の「software」という単語がすべて表示され、フォントサイズが 12 の赤いテキストを使用して「SOFTWARE PAGE 1」に置き換えられます。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python の PDFContentEditor を使用して特定のページのテキストをカスタムフォーマットに置き換える
Abstract: この例は、Facades API 経由で Aspose.PDF for Python を使用してカスタムフォーマットを適用しながら、PDF 内の特定のページのテキストを置き換える方法を示しています。テキスト置換時にフォントのサイズや色を制御する方法を示しています。
---

PDF 内のテキストを置き換える際に、色やフォントサイズなどの書式を変更する必要がある場合もあります。TextState を使用すると、スタイルプロパティを定義して置換時に適用できます。これにより、変更されたテキストを強調表示したり、文書全体で一貫したフォーマットを適用したりできます。

1. を作成 [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) インスタンス。
1. 入力 PDF ドキュメントをバインドします。
1. カスタムフォーマットで TextState を定義します。
1. 交換戦略を設定します。
1. 特定のページのテキストを置換します。
1. 更新した PDF ドキュメントを保存します。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_on_page_with_state(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.red
    text_state.font_size = 12

    # Replace text on a specific page with explicit text formatting
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text("software", 1, "SOFTWARE PAGE 1", text_state)
    # Save updated document
    content_editor.save(outfile)
```

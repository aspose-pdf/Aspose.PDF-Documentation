---
title: ページ上のテキストを置換
type: docs
weight: 10
url: /ja/python-net/replace-text-on-page/
description: この例では、「PDF」という単語が最初に出現した部分が、指定されたフォントサイズを使用して「Page 1 Replaced Text」に置き換えられます。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python の PDFコンテンツエディターを使用して特定のページのテキストを置換する
Abstract: この例は、Facades API 経由で Aspose.PDF for Python を使用して PDF ドキュメント内のテキストを置き換える方法を示しています。ページ上で最初に出現するテキストを置換し、更新された文書を保存する方法を示しています。
---

PDF ドキュメントを更新する場合、テキスト置換は一般的な要件です。を使用する [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)、特定のテキストを検索して新しいコンテンツに置き換えることができます。「replace_text_strategy」プロパティを使用すると、置換されるオカレンスの数を制御できます。

1. PDF コンテンツエディターのインスタンスを作成します。
1. 入力 PDF ドキュメントをバインドします。
1. テキスト置換戦略を設定します。
1. ターゲットテキストを置換します。
1. 更新した PDF ドキュメントを保存します。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_on_page(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace text on page 1
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_FIRST
    )
    content_editor.replace_text("PDF", "Page 1 Replaced Text", 14)
    # Save updated document
    content_editor.save(outfile)
```

---
title: テキスト正規表現を置換
type: docs
weight: 30
url: /ja/python-net/replace-text-regex/
description: この例では、文書内のすべての 4 桁の数字がプレースホルダー「[NUMBER]」に置き換えられます。これは、機密データをマスクしたり、コンテンツを正規化したり、文書を匿名化したりする場合に便利です。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python の PDFContentEditor による正規表現によるテキストの置換
Abstract: この例は、正規表現を使用して PDF 内のテキストを Facades API 経由で Aspose.PDF for Python に置き換える方法を示しています。パターンを検索し、文書全体で一致したものをすべて置換する方法を示しています。
---

正規表現を使うと、固定文字列の代わりにパターンに基づいて柔軟にテキストを置換できます。'replace_text_strategy 'で正規表現サポートを有効にすることで、数値、日付、フォーマットされた文字列などの動的コンテンツを照合できます。

1. を作成 [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) インスタンス。
1. 入力 PDF ドキュメントをバインドします。
1. 正規表現を使用するように置換ストラテジーを設定します。
1. 文書全体で一致するパターンを置き換えます。
1. 更新した PDF ドキュメントを保存します。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_regex(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace text in the whole document
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text_strategy.is_regular_expression_used = True
    content_editor.replace_text(r"\d{4}", "[NUMBER]")
    # Save updated document
    content_editor.save(outfile)
```

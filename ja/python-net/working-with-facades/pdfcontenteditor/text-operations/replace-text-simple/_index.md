---
title: テキストを簡単に置換
type: docs
weight: 40
url: /ja/python-net/replace-text-simple/
description: この例では、文書全体で「33」のすべての出現箇所が「XXXIII」に置き換えられます。これは、カスタムフォーマットや正規表現を使わずに、簡単に文字列を置換できることを示しています。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python の PDF コンテンツエディタを使用して PDF 全体のテキストを置換
Abstract: この例は、Facades API 経由で Aspose.PDF for Python を使用して PDF ドキュメント全体のテキストを置換する方法を示しています。指定した文字列が出現する箇所をすべて新しいテキストに置き換えます。
---

単純なテキスト置換は、文書内の繰り返し値を更新する場合に便利です。と [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)、置換範囲を定義し、すべてのページでグローバルにテキストを置換できます。

1. を作成 [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) インスタンス。
1. 入力 PDF ドキュメントをバインドします。
1. すべてのオカレンスの置換範囲を設定します。
1. ターゲットテキストを置換します。
1. 更新した PDF ドキュメントを保存します。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_simple(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace text in the whole document
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text("33", "XXXIII ")
    # Save updated document
    content_editor.save(outfile)
```

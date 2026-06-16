---
title: フリーテキスト注釈の追加
type: docs
weight: 20
url: /ja/python-net/add-free-text-annotation/
description: 次の使用例は、既存の PDF ファイルを読み込み、最初のページの定義した位置にフリーテキスト注釈を追加し、変更した文書を保存します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF にフリーテキストアノテーションを追加する
Abstract: この例は、Facades API 経由で Aspose.PDF for Python を使用して PDF ドキュメントにフリーテキスト注釈を挿入する方法を示しています。PDF のバインド方法、注釈配置の定義、カスタムテキストの追加方法、および更新した文書を保存する方法を示します。
---

フリーテキスト注釈を使用すると、ポップアップコメントを必要とせずに、表示されているテキストをPDFページに直接配置できます。PDFContentEditor を使用すると、注釈の四角形、表示されるテキスト、およびターゲットページを指定できます。

1. 作成 [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 対象。
1. 入力 PDF をバインドします。
1. 注釈の位置を定義します。
1. フリーテキスト注釈を追加します。
1. 更新したドキュメントを保存します。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_free_text_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add free text annotation to page 1
    content_editor.create_free_text(
        apd.Rectangle(200, 480, 150, 25), "This is a free text annotation", 1
    )
    # Save updated document
    content_editor.save(outfile)
```

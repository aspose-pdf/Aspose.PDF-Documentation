---
title: テキスト注釈を追加
type: docs
weight: 50
url: /ja/python-net/add-text-annotation/
description: .NET 経由で Aspose.PDF for Python の PDFContentEditor クラスを使用して PDF ドキュメントにテキスト注釈を追加します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python でのテキストアノテーションの追加
Abstract: .NET 経由で Aspose.PDF for Python の PDFContentEditor クラスを使用して PDF ドキュメントにテキスト注釈を追加する方法を学びましょう。この例は、テキスト注釈を特定の位置に配置し、タイトルと内容を定義し、更新された PDF ファイルを保存する方法を示しています。
---

この記事では、を使用して PDF ドキュメントにテキスト注釈を追加する方法を説明します。 [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) Aspose.PDF のクラス。

テキスト注釈を使用すると、PDF ページの特定の部分にコメント、メモ、または追加情報を添付できます。これらの注釈はアイコンとして表示され、ユーザーが文書を表示するときに展開できます。

この例では以下のようになります。

- PDF ドキュメントが PDF コンテンツエディターに読み込まれます。
- テキスト注釈はページの特定の位置に追加されます。
- 注釈には、タイトル、コンテンツ、アイコンタイプ、表示設定が含まれます。
- 変更されたドキュメントは、新しいファイルに保存されます。

1. PDF コンテンツエディターオブジェクトを作成します。
1. 入力 PDF ドキュメントをバインドします。
1. 注釈の位置を定義します。
1. テキスト注釈を追加します。
1. 更新した PDF を保存します。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_text_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add text annotation to page 1
    content_editor.create_text(
        apd.Rectangle(100, 400, 50, 50),
        "Text Annotation",
        "This is a text annotation",
        True,
        "Insert",
        1,
    )
    # Save updated document
    content_editor.save(outfile)
```

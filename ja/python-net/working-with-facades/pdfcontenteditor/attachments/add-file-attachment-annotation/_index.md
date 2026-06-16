---
title: 添付ファイル注記を追加
type: docs
weight: 30
url: /ja/python-net/add-file-attachment-annotation/
description: この例では、入力 PDF をバインドし、ファイルパスを使用して最初のページに添付ファイルの注釈を追加し、更新された文書を保存します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF に添付ファイルの注釈を追加
Abstract: この例は、Facades API 経由で Aspose.PDF for Python のファイルパスを使用して PDF に添付ファイルの注釈を作成する方法を示しています。注釈の配置を定義し、説明テキストを設定し、アイコンタイプを選択し、変更した文書を保存する方法を示します。
---

ファイル添付注釈を使用すると、外部ファイルをインタラクティブなアイコンとして PDF ページに埋め込むことができます。ファイルパスオーバーロードを使用すると、ストリームを手動で開かなくてもディスクから直接ファイルを添付できます。この方法では、注釈アイコンをカスタマイズしたり、ユーザーに説明を提供したりすることもできます。

1. 作成 [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 対象。
1. 入力 PDF をバインドします。
1. 注釈長方形を定義します。
1. 添付ファイルの注釈を追加します。
1. 更新したドキュメントを保存します。

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_file_attachment_annotation(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Create file attachment annotation on page 1
    content_editor.create_file_attachment(
        apd.Rectangle(100, 520, 20, 20),
        "Attachment annotation contents",
        attachment_file,
        1,
        "PushPin",
    )
    # Save updated document
    content_editor.save(outfile)
```

---
title: ストリームから添付ファイルの注釈を追加
type: docs
weight: 40
url: /ja/python-net/add-file-attachment-annotation-from-stream/
description: この例では、PDF を読み込み、外部ファイルをメモリストリームに読み込み、最初のページに添付ファイルの注釈を追加して、変更された文書を保存します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python のストリームから PDF への添付ファイルの注釈の追加
Abstract: この例は、Facades API 経由で Aspose.PDF for Python のファイルストリームを使用して PDF に添付ファイルの注釈を作成する方法を示しています。注釈の位置を指定し、説明を設定し、不透明度値を追加し、変更した文書を保存する方法を示します。
---

添付ファイルに注釈を付けると、ファイルをインタラクティブなアイコンとしてPDFページに埋め込むことができます。ストリームベースのアプローチを使用すると、物理的なファイルパスに頼らずにファイルを動的に添付できます。この方法では、不透明度などの注釈の外観のカスタマイズもサポートされています。

1. PDF コンテンツエディターオブジェクトを作成します。
1. 入力 PDF をバインドします。
1. 添付ファイルをストリームとして読み取ります。
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


def add_file_attachment_annotation_from_stream(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    with open(attachment_file, "rb") as source_stream:
        attachment_stream = BytesIO(source_stream.read())

    # Create file attachment annotation using stream+opacity overload
    content_editor.create_file_attachment(
        apd.Rectangle(130, 520, 20, 20),
        "Attachment annotation from stream",
        attachment_stream,
        path.basename(attachment_file),
        1,
        "Tag",
        0.75,
    )
    # Save updated document
    content_editor.save(outfile)
```

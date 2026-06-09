---
title: パスから添付ファイルを追加
type: docs
weight: 20
url: /ja/python-net/add-attachment-from-path/
description: この例では、入力 PDF をバインドし、そのファイルパスを使用して外部ファイルを添付し、修正された PDF を埋め込まれた添付ファイルとともに保存します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python のファイルパスオーバーロードを使用して PDF にファイルを添付する
Abstract: この例は、Facades API 経由で Aspose.PDF for Python の「add_document_attachment ()」のファイルパスオーバーロードを使用して外部ファイルを PDF ドキュメントに添付する方法を示しています。これにより、ファイルストリームを手動で開かなくても簡単に添付ファイルを追加できます。
---

PDF には、参照または配布用のドキュメント、スプレッドシート、画像などの埋め込みファイルを含めることができます。「add_document_attachment ()」のファイルパスオーバーロードにより、添付ファイルをファイルパスから直接追加できるため、ファイルを手動で開く必要がなくなります。

1. 作成 [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 対象。
1. 入力 PDF をバインドします。
1. ファイルパスを使用して添付ファイルを追加します。
1. 更新したドキュメントを保存します。

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_attachment_from_path(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add attachment using file-path overload
    content_editor.add_document_attachment(
        attachment_file,
        "Attachment added using file path overload.",
    )
    # Save updated document
    content_editor.save(outfile)
```

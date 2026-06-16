---
title: 添付ファイルを追加
type: docs
weight: 10
url: /ja/python-net/add-attachment/
description: この例では、入力 PDF をバインドし、最初のページに外部ファイルを添付し、修正した PDF を添付添付ファイル付きで保存します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF に添付ファイルを追加する
Abstract: この例は、Facades API 経由で Aspose.PDF for Python を使用して外部ファイルを PDF ドキュメントに添付する方法を示しています。PDF をバインドする方法、説明付きの添付ファイルを追加する方法、更新した文書を保存する方法を示しています。
---

PDF の添付ファイルを使用すると、補足文書、画像、またはその他のリソースを PDF 内に直接含めることができます。と [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)、プログラムによって特定のページにファイルを添付したり、添付ファイル名を設定したり、説明を入力したりできます。

1. PDF コンテンツエディターオブジェクトを作成します。
1. 入力 PDF をバインドします。
1. 添付ファイルを開きます。
1. PDF に添付ファイルを追加します。
1. 更新したドキュメントを保存します。

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_attachment(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add attachment to page 1
    with open(attachment_file, "rb") as attachment_stream:
        content_editor.add_document_attachment(
            attachment_stream,
            path.basename(attachment_file),
            "This is a sample attachment for demonstration purposes.",
        )
    # Save updated document
    content_editor.save(outfile)
```

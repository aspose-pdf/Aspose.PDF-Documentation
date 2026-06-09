---
title: 添付ファイルを削除
type: docs
weight: 50
url: /ja/python-net/remove-attachments/
description: この例では、入力 PDF をバインドし、すべての添付ファイルを削除し、修正した PDF を埋め込みファイルなしで保存します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF からすべての添付ファイルを削除する
Abstract: この例は、Facades API 経由で Aspose.PDF for Python を使用して PDF ドキュメントからすべての添付ファイルを削除する方法を示しています。PDF をバインドする方法、埋め込まれた添付ファイルを削除する方法、更新した文書を保存する方法を示しています。
---

PDF には、文書、画像、その他のファイルなどの添付ファイルが含まれている場合があります。セキュリティ、プライバシー、または配布を目的として、PDF からすべての添付ファイルを削除する必要がある場合があります。を使用する [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)、ドキュメントに埋め込まれたすべての添付ファイルをプログラムで削除できます。

1. PDF コンテンツエディターオブジェクトを作成します。 
1. 入力 PDF をバインドします。
1. 添付ファイルをすべて削除します。
1. 更新したドキュメントを保存します。

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_attachments(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Remove all attachments from document
    content_editor.delete_attachments()
    # Save updated document
    content_editor.save(outfile)
```

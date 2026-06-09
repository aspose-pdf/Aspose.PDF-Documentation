---
title: インデックスでスタンプを削除
type: docs
weight: 50
url: /ja/python-net/delete-stamp-by-index/
description: この例では、2 ページ目にラバースタンプを 2 つ作成します。その後、インデックスを指定してスタンプを削除できます。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python の PDFContentEditor を使用して PDF 内のインデックスでラバースタンプを削除する
Abstract: この例は、Facades API 経由で Aspose.PDF for Python のインデックスを使用して PDF 内のラバースタンプの注釈を削除する方法を示しています。複数のスタンプを追加し、ページ上の順序に基づいてそのうちの 1 つを削除する方法を示しています。
---

ページに複数のラバースタンプがある場合は、そのインデックスを使って特定のラバースタンプを削除できます。delete_stamp () メソッドを使用すると、順序に従って注釈を削除できます。これは、スタンプ ID は追跡できないが、順序はわかっている場合に便利です。

1. を作成 [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) インスタンス。
1. 入力 PDF ドキュメントをバインドします。
1. bind_pdf (ファイル内) を使用して、入力 PDF ファイルを PDFContentEditor インスタンスにバインドします。
1. 'delete_stamp (1, [2, 3]) 'を呼び出して、2 ページ目と 3 ページ目からインデックス 1 のスタンプを削除します。
1. save (outfile) を使用して、変更した PDF ドキュメントを出力ファイルに保存します。

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_stamp_by_index(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    content_editor.delete_stamp(1, [2, 3])
    # Save updated document
    content_editor.save(outfile)
```

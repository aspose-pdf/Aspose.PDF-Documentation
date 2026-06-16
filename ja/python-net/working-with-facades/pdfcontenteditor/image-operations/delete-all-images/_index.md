---
title: PDF からすべての画像を削除
type: docs
weight: 10
url: /ja/python-net/delete-all-images/
description: ファサード API 経由で Aspose.PDF for Python を使用して PDF ドキュメントからすべての画像を削除します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python の PDF コンテンツエディターを使用して PDF からすべての画像を削除する
Abstract: この例は、Facades API 経由で Aspose.PDF for Python を使用して PDF ドキュメントからすべての画像を削除する方法を示しています。PDF をバインドし、埋め込まれたすべての画像を削除し、更新した文書を保存する方法を示しています。
---

PDF ドキュメントには、多くの場合、イラスト、ブランディング、または装飾用の画像が含まれています。ファイルサイズを小さくする、センシティブな画像を保護する、テキストのみのバージョンを用意するなど、PDF からすべての画像を削除する必要がある場合があります。

使用する [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)、PDF からすべての画像をプログラムで削除して、文書にテキストコンテンツのみを含めることができます。この例では、入力 PDF をバインドし、すべての画像を削除して、変更したファイルを保存します。

1. PDF コンテンツエディターオブジェクトを作成します。
1. 入力 PDF をバインドします。
1. すべての画像を削除します。
1. 更新したドキュメントを保存します。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_all_image(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Delete all images from the document
    content_editor.delete_image()
    # Save updated document
    content_editor.save(outfile)
```

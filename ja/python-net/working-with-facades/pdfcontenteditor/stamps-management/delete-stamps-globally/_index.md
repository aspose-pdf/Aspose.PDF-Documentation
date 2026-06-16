---
title: スタンプをグローバルに削除
type: docs
weight: 60
url: /ja/python-net/delete-stamps-globally/
description: この例は、Facades API 経由で Aspose.PDF for Python を使用して、PDF 内のすべてのページでラバースタンプの注釈をグローバルに削除する方法を示しています。個々のページを指定せずに ID ごとにスタンプを削除する方法を示しています。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python の PDF コンテンツエディターを使用して PDF 内のラバースタンプをグローバルに削除する
Abstract: この例は、Facades API 経由で Aspose.PDF for Python を使用して、PDF 内のすべてのページでラバースタンプの注釈をグローバルに削除する方法を示しています。個々のページを指定せずに ID ごとにスタンプを削除する方法を示しています。
---

複数のページを扱う場合、文書全体から特定のスタンプを削除する必要がある場合があります。'delete_stamp_by_id () 'メソッドと 'delete_stamp_by_ids ()' メソッドを使用すると、スタンプを識別子ごとにグローバルに削除できるため、各ページを手動で繰り返し処理する必要がなくなります。

1. を作成 [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) インスタンス。
1. 入力 PDF ドキュメントをバインドします。
1. ラバースタンプを複数のページに追加します。
1. ID を使用してスタンプをグローバルに削除します。
1. 更新した PDF ドキュメントを保存します。

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_stamps_globally(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    # Add stamps across multiple pages so global deletion is meaningful
    for page in range(1, 5):
        content_editor.create_rubber_stamp(
            page,
            apd.Rectangle(120, 500, 180, 60),
            "Draft",
            "Stamp for global deletion",
            apd.Color.gray,
        )

    # delete_stamp_by_id without page number removes stamp ID from all pages
    content_editor.delete_stamp_by_id(1)
    # delete_stamp_by_ids without page number removes a list of IDs from all pages
    content_editor.delete_stamp_by_ids([2, 3])

    # Save updated document
    content_editor.save(outfile)
```

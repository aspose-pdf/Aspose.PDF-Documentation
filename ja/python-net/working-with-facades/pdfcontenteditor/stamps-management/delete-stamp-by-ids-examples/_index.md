---
title: ID でスタンプを削除
type: docs
weight: 85
url: /ja/python-net/delete-stamp-by-ids-examples/
description:
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDFContentEditor を使用して PDF 内の 1 つまたは複数の ID でラバースタンプを削除する
Abstract: この例は、Facades API 経由で Aspose.PDF for Python を使用して、固有の ID に基づいて PDF からラバースタンプの注釈を削除する方法を示しています。単一 ID の削除と複数 ID の削除の両方を対象としています。
---

複数のスタンプを含むPDFで作業する場合、他のスタンプに影響を与えずに特定のスタンプを削除する必要があることがよくあります。ID ベースの削除機能を使うと、どのスタンプを削除するかを正確に制御できます。

- 'delete_stamp_by_id (stamp_id, page_number) '— 特定のページの ID を指定してスタンプを 1 つ削除する
- 'delete_stamp_by_ids (ページ番号, stamp_ids) '— 特定のページにある複数のスタンプを ID で削除します

1. を作成 [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) インスタンス。
1. 入力 PDF ドキュメントをバインドします。
1. ID が異なる 2 つのラバースタンプを追加します。
1. 単一 ID と複数 ID の両方の削除方法を使用してスタンプを削除します。
1. 更新した PDF を保存します。

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_stamp_by_ids_examples(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    # Create two stamps on page 1 so they can be deleted by ID
    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(120, 320, 180, 60),
        "Draft",
        "Delete by single ID",
        apd.Color.orange,
    )
    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(120, 250, 180, 60),
        "Draft",
        "Delete by multiple IDs",
        apd.Color.orange,
    )

    # Delete by single ID overload and by IDs overload
    content_editor.delete_stamp_by_id(1, 1)
    content_editor.delete_stamp_by_ids(1, [2])

    # Save updated document
    content_editor.save(outfile)
```


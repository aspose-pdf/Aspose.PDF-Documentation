---
title: 「ドキュメントを追加」アクション
type: docs
weight: 20
url: /ja/python-net/add-document-action/
description: この例では、PDF を開いたときに表示される JavaScript アラートを追加します。スクリプトは文書を開くイベントに添付され、サポートされている PDF ビューアで自動的に実行されます。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF にドキュメントを開く JavaScript アクションを追加
Abstract: この例は、PDF が開かれたときにトリガーされるドキュメントレベルの JavaScript アクションを追加する方法を示しています。このサンプルでは、Facades API 経由で Aspose.PDF for Python を使用して、ドキュメントをバインドし、開くイベントアクションを割り当てて、更新された PDF を保存する方法を示しています。
---

ドキュメントレベルのアクションでは、PDF を開くなど、特定のイベントが発生したときに自動的に実行される動作を定義できます。と [PDF コンテンツエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)、これらのイベントには JavaScript コードを添付できます。これは通知、検証ロジック、またはインタラクティブなワークフローに使用できます。

1. PDF コンテンツエディターオブジェクトを作成します。
1. 入力 PDF をバインドします。
1. ドキュメントレベルのアクションを追加します。
1. 更新したドキュメントを保存します。

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_document_action(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add JavaScript action for document open event
    content_editor.add_document_additional_action(
        content_editor.DOCUMENT_OPEN,
        "app.alert('Document opened with PdfContentEditor action');",
    )
    # Save updated document
    content_editor.save(outfile)
```

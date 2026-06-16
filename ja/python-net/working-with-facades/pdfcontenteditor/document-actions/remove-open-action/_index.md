---
title: オープンアクションを削除
type: docs
weight: 30
url: /ja/python-net/remove-open-action/
description: 次の使用例は、既存の PDF を読み込み、開く操作を削除して、クリーンアップされた文書を保存します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF からドキュメントを開くアクションを削除する
Abstract: この例は、Facades API 経由で Aspose.PDF for Python を使用して PDF からドキュメントを開くアクションを削除する方法を示しています。PDF をバインドし、開くアクションをクリアし、更新した文書を保存する方法を示しています。
---

PDF ドキュメントには、JavaScript アラート、ナビゲーションコマンド、その他の動作など、ファイルが開かれたときに自動的に実行されるアクションが含まれている場合があります。シナリオによっては、セキュリティ、コンプライアンス、またはユーザーエクスペリエンスの理由から、これらのアクションを削除する必要がある場合があります。

PDFContentEditorを使用すると、ドキュメントを開くアクションを簡単に削除して、自動動作を実行せずにPDFを開くことができます。

1. PDF コンテンツエディターオブジェクトを作成します。
1. 入力 PDF をバインドします。
1. ドキュメントを開くアクションを削除します。
1. 更新したドキュメントを保存します。

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_open_action(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Remove open action from the document
    content_editor.remove_document_open_action()
    # Save updated document
    content_editor.save(outfile)
```

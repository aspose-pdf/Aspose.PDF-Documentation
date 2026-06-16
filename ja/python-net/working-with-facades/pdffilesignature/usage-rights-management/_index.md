---
title: 使用権管理
type: docs
weight: 100
url: /ja/python-net/usage-rights-management/
description: Python の PDFFileSignature を使用して PDF ドキュメントから使用権限を検出して削除する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python での PDF 使用権限の削除
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメントの使用権限を検査および削除する方法について説明します。PDF に使用権限が含まれているかどうかを確認する方法と、それらの権限が削除された後に文書の新しいバージョンを保存する方法を示します。
---

.NET 経由の Python 用 Aspose.PDF は [PDF ファイル署名](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) 署名付きPDFおよび関連する使用権限設定を操作するためのファサード。ワークフローによっては、更新されたバージョンのファイルを保存する前に、文書に使用権限が含まれているかどうかを調べて削除する必要がある場合があります。

この例は、一般的な使用権限管理タスクの 1 つを示しています。

1. PDF に使用権限が含まれているかどうかを確認します。
1. ドキュメントから使用権限を削除します。
1. 更新した PDF ファイルを保存します。

## PDF に使用権限が含まれているかどうかを確認する

使用権限を削除する前に、この例では以下を呼び出してドキュメントの現在の状態を確認します。 `contains_usage_rights()`。これにより、変更を加える前に使用権限があるかどうかを確認できます。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def check_usage_rights(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        had_usage_rights = pdf_signature.contains_usage_rights()
        print(f"PDF contains usage rights: {had_usage_rights}")
    finally:
        pdf_signature.close()
```

## PDF から使用権限を削除する

使用 `remove_usage_rights()` ドキュメントが既存の使用権限設定を保持する必要がなくなったとき。この例では、初期状態を確認して権限を削除し、更新された PDF を新しいファイルに保存します。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def remove_usage_rights(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        had_usage_rights = pdf_signature.contains_usage_rights()
        print(f"PDF contains usage rights before removal: {had_usage_rights}")
        pdf_signature.remove_usage_rights()
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

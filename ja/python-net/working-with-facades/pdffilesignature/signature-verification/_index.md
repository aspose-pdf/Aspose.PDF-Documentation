---
title: 署名検証
type: docs
weight: 90
url: /ja/python-net/signature-verification/
description: Python の PDFFileSignature を使用して、デジタル署名を検証し、PDF に署名が含まれているかどうかを確認する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python での PDF 署名の検証
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメント内のデジタル署名を検証する方法について説明します。既存の署名を検証する方法と、PDF に署名が含まれているかどうかを確認する方法を示します。
---

.NET 経由の Python 用 Aspose.PDF は [PDF ファイル署名](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) 署名されたPDF文書を検証するためのファサード。PDF に署名したら、その署名を使用して署名が有効であることを確認したり、文書に署名エントリが含まれているかどうかを確認したりできます。

この例は、2 つの一般的な検証タスクを示しています。

1. 既存の PDF 署名が有効であることを確認します。
1. PDF に署名が含まれているかどうかを確認します。

## PDF 署名を検証する

使用 `verify_signature()` 文書内の特定の署名を検証する必要がある場合。この例では最初に見つかった署名名を解決し、その署名が有効かどうかを検証します。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def verify_pdf_signature(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        is_valid = pdf_signature.verify_signature(sign_name)
        print(f"Signature '{sign_name}' is valid: {is_valid}")
    finally:
        pdf_signature.close()
```

## PDF に署名が含まれているかどうかを確認する

使用 `contains_signature()` PDFに署名が含まれているかどうかだけを知りたい場合。これは、より詳細な検証または抽出ロジックを実行する前に簡単に確認できるので便利です。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def check_if_pdf_contains_signatures(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        contains_signatures = pdf_signature.contains_signature()
        print(f"PDF contains signatures: {contains_signatures}")
    finally:
        pdf_signature.close()
```

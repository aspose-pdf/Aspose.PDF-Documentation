---
title: 署名整合性チェック
type: docs
weight: 70
url: /ja/python-net/signature-integrity-checks/
description: Python の PDFFileSignatureを使用して、PDF署名が文書全体をカバーしているかどうかを確認し、署名された文書の整合性を検証する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python で PDF 署名のカバレッジと整合性を検証する方法
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して、署名付き PDF 文書の電子署名の整合性を検査する方法について説明します。署名が文書全体をカバーしているかどうかを確認する方法と、署名された内容の整合性を検証する方法を示します。
---

.NET 経由の Python 用 Aspose.PDF は [PDF ファイル署名](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) 署名されたPDF文書を検証するためのファサード。ファイルに署名が済んだら、その署名が文書全体に適用されているかどうか、署名された内容がまだ有効かどうかを確認できます。

この例は、2 つの一般的な整合性チェックを示しています。

1. 署名が文書全体をカバーしているかどうかを確認してください。
1. 署名された PDF コンテンツの整合性を検証します。

## 署名が文書全体をカバーしているかどうかを確認する

使用 `covers_whole_document()` 署名がコンテンツの一部だけでなくPDF全体に適用されていることを確認する必要がある場合。この例では、最初に利用可能な署名名を読み取り、その範囲をチェックします。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def check_signature_coverage(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        covers_document = pdf_signature.covers_whole_document(sign_name)
        print(f"Signature '{sign_name}' covers the whole document: {covers_document}")
    finally:
        pdf_signature.close()
```

## 文書の整合性を検証

使用 `verify_signed()` 署名が適用された後に、署名された文書の内容が変更されていないことを確認します。この方法は、選択した署名に対して文書が有効であるかどうかを確認するのに役立ちます。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def validate_document_integrity(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        is_valid = pdf_signature.verify_signed(sign_name)
        print(f"Document integrity for '{sign_name}' is valid: {is_valid}")
    finally:
        pdf_signature.close()
```


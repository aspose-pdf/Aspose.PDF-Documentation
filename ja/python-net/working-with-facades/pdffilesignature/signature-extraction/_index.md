---
title: シグネチャ抽出
type: docs
weight: 50
url: /ja/python-net/signature-extraction/
description: Python の PDFFileSignatureを使用して、署名されたPDFから署名画像と署名証明書を抽出する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python で PDF から署名イメージと証明書を抽出する方法
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して、署名付き PDF ドキュメントから署名関連のデータを抽出する方法について説明します。最初に利用可能な署名を読み取り、その画像をエクスポートし、関連する証明書ストリームを出力ファイルに保存する方法を示します。
---

.NET 経由の Python 用 Aspose.PDF は [PDF ファイル署名](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) 署名されたPDF文書からデータを検査および抽出するためのファサード。PDF に署名したら、その PDF を使用して、視覚的な署名画像や署名に関連する証明書などの署名リソースをエクスポートできます。

この例は、2 つの一般的な抽出タスクを示しています。

1. 署名に関連するビジュアルイメージを抽出します。
1. 署名済み PDF から署名証明書を抽出します。

## 署名画像を抽出する

この方法は、PDF に目に見える署名が含まれていて、その画像データをエクスポートする場合に使用します。この例では、署名された文書を開き、最初に利用できる署名名を取得し、イメージストリームを抽出してファイルに書き込みます。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def extract_signature_image(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_image = pdf_signature.extract_image(sign_name)
        write_stream_data(signature_image, outfile)
    finally:
        pdf_signature.close()
```

## 署名証明書を抽出する

使用 `extract_certificate()` 署名に添付された証明書データが必要な場合これは、検査や検証のワークフローや、署名者証明書を PDF 文書とは別に保管する場合に役立ちます。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def extract_signature_certificate(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_certificate = pdf_signature.extract_certificate(sign_name)
        write_stream_data(signature_certificate, outfile)
    finally:
        pdf_signature.close()
```


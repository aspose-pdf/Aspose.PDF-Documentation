---
title: PDF ドキュメントへの署名
type: docs
weight: 10
url: /ja/python-net/pdf-signing/
description: 証明書ベースの名前付き可視デジタル署名付きPDFFileSignatureを使用して、PythonでPDF文書に署名する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python でデジタル署名を使用して PDF ドキュメントに署名する方法
Abstract: この記事では、PDFFileSignature ファサードを使用して、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメントに署名する方法を説明します。証明書の設定、基本パラメーターによる署名、PKCS7 オブジェクトによる署名、署名名の割り当て、署名の表示方法の適用について説明します。
---

.NET 経由の Python 用 Aspose.PDF は [PDF ファイル署名](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) 既存のPDF文書にデジタル署名を適用するためのファサード。証明書ファイルを使用すると、プログラムによる文書への署名、ページへの署名、署名メタデータの割り当て、署名の表示方法のカスタマイズを行うことができます。

この記事では、一般的な署名ワークフローをいくつか紹介します。

1. を作成してバインドする `PdfFileSignature` 入力 PDF へのオブジェクト。
1. 署名証明書を設定します。
1. ターゲットページにデジタル署名を適用します。
1. 必要に応じて、署名名と表示方法を割り当てることができます。
1. 署名済み PDF を保存します。

## 再利用可能な署名ヘルパーを用意する

PDF にデジタル署名を適用する前に、再利用可能なヘルパー関数をいくつか設定しておくと便利です。これらのヘルパーは、署名ハンドラーの初期化、可視署名領域の定義、証明書の設定、再利用可能な PKCS #7 署名オブジェクトの構築を行います。これにより、以下の署名例は独立していてわかりやすくなります。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd


DEFAULT_CERTIFICATE_PASSWORD = "Aspose2021"
DEFAULT_SIGNATURE_NAME = "Signature1"


def create_pdf_file_signature(infile):
    pdf_signature = pdf_facades.PdfFileSignature()
    pdf_signature.bind_pdf(infile)
    return pdf_signature


def create_signature_rectangle():
    return apd.Rectangle(10, 10, 200, 60)


def configure_signature_certificate(
    pdf_signature, certificate_path, certificate_password=DEFAULT_CERTIFICATE_PASSWORD
):
    pdf_signature.set_certificate(certificate_path, certificate_password)


def create_pkcs7_signature(
    certificate_path, certificate_password=DEFAULT_CERTIFICATE_PASSWORD
):
    signature = ap.forms.PKCS7(certificate_path, certificate_password)
    signature.reason = "Document approval"
    signature.contact_info = "qa@example.com"
    signature.location = "New York, USA"
    signature.authority = "Aspose.PDF Example"
    return signature


def create_custom_signature_appearance():
    appearance = ap.forms.SignatureCustomAppearance()
    appearance.font_family_name = "Arial"
    appearance.font_size = 10
    appearance.show_contact_info = True
    appearance.show_location = True
    appearance.show_reason = True
    return appearance
```

## 基本的な証明書パラメータを使用して PDF に署名する

この方法では、証明書をに直接設定します。 `PdfFileSignature` 対象。標準の署名メタデータを使用し、個別の署名オブジェクト管理は不要な、わかりやすい署名フローが必要な場合に便利です。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def sign_pdf_with_basic_parameters(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        configure_signature_certificate(pdf_signature, certificate_path)
        pdf_signature.sign(
            1,
            "Document approval",
            "qa@example.com",
            "New York, USA",
            False,
            create_signature_rectangle(),
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## PKCS7 オブジェクトを使用して PDF に署名する

を使う `PKCS7` 最初に署名を準備してから署名呼び出しに渡す必要がある場合は、オブジェクトを指定します。このパターンを使うと、署名設定をより細かく制御でき、より高度なワークフローの基礎として役立ちます。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def sign_pdf_with_certificate_object(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        signature = create_pkcs7_signature(certificate_path)
        pdf_signature.sign(1, False, create_signature_rectangle(), signature)
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## 名前付き署名で PDF に署名する

文書ワークフローが定義済みの署名フィールド名に依存している場合は、その名前をに渡してください `sign()`。これにより、後で署名を参照して検証、処理、承認ワークフローとの統合を行うのが簡単になります。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def sign_pdf_with_named_signature(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        signature = create_pkcs7_signature(certificate_path)
        signature.reason = "Approved by signing workflow"
        pdf_signature.sign(
            1,
            DEFAULT_SIGNATURE_NAME,
            "Approved by signing workflow",
            "qa@example.com",
            "New York, USA",
            True,
            create_signature_rectangle(),
            signature,
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## 目に見える署名を適用

にカスタムの外観を割り当てることで、署名を PDF ページに表示できます。 `PKCS7` 対象。これは、出力文書に理由、場所、連絡先情報などの承認詳細をエンドユーザーに表示する必要がある場合に役立ちます。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def apply_visible_signature(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        signature = create_pkcs7_signature(certificate_path)
        signature.reason = "Visible approval signature"
        signature.custom_appearance = create_custom_signature_appearance()
        pdf_signature.sign(
            1,
            "Visible approval signature",
            "qa@example.com",
            "New York, USA",
            True,
            create_signature_rectangle(),
            signature,
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

---
title: Python で PDF から署名情報を抽出する方法
linktitle: 署名から詳細を抽出
type: docs
weight: 20
url: /ja/python-net/extract-image-and-signature-information/
description: Python で PDF ファイルから署名画像、証明書、電子署名の詳細を抽出する方法を学びます。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python で PDF から署名画像と証明書の詳細を抽出します
Abstract: この記事では、Aspose.PDF for Python を使用して PDF 文書から画像およびデジタル署名情報を抽出する方法について説明します。署名された PDF ファイル内の署名画像の取得、証明書データの抽出、署名アルゴリズムの検査、および侵害された署名の検出の方法を学びます。
---

## 署名フィールドから画像を抽出

.NET 経由の Python 用 Aspose.PDF を使用すると、に埋め込まれたビジュアルイメージを取得できます [署名フィールド](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/)。これは、PDF 全体をレンダリングせずに署名の外観を表示またはアーカイブする必要がある場合に便利です。

以下の例では、すべてのフォームフィールドを繰り返し処理し、それぞれを検索します。 `SignatureField`そして、その画像を JPEG ファイルとして保存します。

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def extract_images_from_signature_field(infile: str, outfile: str) -> None:
    """Extract the image stored in a signature field."""
    with ap.Document(infile) as document:
        for field in document.form:
            if not isinstance(field, ap.forms.SignatureField):
                continue

            image_stream = field.extract_image()
            if image_stream is None:
                continue

            image = drawing.Bitmap.from_stream(image_stream)
            image.save(outfile, drawing.imaging.ImageFormat.jpeg)
```

## 署名アルゴリズムの詳細を読み込む

使用 `PdfFileSignature.get_signatures_info()` 文書内の各署名の暗号化メタデータ (ダイジェストアルゴリズム、アルゴリズムタイプ、暗号化標準、署名名を含む) を読み取るには:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def get_signatures_info(infile: str) -> None:
    """Print information about all signatures in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_info in signature.get_signatures_info():
                print(signature_info.DIGEST_HASH_ALGORITHM)
                print(signature_info.ALGORITHM_TYPE)
                print(signature_info.CRYPTOGRAPHIC_STANDARD)
                print(signature_info.signature_name)
```

## 署名フィールドからデジタル証明書を抽出する

を使う [エクストラクト_証明書](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/#methods) a のメソッド `SignatureField` 埋め込まれた証明書をバイトストリームとして取得し、外部検証用にディスクに保存するには：

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def extract_certificate(infile: str, outfile: str) -> None:
    """Extract a certificate from a signature field and save it to disk."""
    with ap.Document(infile, password="owner") as document:
        for field in document.form:
            if not isinstance(field, ap.forms.SignatureField):
                continue

            certificate_stream = field.extract_certificate()
            if certificate_stream is None:
                continue

            with certificate_stream:
                bytes_data = bytearray(certificate_stream.length)
                certificate_stream.read(bytes_data, 0, len(bytes_data))
                with open(outfile, "wb") as file_stream:
                    file_stream.write(bytes_data)
                return
```

## PDFファイル署名ファサードを使用して証明書を抽出する

`PdfFileSignature.try_extract_certificate()` には、署名名で証明書を取得する代替方法が用意されています。次の例では、すべての署名名を繰り返し処理し、それぞれについて抽出を試みます。

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def extract_certificate_try_extract_certificate_method(infile: str) -> None:
    """Extract certificates with the try_extract_certificate facade method."""
    with ap.Document(infile, password="owner") as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_name in signature.get_signature_names(True):
                certificate = []
                if signature.try_extract_certificate(signature_name, certificate):
                    print("The certificate extraction succeeded")
```

## 外部デジタル署名の検証

署名後に文書が変更されていないことを確認するには、以下を使用して各外部署名を検証します。 `PdfFileSignature.verify_signature()`。以下の例では、署名が検証に失敗すると例外が発生します。

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_external_signature(infile: str) -> None:
    """Verify an external signature in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as pdf_signature:
            for signature_name in pdf_signature.get_signature_names(True):
                if not pdf_signature.verify_signature(signature_name):
                    raise Exception("Not verified")
```

## 侵害されたシグネチャを検出

`SignaturesCompromiseDetector` 文書内のデジタル署名が、その後の変更によって無効になったかどうかを確認します。文書の完全性を保証する必要がある法律、財務、またはコンプライアンスのワークフローでこれを使用してください。

以下の例では、侵害された署名がないかチェックし、文書全体の署名範囲とともに名前を報告します。

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def check(infile: str) -> None:
    """Check whether a PDF contains compromised signatures."""
    with ap.Document(infile) as document:
        detector = ap.SignaturesCompromiseDetector(document)
        result = []

        if detector.check(result):
            print("No signature compromise detected")
            return

        if result[0].has_compromised_signatures:
            print(
                f"Count of compromised signatures: {len(result[0].COMPROMISED_SIGNATURES)}"
            )
            for signature_name in result[0].COMPROMISED_SIGNATURES:
                print(f"Signature name: {signature_name.FULL_NAME}")

        print(result[0].signatures_coverage)
```

## 関連するセキュリティトピック

- [Python で PDF ファイルを保護して署名する方法](/pdf/ja/python-net/securing-and-signing/)
- [Python で PDF ファイルにデジタル署名する方法](/pdf/ja/python-net/digitally-sign-pdf-file/)
- [Python のスマートカードから PDF ドキュメントに署名する](/pdf/ja/python-net/sign-pdf-document-from-smart-card/)
- [Python での PDF ファイルの暗号化と復号化](/pdf/ja/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)

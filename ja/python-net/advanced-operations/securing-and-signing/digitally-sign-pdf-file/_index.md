---
title: Python で PDF にデジタル署名を追加したり、PDF にデジタル署名したりできます。
linktitle: PDF にデジタル署名する
type: docs
weight: 10
url: /ja/python-net/digitally-sign-pdf-file/
description: Python で PDF 文書にデジタル署名し、タイムスタンプを追加し、署名を検証する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF ファイルにデジタル署名する
Abstract: このガイドでは、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメントにデジタル署名する方法について説明します。標準および高度なデジタル署名の適用、証明書 (PFX と PKCS #12) の活用、署名の外観と動作のカスタマイズのプロセスについて詳しく説明します。このドキュメントには、既存の PDF への署名、タイムスタンプの追加、署名の有効性の検証を行う方法を示すコード例が含まれています。これにより、開発者は Python アプリケーションにおける文書の信頼性、完全性、電子署名標準への準拠を確認することができます。
---

## デジタル署名で PDF に署名

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_document(infile: str, outfile: str, pfxfile: str) -> None:
    """Sign a PDF document with a PKCS#7 certificate."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7(pfxfile, "12345")
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            signature.save(outfile)
```

**PKCS #7 分離署名**は、署名ブロックにコンテンツを埋め込まずに文書にデジタル署名を追加します。

証明書ベースの署名を PDF ファイルに適用したり、署名の有効性を検証したり、署名済み文書に信頼できるタイムスタンプを追加したりする必要がある場合は、これらの例を使用してください。

次の例では、PKCS #7 デタッチデジタル署名を使用して PDF 文書に署名し、指定された長方形の領域の最初のページに署名を付けます。

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_document_PKCS7_detached(
    infile: str,
    outfile: str,
    pfxfile: str,
    password: str,
) -> None:
    """Sign a PDF document with a detached PKCS#7 certificate."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7Detached(
                pfxfile,
                password,
                ap.DigestHashAlgorithm.SHA256,
            )
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            signature.save(outfile)
```

** PDF 文書内のすべてのデジタル署名を確認**

1. PDF 内の署名を操作できるようにする PDFFileSignature のインスタンスを作成します。
1. シグネチャ名のリストを取得 `get_signature_names(True)`.
1. リスト内の最初の署名をチェックします `verify_signature` 指定された証明書に準拠していること。

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify(infile: str) -> None:
    """Verify all digital signatures in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_name in signature.get_signature_names(True):
                if not signature.verify_signature(signature_name):
                    raise Exception("Not verified")
```

**公開鍵証明書ファイルで署名を検証**

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_with_public_key_certificate1(certificate: str, infile: str) -> None:
    """Verify a signature with a public key certificate file."""
    with ap.facades.PdfFileSignature(infile) as file_sign:
        signature_names = file_sign.get_signature_names(True)
        with open(certificate, "rb") as file_stream:
            certificate_bytes = file_stream.read()
        print(file_sign.verify_signature(signature_names[0], certificate_bytes))
```

**ファイルから抽出した証明書で署名を確認してください**

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_with_public_key_certificate_from_signature(infile: str) -> None:
    """Verify a signature with the certificate extracted from the file."""
    with ap.facades.PdfFileSignature(infile) as file_sign:
        signature_names = file_sign.get_signature_names(True)
        certificate = []
        if file_sign.try_extract_certificate(signature_names[0], certificate):
            print(file_sign.verify_signature(signature_names[0], certificate[0]))
        else:
            print(False)
```

**証明書チェーン検証を有効にして署名を検証**

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_signature_with_certificate_check(infile: str) -> None:
    """Verify signatures with certificate-chain validation enabled."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_name in signature.get_signature_names(True):
                options = ap.security.ValidationOptions()
                options.validation_mode = ap.security.ValidationMode.STRICT
                options.validation_method = ap.security.ValidationMethod.AUTO
                options.check_certificate_chain = True
                options.request_timeout = 20000
                validation_result = []
                verified = signature.verify_signature(
                    signature_name,
                    options,
                    validation_result,
                )
                print(f"Certificate validation result: {validation_result[0].status}")
                print(f"Is verified: {verified}")
```

## デジタル署名にタイムスタンプを追加

### タイムスタンプ付きの PDF にデジタル署名する方法

Aspose.PDF for Python は、タイムスタンプサーバーまたは Web サービスを使用して PDF にデジタル署名することをサポートしています。

この要件を満たすためには、 [タイムスタンプ設定](https://reference.aspose.com/pdf/python-net/aspose.pdf/timestampsettings/) クラスが Aspose.PDF 名前空間に追加されました。タイムスタンプを取得して PDF ドキュメントに追加する次のコードスニペットを見てください。

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_with_time_stamp_server(
    infile: str,
    outfile: str,
    pfxfile: str,
    password: str,
) -> None:
    """Sign a PDF document and apply a timestamp from an external server."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7(pfxfile, password)
            pkcs.timestamp_settings = ap.TimestampSettings(
                "https://freetsa.org/tsr",
                "",
                ap.DigestHashAlgorithm.SHA256,
            )
            rect = drawing.Rectangle(100, 100, 200, 100)
            signature.sign(
                1, "Signature Reason", "Contact", "Location", True, rect, pkcs
            )
            signature.save(outfile)
```

## ECDSA を使用して PDF ドキュメントに署名する

ECDSA（楕円曲線デジタル署名アルゴリズム）を使用してPDF文書に署名するには、楕円曲線暗号を利用してデジタル署名を生成する必要があります。

上記のコードスニペットは、Aspose.PDF for Python を使用して PKCS #7 デタッチデジタル署名を PDF ドキュメントに適用する方法を示しています。この例は、文書を読み込み、署名の外観とセキュリティ設定を構成し、結果を保存することで、PDF ファイルにデジタル署名するための完全で信頼性の高いワークフローを示しています。

この方法では、最初のページに安全で検証可能な署名を埋め込むことで、文書の信頼性と整合性を確保します。SHA-256をダイジェストアルゴリズムとして使用することで最新の暗号標準を満たし、署名の配置を制御できるため、承認マークを柔軟に表示できます。

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_ecdsa(infile: str, outfile: str, pfxfile: str, password: str) -> None:
    """Sign a PDF document with an ECDSA signature."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7Detached(
                pfxfile,
                password,
                ap.DigestHashAlgorithm.SHA256,
            )
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            signature.save(outfile)
```

** PDF ドキュメント内の ECDSA 署名の検証**

```python
def verify_ecdsa(infile: str) -> None:
    """Verify ECDSA signatures in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            if not signature.contains_signature():
                raise Exception("Not contains signature")

            for signature_name in signature.get_signature_names(True):
                if not signature.verify_signature(signature_name):
                    raise Exception("Not verified")
```

## 関連するセキュリティトピック

- [Python で PDF ファイルを保護して署名する方法](/pdf/ja/python-net/securing-and-signing/)
- [Python で画像と署名情報を抽出する](/pdf/ja/python-net/extract-image-and-signature-information/)
- [Python のスマートカードから PDF ドキュメントに署名する](/pdf/ja/python-net/sign-pdf-document-from-smart-card/)
- [Python での PDF ファイルの暗号化と復号化](/pdf/ja/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)
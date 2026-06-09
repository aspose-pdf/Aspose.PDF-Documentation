---
title: Python でスマートカードから PDF ドキュメントに署名する
linktitle: スマートカードによる PDF 署名
type: docs
weight: 30
url: /ja/python-net/sign-pdf-document-from-smart-card/
description: Python でスマートカードと外部証明書を使用して PDF 文書に署名する方法を学習します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用してスマートカードから PDF ドキュメントに署名する
Abstract: このガイドでは、.NET 経由で Aspose.PDF for Python でスマートカードを使用して PDF ドキュメントにデジタル署名する方法について説明します。ハードウェアデバイス (USB トークンやスマートカードなど) に保存されている証明書に Windows 証明書ストア経由でアクセスし、それを PDF ファイルの署名に適用する方法を示します。このドキュメントには、適切な証明書を検索する方法、署名プロパティを設定する方法、およびデジタル署名を PDF に埋め込む方法を示すコード例が含まれています。これにより、デジタル署名標準に準拠した安全なハードウェアベースの署名が可能になり、信頼度の高い企業や法務ワークフローに適しています。
---

Aspose.PDF には、ビジュアル署名コンポーネントと暗号署名コンポーネントを統合するための堅牢な機能が用意されているため、デジタル署名された PDF 文書の信頼性とプロフェッショナルな表示の両方が保証されます。

このワークフローは、スマートカード、USB トークン、マネージド証明書ストアなどのハードウェアベースのデバイスに保存されている証明書を署名プロセスに依存する場合に使用します。

## 署名フィールドを使用してスマートカードで署名する

この例は、Aspose.PDF for Python で外部証明書を使用して PDF ドキュメントにデジタル署名し、カスタムの署名外観画像を適用する方法を示しています。

1. PDF ドキュメントを開きます。
1. PDFFileSignatureオブジェクトを作成し、それをドキュメントにバインドします。
1. カスタムメソッドによるローカルデジタル証明書の取得 `get_local_certificate()`.
1. 選択した証明書に基づいて外部署名を設定します。
1. カスタム署名の外観画像（会社のロゴや手書きの署名など）を適用します。
1. 指定されたメタデータ (理由、連絡先、場所) を使用して文書の最初のページにデジタル署名します。
1. 署名済み文書を新しい出力ファイルに保存します。

この方法は、ハードウェアトークン、証明書ストア、信頼できるプロバイダーなどの外部証明書を使用して署名をプログラムで適用し、パーソナライズされた視覚的レイアウトで表示する必要がある場合に最適です。

スマートカードから PDF 文書に署名するためのコードスニペットを以下に示します。

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_with_smart_card(infile: str, outfile: str, pngfile: str) -> None:
    """Sign a PDF document using a smart-card certificate."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature() as pdf_signature:
            pdf_signature.bind_pdf(document)
            external_signature = ap.forms.ExternalSignature(get_local_certificate())
            pdf_signature.signature_appearance = pngfile
            pdf_signature.sign(
                1,
                "Reason",
                "Contact",
                "Location",
                True,
                drawing.Rectangle(100, 100, 200, 200),
                external_signature,
            )
            pdf_signature.save(outfile)
```

## デジタル署名の検証

このコードスニペットは、Aspose.PDF for Python を使用して PDF ドキュメント内のデジタル署名を検証する方法を示しています。

1. PDF ファイルを開きます。
1. 「PDFFileSignatureオブジェクト」を作成し、それをドキュメントにバインドします。
1. 'get_signature_names () 'を使用してすべての署名フィールド名のリストを取得します。
1. 「verify_signature ()」を使用して各シグネチャを反復処理し、その有効性を検証します。
1. いずれかの署名が検証に失敗した場合は例外を発生させます。

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

## 外部証明書で署名

このコードスニペットは、Aspose.PDF for Python と外部証明書を使用して PDF ドキュメントにデジタル署名フィールドを追加して署名する方法を示しています。

1. PDF ファイルをバイナリストリームとして開きます。
1. SignatureField を作成し、それを文書の最初のページの指定された位置に配置します。
1. カスタムメソッドによるローカルデジタル証明書の取得 `get_local_certificate()`.
1. 権限、理由、連絡先情報などのメタデータを使用して外部署名を設定します。
1. 署名フィールドに一意のフィールド名を割り当てます (partial_name =「sig1")。
1. PDF のフォームフィールドに署名フィールドを追加します。
1. 外部証明書を使用してフィールドに署名します。
1. 署名済み文書を出力ファイルに保存します。

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def get_signature_info_using_signature_field(infile: str, outfile: str) -> None:
    """Create a signature field and sign it with an external certificate."""
    with open(infile, "rb+") as file_stream:
        document = ap.Document(file_stream)
        signature_field = ap.forms.SignatureField(
            document.pages[1],
            ap.Rectangle(100, 400, 10, 10, True),
        )
        selected_certificate = get_local_certificate()
        external_signature = ap.forms.ExternalSignature(selected_certificate)
        external_signature.authority = "Me"
        external_signature.reason = "Reason"
        external_signature.contact_info = "Contact"
        signature_field.partial_name = "sig1"
        document.form.add(signature_field, 1)
        signature_field.sign(external_signature)
        document.save(outfile)
```

## 関連するセキュリティトピック

- [Python で PDF ファイルを保護して署名する方法](/pdf/ja/python-net/securing-and-signing/)
- [Python で PDF ファイルにデジタル署名する方法](/pdf/ja/python-net/digitally-sign-pdf-file/)
- [Python で PDF から署名情報を抽出する方法](/pdf/ja/python-net/extract-image-and-signature-information/)
- [Python での PDF ファイルの暗号化と復号化](/pdf/ja/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)


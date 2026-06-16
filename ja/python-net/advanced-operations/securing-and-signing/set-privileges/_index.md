---
title: Python での PDF ファイルの暗号化と復号化
linktitle: PDF ファイルの暗号化と復号化
type: docs
weight: 70
url: /ja/python-net/set-privileges-encrypt-and-decrypt-pdf-file/
description: Python で PDF 権限の設定、ファイルの暗号化、保護された PDF の復号化、パスワードの変更を行う方法を学びます。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python での PDF 権限の設定と暗号化の管理
Abstract: このドキュメントページでは、Aspose.PDF for Python を使用して PDF ファイルの権限を設定する方法、暗号化を適用する方法、および復号化する方法について説明します。開発者向けに、ユーザーパスワードと所有者パスワードの設定、アクセス制限 (印刷、コピー、編集など) の定義を行います。コード例は、Python アプリケーション内で機密コンテンツを保護し、PDF のセキュリティを効果的に管理して、アクセス制御とデータの機密性を確保する方法を示しています。
---

機密コンテンツやビジネスクリティカルなコンテンツを扱う場合は、ドキュメントセキュリティの管理が不可欠です。.NET 経由の Aspose.PDF for Python には、プログラムによる暗号化の適用、権限によるアクセス制御、保護された PDF ファイルの復号化を行うための堅牢な API が用意されています。

この記事では、権限の設定、暗号化の適用と削除、パスワードの変更、保護状態の検出など、すべてを PDF ワークフロー内で行う実践的な例を Python 開発者に紹介します。

.NET 経由の Python 用 Aspose.PDF を利用すると、開発者が PDF のセキュリティを完全に制御できるようになります。

**権限の設定**-権限を使用したきめ細かなアクセス制御。
**ファイルの暗号化**-カスタムパスワードで AES または RC4 暗号化を適用します。
**Decrypt File **-所有者パスワードを使用してセキュリティを削除します。
**パスワードの変更**-内容を変更せずに認証情報をローテーションまたは更新します。
**セキュリティ検査**-暗号化ステータスまたは必要なパスワードタイプを検出します。

このページは、PDF ドキュメントをパスワードで保護したり、印刷やコピーを制限したり、認証情報をローテーションしたり、ドキュメントが暗号化されているかどうかを確認したりする必要がある場合に使用します。

## 既存の PDF ファイルへの権限の設定

アクセス権限とともにユーザーパスワードと所有者パスワードを割り当てることにより、特定の操作 (印刷、コピー、フォーム入力など) を制限または許可できます。

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def set_privileges_on_existing_pdf_file(infile: str, outfile: str) -> None:
    """Set restricted privileges on an existing PDF document."""
    with ap.Document(infile) as document:
        document_privilege = ap.facades.DocumentPrivilege.forbid_all
        document_privilege.allow_screen_readers = True
        document.encrypt(
            "user",
            "owner",
            document_privilege,
            ap.CryptoAlgorithm.AESx128,
            False,
        )
        document.save(outfile)
```

## さまざまな暗号化タイプとアルゴリズムを使用して PDF ファイルを暗号化する

PDF を暗号化すると、有効な資格情報を持つユーザーだけがファイルを開いたり変更したりできるようになります。

>主な用語:

- ユーザーパスワード。文書を開くために必要です。

- 所有者パスワード。権限の変更や暗号化の解除に必要です。

- キーサイズ。AE_SX128 を使用すると、最新のワークフローのセキュリティを最大限に高めることができます。

次のコードスニペットは、PDF ファイルを暗号化する方法を示しています。

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def encrypt_pdf_file(infile: str, outfile: str) -> None:
    """Encrypt a PDF document with user and owner passwords."""
    with ap.Document(infile) as document:
        document.encrypt(
            "user",
            "owner",
            ap.Permissions.EXTRACT_CONTENT,
            ap.CryptoAlgorithm.AESx128,
        )
        document.save(outfile)
```

## 所有者パスワードを使用して PDF ファイルを復号化する

パスワード保護を解除してフルアクセスを回復するには:

1. 正しいパスワード (「password」はユーザーまたは所有者のパスワード) を使用して暗号化された PDF をロードします。
1. 文書からすべてのパスワード保護と暗号化設定を削除します。
1. 保護が解除された PDF を、指定した出力ファイルに保存します。

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def decrypt_pdf_file(infile: str, outfile: str) -> None:
    """Decrypt a password-protected PDF document."""
    with ap.Document(infile, "password") as document:
        document.decrypt()
        document.save(outfile)
```

## 公開鍵証明書による PDF の暗号化と復号化

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def pub_sec_encryption(
    crypto_algorithm,
    pub_cert: str,
    in_pfx: str,
    outfile: str,
) -> None:
    """Demonstrate public-key encryption and decryption."""
    pfx_password = "12345"

    with ap.Document() as document:
        document.info.title = "TestTitle"
        document.info.author = "TestAuthor"
        page = document.pages.add()
        page.paragraphs.add(ap.text.TextFragment("Hello World!"))

        with open(pub_cert, "rb") as file_stream:
            byte_content = file_stream.read()

        document.encrypt(
            ap.Permissions.PRINT_DOCUMENT,
            crypto_algorithm,
            [byte_content],
        )
        document.save(outfile)

    with ap.Document(
        outfile,
        ap.security.CertificateEncryptionOptions(pub_cert, in_pfx, pfx_password),
    ) as document:
        print(document.info.title)
        print(document.info.author)

        text_absorber = ap.text.TextAbsorber()
        document.pages[1].accept(text_absorber)
        print(text_absorber.text)

        document.decrypt()
        document.save(path.join(path.dirname(outfile), "pubsec_decrypted_out.pdf"))
```

## PDF ファイルのパスワードの変更

PDF ドキュメントのコンテンツと構造を維持したまま、セキュリティ認証情報 (ユーザーパスワードと所有者パスワード) を更新すること。

1. 既存の所有者パスワード ('owner') を使用して PDF を開きます。これにより、セキュリティ設定を変更する権限を含むフルアクセスが可能になります。
1. 古いパスワードを新しいユーザーパスワード ('newuser') と新しい所有者パスワード ('newowner') に置き換えます。
1. PDF を更新したパスワード設定で保存します。

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def change_password(infile: str, outfile: str) -> None:
    """Change the passwords of a password-protected PDF document."""
    with ap.Document(infile, "owner") as document:
        document.change_passwords("owner", "newuser", "newowner")
        document.save(outfile)
```

## 方法-ソース PDF がパスワードで保護されているかどうかを確認する

### Array から正しいパスワードを確認

シナリオによっては、セキュリティで保護された PDF にアクセスするために、候補のリストから正しいパスワードを特定する必要がある場合があります。以下のコードスニペットは、PDF ファイルがパスワードで保護されているかどうかを確認し、.NET 経由の Aspose.PDF for Python を使用して定義済みのパスワードリストを繰り返し処理してロック解除を試みる方法を示しています。

このプロセスには以下が含まれます。

1. PDFFileInfo を使用して PDF が暗号化されているかどうかを検出します。
1. AP.Document () を使用して各パスワードでPDFを開こうとします。
1. 成功すると、ページ数が印刷されます。
1. そうでない場合は、例外をキャッチし、失敗したパスワードを報告します。

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def determine_correct_password_from_array(infile: str) -> None:
    """Try a list of passwords until the document opens successfully."""
    with ap.facades.PdfFileInfo() as pdf_file_info:
        pdf_file_info.bind_pdf(infile)
        print(f"File is password protected {pdf_file_info.is_encrypted}")

    passwords = ["test", "test1", "test2", "test3", "sample"]

    for password in passwords:
        try:
            with ap.Document(infile, password) as document:
                if len(document.pages) > 0:
                    print(f"Password = {password} is correct")
                    print(f"Number of pages in document = {len(document.pages)}")
                    break
        except Exception:
            print(f"Password = {password} is not correct")
```

## 関連するセキュリティトピック

- [Python で PDF ファイルを保護して署名する方法](/pdf/ja/python-net/securing-and-signing/)
- [Python で PDF ファイルにデジタル署名する方法](/pdf/ja/python-net/digitally-sign-pdf-file/)
- [Python で PDF から署名情報を抽出する方法](/pdf/ja/python-net/extract-image-and-signature-information/)
- [Python のスマートカードから PDF ドキュメントに署名する](/pdf/ja/python-net/sign-pdf-document-from-smart-card/)


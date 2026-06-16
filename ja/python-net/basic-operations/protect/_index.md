---
title: Python で PDF ファイルを保護する方法
linktitle: PDF ファイルの暗号化と復号化
type: docs
weight: 70
url: /ja/python-net/protect-pdf-file/
description: Python でファイルを暗号化し、保護された PDF を解読し、パスワードを変更する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python での PDF 権限の設定と暗号化の管理
Abstract: このページでは、.NET 経由で Aspose.PDF for Python を使用してドキュメント権限を設定する方法、暗号化を適用する方法、PDF ファイルを復号化する方法、およびパスワードを変更する方法について説明します。Python アプリケーションでの、ユーザーパスワードと所有者パスワードの設定、アクセス制限の定義 (印刷、コピー、編集など)、および PDF セキュリティの管理について説明します。
---

## PDF をパスワードと権限で暗号化

.NET 経由で Aspose.PDF for Python を使用すると、パスワードベースの暗号化と制限付き権限で PDF ドキュメントを保護できます。

1. PDF ドキュメントをロードします。
1. を作成 `DocumentPrivilege` 権限オブジェクト。
1. 必要な権限を有効にします。
1. ユーザーパスワードと所有者パスワードを設定します。
1. 暗号化アルゴリズムを選択します。
1. 文書に暗号化を適用します。
1. 暗号化された PDF を保存します。

```python
import aspose.pdf as ap

def encrypt_password(infile, outfile):
    """
    Encrypt PDF with password and permissions.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        encrypt_password("sample.pdf", "sample_protected.pdf")

    Note:
        Uses AES 128-bit encryption. Allows screen readers, forbids all other operations.
        User password: "userpassword", Owner password: "ownerpassword".
    """
    document = ap.Document(infile)
    document_privilege = ap.facades.DocumentPrivilege.forbid_all
    document_privilege.allow_screen_readers = True

    document.encrypt(
        "userpassword",
        "ownerpassword",
        document_privilege,
        ap.CryptoAlgorithm.AESx128,
        False,
    )
    document.save(outfile)
```

## フル権限で PDF を暗号化

.NET 経由で Aspose.PDF for Python を使用して、フルアクセス権限を許可しながら PDF ドキュメントを暗号化します。この例では、古い PDF ビューアとの互換性を保つため RC4 128 ビット暗号化を使用しています。

1. PDF ドキュメントをロードします。
1. ユーザーパスワードと所有者パスワードを定義します。
1. フルアクセス権限を設定します。
1. 暗号化アルゴリズムを選択します。
1. コール `encrypt()` パスワード、権限、およびアルゴリズムを使用します。
1. 暗号化された PDF を保存します。

```python
import aspose.pdf as ap

def encrypt_pdf_file(infile, outfile):
    """
    Encrypt PDF with full permissions.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        encrypt_pdf_file("sample.pdf", "sample_protected.pdf")

    Note:
        Uses RC4 128-bit encryption with allow_all privileges.
    """
    document = ap.Document(infile)
    document.encrypt(
        "userpassword",
        "ownerpassword",
        ap.facades.DocumentPrivilege.allow_all,
        ap.CryptoAlgorithm.RC4x128,
        False,
    )
    document.save(outfile)
```

## 所有者パスワードを使用して PDF ファイルを復号化する

パスワード保護を解除してフルアクセスを回復するには:

1. 正しいパスワード (ユーザーまたは所有者) を使用して暗号化された PDF をロードします。
1. 文書からパスワード保護と暗号化の設定をすべて削除します。
1. 保護が解除された PDF を、指定した出力ファイルに保存します。

```python
import aspose.pdf as ap

def decrypt_pdf_file(infile, outfile):
    """
    Decrypt password-protected PDF.

    Args:
        infile (str): Input encrypted PDF filename
        outfile (str): Output decrypted PDF filename

    Returns:
        None

    Example:
        decrypt_pdf_file("sample_protected.pdf", "sample_unprotected.pdf")

    Note:
        Requires user password to open document.
    """
    document = ap.Document(infile, "userpassword")
    document.decrypt()
    document.save(outfile)
```

## PDF ファイルのパスワードの変更

PDF ドキュメントのコンテンツと構造を維持したまま、セキュリティ認証情報 (ユーザーパスワードと所有者パスワード) を更新します。

1. 既存の所有者パスワードを使用して PDF を開きます。これにより、セキュリティ設定へのフルアクセスが可能になります。
1. 古いパスワードを新しいユーザーパスワードと新しい所有者パスワードに置き換えます。
1. PDF を更新したパスワード設定で保存します。

```python
import aspose.pdf as ap

def change_password(infile, outfile):
    """
    Change user and owner passwords.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        change_password("sample_protected.pdf", "sample_changepassword.pdf")

    Note:
        Changes from ownerpassword to newuser/newowner.
    """
    document = ap.Document(infile, "ownerpassword")
    document.change_passwords("ownerpassword", "newuser", "newowner")
    document.save(outfile)

```

## Array から正しいパスワードを確認

シナリオによっては、セキュリティで保護された PDF にアクセスするために、候補のリストから正しいパスワードを特定する必要がある場合があります。以下のスニペットは、PDF ファイルが暗号化されているかどうかを確認し、あらかじめ定義されているパスワードのリストを繰り返し処理してファイルを開こうとします。

このプロセスには以下が含まれます。

1. 使用 `PdfFileInfo` PDF が暗号化されているかどうかを検出します。
1. を使用して各パスワードでPDFを開きます `ap.Document()`.
1. 成功すると、ページ数が印刷されます。
1. そうでない場合は、例外をキャッチし、失敗したパスワードを報告します。

```python
import aspose.pdf as ap

def determine_correct_password_from_list(infile):
    """
    Test multiple passwords to find correct one.

    Args:
        infile (str): Input encrypted PDF filename

    Returns:
        None

    Example:
        determine_correct_password_from_list("sample_protected.pdf")

    Note:
        Tries passwords: test, test1, test2, test3, userpassword.
        Prints page count if password is correct.
    """
    info = ap.facades.PdfFileInfo(infile)
    print(f"File is password protected {info.is_encrypted}")

    passwords = "test", "test1", "test2", "test3", "userpassword"

    for password in passwords:
        try:
            document = ap.Document(infile, password)
            count = len(document.pages)
            if count > 0:
                print(f"Number of Page in document are = {count}")
        except RuntimeError as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
```

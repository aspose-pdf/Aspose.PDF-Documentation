---
title: PDF ファイルを暗号化
type: docs
weight: 30
url: /ja/python-net/encrypt-pdf-file/
description: PDF ドキュメントを暗号化し、ユーザーがそのファイルに対して実行できる操作を制御する権限を設定します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF の暗号化とユーザーアクションの制御
Abstract: .NET 経由で Aspose.PDF for Python を使用して特定のユーザー権限を定義しながら PDF を暗号化する方法について説明します。このガイドでは、文書を安全に保ちながら、印刷やコピーなどの操作を許可または制限する方法を説明します。
---

## ユーザーパスワードと所有者パスワードで PDF を暗号化

機密コンテンツや制限付きコンテンツを共有する場合、PDF ドキュメントを保護することが不可欠です。暗号化により、文書をパスワードで保護し、ユーザーが実行できる操作を定義できます。このコードスニペットでは、PDF ファイルを保護するために、アクセス権に加えてユーザーパスワードと所有者パスワードを適用する方法を示しています。

1. PDF ファイルセキュリティオブジェクトを作成します。
1. 入力 PDF をバインドします。
1. 文書権限を定義します。
1. PDF を暗号化します。
1. 暗号化された PDF を保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Encrypt PDF with User and Owner Password
def encrypt_pdf_with_user_owner_password(infile, outfile):
    """Encrypt a PDF document using user and owner passwords."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define document privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Encrypt the PDF
    file_security.encrypt_file(
        "user_password", "owner_password", privilege, pdf_facades.KeySize.X128
    )

    # Save encrypted PDF
    file_security.save(outfile)
```

## PDF を権限付きで暗号化

次のコードスニペットでは、印刷やコピーなどの選択したアクションを許可し、他のアクションを制限する方法について説明します。

1. を初期化します [PDF ファイルセキュリティ](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/) クラス。
1. 入力 PDF をバインドします。
1. ドキュメント権限を設定します。
1. 「暗号化ファイル ()」メソッドを呼び出します。
1. 暗号化された PDF を保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Encrypt PDF with Permissions
def encrypt_pdf_with_permissions(infile, outfile):
    """Encrypt a PDF document and configure specific permissions."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Configure privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True
    privilege.allow_copy = True

    # Encrypt the PDF
    file_security.encrypt_file(
        "user_password", "owner_password", privilege, pdf_facades.KeySize.X128
    )

    # Save encrypted PDF
    file_security.save(outfile)
```

## 暗号化アルゴリズムによる PDF の暗号化

PDF暗号化では、文書をパスワードで保護するだけでなく、暗号化アルゴリズムと強度を選択することもできます。適切なアルゴリズムを選択することで、機密文書のセキュリティを強化できます。

1. PDF ファイルセキュリティオブジェクトを作成します。
1. 入力 PDF をバインドします。
1. 文書権限を定義します。
1. PDF をアルゴリズムで暗号化します。
1. 暗号化された PDF を保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Encrypt PDF with Encryption Algorithm
def encrypt_pdf_with_encryption_algorithm(infile, outfile):
    """Encrypt a PDF document using a specific encryption algorithm."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Encrypt the PDF using AES algorithm
    file_security.encrypt_file(
        "user_password",
        "owner_password",
        privilege,
        pdf_facades.KeySize.X256,
        pdf_facades.Algorithm.AES,
    )

    # Save encrypted PDF
    file_security.save(outfile)
```

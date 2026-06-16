---
title: 既存の PDF ファイルへの権限の設定
type: docs
weight: 40
url: /ja/python-net/set-privileges/
description: PDF ドキュメントの権限を設定および管理して、印刷、コピー、編集などのユーザーアクションを制御します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF 権限とアクセス制御の管理
Abstract: .NET 経由で Aspose.PDF for Python を使用してドキュメント権限を設定することで、ユーザーが PDF で何をできるかを制御する方法について説明します。このガイドでは、印刷、コピー、編集などの操作を制限するために、パスワードの有無にかかわらず権限を適用する方法について説明します。
---

## パスワードなしで PDF 権限を設定

.NET 経由の Aspose.PDF for Python を使用して、ユーザーまたは所有者のパスワードを指定せずに PDF にドキュメント権限を適用する方法を確認してください。このコードスニペットは、ドキュメントにアクセス可能な状態を維持したまま、許可されるアクションを制御する方法を示しています。

1. 「PDF ファイルセキュリティ」オブジェクトを作成します。
1. 入力 PDF をバインドします。
1. ドキュメント権限を定義します。
1. パスワードを渡さずに 'set_privilege () 'メソッドを呼び出します。
1. 更新した PDF を保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Set PDF Privileges Without Passwords
def set_pdf_privileges_without_passwords(infile, outfile):
    """Set PDF privileges without specifying user and owner passwords."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Apply privileges (owner password will be generated automatically)
    file_security.set_privilege(privilege)

    # Save updated PDF
    file_security.save(outfile)
```

## ユーザーパスワードと所有者パスワードによる PDF 権限の設定

PDF ドキュメントを完全に保護するには、アクセス制御 (パスワード) と使用制限 (権限) の両方が必要になることがよくあります。これらを組み合わせることで、権限のあるユーザーだけが文書を開いて特定の操作を実行できるようにすることができます。

set_privilege メソッドをパスワードパラメータと共に使用すると、次のことが可能になります。

- ユーザーパスワードで文書を保護する
- フルコントロール用の所有者パスワードの定義
- 許可されたアクションと制限されたアクションの設定
- ドキュメントレベルのセキュリティポリシーを適用

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Set PDF Privileges with User and Owner Passwords
def set_pdf_privileges_with_passwords(infile, outfile):
    """Set PDF privileges using user and owner passwords."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True
    privilege.allow_copy = False

    # Apply privileges with passwords
    file_security.set_privilege("user_password", "owner_password", privilege)

    # Save updated PDF
    file_security.save(outfile)
```

## 例外なく PDF 権限を設定してみてください

このコードスニペットでは、アクセスを制御し、コピーなどのアクションを制限しながら、印刷など他のアクションを許可する方法について説明します。

1. 「PDFFileSecurity」オブジェクトを作成します。
1. 'bind_pdf () 'メソッドを使用してソース PDF をロードします。
1. ドキュメント権限を定義します。
1. パスワードで権限を適用します。
1. 更新した PDF を保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Try Set PDF Privileges Without Exception
def try_set_pdf_privileges_without_exception(infile, outfile):
    """Attempt to set PDF privileges without throwing an exception on failure."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Attempt to apply privileges
    result = file_security.try_set_privilege(
        "user_password", "owner_password", privilege
    )

    # Save only if operation succeeded
    if result:
        file_security.save(outfile)
    else:
        print("Setting privileges failed. Check passwords or document state.")
```

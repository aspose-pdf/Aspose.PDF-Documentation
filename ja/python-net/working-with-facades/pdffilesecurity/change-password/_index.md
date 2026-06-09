---
title: PDF ファイルのパスワードを変更
type: docs
weight: 10
url: /ja/python-net/change-password/
description: .NET 経由で Aspose.PDF for Python を使用して、保護された PDF ドキュメントのユーザーパスワードと所有者パスワードを変更します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF パスワードの更新
Abstract: .NET 経由で Aspose.PDF for Python を使用して、保護された PDF ファイル内のユーザーパスワードと所有者パスワードの両方を変更する方法について説明します。この例は、既存の暗号化と権限をそのまま維持したまま、アクセス認証情報を安全に更新する方法を示しています。
---

## ユーザーと所有者のパスワードの変更

多くの場合、既存のセキュリティ設定を変更せずに、保護された PDF のパスワードを更新する必要がある場合があります。これは、認証情報のローテーション、所有権の移転、または文書のセキュリティ強化に役立ちます。

の「パスワード変更」メソッド [PDF ファイルセキュリティ](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/) クラスでは次のことができます。

- ユーザーパスワードの更新 (文書を開くために必要)
- 所有者パスワードの更新 (権限の管理に使用)
- 現在の暗号化と権限の設定を保持

1. 「PDFFileSecurity」オブジェクトを作成します。
1. 入力 PDF をバインドします。
1. 'change_password () 'メソッドを使用してパスワードを変更します。
1. 更新した PDF を保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Change User and Owner Password
def change_user_and_owner_password(infile, outfile):
    """Change user and owner passwords while keeping existing security settings."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Change passwords
    file_security.change_password(
        "owner_password", "new_user_password", "new_owner_password"
    )

    # Save updated PDF
    file_security.save(outfile)
```

## パスワードの変更とセキュリティのリセット

保護された PDF 文書を扱う場合、パスワードを変更するだけでは不十分な場合があります。また、印刷、コピー、編集権限などの権限を調整する必要がある場合もあります。

.NET 経由の Aspose.PDF for Python で PDF のセキュリティ設定をリセットしながら、ユーザーと所有者のパスワードを更新する方法について説明します。この例は、新しいアクセス認証情報とともに、文書の権限と暗号化強度を再定義する方法を示しています。

1. 「PDFFileSecurity」オブジェクトを作成します。
1. 入力 PDF をバインドします。
1. 「DocumentPrivilege」オブジェクトを作成し、許可されるアクションを設定します。
1. パスワードを変更し、セキュリティをリセットします。
1. 更新した PDF を保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Change Password and Reset Security
def change_password_and_reset_security(infile, outfile):
    """Change passwords and reset document security settings."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define new privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Change passwords and reset security
    file_security.change_password(
        "owner_password",
        "new_user_password",
        "new_owner_password",
        privilege,
        pdf_facades.KeySize.X128,
    )

    # Save updated PDF
    file_security.save(outfile)
```

## 例外なくパスワードを変更してみてください

一部のワークフロー、特にバッチ処理や自動化システムでは、実行を中断する可能性のある例外を回避することが重要です。エラーを発生させるよりも、成功または失敗を報告する安全な操作の方が望ましい場合もあります。

の「パスワード変更試行」メソッド [PDF ファイルセキュリティ](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/) クラスは次の方法でこの機能を提供します。

1. 「PDFFileSecurity」オブジェクトを作成します。
1. 'bind_pdf () 'メソッドを使用して PDF ドキュメントをロードします。
1. パスワードを変更してみます。
1. 結果を確認してください。
1. 更新した PDF を保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Try Change Password Without Exception
def try_change_password_without_exception(infile, outfile):
    """Attempt to change passwords without throwing an exception on failure."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Attempt to change passwords
    result = file_security.try_change_password(
        "owner_password", "new_user_password", "new_owner_password"
    )

    # Save only if operation succeeded
    if result:
        file_security.save(outfile)
    else:
        print("Password change failed. Check owner password or document security.")
```

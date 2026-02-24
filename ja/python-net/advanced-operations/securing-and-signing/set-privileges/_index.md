---
title: 権限の設定、PDFの暗号化と復号化
linktitle: PDFファイルの暗号化と復号化
type: docs
weight: 70
url: /ja/python-net/set-privileges-encrypt-and-decrypt-pdf-file/
description: Pythonを使用してさまざまな暗号化タイプとアルゴリズムでPDFファイルを暗号化します。また、所有者パスワードを使用してPDFファイルを復号化します。
lastmod: "2025-06-22"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PythonでPDFファイルを暗号化または復号化する
Abstract: このドキュメントページでは、Aspose.PDF for Python を使用してドキュメントの権限を設定し、暗号化を適用し、PDF ファイルを復号化する方法を説明します。開発者がユーザー パスワードと所有者パスワードを構成し、印刷、コピー、編集などのアクセス制限を定義する手順を案内します。コード例は、機密コンテンツを保護し、Python アプリケーション内で PDF のセキュリティを効果的に管理する方法を示し、アクセス制御とデータ機密性を確保します。
---

機密情報や業務上重要なコンテンツを扱う際、ドキュメントのセキュリティ管理は不可欠です。Aspose.PDF for Python via .NET は、プログラムで暗号化を適用し、権限によってアクセスを制御し、保護された PDF ファイルを復号化するための堅牢な API を提供します。

この記事では、Python 開発者に対し、権限設定、暗号化の適用と削除、パスワードの変更、保護状態の検出といった実用的な例を PDF ワークフロー内で順に解説します。

Aspose.PDF for Python via .NET は、開発者に PDF セキュリティに対する完全なコントロールを提供します：

**権限の設定** - 権限を使用した細かいアクセス制御。
**ファイルの暗号化** - カスタムパスワードで AES または RC4 暗号化を適用します。
**ファイルの復号化** - 所有者パスワードを使用してセキュリティを解除します。
**パスワードの変更** - コンテンツを変更せずに資格情報をローテーションまたは更新します。
**セキュリティの検査** - 暗号化状態や必要なパスワードタイプを検出します。

## 既存の PDF ファイルに権限を設定する

ユーザー パスワードと所有者パスワード、およびアクセス権限を割り当てることで、印刷やコピー、フォーム入力などの特定の操作を制限または許可できます。

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Instantiate Document Privileges object
        # Apply restrictions on all privileges
        document_privilege = ap.facades.DocumentPrivilege.forbid_all
        # Only allow screen reading
        document_privilege.allow_screen_readers = True
        # Encrypt the file with User and Owner password
        # Need to set the password, so that once the user views the file with user password
        # Only screen reading option is enabled
        document.encrypt("user", "owner", document_privilege, ap.CryptoAlgorithm.AE_SX128, False)
        # Save PDF document
        document.save(path_outfile)
```

## 異なる暗号化タイプとアルゴリズムを使用した PDF の暗号化

PDF を暗号化することで、有効な資格情報を持つユーザーのみがファイルを開いたり変更したりできるようになります。

>キー用語：

- ユーザーパスワード。文書を開くために必要です。

- 所有者パスワード。権限の変更や暗号化の解除に必要です。

- キーサイズ。最新のワークフローで最大のセキュリティを得るために AE_SX128 を使用してください。

以下のコードスニペットは、PDF ファイルを暗号化する方法を示しています。

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Encrypt PDF
        document.encrypt("user", "owner", ap.Permissions.EXTRACT_CONTENT, ap.CryptoAlgorithm.AE_SX128)
        # Save PDF document
        document.save(path_outfile)
```

## 所有者パスワードを使用した PDF の復号化

パスワード保護を解除し、完全なアクセスを復元するには：

1. 正しいパスワード（'password' はユーザーまたは所有者パスワード）を使用して暗号化された PDF を読み込みます。
1. 文書からすべてのパスワード保護と暗号化設定を削除します。
1. 保護が解除された PDF を指定された出力ファイルに保存します。

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document with password
    with ap.Document(path_infile, "password") as document:
        # Decrypt PDF
        document.decrypt()
        # Save PDF document
        document.save(path_outfile)
```

## PDF ファイルのパスワード変更

PDF ドキュメントのセキュリティ資格情報（ユーザーおよび所有者パスワード）を、コンテンツと構造を保持したまま更新するには。

1. 既存の所有者パスワード（'owner'）を使用して PDF を開きます。これにより、セキュリティ設定の変更権限を含む完全なアクセスが可能になります。
1. 古いパスワードを新しいユーザーパスワード（'newuser'）と新しい所有者パスワード（'newowner'）に置き換えます。
1. 更新されたパスワード設定で PDF を保存します。

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document with password
    with ap.Document(path_infile, "owner") as document:
        # Change password
        document.change_passwords("owner", "newuser", "newowner")
        # Save PDF document
        document.save(path_outfile)
```

## 方法 - ソース PDF がパスワードで保護されているかどうかを判断する

### 配列から正しいパスワードを判定する

場合によっては、保護された PDF にアクセスするために候補リストから正しいパスワードを特定する必要があります。以下のコードスニペットは、PDF ファイルがパスワードで保護されているかどうかを確認し、Aspose.PDF for Python via .NET を使用して事前定義されたパスワードリストを反復処理しながら解除を試みる方法を示しています。

プロセスは以下を含みます：

1. PdfFileInfo を使用して PDF が暗号化されているか検出します。
1. ap.Document() を使用して各パスワードで PDF のオープンを試みます。
1. 成功した場合、ページ数を出力します。
1. 失敗した場合は例外を捕捉し、失敗したパスワードを報告します。

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    with ap.facades.PdfFileInfo() as pdf_file_info:
        # Bind PDF document
        pdf_file_info.bind_pdf(path_infile)
        # Determine if the source PDF is encrypted
        print("File is password protected " + str(pdf_file_info.is_encrypted))

        passwords = ["test", "test1", "test2", "test3", "sample"]

        for password_index in range(len(passwords)):
            try:
                with ap.Document(path_infile, passwords[password_index]) as document:
                    if len(document.pages) > 0:
                        print("Number of Pages in document are = " + str(len(document.pages)))
                    password_index = password_index + 1
            except Exception as e:
                print("Password = " + passwords[password_index] + " is not correct")
                password_index = password_index + 1
```



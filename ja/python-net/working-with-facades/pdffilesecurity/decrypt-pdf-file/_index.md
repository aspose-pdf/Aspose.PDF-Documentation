---
title: PDF ファイルを復号化
type: docs
weight: 20
url: /ja/python-net/decrypt-pdf-file/
description: このガイドでは、印刷、コピー、編集などの制限を解除して、PDFドキュメントに完全にアクセスする方法について説明します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF からパスワード保護を削除する
Abstract: この記事では、所有者パスワードを使用して PDF ファイルを復号化する方法を説明します。コンテンツの印刷、編集、コピーなどの操作を制限するセキュリティ制限を解除する手順について説明します。正しい所有者パスワードを適用することで、ユーザーは文書のロックを解除し、その機能を完全に制御できるようになります。
---

## 所有者パスワードで PDF を復号化

.NET 経由の Aspose.PDF for Python を使用して、所有者パスワードを使用してパスワードで保護された PDF ドキュメントを復号化します。この操作により暗号化が解除され、ドキュメントへの無制限のアクセスが可能になります。

1. 「PDFFileSecurity」オブジェクトを作成します。
1. 'bind_pdf () 'メソッドを使用して暗号化された PDF をロードします。
1. ドキュメントを復号化します。
1. 復号化された PDF を保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Decrypt PDF with Owner Password
def decrypt_pdf_with_owner_password(infile, outfile):
    """Decrypt a PDF document using the owner password."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Decrypt the PDF
    file_security.decrypt_file("owner_password")

    # Save decrypted PDF
    file_security.save(outfile)
```

## 例外なく PDF を復号化してみてください

PDF 文書は、アクセスや使用を制限するためにパスワードで保護されていることがよくあります。このような文書に完全にアクセスしたり変更したりするには、暗号化を解除する必要がある場合があります。.NET 経由の Aspose.PDF for Python を使用して、所有者パスワードを使用して保護された PDF ドキュメントを復号化し、暗号化とアクセス制限を解除します。

1. 「PDFFileSecurity」オブジェクトを作成します。
1. 入力 PDF をバインドします。
1. PDF を復号化します。
1. 出力 PDF を保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Try Decrypt PDF Without Exception
def try_decrypt_pdf_without_exception(infile, outfile):
    """Attempt to decrypt a PDF without throwing an exception on failure."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Attempt to decrypt the PDF
    result = file_security.try_decrypt_file("owner_password")

    # Save only if decryption was successful
    if result:
        file_security.save(outfile)
    else:
        print("Decryption failed. Check password or document security.")
```

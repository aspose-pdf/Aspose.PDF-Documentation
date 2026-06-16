---
title: PDF メタデータを取得
type: docs
weight: 20
url: /ja/python-net/get-pdf-metadata/
description: Aspose.PDF for Python を使用して PDF ドキュメントからメタデータを抽出して表示します。
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python 用 Aspose.PDF を使用して PDF メタデータを取得します。
Abstract: このガイドでは、Aspose.PDF for Python を使用して PDF ドキュメントからメタデータを抽出して表示する方法を示します。タイトル、作成者、キーワード、作成日/変更日、カスタムメタデータフィールドなどの標準の PDF プロパティにアクセスする方法を学習します。さらに、このガイドでは PDF の有効性、暗号化、およびポートフォリオステータスのチェックについても説明しています。
---

PDF ドキュメントには、多くの場合、ドキュメントの内容、作成者、および権限を説明する貴重なメタデータが含まれています。Aspose.PDF には、標準メタデータプロパティとカスタムメタデータプロパティの両方を取得するための便利な API が用意されています。このコードスニペットは、の使い方を抜粋したものです。 [PDF ファイル情報](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) クラスを使用して PDF ファイルをプログラムで検査します。Python のステップバイステップの例も含まれています。

1. PDF ファイルをロードします。
1. 標準メタデータを取得します。
1. PDF のステータスとセキュリティを確認してください。
1. カスタムメタデータを取得します。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_pdf_metadata(infile):

    # Get and display PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)
    print(f"Subject: {pdf_info.subject}")
    print(f"Title: {pdf_info.title}")
    print(f"Keywords: {pdf_info.keywords}")
    print(f"Creator: {pdf_info.creator}")
    print(f"Creation Date: {pdf_info.creation_date}")
    print(f"Modification Date: {pdf_info.mod_date}")

    # Check PDF status
    print(f"Is Valid PDF: {pdf_info.is_pdf_file}")
    print(f"Is Encrypted: {pdf_info.is_encrypted}")
    print(f"Has Open Password: {pdf_info.has_open_password}")
    print(f"Has Edit Password: {pdf_info.has_edit_password}")
    print(f"Is Portfolio: {pdf_info.has_collection}")

    # Retrieve and display a specific custom attribute
    reviewer = pdf_info.get_meta_info("Reviewer")
    print(f"Reviewer: {reviewer if reviewer else 'No Reviewer metadata found.'}")
```

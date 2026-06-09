---
title: 署名情報
type: docs
weight: 60
url: /ja/python-net/signature-information/
description: Python の PDFFileSignature を使用して、署名済み PDF ファイルから署名名、署名者の詳細、タイムスタンプ、署名メタデータを読み取る方法を学びます。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python で PDF ドキュメントから署名の詳細を読み込む
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して署名付き PDF ドキュメント内の署名メタデータを検査する方法について説明します。署名名の一覧表示、署名者の詳細の読み取り、署名日時の取得、署名の理由と場所の抽出を行う方法を説明します。
---

.NET 経由の Python 用 Aspose.PDF は [PDF ファイル署名](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) PDF文書のデジタル署名を検査するためのファサード。文書に署名したら、その文書を使用して署名名を読み取り、署名者名、連絡先情報、署名時間、理由、場所などのメタデータを取得できます。

この例は、4 つの一般的な署名情報タスクを示しています。

1. 署名済みの PDF にすべての署名名を一覧表示します。
1. 選択した署名の署名者の詳細を読み取ります。
1. 署名日時を取得します。
1. 署名の理由と場所を読んでください。

## 署名名を取得

この方法は、PDF に 1 つ以上の署名が含まれている場合で、どの署名エントリが使用可能かを調べたい場合に使用します。この例では文書を開き、によって返されたリストを印刷します。 `get_sign_names()`.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_names(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        signature_names = list_signature_names(pdf_signature)
        print(f"Signature Names: {signature_names}")
    finally:
        pdf_signature.close()
```

## 署名者の詳細を取得

署名名がわかれば、署名者固有のメタデータを取得できます。この例では、文書内の最初の署名の署名者名と連絡先情報を読み取ります。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signer_details(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signer_name = pdf_signature.get_signer_name(sign_name)
        contact_info = pdf_signature.get_contact_info(sign_name)
        print(
            f"Signer Details for '{sign_name}': "
            f"signer_name={signer_name}, contact_info={contact_info}"
        )
    finally:
        pdf_signature.close()
```

## 署名の日付と時刻を取得

使用 `get_date_time()` 特定の署名がいつ適用されたかを判断します。これは文書ワークフローの監査や署名履歴の表示に役立ちます。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_date_and_time(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_date = pdf_signature.get_date_time(sign_name)
        print(f"Signature Date and Time for '{sign_name}': {signature_date}")
    finally:
        pdf_signature.close()
```

## 署名の理由と場所を取得

デジタル署名には、署名の理由や場所などの説明的なメタデータも保存できます。この例では、選択した署名の 2 つの値を取得し、まとめて印刷します。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_reason_and_location(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_reason = pdf_signature.get_reason(sign_name)
        signature_location = pdf_signature.get_location(sign_name)
        print(
            f"Signature Reason and Location for '{sign_name}': "
            f"reason={signature_reason}, location={signature_location}"
        )
    finally:
        pdf_signature.close()
```


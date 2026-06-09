---
title: 改訂と権限
type: docs
weight: 40
url: /ja/python-net/revision-permissions/
description: Python の PDFFileSignatureを使用して、PDFファイル内の署名の改訂、文書の改訂、および認証権限を検査する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python での PDF 署名リビジョンとアクセス権データの読み取り
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して、署名済みまたは認証済み PDF ファイルのリビジョンおよび権限情報を調べる方法を説明します。署名のリビジョン番号を取得する方法、文書の改訂総数を数える方法、認証済み PDF からアクセス権限を読み取る方法を説明します。
---

.NET 経由の Python 用 Aspose.PDF は [PDF ファイル署名](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) 署名および認証されたPDF文書を扱うためのファサード。署名を追加するだけでなく、署名メタデータを調べて、文書に含まれる改訂の数や、認証後にどのような変更が許可されるかを把握することもできます。

この例は、3 つの一般的な検査タスクを示しています。

1. 既存の署名のリビジョン番号を取得します。
1. 署名済み文書の改訂の合計数を取得します。
1. 認証済み PDF のアクセス権限を読み取ります。

## 署名のリビジョン番号を取得

この方法は、PDF にすでに 1 つ以上の署名が含まれていて、特定の署名に関連付けられているリビジョンを識別する必要がある場合に使用します。この例では、最初に使用可能な署名名を解決してから呼び出します。 `get_revision()`.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_revision(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_revision = pdf_signature.get_revision(sign_name)
        print(f"Signature Revision for '{sign_name}': {signature_revision}")
    finally:
        pdf_signature.close()
```

## ドキュメントのリビジョンの合計数を取得する

使用 `get_total_revision()` 署名済み PDF に保存されているリビジョン数を知る必要がある場合。これは、元の署名が適用された後に文書が複数回更新されたかどうかを確認するのに役立ちます。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_total_document_revisions(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        total_revisions = pdf_signature.get_total_revision()
        print(f"Total Document Revisions: {total_revisions}")
    finally:
        pdf_signature.close()
```

## 認証済み PDF からアクセス権限を取得

認証済み文書では、認証後にどのような変更が許可されるかを定義できます。使用 `get_access_permissions()` その権限レベルを調べ、文書が変更やフォームへの記入、その他の制御された変更を許可していないかどうかを判断します。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_access_permissions(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        access_permissions = pdf_signature.get_access_permissions()
        print(f"Access Permissions: {access_permissions}")
    finally:
        pdf_signature.close()
```


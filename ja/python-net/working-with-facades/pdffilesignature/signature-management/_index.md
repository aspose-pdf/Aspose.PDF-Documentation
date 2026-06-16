---
title: シグネチャ管理
type: docs
weight: 80
url: /ja/python-net/signature-management/
description: Python の PDFFileSignature を使用して PDF ドキュメントからデジタル署名を削除する方法と、必要に応じて署名フィールドをクリーンアップする方法について説明します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python での PDF 署名の削除と署名フィールドのクリーンアップ
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメント内の既存のデジタル署名を管理する方法について説明します。PDF から署名を削除する方法と、署名とそれに関連する署名フィールドを削除する方法を示します。
---

.NET 経由の Python 用 Aspose.PDF は [PDF ファイル署名](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) PDF文書内の既存のデジタル署名を操作するためのファサード。署名の読み取りと検証に加えて、ワークフローで署名済みコンテンツの更新や署名フィールドのクリアが必要な場合には、署名を削除することもできます。

この例は、2 つの一般的な署名管理タスクを示しています。

1. PDF ドキュメントから署名を削除します。
1. 署名を削除し、関連する署名フィールドをクリーンアップします。

## PDF から署名を削除する

使用 `remove_signature()` 基になる署名フィールド構造を維持したまま、選択した署名を文書から削除したい場合。この例では、署名付き PDF を開き、署名名を解決して削除し、更新された出力ファイルを保存します。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def remove_signature_from_pdf(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        pdf_signature.remove_signature(sign_name)
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## 署名を削除してフィールドをクリーンアップする

追加でオーバーロードを使用する `True` 署名を削除したいときや、関連する署名フィールドをクリーンアップしたいときにフラグを付けます。これは、署名が削除された後にそのフィールドを文書に残してはいけない場合に便利です。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def remove_signature_with_field_cleanup(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        pdf_signature.remove_signature(sign_name, True)
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

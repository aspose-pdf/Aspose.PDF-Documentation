---
title: PDF 証明書
type: docs
weight: 30
url: /ja/python-net/pdf-certification/
description: PDFFileSignatureとDocMDPSignatureを使用して異なるドキュメント変更権限を使用してPythonでPDFドキュメントを認証する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python の DocMDP パーミッションを使用して PDF ドキュメントを認証する方法
Abstract: この記事では、PDFFileSignature ファサードを使用して、.NET 経由で Aspose.PDF for Python で PDF ドキュメントを認証する方法について説明します。DocMDPSignature を作成する方法、フォーム入力権限で証明書を適用する方法、認証レベルを変更しないドキュメントをロックする方法について説明します。
---

.NET 経由の Python 用 Aspose.PDF では、以下のようにドキュメントレベルの署名を適用して PDF ドキュメントを認証できます。 [PDF ファイル署名](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/)。認証は、文書が認証された後にどのような変更が許可されるかを定義する点で、標準の承認署名とは異なります。

この記事では、次の 2 つの一般的な認定ワークフローについて説明します。

1. PDF を認証し、認証後にフォームへの入力を許可します。
1. PDF を認証し、それ以上変更されないようにします。

## フォーム入力用の PDF の認証

この方法は、文書は認証されたままでも、ユーザーがインタラクティブフォームへの記入やファイルへの署名を続ける必要がある場合に使用します。は `FILLING_IN_FORMS` 権限レベルでは、証明書の有効性を維持したまま、これらの制御された変更が可能になります。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def certify_pdf_with_mdp_signature(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        doc_mdp_signature = create_doc_mdp_signature(
            certificate_path,
            ap.forms.DocMDPAccessPermissions.FILLING_IN_FORMS,
            reason="Certified for form filling and signing",
        )
        pdf_signature.certify(
            1,
            "Certified for form filling and signing",
            "security@example.com",
            "New York, USA",
            True,
            create_signature_rectangle(),
            doc_mdp_signature,
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## 変更なしで文書レベルの認証を適用

このモードは、認証後に認証済み文書を変更しないでおく必要がある場合に使用します。は `NO_CHANGES` 権限レベルは、後で変更すると認証状態が無効になるファイナライズ済みPDFに適しています。

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def apply_document_level_certification(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        doc_mdp_signature = create_doc_mdp_signature(
            certificate_path,
            ap.forms.DocMDPAccessPermissions.NO_CHANGES,
            reason="Certified with no further changes allowed",
        )
        pdf_signature.certify(
            1,
            "Certified with no further changes allowed",
            "security@example.com",
            "New York, USA",
            True,
            create_signature_rectangle(),
            doc_mdp_signature,
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

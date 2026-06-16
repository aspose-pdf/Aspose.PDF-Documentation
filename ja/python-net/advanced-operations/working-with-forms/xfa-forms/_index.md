---
title: XFA フォームでの作業
linktitle: XFA フォーム
type: docs
weight: 20
url: /ja/python-net/xfa-forms/
description: .NET API 経由の Aspose.PDF for Python を使用すると、PDF ドキュメント内の XFA フィールドと XFA アクロフォームフィールドを操作できます。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## XFA をアクロフォームに変換

{{% alert color="primary" %}}

オンラインで試す
Aspose.PDF 変換の品質を確認したり、次のリンクから結果をオンラインで確認したりできます。 [products.aspose.app/pdf/xfa/acroform](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

次のコードスニペットは、動的 XFA (XML フォームアーキテクチャ) フォームを標準の AcroForm に変換する方法を示しています。

**主な手順は次のとおりです。**

1. 入力 PDF ドキュメントを読み込んでいます。
1. フォームタイプを標準に変更します。
1. 変換したPDFを新しいファイルに保存します。

この変換により、さまざまな PDF リーダーやアプリケーション間での互換性が向上し、一貫したフォーム処理が可能になります。

```python
import aspose.pdf as ap
import sys
from os import path

def convert_dynamic_xfa_to_acroform(infile: str, outfile: str):
    """Convert dynamic XFA form to standard AcroForm."""
    with ap.Document(infile) as document:
        document.form.type = ap.forms.FormType.STANDARD
        document.save(outfile)
```

## Ignoreの使用にはレンダリングが必要

この例は、Aspose.PDF for Python を使用してダイナミック XFA フォームを標準の AcroForm に変換する方法を示しています。このコードでは、入力 PDF に XFA フォームが含まれているかどうかを確認し、必要に応じてレンダリングをオーバーライドします。次に、フォームタイプを STANDARD に設定し、更新された PDF を保存します。

```python
import aspose.pdf as ap
import sys
from os import path

def convert_xfa_form_with_ignore_needs_rendering(infile: str, outfile: str):
    """Convert XFA form ignoring needs rendering flag."""
    with ap.Document(infile) as document:
        if not document.form.needs_rendering and document.form.has_xfa:
            document.form.ignore_needs_rendering = True
        document.form.type = ap.forms.FormType.STANDARD
        document.save(outfile)
```

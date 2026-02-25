---
title: XFA フォームの操作
linktitle: XFA フォーム
type: docs
weight: 20
url: /ja/python-net/xfa-forms/
description: Aspose.PDF for Python via .NET API を使用すると、PDF ドキュメント内の XFA および XFA Acroform フィールドを操作できます。
lastmod: "2025-02-17"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## XFA から Acroform への変換

{{% alert color="primary" %}}

オンラインで試す
このリンクで Aspose.PDF の変換品質を確認し、結果をオンラインで表示できます: [products.aspose.app/pdf/xfa/acroform](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

次のコードスニペットは、動的 XFA (XML Forms Architecture) フォームを標準的な AcroForm に変換する方法を示しています。

**主な手順は以下です:**

1. 入力 PDF ドキュメントを読み込む。
1. フォームタイプを STANDARD に変更する。
1. 変換された PDF を新しいファイルに保存する。

この変換により、さまざまな PDF リーダーやアプリケーション間での互換性が向上し、フォーム処理が一貫します。

```python

    import aspose.pdf as ap


    path_infile = self.data_dir + "DynamicXFAToAcroForm.pdf.pdf"
    path_outfile = self.data_dir + "StandardAcroForm_out.pdf"

    # Load dynamic XFA form
    with ap.Document(path_infile) as document:
        # Set the form fields type as standard AcroForm
        document.form.type = ap.forms.FormType.STANDARD
        # Save PDF document
        document.save(path_outfile)
```

## IgnoreNeedsRendering の使用

この例では、Aspose.PDF for Python を使用して動的 XFA フォームを標準的な AcroForm に変換する方法を示します。コードは入力 PDF に XFA フォームが含まれているかをチェックし、必要に応じてレンダリングをオーバーライドします。その後、フォームタイプを STANDARD に設定し、更新された PDF を保存します。

```python

    import aspose.pdf as ap


    path_infile = self.data_dir + "DynamicXFAToAcroForm.pdf.pdf"
    path_outfile = self.data_dir + "StandardAcroForm_out.pdf"

    # Load dynamic XFA form
    with ap.Document(path_infile) as document:
        # check if XFA is present & if rendering should be overwritten
        if not document.form.needs_rendering and document.form.has_xfa:
            document.form.ignore_needs_rendering = True
        # Set the form fields type as standard AcroForm
        document.form.type = ap.forms.FormType.STANDARD
        # Save the resultant PDF
        document.save(path_outfile)
```


---
title: アクロフォームを抽出-Python で PDF からフォームデータを抽出
linktitle: アクロフォームを抽出
type: docs
weight: 30
url: /ja/python-net/extract-form/
description: .NET 経由で Aspose.PDF for Python を使用して PDF ドキュメントの AcroForm フィールドから値を抽出します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF からフォームデータを取得する方法
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメントの AcroForm フィールドからデータを抽出する方法を説明します。この例では、フォームフィールド名を繰り返し処理し、Form ファサードを使用して値を読み取り、下流処理用の辞書を返します。このワークフローは、レポート、検証、外部システムとの統合に役立ちます。
---

## フォームからデータを抽出

### PDF ドキュメントのすべてのフィールドから値を取得

PDF ドキュメントのすべてのフィールドから値を読み取るには、フォームフィールド名を繰り返し処理して、から各値を取得します。 [フォーム](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) ファサード。

以下の手順を実行してください。

1. 入力 PDF をにバインドする `Form` 対象。
1. イテレートスルー `field_names`.
1. で各値を読み込む `get_field()`.
1. 値をディクショナリに保存します。
1. 抽出された値を返すか処理します。

次の Python コードスニペットは、このアプローチを示しています。

```python
import aspose.pdf as ap


def get_values_from_all_fields(input_file_name):
    form = ap.facades.Form(input_file_name)

    form_values = {}
    for field_name in form.field_names:
        form_values[field_name] = form.get_field(field_name)

    print(form_values)
    return form_values
```

## 関連トピック

- [アクロフォームを作成](/pdf/ja/python-net/create-form/)
- [アクロフォームに記入](/pdf/ja/python-net/fill-form/)
- [フォームデータのインポートとエクスポート](/pdf/ja/python-net/import-export-form-data/)
- [アクロフォームの修正](/pdf/ja/python-net/modifying-form/)
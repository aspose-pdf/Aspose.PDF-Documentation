---
title: アクロフォームへの入力-Python を使用して PDF フォームにデータを入力する
linktitle: アクロフォームに記入
type: docs
weight: 20
url: /ja/python-net/fill-form/
description: .NET 経由で Aspose.PDF for Python を使用して PDF ドキュメントの AcroForm フィールドに入力します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF のフォームフィールドに入力する方法
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメントの AcroForm フィールドを入力する方法について説明します。この例では Form ファサードを使用し、フィールド名を辞書の新しい値にマップし、一致するフィールドを更新して、出力 PDF を保存します。このアプローチは、自動文書完成ワークフローやフォームの一括処理に役立ちます。
---

## PDF ドキュメントのフォームフィールドへの入力

次の例では、を使用して既存の PDF フォームの複数のフィールドに入力します。 [フォーム](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) ファサード。

以下の手順を実行してください。

1. フィールド名と値を含むディクショナリを作成します。
1. 入力 PDF を Form オブジェクトにバインドします。
1. 使用可能なフォームフィールドを繰り返し処理します。
1. 辞書にあるフィールドを入力します。
1. 更新した PDF を保存します。

```python
import aspose.pdf as ap

def fill_form(input_file_name, output_file_name):
    new_field_values = {
        "First Name": "Alexander_New",
        "Last Name": "Greenfield_New",
        "City": "Yellowtown_New",
        "Country": "Redland_New",
    }

    form = ap.facades.Form(input_file_name)

    for field_name in form.field_names:
        if field_name in new_field_values:
            form.fill_field(field_name, new_field_values[field_name])

    form.save(output_file_name)
```

## 関連トピック

- [アクロフォームを作成](/pdf/ja/python-net/create-form/)
- [アクロフォームを抽出](/pdf/ja/python-net/extract-form/)
- [フォームデータのインポートとエクスポート](/pdf/ja/python-net/import-export-form-data/)
---
title: アクロフォームの修正
linktitle: アクロフォームの修正
type: docs
weight: 45
url: /ja/python-net/modifying-form/
description: .NET 経由の Aspose.PDF for Python を使用して PDF ドキュメント内の AcroForm フィールドを変更します。これには、テキストのクリア、制限の設定、フィールドのスタイル設定、フィールドの削除などが含まれます。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF フォームフィールドの管理とカスタマイズ
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して AcroForm フィールドを変更する実際的な例を紹介します。Typewriter フォームコンテンツからのテキストの消去、テキストフィールドの文字制限の設定と読み込み、カスタムフォント表示の適用、および名前によるフィールドの削除について説明します。これらのワークフローは、自動 PDF 処理パイプラインにおける一般的なフォーム管理タスクをサポートします。
---

## フォーム内のテキストをクリア

この例は、.NET 経由で Aspose.PDF for Python を使用して PDF のタイプライターフォームフィールドからテキストを消去する方法を示しています。PDF の最初のページをスキャンし、タイプライターフォームを識別し、その内容を削除して、更新された文書を保存します。この方法は、PDF を再配布する前にフォームフィールドをリセットまたはサニタイズする場合に便利です。

1. 入力 PDF ドキュメントをロードします。
1. 最初のページのフォームにアクセスします。
1. 各フォームを繰り返し処理し、それが次のものであるかどうかを確認します。 `Typewriter` フォーム。
1. TextFragmentAbSorber を使用すると、フォーム内のテキストフラグメントを検索できます。
1. 各フラグメントのテキストを消去します。
1. 変更した PDF を出力ファイルに保存します。

```python
import aspose.pdf as ap


def clear_text_in_form(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    forms = document.pages[1].resources.forms

    for form in forms:
        if form.it == "Typewriter" and form.subtype == "Form":
            absorber = ap.text.TextFragmentAbsorber()
            absorber.visit(form)

            for fragment in absorber.text_fragments:
                fragment.text = ""

    document.save(output_file_name)
```

## フィールド制限を設定

使用 `set_field_limit(field, limit)` から `FormEditor` テキストフィールドに入力できる最大文字数を定義します。

1. を作成 `FormEditor` 対象。
1. 入力 PDF をバインドします。
1. ターゲットフィールドのフィールド制限を設定します。
1. 更新した PDF を保存します。

```python
import aspose.pdf as ap


def set_field_limit(input_file_name, output_file_name):
    form = ap.facades.FormEditor()
    form.bind_pdf(input_file_name)
    form.set_field_limit("First Name", 15)
    form.save(output_file_name)
```

## フィールド制限を取得

テキストフィールドから文字制限を読み取ることもできます。

1. PDF ドキュメントをロードします。
1. ターゲットフォームフィールドにアクセスします。
1. フィールドが a であることを確認してください `TextBoxField`.
1. 読み取りと印刷 `max_len`.

```python
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable


def get_field_limit(input_file_name):
    document = ap.Document(input_file_name)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        text_box_field = cast(ap.forms.TextBoxField, document.form[1])
        print(f"Limit: {text_box_field.max_len}")
```

## フォームフィールドのカスタムフォントの設定

この例では、フォント、サイズ、色など、テキストボックスフィールドのカスタムデフォルト外観を設定します。

1. PDF ドキュメントをロードします。
1. ターゲットフィールドにアクセスして、そのタイプを確認します。
1. でフォントを検索する `FontRepository`.
1. 新しいものを適用 `DefaultAppearance`.
1. 更新した PDF を保存します。

```python
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable


def set_form_field_font(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        text_box_field = cast(ap.forms.TextBoxField, document.form[1])
        font = ap.text.FontRepository.find_font("Calibri")
        text_box_field.default_appearance = ap.annotations.DefaultAppearance(
            font, 10, ap.Color.black.to_rgb()
        )

    document.save(output_file_name)
```

## 既存のフォームのフィールドを削除する

このコードは、PDF ドキュメントから特定のフォームフィールドを (その名前で) 削除し、.NET 経由の Aspose.PDF for Python を使用して更新したファイルを保存します。

1. PDF ドキュメントをロードします。
1. フォームフィールドを名前で削除します。
1. 更新した PDF を保存します。

```python
import aspose.pdf as ap


def delete_form_field(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    document.form.delete("First Name")
    document.save(output_file_name)
```

## 関連トピック

- [アクロフォームを作成](/pdf/ja/python-net/create-form/)
- [アクロフォームに記入](/pdf/ja/python-net/fill-form/)
- [アクロフォームを抽出](/pdf/ja/python-net/extract-form/)
- [フォームデータのインポートとエクスポート](/pdf/ja/python-net/import-export-form-data/)

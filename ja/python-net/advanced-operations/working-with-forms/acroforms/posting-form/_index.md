---
title: Python を使用して PDF 形式でフォームを投稿する
linktitle: 投稿フォーム
type: docs
weight: 75
url: /ja/python-net/posting-form/
description: .NET 経由で Aspose.PDF for Python を使用して PDF AcroForms に送信ボタンと送信アクションを追加します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF に送信ボタンとフォーム送信アクションを追加する方法
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF フォームに送信機能を追加する 2 つの方法を紹介します。FormEditor を使用して既製の送信ボタンを追加することも、SubmitFormAction を使用してカスタムボタンフィールドを作成して高度な制御を行うこともできます。これらのパターンは、PDF フォームをサーバー側のフォーム処理エンドポイントと統合するのに役立ちます。
---

## フォームエディターで送信ボタンを追加

次のコードスニペットは、.NET 経由で Aspose.PDF for Python の FormEditor クラスを使用して PDF フォームに送信ボタンを追加する方法を示しています。このボタンは、クリックすると指定された URL にフォームデータを送信するように設定されています。

1. を作成 `FormEditor` 対象。
1. ターゲットページに送信ボタンを追加します。
1. 送信 URL とボタン座標を設定します。
1. 更新した PDF を保存します。

```python
import aspose.pdf as ap

def add_submit_button(input_file_name, output_file_name):
    editor = ap.facades.FormEditor(input_file_name, output_file_name)
    editor.add_submit_btn(
        "submitbutton", 1, "Submit", "http://localhost/testing/show", 100, 450, 150, 475
    )
    editor.save()
```

## カスタム送信アクションを追加

次のコードスニペットでは、.NET 経由で Aspose.PDF for Python を使用して PDF フォームにカスタム送信ボタンを作成する方法を説明しています。このボタンは、クリックすると指定された URL にフォームデータを送信するように設定されています。

1. AP.ドキュメント () を使用して PDF を開きます。
1. 送信アクションを作成します。
1. ターゲット URL と送信フラグを設定します。
1. ボタンフィールドを作成し、そのクリックアクションをバインドします。
1. ボタンをフォームに追加します。
1. 更新した PDF を保存します。

```python
import aspose.pdf as ap

def add_submit_action(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    submit_action = ap.annotations.SubmitFormAction()
    submit_action.url = ap.FileSpecification("http://localhost:3000/submit")
    submit_action.flags = (
        ap.annotations.SubmitFormAction.EXPORT_FORMAT
        | ap.annotations.SubmitFormAction.SUBMIT_COORDINATES
    )

    rect = ap.Rectangle(10, 10, 100, 40)
    submit_button = ap.forms.ButtonField(document.pages[1], rect)
    submit_button.partial_name = "SubmitButton"
    submit_button.value = "Submit"
    submit_button.actions.on_release_mouse_btn = submit_action

    document.form.add(submit_button, 1)
    document.save(output_file_name)
```

## 関連トピック

- [アクロフォームを作成](/pdf/ja/python-net/create-form/)
- [アクロフォームに記入](/pdf/ja/python-net/fill-form/)
- [アクロフォームの修正](/pdf/ja/python-net/modifying-form/)
- [フォームデータのインポートとエクスポート](/pdf/ja/python-net/import-export-form-data/)
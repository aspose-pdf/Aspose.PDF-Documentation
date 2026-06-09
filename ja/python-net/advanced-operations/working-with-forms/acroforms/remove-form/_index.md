---
title: Python で PDF からフォームを削除する方法
linktitle: フォームを削除
type: docs
weight: 70
url: /ja/python-net/remove-form/
description: .NET 経由で Aspose.PDF for Python を使用して PDF ページからフォームオブジェクトを削除します。これには、完全なクリーンアップや対象を絞った削除が含まれます。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: .NET 経由で Python 用 Aspose.PDF を使用して PDF からフォームを削除する
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメントからフォーム要素を削除する 2 つの方法を紹介します。1 つ目の方法は、選択したページからすべてのフォームオブジェクトを消去し、2 つ目の方法は、一致する Typewriter フォームリソースのみを削除します。これらの例は、フォームのクリーンアップ、テンプレートの準備、文書の正規化のワークフローに役立ちます。
---

## ページからすべてのフォームを削除する

このコードは、で指定されたページからすべてのフォームオブジェクトを削除します。 `page_num` 更新した文書を保存します。

1. PDF ドキュメントをロードします。
1. ページリソースにアクセスします。
1. フォームオブジェクトをクリアします。
1. 更新した文書を保存します。

```python
import aspose.pdf as ap

def remove_all_forms(input_file_name, page_num, output_file_name):
    document = ap.Document(input_file_name)
    forms = document.pages[page_num].resources.forms
    forms.clear()
    document.save(output_file_name)
```

## 特定のフォームタイプを削除する

次の例では、特定の PDF ページのフォームオブジェクトを繰り返し処理し、タイプライターフォームのアノテーションを識別して削除し、.NET 経由で Aspose.PDF for Python を使用して更新された PDF を保存します。

1. PDF ドキュメントをロードします。
1. ページフォームにアクセスします。
1. フォームを繰り返し処理します。
1. タイプライターフォームを確認してください。
1. 一致したフォームを削除します。
1. 更新した文書を保存します。

```python
import aspose.pdf as ap

def remove_specified_form(input_file_name, page_num, output_file_name):
    document = ap.Document(input_file_name)
    forms = document.pages[page_num].resources.forms
    for form in forms:
        if form.it == "Typewriter" and form.subtype == "Form":
            name = forms.get_form_name(form)
            forms.delete(name)
    document.save(output_file_name)
```

## 関連トピック

- [アクロフォームを作成](/pdf/ja/python-net/create-form/)
- [アクロフォームに記入](/pdf/ja/python-net/fill-form/)
- [アクロフォームの修正](/pdf/ja/python-net/modifying-form/)
- [投稿フォーム](/pdf/ja/python-net/posting-form/)

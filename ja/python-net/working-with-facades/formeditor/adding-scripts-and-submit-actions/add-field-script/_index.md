---
title: フィールドスクリプトを追加
type: docs
weight: 10
url: /ja/python-net/add-field-script/
description: インタラクティブ PDF フォームには、ユーザーがフォームフィールドを操作するときのアクションを自動化する JavaScript を含めることができます。Aspose.PDF for Python を使用すると、開発者はボタンやテキストフィールドなどのフォーム要素にスクリプトを簡単に添付できます。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF フォームフィールドに JavaScript アクションを追加する
Abstract: この記事では、PDF フォームを開く方法、特定のフォームフィールドに JavaScript コードを割り当てる方法、スクリプトアクションを追加する方法、更新した文書を保存する方法について説明します。この例では、Aspose.PDF Facades API の FormEditor クラスを使用して、フォームの動作をプログラムで操作しています。
---

## Python を使用して PDF フォームフィールドに JavaScript アクションを追加する

このコードスニペットを使用すると、Aspose.PDF for Python ライブラリを使用して既存の PDF フォームフィールドに JavaScript アクションを追加できます。PDF ドキュメントを開き、フォームフィールドに JavaScript アクションを割り当て、フィールドがトリガーされたときに実行されるスクリプトを追加します。最後に、更新された PDF は新しいファイルとして保存されます。
を使用する [フォームエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) からのクラス [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) モジュールでは、JavaScriptを既存のフォームフィールドにプログラムで添付できます。

1. 既存の PDF フォームを開きます。
1. 特定のフィールドに JavaScript アクションを設定します。
1. 同じフィールドに別の JavaScript アクションを追加します。
1. 変更した PDF ドキュメントを保存します。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_field_script(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Set JavaScript action for the field
    form_editor.set_field_script(
        "Script_Demo_Button", "app.alert('Script 1 has been executed');"
    )

    # Add JavaScript action to the field
    form_editor.add_field_script(
        "Script_Demo_Button", "app.alert('Script 2 has been executed');"
    )

    # Save output PDF file
    form_editor.save(output_file_name)
```

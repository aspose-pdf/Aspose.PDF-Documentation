---
title: フィールドスクリプトを設定
type: docs
weight: 30
url: /ja/python-net/set-field-script/
description: このコードスニペットは、Aspose.PDF for Python を使用して PDF ドキュメントのフォームフィールドに JavaScript アクションを割り当てる方法を示しています。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF フォームフィールドの JavaScript アクションを設定する
Abstract: この記事では、PDF ドキュメントを開く方法、フォームフィールドに JavaScript コードを割り当てる方法、FormEditor クラスを使用してスクリプトを更新する方法、および変更したファイルを保存する方法について説明します。この例は、既存のスクリプトをオーバーライドしてフォームフィールドの動作を変更する方法を示しています。
---

インタラクティブ PDF フォームでは、アラートの表示、入力の検証、動的フォーム動作のトリガーなどのタスクの実行に JavaScript を使用することがよくあります。Aspose.PDF for Python を使用すると、開発者はこれらのスクリプトをプログラムで管理できます。

この例では、最初に JavaScript アクションをフィールドに追加し、次に 'set_field_script' メソッドを使用して別のスクリプトに置き換えます。このアプローチにより、開発者はボタンや入力フィールドなどの PDF フォーム要素のインタラクティブな動作を制御または更新できます。

この例で使用されるフォームフィールドの名前は「Script_Demo_Button」で、これは通常、トリガーされたときに割り当てられたスクリプトを実行するボタンを表します。

を使用する [フォームエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) からのクラス [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) モジュールでは、開発者はフォームフィールドに関連するJavaScriptアクションをプログラムで管理できます。

1. 既存の PDF フォームドキュメントを開きます。
1. フォームフィールドに JavaScript アクションを追加します。
1. JavaScript アクションを新しいスクリプトで設定 (置換) します。
1. 変更した PDF ドキュメントを保存します。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_script(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Add JavaScript action to the field
    form_editor.add_field_script(
        "Script_Demo_Button", "app.alert('Script 1 has been executed');"
    )

    # Set JavaScript action for the field
    form_editor.set_field_script(
        "Script_Demo_Button", "app.alert('Script 2 has been executed');"
    )

    # Save output PDF file
    form_editor.save(output_file_name)
```

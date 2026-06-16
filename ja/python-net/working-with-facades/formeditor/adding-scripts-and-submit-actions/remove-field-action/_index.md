---
title: フィールドアクションを削除
type: docs
weight: 20
url: /ja/python-net/remove-field-action/
description: フォームフィールドから JavaScript を削除すると、インタラクティブ PDF フォームを変更したり、以前に割り当てられたアクションを無効にしたり、不要なスクリプトを含むドキュメントをクリーニングしたりする場合に便利です。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF フォームフィールドから JavaScript アクションを削除する
Abstract: Aspose.PDF for Python を使用すると、開発者はフォームフィールドに添付された JavaScript アクションをプログラムで削除できます。この記事では、既存の PDF フォームを開く方法、FormEditor クラスを使用して特定のフィールドに関連付けられているスクリプトを削除する方法、操作を確認する方法、変更した文書を保存する方法について説明します。
---

PDF フォームには、ユーザーがボタンや入力フィールドなどのフォーム要素を操作したときに実行される JavaScript アクションが含まれていることがよくあります。場合によっては、フォームの動作を簡略化したり、セキュリティを強化したり、フォームロジックを更新したりするために、これらのスクリプトを削除する必要があります。Aspose.PDF for Python を使用して PDF ドキュメントのフォームフィールドから JavaScript アクションを削除します。このコードは既存の PDF フォームを開き、特定のフィールドを見つけ、関連する JavaScript アクションを削除して、更新された文書を新しい PDF ファイルとして保存します。

を使用する [フォームエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) からのクラス [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/)既存の PDF フォームの特定のフィールドから JavaScript アクションを削除できます。

1. 既存の PDF フォームを開きます。
1. 「スクリプト_デモ_ボタン」という名前のフォームフィールドを探します。
1. そのフィールドに関連付けられている JavaScript アクションを削除します。
1. 削除が成功したかどうかを確認してください。
1. 更新した PDF ドキュメントを保存します。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_field_script(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Remove JavaScript action from the field
    if not form_editor.remove_field_action("Script_Demo_Button"):
        raise Exception("Failed to remove field script")

    # Save output PDF file
    form_editor.save(output_file_name)
```

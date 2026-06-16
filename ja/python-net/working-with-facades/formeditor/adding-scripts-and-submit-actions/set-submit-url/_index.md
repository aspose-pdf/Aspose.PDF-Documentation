---
title: 送信 URL を設定
type: docs
weight: 40
url: /ja/python-net/set-submit-url/
description: この例は、Aspose.PDF for Python を使用して PDF フォームのボタンフィールドの送信アクションを設定する方法を示しています。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF フォームボタンの送信 URL を設定する
Abstract: この記事では、既存の PDF フォームを開く方法、FormEditor クラスを使用してボタンフィールドの送信 URL を定義する方法、操作が成功したことを確認する方法、更新された PDF ドキュメントを保存する方法について説明します。
---

PDF フォームは、ユーザーが送信ボタンをクリックしたときにデータを Web サーバーに送信するように設計できます。Aspose.PDF for Python を使用すると、開発者はフォームフィールドの送信アクションをプログラムで設定できます。
送信 URL を設定すると、ボタンがクリックされたときに、フォームはユーザーが入力したデータをサーバーに送信できます。この機能は、PDF フォームが Web アプリケーション、データベース、または処理サービスに情報を送信する必要があるワークフローに役立ちます。

を使用する [フォームエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) からのクラス [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) モジュールでは、開発者が既存の PDF フォームのボタンフィールドにプログラムで送信 URL を割り当てることができます。

1. 既存の PDF フォームを開きます。
1. Script_Demo_Button という名前のボタンフィールドを探します。
1. フォームデータを送信する URL を割り当てます。
1. アクションが正常に適用されたことを確認します。
1. 更新した PDF ドキュメントを保存します。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_submit_url(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Set license
    set_license()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Set submit URL for the button
    if not form_editor.set_submit_url(
        "Script_Demo_Button", "http://www.example.com/submit"
    ):
        raise Exception("Failed to set submit URL")

    # Save output PDF file
    form_editor.save(output_file_name)
```

---
title: 送信フラグを設定
type: docs
weight: 50
url: /ja/python-net/set-submit-flag/
description: Aspose.PDF for Python を使用して PDF フォームボタンの送信フラグをプログラムで設定する方法を学びましょう。これにより、ユーザーがボタンをクリックすると、XFDF などの特定の形式のフォームデータを送信できます。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python 用 Aspose.PDF を使用して PDF フォームボタンの送信フラグを設定する
Abstract: PDF フォームは、フォームデータをさまざまな形式でサーバーまたはエンドポイントに送信するように設定できます。ボタンフィールドに送信フラグを設定することで、開発者はデータの送信方法を定義できます。このチュートリアルでは、FormEditor クラスを使用して PDF 文書内の既存の送信ボタンに送信フラグを設定し、更新されたファイルを保存する方法を示します。
---

PDF フォームには、多くの場合、ユーザー入力をサーバーに送信するための送信ボタンが含まれています。送信フラグは送信されるデータ形式（XFDF、FDF、HTML など）を決定します。

1. PDF ドキュメントをバインドします。
1. 既存の送信ボタンにアクセスします。
1. 目的の形式の送信フラグを設定します。
1. 更新した PDF ドキュメントを保存します。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_submit_flag(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Set submit flag for the form
    form_editor.set_submit_flag("Script_Demo_Button", ap.facades.SubmitFormFlag.XFDF)

    # Save output PDF file
    form_editor.save(output_file_name)
```

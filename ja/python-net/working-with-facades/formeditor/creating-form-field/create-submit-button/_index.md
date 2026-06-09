---
title: 「送信」ボタンを作成
type: docs
weight: 50
url: /ja/python-net/create-submit-button/
description: Aspose.PDF for Python を使用してプログラムで PDF ドキュメントに送信ボタンを追加する方法を学びましょう。このチュートリアルでは、指定した URL にフォームデータを送信し、更新された PDF を保存するボタンを作成する方法を示します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python 用 Aspose.PDF を使用して PDF に送信ボタンを作成する
Abstract: PDF フォームの送信ボタンを使用すると、ユーザーはフォームデータをサーバーまたはエンドポイントに直接送信できます。このガイドでは、Aspose.PDF for Python の FormEditor クラスを使用して PDF に送信ボタンフィールドを追加する方法を学習します。この例は、ボタンの名前、ラベル、ターゲット URL、および位置を設定し、更新された PDF ドキュメントを保存する方法を示しています。
---

インタラクティブ PDF フォームでは、多くの場合、アンケート結果、申請フォーム、フィードバックデータの送信など、処理のためにユーザーが入力を送信する必要があります。送信ボタンフィールドは、ボタンをウェブエンドポイントにリンクすることでこの機能を提供します。

ザの [フォームエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) クラスでは、ボタン、チェックボックス、ラジオボタン、テキストフィールド、およびその他のフォームコントロールを追加できます。

1. 既存の PDF ドキュメントをロードします。
1. 特定のページに送信ボタンフィールドを追加します。
1. ボタンラベルとターゲット送信 URL を設定します。
1. 更新した PDF を新しいボタンで保存します。

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_submit_button(infile, outfile):
    """Create Submit Button in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add Submit Button to PDF form
    pdf_form_editor.add_submit_btn(
        "submitbtn1",
        1,
        "Submit Button",
        "http://example.com/submit",
        100,
        450,
        200,
        470,
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```

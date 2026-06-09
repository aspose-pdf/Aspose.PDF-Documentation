---
title: ラジオボタンフィールドを作成
type: docs
weight: 40
url: /ja/python-net/create-radiobutton-field/
description: Aspose.PDF for Python を使用して、ラジオボタンフォームフィールドをプログラムで PDF ドキュメントに追加する方法を学習します。この例は、ラジオボタングループを作成し、選択可能なオプションを定義し、更新された PDF ファイルを保存する方法を示しています。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Python を使用して PDF にラジオボタンフィールドを作成する
Abstract: ラジオボタンは PDF フォームでよく使用され、あらかじめ定義されている選択肢のグループから 1 つのオプションを選択できます。このチュートリアルでは、Aspose.PDF for Python の FormEditor クラスを使用して PDF にラジオボタンフィールドを作成する方法を学習します。この例は、ラジオボタン項目を定義し、デフォルト選択を設定して、更新した文書を保存する方法を示しています。
---

インタラクティブ PDF フォームを使用すると、文書内で構造化された入力を直接入力できます。ラジオボタンフィールドは、国、性別、好みなど、複数の選択肢から 1 つのオプションだけを選択する必要がある場合に便利です。

ザの [フォームエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) クラスには、テキストボックス、チェックボックス、コンボボックス、リストボックス、ラジオボタンなど、さまざまなタイプのフィールドを作成するメソッドが用意されています。

1. 既存の PDF ドキュメントをロードします。
1. ラジオボタンオプションのリストを定義します。
1. 特定のページにラジオボタンフィールドを追加します。
1. デフォルトの選択値を設定します。
1. 変更した PDF ドキュメントを保存します。

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_radiobutton_field(infile, outfile):
    """Create RadioButton field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add RadioButton field to PDF form
    pdf_form_editor.items = ["Australia", "New Zealand", "Malaysia"]
    pdf_form_editor.add_field(
        pdf_facades.FieldType.RADIO, "radiobutton1", "Malaysia", 1, 240, 498, 256, 514
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```

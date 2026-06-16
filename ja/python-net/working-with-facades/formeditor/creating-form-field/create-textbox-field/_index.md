---
title: テキストボックスフィールドを作成
type: docs
weight: 60
url: /ja/python-net/create-textbox-field/
description: Aspose.PDF for Python を使用して、テキストボックスフィールドをプログラムで PDF ドキュメントに追加する方法を学習します。このチュートリアルでは、複数のテキストフィールドを挿入し、デフォルト値を設定し、更新された PDF ドキュメントを保存する方法を示します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Python を使用して PDF にテキストボックスフィールドを作成する
Abstract: PDF フォームの TextBox フィールドでは、ユーザーがテキストを入力および編集できるため、ドキュメントがインタラクティブで使いやすいものになります。このチュートリアルでは、Aspose.PDF for Python の FormEditor クラスを使用して PDF にテキストボックスフォームフィールドを作成する方法を学習します。この例は、複数のフィールドを追加し、デフォルト値を指定し、変更した PDF を保存する方法を示しています。
---

PDF フォームでは、多くの場合、名前、住所、コメントなど、ユーザーからのテキスト入力が必要です。テキストボックスフィールドは、編集可能なフィールドを PDF 文書内に直接提供することでこの機能を可能にします。

ザの [フォームエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) クラスを使用すると、テキストフィールド、チェックボックス、ラジオボタン、リストボックス、コンボボックス、およびボタンを追加できるため、インタラクティブなPDFを簡単に作成できます。

1. 既存の PDF ドキュメントをロードします。
1. ユーザー入力用に複数のテキストボックスフィールドを追加します。
1. 各フィールドにデフォルト値を設定します。
1. 更新した PDF ドキュメントを保存します。

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_textbox_field(infile, outfile):
    """Create TextBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add TextBox field to PDF form
    pdf_form_editor.add_field(
        pdf_facades.FieldType.TEXT, "first_name", "Alexander", 1, 50, 570, 150, 590
    )
    pdf_form_editor.add_field(
        pdf_facades.FieldType.TEXT, "last_name", "Smith", 1, 235, 570, 330, 590
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```

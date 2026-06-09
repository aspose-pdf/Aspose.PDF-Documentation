---
title: リストボックスフィールドを作成
type: docs
weight: 30
url: /ja/python-net/create-listbox-field/
description: Aspose.PDF for Python を使用して、リストボックスフォームフィールドをプログラムで PDF ドキュメントに追加する方法を学習します。このガイドでは、リストボックスフィールドを挿入し、選択可能な項目を定義し、更新された PDF ファイルを保存する方法を示します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Python を使用して PDF にリストボックスフィールドを作成する
Abstract: PDF フォームでは、オプションを選択したり、データを入力したり、情報をデジタルで送信したりして、文書を操作できます。リストボックスフィールドでは、表示されているオプションのリストから 1 つまたは複数の値を選択できます。このチュートリアルでは、Aspose.PDF for Python の FormEditor クラスを使用して PDF にリストボックスフィールドを作成し、定義済みの項目を入力する方法を学習します。
---

PDF フォームは通常、申請、調査、および登録書類に使用されます。リストボックスフィールドには複数のオプションが同時に表示されるため、ユーザーはリスト内の項目を簡単に確認して選択できます。

ザの [フォームエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) クラスは、ListBox 要素を含むさまざまなタイプのインタラクティブフィールドを追加するための機能を提供します。

1. 既存の PDF ドキュメントをロードします。
1. 選択可能なオプションのリストを定義します。
1. リストボックスフィールドを特定のページに追加します。
1. デフォルトの選択値を設定します。
1. 更新した PDF ドキュメントを保存します。

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_listbox_field(infile, outfile):
    """Create ListBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add ListBox field to PDF form
    pdf_form_editor.items = ["Australia", "New Zealand", "Malaysia"]
    pdf_form_editor.add_field(
        pdf_facades.FieldType.LIST_BOX, "listbox1", "Australia", 1, 230, 398, 350, 514
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```

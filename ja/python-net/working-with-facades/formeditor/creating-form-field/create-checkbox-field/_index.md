---
title: チェックボックスフィールドを作成
type: docs
weight: 10
url: /ja/python-net/create-checkbox-field/
description: Aspose.PDF for Python を使用して PDF 文書にチェックボックスフォームフィールドをプログラム的に追加する方法を学びます。このガイドでは、FormEditor クラスを使用してインタラクティブチェックボックスを既存の PDF ファイルに挿入し、更新した文書を保存する方法を示します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python 用 Aspose.PDF を使用して PDF にチェックボックスフィールドを作成する
Abstract: インタラクティブなフォームフィールドにより、ユーザーはPDF文書にデジタルで入力したり操作したりできます。このチュートリアルでは、Aspose.PDF Python API を使用して PDF にチェックボックスフィールドを追加する方法を学習します。この例は、既存の PDF ドキュメントをバインドし、指定した座標にチェックボックスフォームフィールドを作成し、変更したファイルを保存する方法を示しています。
---

PDF フォームは、申請書、アンケート、契約書などの文書でユーザー入力を収集するために広く使用されています。チェックボックスフィールドを使用すると、ユーザーはフォーム内のオプションを選択または選択解除できます。

Aspose.PDF for Python を使用すると、開発者はプログラムで PDF フォームを操作できます。は [フォームエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) クラスは、PDF ドキュメント内のフォームフィールドを追加、編集、および管理するためのメソッドを提供します。

1. 既存の PDF ファイルをロードします。
1. 'fieldType.check_box' パラメーターを指定して 'add_field () 'メソッドを呼び出して、チェックボックスを作成し、その位置を指定します。
1. フィールド名、キャプション、位置を定義します。
1. 更新した PDF ドキュメントを保存します。

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_checkbox_field(infile, outfile):
    """Create CheckBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add CheckBox field to PDF form
    pdf_form_editor.add_field(
        pdf_facades.FieldType.CHECK_BOX,
        "checkbox1",
        "Check Box 1",
        1,
        240,
        498,
        256,
        514,
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```

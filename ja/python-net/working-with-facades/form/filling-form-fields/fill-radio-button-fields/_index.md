---
title: ラジオボタンフィールドを埋める
type: docs
weight: 30
url: /ja/python-net/fill-radio-button-fields/
description: この例は、.NET 経由で Aspose.PDF for Python を使用して PDF フォームのラジオボタンフィールドをプログラム的に入力する方法を示しています。PDF ドキュメントをバインドし、インデックスを使用してラジオボタンオプションを選択し、更新したファイルを保存する方法を示します。
lastmod: "2026-06-09"
---

ラジオボタンを使用すると、定義済みのグループから、性別や設定フィールドなどのオプションを 1 つ選択できます。この例では、 [フォーム](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) からのファサード [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) モジュールを使用してソース PDF をバインドし、選択したオプションをインデックス値で割り当てます。目的のオプションを選択すると、変更された文書が保存されます。

1. PDF フォームフィールドを管理するには PDF_Facades.form () を初期化します。
1. 'bind_pdf () 'を呼び出して、ラジオボタンフィールドを含む PDF を添付します。
1. 'fill_field () 'を使用して最初のオプション (インデックス 0) を選択します。
1. 更新した PDF を保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Radio Button Fields
def fill_radio_button_fields(infile, outfile):
    """Fill radio button fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill radio button fields by name
    pdf_form.fill_field("gender", 0)  # Select male option (index 0)
    # pdf_form.fill_field("gender", 1) # Select female option (index 1)

    # Save updated PDF
    pdf_form.save(outfile)
```

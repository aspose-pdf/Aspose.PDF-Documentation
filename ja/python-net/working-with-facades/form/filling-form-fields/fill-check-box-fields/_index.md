---
title: チェックボックスフィールドを埋める
type: docs
weight: 20
url: /ja/python-net/fill-check-box-fields/
description: この例は、.NET 経由で Aspose.PDF for Python を使用して PDF フォームのチェックボックスフィールドをプログラム的に入力する方法を示しています。PDF ドキュメントをバインドし、チェックボックス値をフィールド名で更新し、変更したファイルを保存する方法を示します。
lastmod: "2026-06-09"
---

チェックボックスは、PDF フォームで購読や契約確認などの二者択一の選択肢を表すのに一般的に使用されます。この例では、 [フォーム](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) ファサードから [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) フォームフィールドにアクセスし、その値を選択状態に設定するために使用されます。チェックボックスを更新すると、入力された PDF は新しい文書として保存されます。

1. フォームフィールドのインタラクションを管理するには、'PDF_Facades.form () 'を初期化します。
1. 'bind_pdf () 'を使用して、チェックボックスフィールドを含むソース PDF を添付します。
1. 「fill_field ()」を呼び出して、「購読ニュースレター」や「承諾条件」などのフィールドを選択済みとしてマークします。
1. 更新したドキュメントを保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Check Box Fields
def fill_check_box_fields(infile, outfile):
    """Fill check box fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill check box fields by name
    pdf_form.fill_field("subscribe_newsletter", "Yes")
    pdf_form.fill_field("accept_terms", "Yes")

    # Save updated PDF
    pdf_form.save(outfile)
```

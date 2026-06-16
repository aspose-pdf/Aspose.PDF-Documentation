---
title: テキストフィールドを埋める
type: docs
weight: 10
url: /ja/python-net/fill-text-fields/
description: この例は、.NET 経由で Aspose.PDF for Python を使用して PDF フォームのテキストフィールドを自動的に入力する方法を示しています。PDF ドキュメントを読み込み、特定のフォームフィールドに名前を入力して更新したファイルを保存する方法を示します。
lastmod: "2026-06-09"
---

テキストフィールドをプログラムで入力すると、アプリケーションで PDF テンプレートを再利用し、手動で編集しなくても動的コンテンツを挿入できます。この例では、 [フォーム](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) ファサードから [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) PDF フォームをバインドし、名前、住所、電子メールなどの複数のフィールドを更新するために使用されます。値を割り当てると、変更された PDF は新しい文書として保存されます。

1. フォームフィールドの操作を管理するには、'PDF_Facades.Form () 'を初期化します。
1. 'bind_pdf () 'を使用して、テキストフィールドを含む入力 PDF を添付します。
1. 'fill_field () 'を呼び出して、名前、住所、電子メールなどのフィールドにデータを挿入します。
1. 更新した PDF を保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Text Fields
def fill_text_fields(infile, outfile):
    """Fill text fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill text fields by name
    pdf_form.fill_field("name", "John Doe")
    pdf_form.fill_field("address", "123 Main St, Anytown, USA")
    pdf_form.fill_field("email", "john.doe@example.com")

    # Save updated PDF
    pdf_form.save(outfile)
```

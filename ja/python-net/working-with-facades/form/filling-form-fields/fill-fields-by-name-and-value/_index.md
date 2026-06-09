---
title: フィールドを名前と値で入力
type: docs
weight: 60
url: /ja/python-net/fill-fields-by-name-and-value/
description: この記事では、.NET 経由で Aspose.PDF for Python を使用して、複数の PDF フォームフィールドを名前と値で動的に入力する方法を示します。各フィールドを個別に設定する代わりに、ディクショナリ構造を使用してフィールド名を値にマッピングし、ループでデータを入力します。
lastmod: "2026-06-09"
---

名前と値のコレクションを使用してフォームフィールドに入力することで、開発者は PDF フォーム自動化のためのスケーラブルで柔軟なソリューションを作成できます。この例では、 [フォーム](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) ファサードから [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) PDF ドキュメントをバインドし、フィールドデータのディクショナリを反復処理するために使用されます。各エントリは「fill_field メソッド」を使用して適用されるため、フォームフィールドを効率的に一括更新できます。

1. インタラクティブフォームフィールドを操作するには、'PDF_Facades.Form () 'を初期化します。
1. 'bind_pdf () 'を使用してソース PDF ドキュメントを添付してください。
1. フィールド名と挿入する値を含むディクショナリを作成します。
1. 辞書を繰り返し処理し、エントリごとに「fill_field ()」を呼び出します。
1. 更新したドキュメントを保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Fields by Name and Value
def fill_fields_by_name_and_value(infile, outfile):
    """Fill PDF form fields by name and value."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill fields by name and value
    fields = {
        "name": "Jane Smith",
        "address": "456 Elm St, Othertown, USA",
        "email": "jane.smith@example.com",
    }
    for field_name, value in fields.items():
        pdf_form.fill_field(field_name, value)

    # Save updated PDF using outfile
    pdf_form.save(outfile)
```

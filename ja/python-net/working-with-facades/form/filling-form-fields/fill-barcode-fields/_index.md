---
title: バーコードフィールドを記入
type: docs
weight: 50
url: /ja/python-net/fill-barcode-fields/
description: この例は、.NET 経由で Aspose.PDF for Python を使用して PDF フォームのバーコードフィールドをプログラム的に入力する方法を示しています。PDF ドキュメントをバインドし、バーコードフィールドに値を割り当て、更新したファイルを保存する方法を示します。
lastmod: "2026-06-09"
---

PDF フォームのバーコードフィールドでは、エンコードされた情報をバーコードとして保存し、視覚的に表示できます。この例では、 [フォーム](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) からのファサード [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) モジュールは、フォームフィールドにアクセスし、バーコード値を割り当てるために使用されます。データが入力されると、PDF は更新されたバーコードコンテンツとともに保存されます。

1. PDF フォームのインタラクションを管理するには 'PDF_Facades.Form () 'を初期化します。
1. 'bind_pdf () 'を呼び出して、バーコードフィールドを含む PDF を添付します。
1. バーコード値を割り当てるには 'fill_field () 'を使用してください。
1. 更新したドキュメントを保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Barcode Fields
def fill_barcode_fields(infile, outfile):
    """Fill barcode fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill barcode fields by name
    pdf_form.fill_field("product_barcode", "123456789012")

    # Save updated PDF
    pdf_form.save(outfile)
```

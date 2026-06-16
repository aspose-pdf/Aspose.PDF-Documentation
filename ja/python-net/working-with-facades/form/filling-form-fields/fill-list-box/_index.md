---
title: リストボックスを埋める
type: docs
weight: 40
url: /ja/python-net/fill-list-box/
description: この例は、.NET 経由で Aspose.PDF for Python を使用して PDF フォームのリストボックスと複数選択フィールドにプログラムで入力する方法を示しています。PDF ドキュメントを連結し、リストベースのフォームフィールド内の値を選択し、更新したファイルを保存する方法を示します。
lastmod: "2026-06-09"
---

リストボックスと複数選択フィールドでは、定義済みのオプションセットから 1 つまたは複数の値を選択できます。この例では、 [フォーム](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) ファサードから [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) PDF フォームにアクセスし、選択した値を favorite_colors フィールドに割り当てるために使用されます。目的のオプションを選択すると、更新された文書が保存されます。

1. フォームフィールドを管理および更新するには、'PDF_Facades.Form () 'を初期化します。
1. 'bind_pdf () 'を呼び出して、リストボックスまたは複数選択フィールドを含むソース PDF を添付します。
1. 'fill_field () 'を使用して、使用可能なオプションから値を選択します。
1. 更新したドキュメントを保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill List Box / Multi-Select Fields
def fill_list_box_fields(infile, outfile):
    """Fill list box and multi-select fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill list box / multi-select fields by name
    pdf_form.fill_field("favorite_colors", "Red")

    # Save updated PDF
    pdf_form.save(outfile)
```

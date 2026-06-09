---
title: フルフィールド名を解決
type: docs
weight: 60
url: /ja/python-net/resolve-full-field-names/
description: この例は、Aspose.PDF Facades API を使用して PDF ドキュメント内のフォームフィールドの完全修飾名を取得する方法を示しています。
lastmod: "2026-06-09"
---

PDF フォームでは、特にサブフォームを使用する場合に、フィールドを階層的に整理できます。各フィールドにはショートネームと完全修飾名が付いています。完全修飾名はフォーム階層内のフィールドの完全パスを表すもので、フォームデータを操作したり読み込んだりする多くの API メソッドで必要になります。

1. フォームオブジェクトを作成します。
1. PDF ドキュメントをバインドします。
1. すべてのフォームフィールド名にアクセスします。
1. 各フィールドの完全修飾名は get_full_field_name () を使用して解決されます。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Resolve full field names
def resolve_full_field_names(infile):
    """Resolve full field names in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Resolve full field names
    for field in pdf_form.field_names:
        name = pdf_form.get_full_field_name(field)
        print(f"Full field name: {name}")
```

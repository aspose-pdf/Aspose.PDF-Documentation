---
title: フィールド値の取得
type: docs
weight: 50
url: /ja/python-net/get-field-values/
description: フォームクラスを使用して Aspose.PDF ファサードを使用して PDF フォームからフィールド値を取得します。
lastmod: "2026-06-09"
---

このコードスニペットは、Aspose.PDF Facades API を使用して PDF ドキュメントからフォームフィールドの現在の値を取得する方法を示しています。は [get_field ()](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/#methods) メソッドを使用すると、テキストフィールド、チェックボックス、ラジオボタン、その他の AcroForm 要素に入力されたデータにプログラムでアクセスできます。

1. PDF を Form オブジェクトにバインドします。
1. 読みたいフィールド名を指定します。
1. get_field () を使用して各フィールドの値を取得します。

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir


    # Get field values
    def get_field_values(infile):
        """Get field values from a PDF document."""
        # Create Form object
        pdf_form = pdf_facades.Form()

        # Bind PDF document
        pdf_form.bind_pdf(infile)

        # Get field values by their names
        field_names = ["First Name", "Last Name"]
        for field_name in field_names:
            value = pdf_form.get_field(field_name)
            print(f"Value of '{field_name}': {value}")
```
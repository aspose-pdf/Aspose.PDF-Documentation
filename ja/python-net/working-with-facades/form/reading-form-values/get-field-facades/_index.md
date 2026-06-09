---
title: フィールドファサードを取得
type: docs
weight: 10
url: /ja/python-net/get-field-facades/
description: この例は、Aspose.PDF Facades API を使用して PDF ドキュメントから特定のフォームフィールドの値を読み取る方法を示しています。
lastmod: "2026-06-09"
---

PDF フォームには、テキストボックス、チェックボックス、ラジオボタンなど、ユーザーがデータを入力できるフィールドが含まれています。これらのフォームをプログラム的に処理するには、多くの場合、これらのフィールドの現在の値を取得する必要があります。

1. Form オブジェクトを作成します。
1. PDF ドキュメントをフォームオブジェクトにバインドします。
1. フィールド値を取得します。

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
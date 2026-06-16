---
title: 必須フィールド名を取得
type: docs
weight: 30
url: /ja/python-net/get-required-field-names/
description: この例は、Aspose.PDF Facades API を使用して PDF ドキュメント内の必須フォームフィールドの名前を識別して取得する方法を示しています。
lastmod: "2026-06-09"
---

PDF フォームには、送信前にユーザーが入力する必要がある必須フィールドが含まれている場合があります。これらのフィールドは通常、フォームのプロパティで必須とマークされています。

1. フォームオブジェクトを作成します。
1. PDF ドキュメントをバインドします。
1. 「pdf_form.field_names」を使用してすべてのフィールド名にアクセスします。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Get required field names
def get_required_field_names(infile):
    """Get required field names from a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Get required field names
    for field in pdf_form.field_names:
        if pdf_form.is_required_field(field):
            print(f"Required field: {field}")
```

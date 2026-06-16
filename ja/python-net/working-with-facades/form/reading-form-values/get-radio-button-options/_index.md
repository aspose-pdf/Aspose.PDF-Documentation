---
title: ラジオボタンオプションを取得
type: docs
weight: 20
url: /ja/python-net/get-radio-button-options/
description: この記事では、Aspose.PDF Facades API を使用して PDF ドキュメント内のラジオボタンフィールドの現在選択されている値を取得する方法を示します。
lastmod: "2026-06-09"
---

PDF フォームのラジオボタンフィールドはグループ化されたコントロールで、一度に 1 つのオプションしか選択できません。各グループにはフィールド名があり、各オプションには対応する値があります。

1. フォームオブジェクトを作成します。
1. PDF ドキュメントをバインドします。
1. 選択したラジオボタンオプションを取得します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Get radio button options
def get_radio_button_options(infile):
    """Get radio button options from a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Get radio button options by their names
    field_names = ["WorkType"]
    for field_name in field_names:
        options = pdf_form.get_button_option_current_value(field_name)
        print(f"Options for '{field_name}': {options}")
```

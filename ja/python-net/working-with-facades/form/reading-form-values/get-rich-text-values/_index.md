---
title: リッチテキスト値の取得
type: docs
weight: 40
url: /ja/python-net/get-rich-text-values/
description: このセクションでは、Aspose.PDF Facades API を使用して PDF ドキュメント内のフォームフィールドのリッチテキストコンテンツを取得する方法について説明します。プレーンテキストフィールドとは異なり、リッチテキストフィールドには太字、さまざまなフォント、色、段落スタイルなどのフォーマットされたコンテンツを含めることができます。
lastmod: "2026-06-09"
---

PDF フォームには、リッチテキストフォーマットをサポートするテキストフィールドが含まれる場合があります。これらのフィールドには、プレーンテキスト値に加えてスタイル属性を含むコンテンツを保存できます。

1. フォームオブジェクトを作成します。
1. PDF ドキュメントをバインドします。
1. リッチテキスト値を取得します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Get rich text values
def get_rich_text_values(infile):
    """Get rich text values from a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Get rich text values by their names
    field_names = ["Summary"]
    for field_name in field_names:
        rich_text_value = pdf_form.get_rich_text(field_name)
        print(f"Rich text value of '{field_name}': {rich_text_value}")
```

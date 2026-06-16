---
title: フィールド制限を設定
type: docs
weight: 80
url: /ja/python-net/set-field-limit/
description: この例は、Aspose.PDF for Python を使用して PDF ドキュメントのフォームフィールドに最大文字数制限を設定する方法を示しています。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF フォームフィールドの最大文字数制限を設定する
Abstract: この例は、「Last Name」という名前のフィールドの文字制限を 10 文字に設定し、ユーザーが指定された制限を超えて入力できないようにする方法を示しています。
---

PDF ドキュメントのフォームフィールドでは、適切なフォーマットを維持するために入力制限が必要な場合があります。Aspose.PDF for Python を使用すると、開発者はプログラムでフィールドの最大文字数を設定できます。

ザの [フォームエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) クラスには、フィールドの最大入力長を定義する 'set_field_limit' メソッドが用意されています。

1. 既存の PDF フォームを開きます。
1. フォームエディターオブジェクトを作成します。
1. 「姓」フィールドの最大文字数制限を設定します。
1. 更新した PDF を保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_limit(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field limit to 10
    if not form_editor.set_field_limit("Last Name", 10):
        raise Exception(
            "Failed to set field limit. Field may not support specified limit."
        )

    # Save updated document
    form_editor.save(outfile)
```

---
title: リスト項目を追加
type: docs
weight: 10
url: /ja/python-net/add-list-item/
description: この例は、Aspose.PDF for Python を使用して PDF ドキュメントのリストボックスフォームフィールドに項目を追加する方法を示しています。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF リストボックスフィールドへの項目の追加
Abstract: この記事では、PDF ドキュメントを開き、「Country」という名前のリストボックスフィールドに項目を追加し、更新したドキュメントを保存する方法を説明します。
---

PDF のリストボックスフィールドでは、定義済みのセットから 1 つまたは複数のオプションを選択できます。Aspose.PDF for Python を使用すると、開発者はこれらのフィールドに新しい項目をプログラムで追加できます。は [フォームエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) クラスには、既存のリストボックスフィールドに項目を追加するための 'add_list_item' メソッドが用意されています。

1. 既存の PDF フォームを開きます。
1. フォームエディターオブジェクトを作成します。
1. PDF をフォームエディターにバインドします。
1. リストボックスフィールド「Country」に項目を追加します。
1. 更新した文書を保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_list_item(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Add list item to list box field
    form_editor.add_list_item("Country", ["New Zealand", "New Zealand"])
    # Save updated document
    form_editor.save(outfile)
```

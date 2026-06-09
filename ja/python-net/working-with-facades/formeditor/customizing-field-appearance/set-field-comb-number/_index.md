---
title: フィールドコーム番号を設定
type: docs
weight: 70
url: /ja/python-net/set-field-comb-number/
description: この例は、Aspose.PDF for Python を使用して PDF フォームフィールドにコーム番号を設定する方法を示しています。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF フォームフィールドのコーム番号を設定する
Abstract: Aspose.PDF for Python を使用すると、開発者はプログラムでフォームフィールドのボックス数 (くし数) を設定して、固定長の入力を強制できます。この記事では、「PIN」という名前のフィールドにコーム番号を設定する方法を紹介します。
---

くし番号は、フィールドの内容を等間隔のボックスに分割する方法を定義します。このボックスは、PIN コード、シリアル番号、またはその他の固定長の入力フィールドによく使用されます。このコードは既存の PDF を開き、フィールドにコーム番号を設定し、変更された文書を保存します。

ザの [フォームエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) クラスには、フォームフィールド内のボックス (文字) の数を定義する 'set_field_comb_number' メソッドが用意されています。

1. 既存の PDF フォームを開きます。
1. フォームエディターオブジェクトを作成します。
1. 「PIN」という名前のフィールドのコーム番号を 5 に設定します。
1. 更新した文書を保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_comb_number(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field comb number to 5
    form_editor.set_field_comb_number("PIN", 5)

    # Save updated document
    form_editor.save(outfile)
```

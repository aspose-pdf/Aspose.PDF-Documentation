---
title: リスト項目を削除
type: docs
weight: 40
url: /ja/python-net/del-list-item/
description:
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF リストボックスフィールドから項目を削除する
Abstract: この例は、Aspose.PDF for Python を使用して PDF ドキュメントのリストボックスフォームフィールドから項目を削除する方法を示しています。このコードは既存の PDF を開き、リストボックスフィールドから特定の項目を削除して、更新された文書を保存します。
---

PDF のリストボックスフィールドでは、ユーザーは 1 つまたは複数の定義済みオプションを選択できます。Aspose.PDF for Python を使用すると、開発者はこれらのフィールドから項目をプログラムで削除できます。

この記事では、「Country」という名前のリストボックスフィールドから「UK」項目を削除し、フィールドに必要なオプションのみが含まれるようにする方法について説明します。

ザの [フォームエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) クラスには、リストボックスフィールドから特定の項目を削除するための 'del_list_item' メソッドが用意されています。

1. 既存の PDF フォームを開きます。
1. フォームエディターオブジェクトを作成します。
1. PDF ドキュメントをフォームエディターにバインドします。
1. 「国」リストボックスフィールドから「英国」項目を削除します。
1. 更新した文書を保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def del_list_item(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Delete list item from list box field
    form_editor.del_list_item("Country", "UK")
    # Save updated document
    form_editor.save(outfile)
```


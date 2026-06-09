---
title: [フィールドを削除]
type: docs
weight: 60
url: /ja/python-net/remove-field/
description: この例は、「FormEditor」クラスの「remove_field」メソッドを使用して PDF フォームから「国」フィールドを削除する方法を示しています。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF ドキュメントからフォームフィールドを削除する
Abstract: この例は、Aspose.PDF for Python を使用して PDF ドキュメントから既存のフォームフィールドを削除する方法を示しています。このコードは PDF ファイルを読み込み、FormEditor クラスを使用して指定されたフィールドを削除し、更新された文書を保存します。
---

PDF フォームには、デザインの変更やワークフローの更新により不要になったフィールドが含まれている場合があります。Aspose.PDF for Python を使用すると、開発者は特定のフォームフィールドをプログラムで簡単に削除できます。

ザの [フォームエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) Aspose.PDF のクラスには、開発者がフォームフィールドをその名前で削除できる 'remove_field' メソッドが用意されています。

1. PDF ドキュメントをロードします。
1. フォームエディターオブジェクトを作成します。
1. PDF をフォームエディターにバインドします。
1. 指定されたフォームフィールドを削除します。
1. 更新した文書を保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Remove field from document
    form_editor.remove_field("Country")
    # Save updated document
    form_editor.save(outfile)
```

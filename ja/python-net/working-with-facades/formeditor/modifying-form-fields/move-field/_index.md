---
title: フィールドを移動
type: docs
weight: 50
url: /ja/python-net/move-field/
description: 既存のフォームフィールドを PDF ドキュメント内の別の位置に移動します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF フォームフィールドを新しい位置に移動する
Abstract: この例は、Aspose.PDF for Python を使用して、既存のフォームフィールドを PDF ドキュメント内の別の位置に移動する方法を示しています。このコードは既存の PDF を開き、指定されたフォームフィールドを新しい座標に再配置して、更新された文書を保存します。
---

PDF フォームは、多くの場合、作成後にレイアウトを調整する必要があります。Aspose.PDF for Python を使用すると、開発者は既存のフォームフィールドを再作成せずに新しい位置に移動できます。

この例は、ページ内の新しい座標を指定して「Country」フィールドの位置を変更する方法を示しています。は [フォームエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) クラスには、PDF ページ内のフィールドを再配置するための move_field メソッドが用意されています。

1. 既存の PDF フォームを開きます。
1. フォームエディターオブジェクトを作成します。
1. PDF ドキュメントをフォームエディターにバインドします。
1. 座標を使用して「国」フィールドを新しい位置に移動します。
1. 変更した文書を保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def move_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Move field to new page
    form_editor.move_field("Country", 200, 600, 280, 620)
    # Save updated document
    form_editor.save(outfile)
```

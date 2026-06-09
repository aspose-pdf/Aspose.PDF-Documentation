---
title: 単一行フィールドから複数行フィールドへ
type: docs
weight: 80
url: /ja/python-net/single-to-multiple/
description: Aspose.PDF for Python を使用して、1 行のテキストフィールドを PDF ドキュメント内の複数行のフィールドに変換します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF 内の 1 行のテキストフィールドを複数行のフィールドに変換
Abstract: この例は、Aspose.PDF for Python を使用して PDF ドキュメントの 1 行のテキストフィールドを複数行のフィールドに変換する方法を示しています。このコードは既存の PDF フォームを読み込み、複数行のテキストを入力できるように指定されたフィールドを変更し、更新された文書を保存します。
---

PDF フォームには、1 行入力用に設計されたテキストフィールドが含まれることがありますが、これは特定の種類のデータには不十分な場合があります。Aspose.PDF for Python を使用すると、開発者はこのようなフィールドを再作成せずに複数行のテキストフィールドに簡単に変換できます。

を使用する [フォームエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) クラスでは、開発者は位置やその他のプロパティに影響を与えずに既存のテキストフィールドを変更できます。

1. 既存の PDF ドキュメントをロードします。
1. フォームエディターのインスタンスを作成します。
1. PDF ドキュメントをエディターにバインドします。
1. 選択したフィールドをマルチラインに変換します。
1. 更新した文書を保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def single2multiple(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Change a single-lined text field to a multiple-lined one
    form_editor.single_2_multiple("City")
    # Save updated document
    form_editor.save(outfile)
```


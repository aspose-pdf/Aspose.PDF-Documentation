---
title: フィールド名を変更
type: docs
weight: 70
url: /ja/python-net/rename-field/
description: Aspose.PDF for Python を使用して PDF ドキュメント内の既存のフォームフィールドの名前を変更します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF フォームフィールドの名前を変更する方法
Abstract: この例は、Aspose.PDF for Python を使用して PDF ドキュメント内の既存のフォームフィールドの名前を変更する方法を示しています。このコードは入力 PDF を開き、FormEditor クラスを使用して指定されたフォームフィールドの名前を変更し、更新された文書を保存します。
---

PDF フォームでは、スクリプト作成、自動化、データ処理においてフィールド名を使用することがよくあります。Aspose.PDF for Python を使用すると、開発者は既存のフィールドを再作成したりフォームレイアウトを変更したりせずに名前を変更できます。

ザの [フォームエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) クラスには 'rename_field' メソッドが用意されています。これにより、開発者は、位置、値、外観を維持したまま、既存のフィールドの名前を変更できます。

1. 既存の PDF フォームをロードします。
1. フォームエディターのインスタンスを作成します。
1. PDF ドキュメントをエディターにバインドします。
1. ターゲットフィールドの名前を変更します。
1. 更新した PDF を保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def rename_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Rename field in document
    form_editor.rename_field("City", "Town")
    # Save updated document
    form_editor.save(outfile)
```


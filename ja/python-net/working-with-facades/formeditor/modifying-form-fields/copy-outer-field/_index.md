---
title: 外部フィールドをコピー
type: docs
weight: 30
url: /ja/python-net/copy-outer-field/
description: この例は、Aspose.PDF for Python を使用して、ある PDF ドキュメントから別の PDF ドキュメントにフォームフィールドをコピーする方法を示しています。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して別の文書から PDF フォームフィールドをコピーする
Abstract: この記事では、新しい PDF ドキュメントを作成し、ソース PDF の「First Name」フィールドを 1 ページの座標（200、600）にコピーし、更新したターゲットドキュメントを保存する方法について説明します。
---

PDF フォームでは、ある文書のフィールドを別の文書で再利用する必要がある場合があります。Aspose.PDF for Python を使用すると、開発者はプログラムによってフォームフィールドをソース PDF からターゲット PDF にコピーできます。

ザの [フォームエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) クラスには、ソースドキュメントからターゲットドキュメントの指定されたページと座標でフィールドをコピーする 'copy_outer_field' メソッドが用意されています。

このコードは、新しい PDF (ターゲット) を作成し、ページを追加し、既存の PDF (ソース) からターゲットドキュメントに指定された座標でフィールドをコピーします。

1. 新しいターゲット PDF ドキュメントを作成します。
1. ターゲット PDF に少なくとも 1 ページを追加します。
1. 空のターゲットドキュメントを保存します。
1. FormEditor オブジェクトを作成し、ターゲット PDF にバインドします。
1. ソース PDF の「名前」フィールドを 1 ページ目の (200, 600) にコピーします。
1. 更新したターゲット PDF を保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def copy_outer_field(infile, outfile):
    # Since copy_outer_field() method needs to copy field from source document to target document, we need to create a new document as target document first.
    doc = ap.Document()
    doc.pages.add()
    doc.save(outfile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(outfile)
    # Copies an existing field to a new position specified by both page number and ordinates.
    # A new document will be produced, which contains everything the source document has except for the newly copied field.
    form_editor.copy_outer_field(infile, "First Name", 1, 200, 600)
    # Save updated document
    form_editor.save(outfile)
```

**ご注意:**

「copy_outer_field」メソッドのシグネチャは以下のようになります。

```python
copy_outer_field(original_field_name, new_field_name, page_number, x, y)
```

- '元のフィールド名' — 複製したいフィールド。
- 'new_field_name' — 新しいフィールドの名前。
- 'page_number' — 新しいフィールドが表示されるページ。
- x, y — そのページの座標。

page_number は PDF 内の既存のページに対応する正の整数である必要があります (1 から始まるインデックス)。

負のパラメータを渡した場合、例:

```python
form_editor.copy_outer_field("First Name", "First Name Copy", 1, -200, 600)
```

その後、プログラムは以前のパラメータにリセットされます。

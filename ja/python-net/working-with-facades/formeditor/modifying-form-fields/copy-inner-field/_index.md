---
title: 内部フィールドをコピー
type: docs
weight: 20
url: /ja/python-net/copy-inner-field/
description: Aspose.PDF for Python を使用して、Python を使用して PDF フォームフィールドを新しい位置にコピーします。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF フォームフィールドを新しい位置にコピー
Abstract: この例は、Aspose.PDF for Python を使用して、既存のフォームフィールドを PDF ドキュメントの新しい位置にコピーする方法を示しています。このコードは PDF を開き、フィールドを指定されたページに複製して座標を調整し、更新された文書を保存します。
---

PDF フォームでは、元の書式や動作を維持したまま、フィールドを複製しなければならないことがよくあります。Aspose.PDF for Python を使用すると、開発者は既存のフィールドを同じページまたは別のページの新しい位置にプログラムでコピーできます。

この記事では、「First Name」という名前のフィールドを、2 ページ目の特定の座標 (x=200、y=600) にある「First Name Copy」という新しいフィールドにコピーし、新しく配置されたフィールドを含む PDF を作成する方法について説明します。

1. 既存の PDF フォームを開きます。
1. フォームエディターオブジェクトを作成します。
1. PDF ドキュメントをフォームエディターにバインドします。
1. 「ファーストネーム」フィールドを、座標 (200, 600) の 2 ページ目の新しいフィールド「ファーストネームコピー」にコピーします。
1. 更新した文書を保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def copy_inner_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Copies an existing field to a new position specified by both page number and ordinates.
    # A new document will be produced, which contains everything the source document has except for the newly copied field.
    form_editor.copy_inner_field("First Name", "First Name Copy", 2, 200, 600)
    # Save updated document
    form_editor.save(outfile)
```

**ご注意:**

'copy_inner_field' メソッドのシグネチャは以下のようになります。

```python
copy_inner_field(original_field_name, new_field_name, page_number, x, y)
```

- '元のフィールド名' — 複製したいフィールド。
- 'new_field_name' — 新しいフィールドの名前。
- 'page_number' — 新しいフィールドが表示されるページ。
- x, y — そのページの座標。

page_number は PDF 内の既存のページに対応する正の整数である必要があります (1 から始まるインデックス)。

負のパラメータを渡した場合、例:

```python
form_editor.copy_inner_field("First Name", "First Name Copy", -1, 200, 600)
```

その後、プログラムは以前のパラメータにリセットされます。

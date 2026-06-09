---
title: フィールド配置を垂直に設定
type: docs
weight: 40
url: /ja/python-net/set-field-alignment-vertical/
description: この例は、Aspose.PDF for Python を使用して PDF ドキュメント内のフォームフィールドの垂直方向の配置を設定する方法を示しています。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF フォームフィールドの垂直方向の配置を設定する
Abstract: この記事では、PDF を開く方法、FormEditor クラスを使用してフィールドの垂直方向の配置を設定する方法、および更新された PDF を保存する方法について説明します。この例では、「First Name」という名前のフィールドの垂直方向の配置をフィールド領域の下部に設定します。
---

PDF フォームフィールドには、一貫性のあるプロフェッショナルな外観にするために適切な垂直方向の配置が必要なテキストが含まれている場合があります。Aspose.PDF for Python を使用すると、開発者はフォームフィールドの垂直方向の配置をプログラムで変更できます。
垂直方向の配置により、開発者はフィールドのテキストをフィールドのバウンディングボックスの上部、中央、または下部のいずれに表示するかを制御できるため、フォームデータのレイアウトと読みやすさが向上します。

を使用する [フォームエディター](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) クラスと [フォームフィールドファサード](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formfieldfacade/) 定数を使用する場合、開発者は垂直方向の配置をプログラムで調整して、一貫したフォームレイアウトを実現できます。

1. 既存の PDF ドキュメントを開きます。
1. フォームエディターオブジェクトを作成します。
1. 「First Name」という名前のフィールドの垂直方向の配置を下に設定します。
1. 変更した文書を保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_alignment_vertical(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Attempt to set vertical alignment of the "First Name" field to bottom
    if form_editor.set_field_alignment_v(
        "First Name", pdf_facades.FormFieldFacade.ALIGN_BOTTOM
    ):
        # Save updated document
        form_editor.save(outfile)
    else:
        raise Exception(
            "Failed to set field vertical alignment. Field may not support vertical alignment."
        )
```

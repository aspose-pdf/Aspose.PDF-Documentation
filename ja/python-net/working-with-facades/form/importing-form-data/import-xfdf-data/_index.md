---
title: XFDF データのインポート
type: docs
weight: 20
url: /ja/python-net/import-xfdf-data/
description: この例は、.NET 経由で Aspose.PDF for Python を使用して、XFDF ファイルから PDF フォームにフォームデータをインポートする方法を示しています。PDF ドキュメントをバインドする方法、ファイルストリームから XML ベースの XFDF データを読み取る方法、および一致するフォームフィールドに自動的に入力する方法を示します。XFDF データをインポートすると、フォームデータの効率的な交換が可能になり、構造化された XML 形式に依存する自動文書ワークフローがサポートされます。
lastmod: "2026-06-09"
---

XFDF (XML フォームデータフォーマット) は、相互運用性とデータ交換を目的として設計された PDF フォームデータの XML 表現です。この例では、 [フォーム](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) からのファサード [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) モジュールは PDF フォームをバインドし、外部の XFDF ファイルからフィールド値をインポートするために使用されます。データをインポートすると、更新された PDF は新しい文書として保存されます。

1. PDF フォームフィールドを操作するには PDF_Facades.form () を初期化します。
1. 'bind_pdf () 'を呼び出して PDF フォームテンプレートを添付してください。
1. XFDF ファイルを読み込むには 'open () 'を使用してください。
1. 「import_xfdf ()」を呼び出して、XFDF ファイルの値を PDF フィールドに入力します。
1. 更新したドキュメントを保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import Data from XFDF
def import_data_from_xfdf(infile, datafile, outfile):
    """Import form data from XFDF file into PDF form fields."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open XFDF file as stream
    with open(datafile, "rb") as xfdf_input_stream:
        # Import data from XFDF into PDF form fields
        pdf_form.import_xfdf(xfdf_input_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```

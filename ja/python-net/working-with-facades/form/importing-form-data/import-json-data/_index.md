---
title: JSON データをインポートする
type: docs
weight: 30
url: /ja/python-net/import-json-data/
description: この例は、.NET 経由で Aspose.PDF for Python を使用して、フォームフィールドデータを JSON ファイルから PDF フォームにインポートする方法を示しています。PDF ドキュメントをバインドする方法、ファイルストリームを介して構造化された JSON データを読み取る方法、および一致するフォームフィールドを自動的に入力する方法を示しています。
lastmod: "2026-06-09"
---

JSON は、システム間の構造化データの保存と転送に広く使用されています。この例では、 [フォーム](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) からのファサード [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) モジュールは PDF フォームをバインドし、外部 JSON ファイルからフィールド値をインポートするために使用されます。インポート処理後、更新された文書は新しい PDF として保存されます。

1. PDF フォームフィールドを操作するには PDF_Facades.form () を初期化します。
1. 'bind_pdf () 'を呼び出して PDF フォームテンプレートを添付してください。
1. 'FileIO () 'を使用して、フォーム値を含む JSON ファイルを読み取ります。
1. 'import_json () 'を呼び出して、JSON キーと値のペアを使用して PDF フィールドに入力します。
1. 更新した PDF を保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import from JSON
def import_json_to_pdf_form(infile, datafile, outfile):
    """Import form data from JSON file into PDF form fields."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    # Open JSON file as stream
    with FileIO(datafile, "r") as json_stream:
        # Import data from JSON into PDF form fields
        form.import_json(json_stream)

    # Save updated PDF
    form.save(outfile)
```

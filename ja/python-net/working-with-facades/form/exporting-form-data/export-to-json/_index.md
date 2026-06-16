---
title: JSON へのエクスポート
type: docs
weight: 30
url: /ja/python-net/export-to-json/
description: この例は、.NET 経由で Aspose.PDF for Python を使用して PDF フォームフィールド値を JSON ファイルにエクスポートする方法を示しています。PDF フォームを読み込み、Form ファサードからフィールドにアクセスし、抽出されたデータを構造化された JSON 形式で保存する方法を説明します。
lastmod: "2026-06-09"
---

JSON は、アプリケーションとサービス間のシームレスな交換を可能にする、広く使用されているデータ形式です。この例では、 [フォーム](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) からのオブジェクト [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) モジュールは PDF ファイルをバインドし、そのフォームフィールド値を読み取り可能な JSON 構造にエクスポートするために使用されます。

1. フォームフィールドを操作できるように PDF_Facades.form () を初期化します。
1. 'bind_pdf () 'を使用してソース PDF ドキュメントを添付してください。
1. 'FileIO () 'を使用して書き込み可能なストリームを作成します。
1. 'export_json () 'を呼び出してフォームフィールド値を抽出し、フォーマットされた JSON 形式で保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to JSON
def export_form_to_json(infile, outfile):
    """Export PDF form field values to JSON file."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    # Create JSON file stream
    with FileIO(outfile, "w") as json_stream:
        # Export form field values to JSON
        form.export_json(json_stream, indented=True)
```

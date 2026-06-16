---
title: FDF にエクスポート
type: docs
weight: 10
url: /ja/python-net/export-to-fdf/
description: この例では、.NET 経由で Aspose.PDF for Python を使用して PDF フォームフィールドデータを FDF (フォームデータフォーマット) ファイルにエクスポートする方法を説明します。Form ファサードからインタラクティブフォームデータにアクセスし、ソース PDF ドキュメントをバインドし、抽出した値を FDF ストリームに保存する方法を示しています。
lastmod: "2026-06-09"
---

FDFは、文書全体を埋め込むことなくPDFフォームデータを保存および転送するために特別に設計された軽量形式です。この例では、 [フォーム](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) オブジェクトはから初期化されます [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) モジュールにより、開発者はAcroFormフィールドを操作し、その値をエクスポートできます。

1. PDF フォームフィールドを操作するための PDF_Facades.form () のインスタンスを作成します。
1. 'bind_pdf () 'を呼び出して、フォームを含む PDF ドキュメントを添付します。
1. FDF ファイル用の書き込み可能なバイナリストリームを作成するには、'open (')' を使用してください。
1. フォームデータをエクスポートします。'export_fdf () 'を呼び出して、すべてのフォームフィールド値を抽出して保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to FDF
def export_form_data_to_fdf(infile, outfile):
    """Export PDF form data to FDF file."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Create FDF file stream
    with open(outfile, "wb") as fdf_output_stream:
        # Export form data to FDF file
        pdf_form.export_fdf(fdf_output_stream)
```

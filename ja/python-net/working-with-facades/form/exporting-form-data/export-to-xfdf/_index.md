---
title: XFDF にエクスポート
type: docs
weight: 20
url: /ja/python-net/export-to-xfdf/
description: この例は、.NET 経由で Aspose.PDF for Python を使用して PDF フォームフィールドデータを XFDF (XML フォームデータフォーマット) ファイルにエクスポートする方法を示しています。PDF フォームを読み込み、Form ファサードからフィールドにアクセスし、抽出した値を XFDF ストリームに保存する方法を示しています。
lastmod: "2026-06-09"
---

XFDF は PDF フォームデータの XML 表現であり、開発者はフォームフィールドの値を元の文書とは独立して転送できます。この例では、 [フォーム](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) オブジェクト元 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) ソース PDF をバインドし、そのデータを構造化された XFDF ファイルにエクスポートするために使用されます。

1. PDF フォームデータを管理するには、PDF_Facades.form () を初期化します。
1. 'bind_pdf () 'を呼び出して、ソース PDF ドキュメントを添付してください。
1. 書き込み可能なバイナリストリームを作成するには 'open () 'を使用してください。
1. フォームデータをエクスポートします。'export_xfdf () 'を呼び出して、フォームフィールドの値を XFDF 形式で抽出して保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to XFDF
def export_pdf_form_to_xfdf(infile, outfile):
    """Export PDF form data to XFDF file."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Create XFDF file stream
    with open(outfile, "wb") as xfdf_output_stream:
        # Export form data to XFDF file
        pdf_form.export_xfdf(xfdf_output_stream)
```

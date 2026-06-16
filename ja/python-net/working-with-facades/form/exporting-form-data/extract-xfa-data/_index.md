---
title: XFA データを抽出
type: docs
weight: 50
url: /ja/python-net/extract-xfa-data/
description: この例では、.NET 経由で Aspose.PDF for Python を使用して PDF ファイルから XFA フォームデータを抽出する方法を説明します。XFA ベースの PDF ドキュメントを Form ファサードにバインドし、その内部データ構造をファイルストリームにエクスポートする方法を示しています。
lastmod: "2026-06-09"
---

XFA (XML フォームアーキテクチャ) フォームは、データが PDF 内に XML として保存されるという点で、従来の AcroForms とは異なります。この例では、 [フォーム](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) からのオブジェクト [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) モジュールを使用して PDF をバインドし、その XFA データをファイルに直接抽出します。

1. PDF_Facades.form () のインスタンスを作成してフォームデータを管理します。
1. 「bind_pdf ()」を呼び出して、XFA フォームを含むソース PDF を添付します。
1. 'FileIO () 'を使用して書き込み可能なファイルストリームを作成します。
1. 'extract_xfa_data () 'を呼び出して、埋め込まれた XFA XML データをエクスポートします。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Extract XFA Data
def export_xfa_data(infile, outfile):
    """Export XFA form data."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    with FileIO(outfile, "w") as stream:
        # Export embedded XFA XML data to the output stream
        form.extract_xfa_data(stream)
```

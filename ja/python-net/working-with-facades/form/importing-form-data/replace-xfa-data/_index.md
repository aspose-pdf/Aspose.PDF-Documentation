---
title: XFA データを置換
type: docs
weight: 50
url: /ja/python-net/replace-xfa-data/
description: この例は、.NET 経由で Aspose.PDF for Python を使用して PDF 内の既存の XFA フォームデータを置き換える方法を示しています。XFA ベースの PDF ドキュメントをバインドする方法、外部の XFA ファイルから新しいデータを読み込む方法、およびフォームコンテンツをプログラムで更新する方法を示しています。
lastmod: "2026-06-09"
---

XFA (XML フォームアーキテクチャ) フォームは、データを PDF 構造内に XML 形式で格納します。この例では、 [フォーム](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) からのファサード [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) モジュールは PDF をバインドし、外部 XML ストリームを使用して既存の XFA データセットを置き換えるために使用されます。新しいデータを適用すると、更新された PDF は別のファイルとして保存されます。

1. XFA フォームデータを管理するには PDF_Facades.form () を初期化します。
1. 'bind_pdf () 'を呼び出して、XFA フォームを含む PDF を添付してください。
1. XFA XML ファイルを読み込むには 'FileIO () 'を使用してください。
1. 「set_xfa_data ()」を呼び出して、PDF を新しい XFA コンテンツで更新します。
1. 更新したドキュメントを保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Replace from XFA data
def replace_xfa_data(infile, datafile, outfile):
    """Import form data from XFA file into PDF form fields."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    # Open XFA file as stream
    with FileIO(datafile, "r") as xfa_stream:
        # Import data from XFA into PDF form fields
        form.set_xfa_data(xfa_stream)

    # Save updated PDF
    form.save(outfile)
```

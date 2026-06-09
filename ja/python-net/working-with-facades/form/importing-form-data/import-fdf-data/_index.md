---
title: FDF データをインポート
type: docs
weight: 10
url: /ja/python-net/import-fdf-data/
description: この例は、.NET 経由で Aspose.PDF for Python を使用して FDF ファイルから PDF フォームにフォームデータをインポートする方法を示しています。PDF ドキュメントをバインドする方法、FDF ストリームからフォームフィールド値を読み取る方法、および対応するフィールドを自動的に入力する方法を示します。
lastmod: "2026-06-09"
---

FDF（Forms Data Format）は、文書全体を含めずに PDF フォームフィールドの値を保存および転送するために使用される軽量形式です。この例では、 [フォーム](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) ファサードから [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) PDF フォームを読み込み、外部 FDF ファイルからフィールドデータをインポートするために使用されます。インポート処理後、更新された PDF は新しいファイルとして保存されます。

1. PDF_Facades.form () を初期化して、インタラクティブ PDF フォームフィールドを操作できるようにします。
1. 'bind_pdf () 'を呼び出して PDF フォームテンプレートを添付してください。
1. FDF ファイルをバイナリモードで読み込むには 'open () 'を使用してください。
1. 'import_fdf () 'を呼び出して、PDF フィールドに FDF ファイルのデータを入力します。
1. 更新した PDF を保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import Data from FDF
def import_fdf_to_pdf_form(infile, datafile, outfile):
    """Import form data from FDF file into PDF form fields."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open FDF file as stream
    with open(datafile, "rb") as fdf_input_stream:
        pdf_form.import_fdf(fdf_input_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```

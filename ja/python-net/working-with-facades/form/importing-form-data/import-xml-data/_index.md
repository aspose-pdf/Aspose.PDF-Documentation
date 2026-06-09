---
title: XML データをインポート
type: docs
weight: 40
url: /ja/python-net/import-xml-data/
description: この例は、.NET 経由で Aspose.PDF for Python を使用して、XML ファイルから PDF フォームフィールドにフォームデータをインポートする方法を示しています。PDF ドキュメントをバインドする方法、ファイルストリームを介して構造化された XML データを読み取る方法、および対応するフォームフィールドに自動的にデータを入力する方法を示します。
lastmod: "2026-06-09"
---

XML は構造化されたフォームデータの保存によく使用されるため、システム間で値を転送するための実用的な形式です。この例では、 [フォーム](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) ファサードから [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) PDF フォームを読み込み、XML ファイルから直接フィールド値を適用するために使用されます。データをインポートすると、更新された PDF は新しい文書として保存されます。

1. PDF フォームフィールドを操作するには PDF_Facades.form () を初期化します。
1. 'bind_pdf () 'を呼び出して PDF フォームテンプレートを添付してください。
1. 'FileIO () 'を使用して、フォームデータを含む XML ファイルにアクセスします。
1. 'import_xml () 'を呼び出して、XML ファイルの値を PDF フィールドに入力します。
1. 更新した PDF を保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import data from XML
def import_xml_to_pdf_fields(infile, datafile, outfile):
    """Import form data from XML file into PDF form fields."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open XML file as stream
    with FileIO(datafile, "r") as xml_input_stream:
        # Import data from XML into PDF form fields
        pdf_form.import_xml(xml_input_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```

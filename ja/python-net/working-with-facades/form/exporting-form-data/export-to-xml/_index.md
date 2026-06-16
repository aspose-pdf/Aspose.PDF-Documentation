---
title: XML にエクスポート
type: docs
weight: 40
url: /ja/python-net/export-to-xml/
description: この例は、.NET 経由で Aspose.PDF for Python を使用して PDF フォームデータを XML ファイルにエクスポートする方法を示しています。Form Class を使用して PDF ドキュメントを読み込み、Form ファサードからフォームフィールドにアクセスし、抽出したデータを構造化 XML として保存する方法を示しています。
lastmod: "2026-06-09"
---

フォームデータをエクスポートすると、開発者はフィールド値を手動でコピーしなくても PDF AcroForms に保存されている情報を再利用できます。この例では、 [フォーム](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) オブジェクトは aspose.pdf から作成されます。ファサードモジュールでは、ソース PDF がバインドされ、フォームデータが XML ストリームに書き込まれます。

1. フォームオブジェクトを作成します。PDF_Facades.form () を初期化して、フォームフィールドにアクセスして管理します。
1. 'bind_pdf () 'を使用して、ソース PDF ドキュメントをフォームインスタンスに添付します。
1. 'FileIO () 'を使用して書き込み可能なファイルストリームを作成します。
1. 'export_xml () 'を呼び出して、すべてのフォームフィールド値を抽出し、XML ファイルに書き込みます。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to XML
def export_pdf_form_data_to_xml(infile, datafile):
    """Export PDF form data to XML file."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open XML file as stream
    with FileIO(datafile, "w") as xml_output_stream:
        # Export data from PDF form fields to XML
        pdf_form.export_xml(xml_output_stream)
```

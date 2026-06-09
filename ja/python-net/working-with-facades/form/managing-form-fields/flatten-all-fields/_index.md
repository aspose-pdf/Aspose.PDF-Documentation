---
title: すべてのフィールドをフラット化
type: docs
weight: 10
url: /ja/python-net/flatten-all-fields/
description: この例は、.NET 経由で Aspose.PDF for Python を使用して PDF 内のすべてのフォームフィールドをフラット化する方法を示しています。PDF ドキュメントをバインドし、すべてのインタラクティブフォーム要素を静的ページコンテンツに変換し、完成したファイルを保存する方法を示しています。
lastmod: "2026-06-09"
---

フラットニングは、フィールド値をドキュメントレイアウトに直接マージすることで、PDF フォームからインタラクティブ機能を排除します。この例では、 [フォーム](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) ファサードから [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) を使用してソース PDF をバインドし、すべてのフィールドを編集不可能なコンテンツに変換する flatten_all_fields () メソッドを適用します。

1. PDF フォームフィールドを操作するには PDF_Facades.form () を初期化します。
1. 'bind_pdf () 'を呼び出して、ソースドキュメントを添付します。
1. 'flatten_all_fields () 'を呼び出して、すべてのインタラクティブフィールドを静的コンテンツに変換します。
1. 更新したドキュメントを保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Flatten all fields
def flatten_all_fields(infile, outfile):
    """Flatten all fields in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Flatten all fields in the PDF document
    pdf_form.flatten_all_fields()

    # Save updated PDF
    pdf_form.save(outfile)
```

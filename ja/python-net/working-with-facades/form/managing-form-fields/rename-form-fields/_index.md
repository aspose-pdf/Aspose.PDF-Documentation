---
title: フォームフィールドの名前を変更
type: docs
weight: 30
url: /ja/python-net/rename-form-fields/
description: この例は、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメント内のフォームフィールドの名前を変更する方法を示しています。PDF フォームを連結し、既存のフィールド名をプログラムで更新し、変更したファイルを保存する方法を示します。フィールドの名前を変更すると、フォーム構造の標準化、データマッピングの改善、自動化されたワークフローや外部システムとの統合の簡素化に役立ちます。
lastmod: "2026-06-09"
---

フォームフィールドの名前を変更すると、PDF フォームを社内の命名規則に合わせたり、文書を構造化データ処理用に準備したりする場合に便利です。この例では、 [フォーム](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) からのファサード [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) モジュールを使用してソース PDF をバインドし、古いフィールド名を新しいフィールド名に置き換えるマッピングを適用します。フィールド識別子を更新すると、変更が適用された状態で文書が保存されます。

1. PDF フォームフィールドを操作するには PDF_Facades.form () を初期化します。
1. 'bind_pdf () 'を呼び出して PDF ドキュメントを添付してください。
1. 古いフィールド名とそれに対応する新しい名前を含むタプルのリストを作成します。
1. マッピングを繰り返し処理し、エントリごとに「rename_field ()」を呼び出します。
1. 更新したドキュメントを保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Rename form fields
def rename_form_fields(infile, outfile):
    """Rename form fields in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Rename form fields by providing a mapping of old names to new names
    field_renaming_map = [("First Name", "NewFirstName"), ("Last Name", "NewLastName")]
    for old_name, new_name in field_renaming_map:
        pdf_form.rename_field(old_name, new_name)

    # Save updated PDF
    pdf_form.save(outfile)
```

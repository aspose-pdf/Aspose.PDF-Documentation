---
title: ボタンフィールドと画像
type: docs
weight: 40
url: /ja/python-net/button-fields-and-images/
description: この例は、Aspose.PDF Facades API を使用して PDF フォームのボタンフィールドを管理する方法を示しています。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: ボタンフィールドへの画像表示の追加と送信フラグの読み込み
Abstract: PDF フォームには、JavaScript アクションをトリガーするか、フォームデータを送信するインタラクティブなボタンが含まれていることがよくあります。ボタンの見た目に画像を追加してボタンフィールドを視覚的に強化したり、送信時の動作をプログラムで調べたりできます。
---

## ボタンフィールドへの画像表示の追加

このコードスニペットでは、PDF フォームの既存のボタンフィールドに画像の外観を追加する方法について説明します。この操作を行うと、デフォルトの外観がカスタム画像に置き換えられるため、PDF ボタンの視覚的表示が向上します。

1. Form オブジェクトを作成します。
1. PDF ファイルをフォームオブジェクトにバインドします。
1. ボタンフィールドに画像を追加します。

    -PDF に関連付けられている画像ファイルへのパスを特定します
    -イメージを image_stream としてバイナリモードで開きます。
    -完全修飾ボタンフィールド名を指定して fill_image_field () を呼び出します。

1. 更新した PDF を保存します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Add image appearance to button fields
def add_image_appearance_to_button_fields(infile, outfile):
    """Add image appearance to button fields in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Add image appearance to button fields by providing the field name and image stream
    image_path = infile.replace(".pdf", ".jpg")
    with open(image_path, "rb") as image_stream:
        pdf_form.fill_image_field("Image1_af_image", image_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```

## 送信フラグを取得

Python ライブラリを使用すると、Aspose.PDF Facades API を使用して PDF フォーム内の送信ボタンの送信フラグを取得できます。送信フラグは、フォーム全体を送信するか、注釈を含めるか、FDF、XFDF、PDF、HTML 形式で送信するかなど、送信ボタンの動作を定義します。

1. Form オブジェクトを作成します。
1. 完全修飾された送信ボタン名を使用してフォームオブジェクトで get_submit_flags () を呼び出します。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_submit_flags(infile, outfile):
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)
    flags = pdf_form.get_submit_flags("Submit1_af_submit")

    print(f"Submit flags: {flags}")
```

---
title: アクロフォームを作成-Python で入力可能な PDF を作成
linktitle: アクロフォームを作成
type: docs
weight: 10
url: /ja/python-net/create-form/
description: .NET 経由で Aspose.PDF for Python を使用して、PDF ドキュメントに AcroForm フィールドを一から作成してください。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使って PDF でアクロフォームを作成する方法
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメントに AcroForm フィールドを作成する方法について説明します。TextBoxField による基本的なフィールド作成、複数のウィジェットによるテキストボックスの外観のカスタマイズ、およびラジオボタン、コンボボックス、チェックボックス、リストボックス、署名フィールド、バーコードフィールドなどのその他のフィールドタイプについて説明します。これらの例は、データ収集および文書自動化ワークフロー用のインタラクティブな PDF フォームの作成に役立ちます。
---

## フォームを最初から作成

### PDF ドキュメントにフォームフィールドを追加

ザの [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class はという名前のコレクションを提供します [フォーム](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/) PDF ドキュメント内のフォームフィールドを管理するのに役立ちます。

フォームフィールドを追加するには:

1. 追加するフォームフィールドを作成します。
1. フォームコレクションを呼び出す [追加](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/#methods) 方法。

### テキストボックスフィールドの追加

次の例は、を追加する方法を示しています [テキストボックスフィールド](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/).

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_text_box_field(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    rectangle = ap.Rectangle(10, 600, 110, 620, True)
    text_box_field = ap.forms.TextBoxField(page, rectangle)
    text_box_field.partial_name = "textbox1"
    text_box_field.value = "Text Box"

    text_box_field.default_appearance = ap.annotations.DefaultAppearance(
        "Arial", 10, drawing.Color.dark_blue
    )

    border = ap.annotations.Border(text_box_field)
    border.width = 1
    border.style = ap.annotations.BorderStyle.DASHED
    border.dash = ap.annotations.Dash(3, 3)
    text_box_field.border = border

    text_box_field.characteristics.border = ap.Color.red.to_rgb()
    text_box_field.characteristics.background = ap.Color.yellow.to_rgb()

    document.form.add(text_box_field, 1)
    document.save(output_file_name)
```

### PDF のマルチウィジェットテキストボックスフィールド

Python と Aspose.PDF を使用して、PDF に複数のウィジェットが表示されるテキストボックスフォームフィールドを作成します。1 ページに複数のテキスト入力領域を配置し、各ウィジェットに異なるフォントと色を適用し、境界線をカスタマイズし、インタラクティブ PDF フォーム用の背景スタイルを設定します。

1. 新しい PDF ドキュメントを作成します。
1. テキストフィールドの位置を定義します。
1. さまざまなデフォルト外観を作成。
1. テキストボックスフィールドを作成します。
1. 各ウィジェットに外観を適用します。
1. ボーダースタイルをカスタマイズします。
1. フィールドをフォームに追加します。
1. PDF ファイルを保存します。

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_text_box_field_nt(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    rects = [
        ap.Rectangle(10, 600, 110, 620, normalize_coordinates=True),
        ap.Rectangle(10, 630, 110, 650, normalize_coordinates=True),
        ap.Rectangle(10, 660, 110, 680, normalize_coordinates=True),
    ]

    default_appearances = [
        ap.annotations.DefaultAppearance("Arial", 10, drawing.Color.dark_blue),
        ap.annotations.DefaultAppearance("Helvetica", 12, drawing.Color.dark_green),
        ap.annotations.DefaultAppearance(
            ap.text.FontRepository.find_font("Calibri"), 14, drawing.Color.dark_magenta
        ),
    ]

    text_box_field = ap.forms.TextBoxField(page, rects)
    text_box_field.partial_name = "textbox1"
    text_box_field.value = "Some text"

    for i, widget in enumerate(text_box_field):
        widget.default_appearance = default_appearances[i]

    border = ap.annotations.Border(text_box_field)
    border.width = 1
    border.style = ap.annotations.BorderStyle.DASHED
    border.dash = ap.annotations.Dash(3, 3)
    text_box_field.border = border

    text_box_field.characteristics.border = ap.Color.red.to_rgb()
    text_box_field.characteristics.background = ap.Color.yellow.to_rgb()

    document.form.add(text_box_field)
    document.save(output_file_name)
```

## 他のフォームフィールドを追加する

次のコードスニペットは、ラジオボタン、コンボボックス、チェックボックス、リストボックス、署名フィールド、バーコードフィールドなど、さまざまなフィールドタイプを追加する方法を示しています。各関数は新しい PDF ドキュメントを作成し、選択したオプションを含むターゲットフィールドを追加して、更新されたファイルを保存します。

1. ラジオボタンフィールドを追加
1. コンボボックスフィールドを追加
1. チェックボックスフィールドを追加
1. リストボックスフィールドを追加
1. 署名フィールドを追加
1. バーコードフィールドを追加

### ラジオボタンフィールドを追加

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_radio_button(output_file_name):
    document = ap.Document()
    document.pages.add()

    radio = ap.forms.RadioButtonField(document.pages[1])
    radio.add_option(
        "Option 1", ap.Rectangle(100, 640, 120, 680, normalize_coordinates=True)
    )
    radio.add_option(
        "Option 2", ap.Rectangle(140, 640, 160, 680, normalize_coordinates=True)
    )

    document.form.add(radio)
    document.save(output_file_name)
```

### コンボボックスフィールドを追加

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_combo_box(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    combo = ap.forms.ComboBoxField(
        page, ap.Rectangle(100, 640, 150, 656, normalize_coordinates=True)
    )
    combo.add_option("Red")
    combo.add_option("Yellow")
    combo.add_option("Green")
    combo.add_option("Blue")
    combo.selected = 3

    document.form.add(combo)
    document.save(output_file_name)
```

### チェックボックスフィールドを追加

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_checkbox_field_to_pdf(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    checkbox = ap.forms.CheckboxField(
        page, ap.Rectangle(50, 620, 100, 650, normalize_coordinates=True)
    )
    checkbox.characteristics.background = ap.Color.aqua.to_rgb()
    checkbox.style = ap.forms.BoxStyle.CIRCLE

    document.form.add(checkbox)
    document.save(output_file_name)
```

### リストボックスフィールドを追加

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_list_box_field_to_pdf(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    list_box = ap.forms.ListBoxField(
        page, ap.Rectangle(50, 650, 100, 700, normalize_coordinates=True)
    )
    list_box.partial_name = "list"
    list_box.add_option("Red")
    list_box.add_option("Green")
    list_box.add_option("Blue")

    document.form.add(list_box)
    document.save(output_file_name)
```

### 署名フィールドを追加

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_signature_field(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    signature_field = ap.forms.SignatureField(
        page, ap.Rectangle(100, 700, 200, 800, True)
    )
    signature_field.partial_name = "Signature1"
    document.form.add(signature_field)
    document.save(output_file_name)
```

### バーコードフィールドを追加

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_barcode_field(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    barcode = ap.forms.BarcodeField(page, ap.Rectangle(100, 700, 200, 740, True))
    barcode.partial_name = "Barcode1"
    barcode.add_barcode("1234567890")
    document.form.add(barcode)
    document.save(output_file_name)
```

## 関連トピック

- [アクロフォームに記入](/pdf/ja/python-net/fill-form/)
- [アクロフォームを抽出](/pdf/ja/python-net/extract-form/)
- [アクロフォームの修正](/pdf/ja/python-net/modifying-form/)
- [フォームデータのインポートとエクスポート](/pdf/ja/python-net/import-export-form-data/)

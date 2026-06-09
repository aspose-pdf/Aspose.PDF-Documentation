---
title: Python で PDF テキストにツールチップを追加する方法
linktitle: PDF ツールチップ
type: docs
weight: 20
url: /ja/python-net/pdf-tooltip/
description: Python で PDF ドキュメントのテキストフラグメントにツールチップを追加する方法を学びます。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF テキストフラグメントにインタラクティブなツールチップを追加
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF テキストにインタラクティブヘルプを追加するための Python の例を 2 つ紹介します。最初の例では、非表示の「ButtonField」要素を配置して「alternate_name」を設定することで、一致したテキストフラグメントにツールチップを追加します。2 番目の例では、「HideAction` イベントを非表示の「ButtonField」に接続することで、カーソルを合わせると表示される「TextBoxField」という非表示の「TextBoxField」を作成します。
---

## PDF 内の検索テキストへのツールチップの追加

このコードスニペットは、非表示のオーバーレイ方法を示しています [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) 特定の要素 [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) PDF 内のオブジェクトにカーソルを合わせるとツールチップが表示されます。を使うと、短いツールチップメッセージと長いツールチップメッセージの両方がサポートされます。 `alternate_name` のプロパティ `ButtonField`.

このページは、カーソルを合わせたヘルプ、インライン説明、またはコンテキストノートを追加して PDF テキストをよりインタラクティブにする必要がある場合に使用します。

1. 新規作成 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 初期文書を保存します。
1. PDF ドキュメントを再度開きます。
1. を使用してターゲットテキストを検索する [`TextFragmentAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/).
1. 見えないものを追加 [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) 短いツールチップ付き。
1. 2 番目のターゲットテキストを検索します。
1. 見えないものを追加 [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) マッチしたフラグメントの上に長いツールチップが表示されます。
1. 最終文書を保存します。

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing
import sys
from os import path

# region PDF Tooltip
def add_tool_tip_to_searched_text(outfile):
    # Create PDF document
    with ap.Document() as document:
        document.pages.add().paragraphs.add(
            ap.text.TextFragment("Move the mouse cursor here to display a tooltip")
        )
        document.pages[1].paragraphs.add(
            ap.text.TextFragment(
                "Move the mouse cursor here to display a very long tooltip"
            )
        )
        document.save(outfile)

    # Open document with text
    with ap.Document(outfile) as document:
        # Create TextAbsorber object to find all the phrases matching the regular expression
        absorber = ap.text.TextFragmentAbsorber(
            "Move the mouse cursor here to display a tooltip"
        )
        # Accept the absorber for the document pages
        document.pages.accept(absorber)
        # Get the extracted text fragments
        text_fragments = absorber.text_fragments

        # Loop through the fragments
        for fragment in text_fragments:
            # Create invisible button on text fragment position
            field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
            # alternate_name value will be displayed as tooltip by a viewer application
            field.alternate_name = "Tooltip for text."
            # Add button field to the document
            document.form.add(field)

        # Next will be sample of very long tooltip
        absorber = ap.text.TextFragmentAbsorber(
            "Move the mouse cursor here to display a very long tooltip"
        )
        document.pages.accept(absorber)
        text_fragments = absorber.text_fragments

        for fragment in text_fragments:
            field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
            # Set very long text
            field.alternate_name = (
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit,"
                " sed do eiusmod tempor incididunt ut labore et dolore magna"
                " aliqua. Ut enim ad minim veniam, quis nostrud exercitation"
                " ullamco laboris nisi ut aliquip ex ea commodo consequat."
                " Duis aute irure dolor in reprehenderit in voluptate velit"
                " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint"
                " occaecat cupidatat non proident, sunt in culpa qui officia"
                " deserunt mollit anim id est laborum."
            )
            document.form.add(field)

        # Save document
        document.save(outfile)
```

## PDF のカーソルを合わせると表示される隠しテキストブロックの作成

PDF ドキュメントにインタラクティブなフローティングテキストを追加します。見えない部分に重ねて表示されます。 [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) ターゲットフレーズで隠されたフレーズを明らかにする [`TextBoxField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/) ユーザーがその上にカーソルを置いたとき。この手法は、コンテキストヘルプ、注釈、または動的コンテンツの表示に最適です。

1. 新しい PDF ドキュメントを作成します。
1. PDF を保存して、再び開いてインタラクティビティの設定を行えるようにします。
1. PDF ドキュメントを再度開きます。
1. を使用してターゲットテキストを検索します [`TextFragmentAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/).
1. 隠しアイテムを作成 [`TextBoxField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/).
1. 隠しフィールドをドキュメントに追加する [`Form`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/) コレクション。
1. 目に見えないものを作る [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/).
1. マウスアクションの割り当て (`on_enter`, `on_exit`) を使用して [`HideAction`](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/hideaction/) 隠しフィールドを表示/非表示にします。
1. 最終文書を保存します。

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing
import sys
from os import path

def create_hidden_text_block(outfile):
    # Create PDF document
    with ap.Document() as document:
        #  Add paragraph with text
        document.pages.add().paragraphs.add(
            ap.text.TextFragment("Move the mouse cursor here to display floating text")
        )
        # Save PDF document
        document.save(outfile)

    # Open document with text
    with ap.Document(outfile) as document:
        # Create TextAbsorber object to find all the phrases matching the regular expression
        absorber = ap.text.TextFragmentAbsorber(
            "Move the mouse cursor here to display floating text"
        )
        # Accept the absorber for the document pages
        document.pages.accept(absorber)
        # Get the first extracted text fragment
        text_fragments = absorber.text_fragments
        fragment = text_fragments[1]

        # Create hidden text field for floating text in the specified rectangle of the page
        floating_field = ap.forms.TextBoxField(
            fragment.page, ap.Rectangle(100.0, 700.0, 220.0, 740.0, False)
        )
        # Set text to be displayed as field value
        floating_field.value = 'This is the "floating text field".'
        # We recommend to make field 'readonly' for this scenario
        floating_field.read_only = True
        # Set 'hidden' flag to make field invisible on document opening
        floating_field.flags |= ap.annotations.AnnotationFlags.HIDDEN

        # Setting a unique field name isn't necessary but allowed
        floating_field.partial_name = "FloatingField_1"

        # Setting characteristics of field appearance isn't necessary but makes it better
        floating_field.default_appearance = ap.annotations.DefaultAppearance(
            "Helv", 10, drawing.Color.blue
        )
        floating_field.characteristics.background = drawing.Color.light_blue
        floating_field.characteristics.border = drawing.Color.dark_blue
        floating_field.border = ap.annotations.Border(floating_field)
        floating_field.border.width = 1
        floating_field.multiline = True

        # Add text field to the document
        document.form.add(floating_field)
        # Create invisible button on text fragment position
        button_field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
        # Create new hide action for specified field (annotation) and invisibility flag.
        # (You also may refer floating field by the name if you specified it above.)
        # Add actions on mouse enter/exit at the invisible button field

        button_field.actions.on_enter = ap.annotations.HideAction(floating_field, False)
        button_field.actions.on_exit = ap.annotations.HideAction(floating_field)

        # Add button field to the document
        document.form.add(button_field)

        # Save document
        document.save(outfile)
```

## 関連テキストトピック

- [Python を使用して PDF 内のテキストを操作する](/pdf/ja/python-net/working-with-text/)
- [Python の PDF テキストレイアウトにフローティングボックスを使用する](/pdf/ja/python-net/floating-box/)
- [Python で PDF テキストを検索して抽出する](/pdf/ja/python-net/search-and-get-text-from-pdf/)
- [PDF へのテキストの追加](/pdf/ja/python-net/add-text-to-pdf-file/)
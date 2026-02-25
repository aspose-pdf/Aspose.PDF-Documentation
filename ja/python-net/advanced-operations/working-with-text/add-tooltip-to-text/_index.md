---
title: テキストにツールチップを作成する
linktitle: PDF ツールチップ
type: docs
weight: 20
url: /ja/python-net/pdf-tooltip/
description: Python と Aspose.PDF を使用して PDF のテキストフラグメントにツールチップを追加する方法を学びます
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF のテキストフラグメントにツールチップを追加する
Abstract: この記事では、Aspose.PDF ライブラリを使用して PDF ドキュメントのインタラクティビティを向上させるための 2 つの Python コード例を提供します。最初の例は、テキスト上に不可視の ButtonField 要素を作成し、`alternate_name` プロパティをツールチップとして設定することで、PDF 内の特定のテキストフラグメントにツールチップを追加する方法を示します。2 番目の例は、`TextFragment` が見つかった位置に隠し `TextBoxField` を作成し、不可視の ButtonField に `HideAction` イベントを割り当てて、ホバー時に浮動テキストブロックを表示または非表示にする方法を示します。
---

## PDF の検索テキストにツールチップを追加する

このコードスニペットは、PDF の特定の [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) オブジェクト上に不可視の [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) 要素を重ねて、ユーザーがホバーしたときにツールチップを表示する方法を示します。`ButtonField` の `alternate_name` プロパティを使用して、短いツールチップと長いツールチップの両方をサポートします。

1. 新しい [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) を作成します。
1. 最初のドキュメントを保存します。
1. PDF ドキュメントを再度開きます。
1. [`TextFragmentAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) を使用して対象テキストを検索します。
1. 短いツールチップを持つ不可視の [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) を追加します。
1. 2 番目の対象テキストを検索します。
1. マッチしたフラグメント上に長いツールチップを持つ不可視の [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) を追加します。
1. 最終ドキュメントを保存します。

```python

import os
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def add_tool_tip_to_searched_text(outfile):
    """
    Add tooltips to searched text in a PDF document.

    Creates a PDF with text fragments and adds invisible button fields over them
    to display tooltips when users hover with their mouse cursor. Demonstrates
    both short and long tooltip text implementations.

    Args:
        outfile (str): Path where the PDF with tooltips will be saved.

    Returns:
        None: The function creates and saves a PDF file with tooltip functionality.

    Note:
        - Creates invisible ButtonField elements over text fragments
        - Uses alternate_name property to define tooltip content
        - Supports both short and very long tooltip text
        - TextFragmentAbsorber finds specific text to add tooltips to
        - Tooltips appear on mouse hover in PDF viewers that support this feature
        - Long tooltips demonstrate Lorem ipsum text for extensive content

    Example:
        >>> add_tool_tip_to_searched_text("tooltips.pdf")
        # Creates a PDF with interactive text tooltips
    """

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
        absorber = ap.text.TextFragmentAbsorber("Move the mouse cursor here to display a tooltip")
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
        absorber = ap.text.TextFragmentAbsorber("Move the mouse cursor here to display a very long tooltip")
        document.pages.accept(absorber)
        text_fragments = absorber.text_fragments

        for fragment in text_fragments:
            field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
            # Set very long text
            field.alternate_name = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit,"
                                    " sed do eiusmod tempor incididunt ut labore et dolore magna"
                                    " aliqua. Ut enim ad minim veniam, quis nostrud exercitation"
                                    " ullamco laboris nisi ut aliquip ex ea commodo consequat."
                                    " Duis aute irure dolor in reprehenderit in voluptate velit"
                                    " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint"
                                    " occaecat cupidatat non proident, sunt in culpa qui officia"
                                    " deserunt mollit anim id est laborum.")
            document.form.add(field)

        # Save document
        document.save(outfile)
```

## PDF でホバー時に表示される隠しテキストブロックを作成する

PDF ドキュメントにインタラクティブな浮動テキストを追加します。対象フレーズ上に不可視の [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) を重ね、ユーザーがホバーすると隠し [`TextBoxField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/) が表示されます。この手法は、コンテキストヘルプ、注釈、または動的コンテンツの提示に最適です。

1. 新しい PDF ドキュメントを作成します。
1. インタラクティブ設定のために再度開けるように PDF を保存します。
1. PDF ドキュメントを再度開きます。
1. [`TextFragmentAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) を使用して対象テキストを特定します。
1. 隠し [`TextBoxField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/) を作成します。
1. ドキュメントの [`Form`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/) コレクションに隠しフィールドを追加します。
1. 不可視の [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) を作成します。
1. マウスアクション (`on_enter`, `on_exit`) を [`HideAction`](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/hideaction/) で割り当て、隠しフィールドの表示/非表示を制御します。
1. 最終ドキュメントを保存します。

```python

import os
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def create_hidden_text_block(outfile):
    """
    Create a hidden text block that appears on mouse hover.

    Demonstrates advanced interactive PDF functionality by creating a hidden
    text field that becomes visible when users hover over specific text.
    Uses mouse enter/exit actions to control visibility.

    Args:
        outfile (str): Path where the PDF with hidden text functionality will be saved.

    Returns:
        None: The function creates and saves a PDF file with floating text capability.

    Note:
        - Creates a hidden TextBoxField with floating text content
        - Uses HideAction to control field visibility on mouse events
        - ButtonField acts as invisible trigger area over target text
        - Field is initially hidden and appears on mouse enter
        - Supports custom styling: colors, borders, fonts
        - Read-only field prevents user editing of floating text
        - Demonstrates advanced PDF interactivity features

    Example:
        >>> create_hidden_text_block("floating_text.pdf")
        # Creates a PDF with text that reveals hidden content on hover
    """

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
        absorber = ap.text.TextFragmentAbsorber("Move the mouse cursor here to display floating text")
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
        floating_field.default_appearance = ap.annotations.DefaultAppearance("Helv", 10, drawing.Color.blue)
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

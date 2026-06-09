---
title: 在 Python 中为 PDF 文本添加工具提示
linktitle: PDF 工具提示
type: docs
weight: 20
url: /zh/python-net/pdf-tooltip/
description: 了解如何在 Python 中向 PDF 文档的文本片段添加工具提示。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 为 PDF 文本片段添加交互式工具提示
Abstract: 本文提供了两个使用 Aspose.PDF for Python via .NET 为 PDF 文本添加交互式帮助的 Python 示例。第一个示例通过放置不可见的 `ButtonField` 元素并设置 `alternate_name` 来为匹配的文本片段添加工具提示。第二个示例创建一个隐藏的 `TextBoxField`，通过将 `HideAction` 事件绑定到不可见的 `ButtonField` 实现悬停时显示。
---

## 在 PDF 中为搜索的文本添加工具提示

此代码片段展示了如何覆盖不可见的 [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) 特定元素 [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) 在 PDF 中的对象在用户将鼠标悬停其上时显示工具提示。它支持使用的短提示和长提示消息 `alternate_name` 的属性 `ButtonField`.

当您需要通过添加悬停帮助、内联解释或上下文注释来使 PDF 文本更具交互性时，请使用此页面。

1. 创建一个新 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 保存初始文档。
1. 重新打开 PDF 文档。
1. 使用搜索目标文本 [`TextFragmentAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/).
1. 添加一个不可见的 [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) 带有简短的工具提示。
1. 搜索第二个目标文本。
1. 添加一个不可见的 [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) 在匹配的片段上显示长工具提示。
1. 保存最终文档。

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

## 在 PDF 中创建悬停时出现的隐藏文本块

向 PDF 文档添加交互式浮动文本。它覆盖一个不可见的 [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) 在目标短语上并显示隐藏的 [`TextBoxField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/) 当用户将鼠标悬停在其上时。此技术非常适合上下文帮助、批注或动态内容呈现。

1. 创建一个新的 PDF 文档。
1. 保存 PDF，以便以后重新打开进行交互设置。
1. 重新打开 PDF 文档。
1. 使用定位目标文本 [`TextFragmentAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/).
1. 创建隐藏的 [`TextBoxField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/).
1. 将隐藏字段添加到文档的 [`Form`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/) 集合。
1. 创建一个不可见的 [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/).
1. 分配鼠标操作（`on_enter`, `on_exit`) 使用 [`HideAction`](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/hideaction/) 显示/隐藏隐藏字段。
1. 保存最终文档。

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

## 相关文本主题

- [使用 Python 在 PDF 中处理文本](/pdf/zh/python-net/working-with-text/)
- [在 Python 中使用 FloatingBox 进行 PDF 文本布局](/pdf/zh/python-net/floating-box/)
- [在 Python 中搜索并提取 PDF 文本](/pdf/zh/python-net/search-and-get-text-from-pdf/)
- [向 PDF 添加文本](/pdf/zh/python-net/add-text-to-pdf-file/)
---
title: 텍스트에 툴팁 만들기
linktitle: PDF 툴팁
type: docs
weight: 20
url: /ko/python-net/pdf-tooltip/
description: Python 및 Aspose.PDF를 사용하여 PDF의 텍스트 조각에 툴팁을 추가하는 방법을 배웁니다.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 텍스트 조각에 툴팁 추가
Abstract: 이 문서에서는 Aspose.PDF 라이브러리를 사용하여 PDF 문서의 상호작용을 향상시키는 두 가지 Python 코드 예제를 제공합니다. 첫 번째 예제는 텍스트 위에 보이지 않는 ButtonField 요소를 생성하고 `alternate_name` 속성을 툴팁으로 설정하여 PDF 내 특정 텍스트 조각에 툴팁을 추가하는 방법을 보여줍니다. 두 번째 예제는 `TextFragment`가 위치한 곳에 숨겨진 `TextBoxField`를 만들고, 보이지 않는 `ButtonField`에 `HideAction` 이벤트를 연결하여 마우스를 올리면 떠다니는 텍스트 블록이 표시되거나 숨겨지도록 하는 방법을 보여줍니다.
---

## PDF에서 검색된 텍스트에 툴팁 추가

이 코드 조각은 PDF에서 특정 [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) 객체 위에 보이지 않는 [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) 요소를 겹쳐서 사용자가 마우스를 올릴 때 툴팁을 표시하는 방법을 보여줍니다. `ButtonField`의 `alternate_name` 속성을 사용하여 짧은 툴팁 메시지와 긴 툴팁 메시지 모두를 지원합니다.

1. 새로운 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 생성.
1. 초기 문서를 저장합니다.
1. PDF 문서를 다시 엽니다.
1. [`TextFragmentAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/)를 사용하여 대상 텍스트를 검색합니다.
1. 짧은 툴팁이 있는 보이지 않는 [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/)를 추가합니다.
1. 두 번째 대상 텍스트를 검색합니다.
1. 일치하는 조각 위에 긴 툴팁이 있는 보이지 않는 [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/)를 추가합니다.
1. 최종 문서를 저장합니다.

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

## PDF에서 마우스를 올리면 나타나는 숨겨진 텍스트 블록 만들기

PDF 문서에 인터랙티브한 떠다니는 텍스트를 추가합니다. 대상 구절 위에 보이지 않는 [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/)을 겹쳐 놓고 사용자가 마우스를 올리면 숨겨진 [`TextBoxField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/)이 나타납니다. 이 기법은 상황별 도움말, 주석 또는 동적 콘텐츠 표시 등에 이상적입니다.

1. 새로운 PDF 문서를 생성합니다.
1. 인터랙티브 설정을 위해 PDF를 저장하고 다시 열 수 있도록 합니다.
1. PDF 문서를 다시 엽니다.
1. [`TextFragmentAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/)를 사용하여 대상 텍스트를 찾습니다.
1. 숨겨진 [`TextBoxField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/)를 생성합니다.
1. 숨겨진 필드를 문서의 [`Form`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/) 컬렉션에 추가합니다.
1. 보이지 않는 [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/)를 생성합니다.
1. 마우스 동작(`on_enter`, `on_exit`)을 [`HideAction`](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/hideaction/)을 사용하여 숨겨진 필드를 보이거나 숨기도록 지정합니다.
1. 최종 문서를 저장합니다.

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

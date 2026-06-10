---
title: Python에서 PDF 텍스트에 툴팁 추가
linktitle: PDF 툴팁
type: docs
weight: 20
url: /ko/python-net/pdf-tooltip/
description: Python에서 PDF 문서의 텍스트 조각에 툴팁을 추가하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 텍스트 조각에 대화형 도구 설명 추가
Abstract: 이 문서에서는.NET을 통해 파이썬용 Aspose.PDF 를 사용하여 PDF 텍스트에 대화형 도움말을 추가하는 두 가지 Python 예제를 제공합니다.첫 번째 예제에서는 보이지 않는 `ButtonField` 요소를 배치하고 `alternate_name`을 설정하여 일치하는 텍스트 조각에 툴팁을 추가합니다.두 번째 예제에서는 'HideAction' 이벤트를 보이지 않는 'ButtonField'에 와이어링하여 가리키면 나타나는 숨겨진 'TextBoxField'를 만듭니다.
---

## PDF에서 검색한 텍스트에 툴팁 추가

이 코드 스니펫은 보이지 않는 것을 오버레이하는 방법을 보여줍니다. [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) 특정 요소 [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) PDF의 개체를 마우스로 가리키면 툴팁이 표시됩니다.를 사용한 짧은 도구 설명 메시지와 긴 도구 설명 메시지를 모두 지원합니다. `alternate_name` 의 재산 `ButtonField`.

마우스오버 도움말, 인라인 설명 또는 문맥 메모를 추가하여 PDF 텍스트를 보다 인터랙티브하게 만들어야 할 때 이 페이지를 사용하십시오.

1. 새 만들기 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 초기 문서를 저장합니다.
1. PDF 문서를 다시 엽니다.
1. 를 사용하여 대상 텍스트 검색 [`TextFragmentAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/).
1. 보이지 않는 항목 추가 [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) 짧은 툴팁과 함께.
1. 두 번째 대상 텍스트를 검색합니다.
1. 보이지 않는 항목 추가 [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) 일치하는 프래그먼트 위에 긴 툴팁이 있습니다.
1. 최종 문서를 저장합니다.

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

## PDF에서 마우스 오버 시 나타나는 숨겨진 텍스트 블록 만들기

PDF 문서에 대화형 플로팅 텍스트를 추가합니다.보이지 않는 부분을 오버레이합니다. [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) 대상 문구에 숨겨져 있는 문장을 보여줍니다. [`TextBoxField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/) 사용자가 그 위에 마우스를 가져갈 때이 기법은 상황에 맞는 도움말, 주석 또는 동적 콘텐츠 프레젠테이션에 적합합니다.

1. 새 PDF 문서 만들기
1. 대화형 설정을 위해 다시 열 수 있도록 PDF를 저장합니다.
1. PDF 문서를 다시 엽니다.
1. 를 사용하여 대상 텍스트 찾기 [`TextFragmentAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/).
1. 숨겨진 항목 만들기 [`TextBoxField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/).
1. 문서에 숨겨진 필드 추가 [`Form`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/) 컬렉션.
1. 보이지 않는 것 만들기 [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/).
1. 마우스 액션 지정 (`on_enter`, `on_exit`) 사용 [`HideAction`](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/hideaction/) 숨겨진 필드를 표시하거나 숨길 수 있습니다.
1. 최종 문서를 저장합니다.

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

## 관련 텍스트 주제

- [Python을 사용하여 PDF에서 텍스트 작업하기](/pdf/ko/python-net/working-with-text/)
- [파이썬에서 PDF 텍스트 레이아웃에 플로팅 박스 사용하기](/pdf/ko/python-net/floating-box/)
- [파이썬에서 PDF 텍스트 검색 및 추출](/pdf/ko/python-net/search-and-get-text-from-pdf/)
- [PDF에 텍스트 추가](/pdf/ko/python-net/add-text-to-pdf-file/)
---
title: 파이썬에서 PDF 액션으로 작업하기
linktitle: 액션
type: docs
weight: 20
url: /ko/python-net/actions/
description: Python을 사용하여 PDF 파일에서 문서, 페이지 및 양식 작업을 추가, 업데이트 및 제거하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Python에서 PDF 파일에 문서, 페이지 및 양식 액션 추가
Abstract: 이 문서에서는 문서 수준, 페이지 수준 및 양식 수준 상호 작용을 포함하여 Aspose.PDF 라이브러리를 사용하여 PDF 문서에서 작업을 수행하는 방법을 살펴봅니다.PDF 액션은 사용자 이벤트에 응답하여 탐색, JavaScript 실행, 멀티미디어 재생, 양식 제출 등을 가능하게 하는 사전 정의되거나 사용자 정의 가능한 트리거입니다.이 가이드에서는 문서 이벤트에서 URL 열기, 페이지별 탐색 또는 확대/축소 효과 만들기, 인쇄 및 탐색을 위한 대화형 버튼 추가, 양식 요소를 동적으로 숨기고, 양식 데이터를 웹 엔드포인트에 제출하는 등의 작업을 추가, 사용자 지정 및 제거하는 방법을 설명합니다.자세한 Python 코드 예제를 통해 독자는 뷰어 호환성 고려 사항을 이해하면서 PDF 상호 작용을 향상시키고 워크플로를 간소화하고 PDF를 외부 시스템과 통합하는 방법을 배웁니다.
---

PDF의 동작은 사용자 상호 작용이나 문서 이벤트에 의해 트리거되는 사전 정의된 작업입니다.다음과 같은 용도로 사용할 수 있습니다.

- 특정 페이지 또는 외부 파일로 이동
- 웹 링크 열기
- 멀티미디어 콘텐츠 재생
- 자바스크립트 실행
- 양식 제출 또는 재설정
- 필드 표시/숨기기
- 확대/축소 수준 또는 보기 모드 변경

거의 모든 작업은 기본 제공 매개 변수를 사용하지만 일부 작업은 사용자 지정할 수 있습니다.자바스크립트 액션을 예로 들 수 있습니다.

## PDF 실행 작업 추가

Python과 Aspose.PDF 를 사용하여 PDF 문서에 자바스크립트 기반 실행 액션을 추가합니다.열기, 저장 및 인쇄와 같은 주요 문서 이벤트에 작업을 할당하여 지원되는 PDF 뷰어에서 해당 이벤트가 발생할 때 URL이 자동으로 실행되도록 합니다.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_launch_actions(infile, outfile):
    """Add JavaScript launch actions for document events.

    Adds JavaScript actions that launch URLs when specific document events occur:
    - On document open: launches http://localhost:3000/open
    - Before saving: launches http://localhost:3000/save
    - Before printing: launches http://localhost:3000/print

    Args:
        infile (str): Path to the input PDF file.
        outfile (str): Path to save the output PDF with document actions.

    Returns:
        None

    Example:
        >>> add_launch_actions("sample_data/input/add_launch_actions_in.pdf", "sample_data/output/add_launch_actions_out.pdf")

    Notes:
        - Uses `ap.annotations.JavascriptAction` with `app.launchURL()`.
        - URLs are opened in the default browser depending on viewer support.
    """

    document = ap.Document(infile)

    # Add JavaScript actions for document events
    document.open_action = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/open');"
    )
    document.actions.before_saving = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/save');"
    )
    document.actions.before_printing = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/print');"
    )

    document.save(outfile)
```

## PDF 문서에서 작업 제거

액션을 정리 (또는 제거) 하려면 handler를 다음으로 설정하십시오. `None`.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def remove_page_actions(infile, outfile):
    document = ap.Document(infile)

    if len(document.pages) < 3:
        print("Error: The document does not have at least 3 pages.")
        return

    page = document.pages[3]
    page.actions.remove_actions()

    document.save(outfile)
```

## PDF 문서의 페이지에 작업 추가

페이지에도 비슷한 트리거가 제공됩니다. `on_open`, `on_close`.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_page_actions(infile, outfile):
    document = ap.Document(infile)

    if len(document.pages) < 3:
        print("Error: The document does not have at least 3 pages.")
        return

    page = document.pages[3]

    # Add GoTo action on page open - navigate to top of page
    action = ap.annotations.GoToAction(page)
    action.destination = ap.annotations.XYZExplicitDestination(
        page, 0, page.page_info.height, 1
    )
    page.actions.on_open = action

    # Add JavaScript action on page close
    page.actions.on_close = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/page/3');"
    )

    document.save(outfile)
```

## 아크로폼에서의 액션

### 내비게이션 액션 사용

PDF 표준은 특정 명명된 작업 세트를 제공합니다.이러한 액션의 의미는 이름에 따라 결정됩니다.
다음 코드에서는 탐색을 위한 액션을 사용합니다.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_navigation_buttons(infile, outfile):
    # Configuration for each navigation button
    button_config = [
        ("First Page", 10.0, PredefinedAction.FIRST_PAGE, lambda p, t: p == 1),
        ("Previous Page", 120.0, PredefinedAction.PREV_PAGE, lambda p, t: p == 1),
        ("Next Page", 230.0, PredefinedAction.NEXT_PAGE, lambda p, t: p == t),
        ("Last Page", 340.0, PredefinedAction.LAST_PAGE, lambda p, t: p == t),
    ]

    document = ap.Document(infile)
    total_pages = len(document.pages)

    # Add navigation buttons to each page
    for page in document.pages:
        for name, x_pos, action, is_readonly_fn in button_config:
            # Create button rectangle
            rect = Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
            button = ButtonField(page, rect)
            button.partial_name = name
            button.value = name
            button.characteristics.border = ap.Color.red.to_rgb()
            button.characteristics.background = ap.Color.orange.to_rgb()
            # Disable button when not applicable
            button.read_only = is_readonly_fn(page.number, total_pages)
            button.actions.on_release_mouse_btn = NamedAction(action)
            document.form.add(button)

    document.save(outfile)
```

이 코드는 PDF 문서의 모든 페이지에 탐색 버튼을 추가하여 사용자가 페이지 사이를 쉽게 이동할 수 있도록 합니다.먼저 도우미 메서드를 사용하여 입력 및 출력 파일의 전체 파일 경로를 결정합니다.button_config 목록은 네 가지 유형의 탐색 버튼 (첫 페이지, 이전 페이지, 다음 페이지, 마지막 페이지) 을 가로 위치, 트리거하는 사전 정의된 탐색 작업, 지정된 페이지에서 각 버튼이 읽기 전용이어야 하는지 여부를 결정하는 람다 함수를 정의합니다 (예: 첫 번째 페이지에서 “첫 페이지” 및 “이전 페이지” 버튼은 읽기 전용이어야 함).

그러면 코드가 PDF를 로드하고 각 페이지를 반복합니다.모든 페이지에서 버튼 구성을 반복하여 각 버튼에 사각형 영역을 만들고 해당 위치에 ButtonField를 인스턴스화합니다.각 버튼에는 이름이 지정되고, 읽기 전용 상태는 현재 페이지를 기준으로 설정되며, 클릭 동작은 해당 탐색 동작에 할당됩니다.그러면 단추가 PDF 양식 필드에 추가됩니다.

모든 페이지에 모든 버튼을 추가하면 수정된 문서가 저장됩니다.이 과정에서 오류가 발생하면 오류를 발견하여 인쇄합니다.이 방법을 사용하면 모든 페이지에 일관된 탐색 컨트롤 세트를 사용할 수 있으므로 여러 페이지로 구성된 PDF의 유용성이 향상됩니다.한 가지 미묘한 점은 is_readonly_fn 람다를 사용하여 의미가 없을 때 탐색 버튼을 비활성화하는 것입니다 (예: 마지막 페이지의 “다음 페이지”). 이렇게 하면 사용자 혼동을 방지하는 데 도움이 됩니다.

### 인쇄 작업 사용

PDF 양식을 사용할 때 이러한 PDF 문서를 인쇄해야 하는 경우가 종종 있습니다.이 작업은 PDF Reader를 사용하여 수행할 수 있지만 특수 단추를 사용하여 문서에서 직접 수행하는 것이 더 편리한 경우도 있습니다.

사실 이것은 명명된 액션을 사용하는 방법의 또 다른 예입니다.다음을 사용할 것입니다. `PredefinedAction.FILE_PRINT` (파일->인쇄 메뉴 항목 사용 시뮬레이션). 하지만 다음을 사용할 수도 있습니다. `PredefinedAction.PRINT` 또는 `PredefinedAction.PRINT_DIALOG`, 자신의 목적에 따라.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_named_action_print(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    # Create print button with specific dimensions and position
    rect = Rectangle(10, 10, 100, 40, True)
    print_button = ButtonField(page, rect)
    print_button.partial_name = "printButton"
    print_button.value = "Print"
    print_button.actions.on_release_mouse_btn = NamedAction(PredefinedAction.FILE_PRINT)

    # Add border for better visibility
    border = ap.annotations.Border(print_button)
    border.width = 1
    print_button.border = border

    # Add button to the form on page 1
    document.form.add(print_button, 1)
    document.save(outfile)
```

이 코드 스니펫은 PDF 문서의 첫 페이지에 “인쇄” 버튼을 추가하는 방법을 보여줍니다.먼저 지정된 입력 파일 경로에서 PDF를 로드하고 첫 페이지 (document.pages [1]) 를 선택합니다.

직사각형 영역은 페이지에서의 버튼 위치 및 크기에 맞게 정의됩니다.그러면 이 위치에 “PrintButton”이라는 이름이 지정된 ButtonField가 생성되고 표시 값이 “인쇄”로 설정됩니다.버튼을 클릭하면 (특히 마우스 버튼을 놓으면) 미리 정의된 “파일 인쇄” 동작이 트리거되어 PDF 뷰어에게 인쇄 대화 상자를 열라는 메시지가 표시되도록 버튼이 구성됩니다.

단추의 모양을 향상시키기 위해 테두리를 만들어 단추에 할당하고 너비를 1단위로 설정합니다.그러면 첫 페이지의 PDF 양식 필드에 버튼이 추가됩니다.마지막으로 수정된 문서가 출력 파일 경로에 저장됩니다.이 방법을 사용하면 PDF 내에서 직접 문서를 인쇄할 수 있는 편리한 방법을 사용할 수 있습니다.참고로 이 기능의 효율성은 대화형 양식 필드와 사전 정의된 작업에 대한 PDF 뷰어의 지원에 따라 달라집니다.

### 숨기기 액션 사용

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_named_action_hide(infile, outfile):
    document = ap.Document(infile)
    # Collect all checkbox fields in the document
    checkboxes = [
        field for field in document.form if is_assignable(field, CheckboxField)
    ]

    # Create the hide button
    rect = Rectangle(10, 410, 140, 440, True)
    hide_button = ButtonField(document.pages[1], rect)
    hide_button.partial_name = "HideButton"
    hide_button.value = "Hide Checkboxes"

    # Add HideAction to button - will hide all checkboxes when clicked
    hide_button.actions.on_release_mouse_btn = HideAction(checkboxes, True)

    # Add button to the form on page 1
    document.form.add(hide_button, 1)

    # Save the modified PDF
    document.save(outfile)
```

이 코드 스니펫은 PDF의 첫 페이지에 버튼을 추가합니다. 이 버튼을 클릭하면 문서의 모든 확인란 필드가 숨겨집니다.먼저 도우미 메서드를 사용하여 전체 입력 및 출력 파일 경로를 확인합니다.PDF가 로드되고 인스턴스의 양식 필드를 필터링하여 모든 확인란 필드를 수집합니다. `ap.CheckboxField`.

페이지 상단 근처의 새 버튼 위치에 대해 사각형 영역이 정의됩니다.이 위치에 “HideButton”이라는 이름과 “확인란 숨기기”라는 레이블이 붙은 버튼 필드가 생성됩니다.버튼을 클릭하면 (마우스 버튼을 놓을 때) 수집된 모든 체크상자를 숨기는 HideAction이 트리거되도록 구성되어 있습니다.

그러면 첫 페이지의 양식 필드에 단추가 추가되고 수정된 PDF가 출력 파일에 저장됩니다.이 과정에서 오류가 발생하면 해당 오류가 발견되어 인쇄됩니다.이 기능을 통해 사용자는 PDF의 모든 확인란을 빠르게 숨길 수 있으며, 이는 문서의 모양이나 작업 흐름을 사용자 지정하는 데 유용할 수 있습니다.

### 제출 작업 적용

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_submit_action(infile, outfile):
    document = ap.Document(infile)

    # Create the submit action
    submit_action = SubmitFormAction()
    submit_action.url = ap.FileSpecification("http://localhost:3000/submit")
    submit_action.flags = (
        SubmitFormAction.EXPORT_FORMAT | SubmitFormAction.SUBMIT_COORDINATES
    )

    # Create the submit button
    rect = Rectangle(10, 10, 100, 40, True)
    submit_button = ButtonField(document.pages[1], rect)
    submit_button.partial_name = "SubmitButton"
    submit_button.value = "Submit"
    submit_button.actions.on_release_mouse_btn = submit_action

    # Add the button to the form on page 1
    document.form.add(submit_button, 1)

    # Save the document
    document.save(outfile)
```

이 함수는 PDF 양식의 첫 페이지에 “제출” 버튼을 추가하여 사용자가 양식 데이터를 지정된 웹 엔드포인트에 제출할 수 있도록 합니다.먼저 입력 및 출력 PDF 파일의 전체 경로를 구성한 다음 Aspose.PDF 라이브러리를 사용하여 입력 PDF를 로드합니다.

A `SubmitFormAction` 버튼을 클릭할 때의 동작을 정의하기 위해 생성됩니다.액션의 URL은 를 사용하여 설정됩니다. `FileSpecification` 가리키고 있습니다 http://localhost:3000/submit, 즉, 양식 데이터가 이 URL로 전송됩니다.flags 속성은 결합됩니다. `EXPORT_FORMAT` 과 `SUBMIT_COORDINATES`양식 데이터를 표준 형식으로 내보내고 버튼 클릭 좌표가 제출 자료에 포함되도록 합니다.

직사각형 영역은 페이지에서의 버튼 위치 및 크기에 맞게 정의됩니다.첫 페이지의 이 위치에 “SubmitButton”이라는 이름이 지정된 버튼 필드가 생성되고 표시 값이 “제출”로 설정됩니다.제출 액션은 버튼의 마우스 릴리즈 이벤트에 할당되므로 사용자가 버튼을 클릭하면 액션이 트리거됩니다.

마지막으로 첫 페이지의 양식 필드에 버튼이 추가되고 수정된 PDF가 출력 파일에 저장됩니다.이 과정에서 오류가 발생하면 해당 오류가 발견되어 인쇄됩니다.이 방법은 PDF 사용자가 양식 데이터를 서버 엔드포인트에 직접 제출할 수 있는 사용자 친화적인 방법을 제공합니다.

## 관련 내비게이션 주제

- [Python을 사용한 PDF 탐색 및 상호 작용](/pdf/ko/python-net/navigation-and-interaction/)
- [Python을 사용하여 PDF에서 북마크로 작업하기](/pdf/ko/python-net/bookmarks/)
- [Python을 사용하여 PDF에서 링크 작업하기](/pdf/ko/python-net/links/)

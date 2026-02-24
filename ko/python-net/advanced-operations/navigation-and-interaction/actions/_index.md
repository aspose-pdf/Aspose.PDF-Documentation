---
title: PDF 문서에서 액션 작업
linktitle: 액션
type: docs
weight: 20
url: /ko/python-net/actions/
description: Python과 Aspose.PDF를 사용하여 저자 및 제목과 같은 PDF 메타데이터를 추출하고 관리하는 방법을 살펴봅니다.
lastmod: "2025-07-10"
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Python을 사용한 PDF 문서에서 액션 처리
Abstract: 이 기사에서는 Aspose.PDF 라이브러리를 사용하여 PDF 문서에서 액션을 다루는 방법을 살펴봅니다. 여기에는 문서 수준, 페이지 수준 및 양식 수준 상호작용이 포함됩니다. PDF 액션은 사용자 이벤트에 반응하는 사전 정의되거나 사용자 정의 가능한 트리거로, 네비게이션, JavaScript 실행, 멀티미디어 재생, 양식 제출 등 다양한 기능을 제공합니다. 이 가이드는 문서 이벤트 시 URL 열기, 페이지별 네비게이션 및 줌 효과 생성, 인쇄 및 네비게이션을 위한 인터랙티브 버튼 추가, 양식 요소 동적 숨기기, 웹 엔드포인트로 양식 데이터 제출 등 액션을 추가, 맞춤화 및 제거하는 방법을 보여줍니다. 상세한 Python 코드 예제를 통해 독자는 PDF 인터랙티브성을 향상하고 작업 흐름을 간소화하며, PDF를 외부 시스템과 통합하는 방법을 배우고 뷰어 호환성 고려 사항을 이해하게 됩니다.
---

PDF의 액션은 사용자 상호작용이나 문서 이벤트에 의해 트리거되는 사전 정의된 작업입니다. 이를 사용하여 다음을 수행할 수 있습니다:

- 특정 페이지 또는 외부 파일로 이동
- 웹 링크 열기
- 멀티미디어 콘텐츠 재생
- JavaScript 실행
- 양식 제출 또는 재설정
- 필드 표시/숨기기
- 줌 레벨 또는 보기 모드 변경

거의 모든 액션은 기본 제공 파라미터를 사용하지만, 사용자 정의할 수 있는 경우도 있습니다. 예를 들어 JavaScript 액션이 있습니다.

## 문서 수준 액션

### PDF 문서에 액션 추가

PDF 문서는 문서 열기 시 또는 특정 이벤트에 응답하여 실행되는 코드를 포함한 여러 문서 수준 액션을 지원합니다. 열기 시 액션에는 `open_action` 속성을 사용하고, 기타 액션은 `actions` 컬렉션에서 관리합니다.

`open_action`을 어떻게 사용하는지 살펴보겠습니다.

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

document = ap.Document(path_infile)
document.open_action = ap.annotations.JavascriptAction(
    "app.launchURL('http://localhost:3000/open');"
)
document.save(path_outfile)
```

이 예제에서는 `app` 객체의 `launchURL` 메서드를 호출하여 웹 사이트를 엽니다(데모 목적).

다른 액션도 같은 방식으로 추가할 수 있지만 약간의 변경이 필요합니다:

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

document = ap.Document(path_infile)
document.actions.before_saving = ap.annotations.JavascriptAction(
    "app.launchURL('http://localhost:3000/save');"
)
document.actions.before_printing = ap.annotations.JavascriptAction(
    "app.launchURL('http://localhost:3000/print');"
)
```

다음 이벤트에 대한 액션을 추가할 수 있습니다: `before_saving`, `before_printing`, `before_closing`, `after_saving`, `after_printing`.

이 코드 조각은 PDF의 다양한 문서 수준 이벤트에 JavaScript 액션을 연결하는 방법을 보여줍니다. 먼저 지정된 입력 파일 경로에서 기존 PDF 문서를 로드합니다. `document.open_action` 속성은 문서가 열릴 때 URL을 실행하는 JavaScript 액션으로 설정되어, PDF 뷰어가 사용자의 브라우저에서 `http://localhost:3000/open`을 열도록 합니다.

다음으로, 문서의 `before_saving` 및 `before_printing` 이벤트에 두 개의 추가 JavaScript 액션을 할당합니다. 이러한 액션은 사용자가 문서를 저장하거나 인쇄하려 할 때 각각 트리거되어 브라우저에서 서로 다른 URL(`/save` 또는 `/print`)을 열게 됩니다. 이는 사용자 상호작용을 추적하거나 웹 기반 워크플로와 통합하는 데 유용할 수 있습니다.

### PDF 문서에서 액션 제거

액션을 정리(또는 제거)하려면 핸들러를 `None`으로 설정하면 됩니다.

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

document = ap.Document(path_infile)
document.open_action = None
document.actions.before_saving = None
document.actions.before_printing = None
document.save(path_outfile)
```

## 페이지 수준 액션

### PDF 문서 페이지에 액션 추가

페이지에 대해서도 유사한 트리거가 제공됩니다: `on_open`, `on_close`.

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...

def add_page_actions(self, infile, outfile):
    """
    Add actions to the third page of the PDF.

    Adds two actions to page 3:
    - On page open: Navigate to the top of the page with specific zoom
    - On page close: Launch a URL with page-specific information

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Raises:
        ValueError: If document has fewer than 3 pages

    Example:
        >>> actions.add_page_actions("multipage.pdf", "page_actions.pdf")
    """
    path_infile, path_outfile = self._get_file_paths(infile, outfile)

    document = ap.Document(path_infile)

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

    document.save(path_outfile)

```

이 페이지에 두 개의 액션을 추가합니다. 첫 번째는 페이지가 열릴 때 트리거되는 "GoTo" 액션을 생성합니다. 이 액션은 명시적인 목적지를 사용해 특정 줌 레벨에서 페이지의 좌측 상단으로 이동합니다. 두 번째는 페이지가 닫힐 때 실행되는 JavaScript 액션을 연결하여 PDF 뷰어가 브라우저에서 특정 URL을 열도록 합니다. 마지막으로 수정된 문서를 지정된 출력 경로에 저장합니다.

주의해야 할 미묘한 점은 페이지 인덱싱이며, 잘못된 인덱스를 사용하면 예기치 않은 동작이나 오류가 발생할 수 있습니다. 또한 PDF에서 JavaScript 액션 사용은 모든 PDF 뷰어에서 지원되지 않을 수 있어 이 기능이 모든 환경에서 동작하지 않을 수도 있습니다.

### PDF 페이지에서 액션 제거

페이지에서 액션을 제거하려면 `remove_actions`를 사용합니다.

```python

import aspose.pdf as ap
from os import path

document = ap.Document(path_infile)

if len(document.pages) < 3:
    print("Error: The document does not have at least 3 pages.")
    return

page = document.pages[3]
page.actions.remove_actions()

document.save(path_outfile)

```

## AcroForms에서 액션

### 네비게이션 액션 사용

PDF 표준은 특정 이름이 지정된 액션 집합을 제공합니다. 이러한 액션의 의미는 이름에 따라 결정됩니다.
다음 코드에서는 네비게이션을 위한 액션을 사용할 것입니다.

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...

def add_navigation_buttons(self, infile, outfile):
    """
    Add navigation buttons to each page of the PDF.

    Creates four navigation buttons on each page:
    - First Page: Navigate to the first page
    - Previous Page: Navigate to the previous page
    - Next Page: Navigate to the next page
    - Last Page: Navigate to the last page

    Buttons are automatically disabled when not applicable (e.g.,
    "Previous" is disabled on the first page).

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Example:
        >>> actions.add_navigation_buttons("multipage.pdf", "nav_buttons.pdf")
    """
    path_infile, path_outfile = self._get_file_paths(infile, outfile)

    # Configuration for each navigation button
    button_config = [
        ("First Page", 10.0, PredefinedAction.FIRST_PAGE, lambda p, t: p == 1),
        ("Previous Page", 120.0, PredefinedAction.PREV_PAGE, lambda p, t: p == 1),
        ("Next Page", 230.0, PredefinedAction.NEXT_PAGE, lambda p, t: p == t),
        ("Last Page", 340.0, PredefinedAction.LAST_PAGE, lambda p, t: p == t),
    ]

    try:
        document = ap.Document(path_infile)
        total_pages = len(document.pages)

        # Add navigation buttons to each page
        for page in document.pages:
            page_number = page.number

            for name, x_pos, action, is_readonly_fn in button_config:
                # Create button rectangle
                rect = Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
                button = ButtonField(page, rect)
                button.partial_name = name

                # Disable button when not applicable
                button.read_only = is_readonly_fn(page_number, total_pages)
                button.actions.on_release_mouse_btn = NamedAction(action)

                document.form.add(button)

        document.save(path_outfile)

    except Exception as e:
        print(f"Error adding navigation buttons: {e}")

```

이 코드는 PDF 문서의 모든 페이지에 네비게이션 버튼을 추가하여 사용자가 페이지 간 이동을 쉽게 할 수 있게 합니다. 먼저 헬퍼 메서드를 사용해 입력 및 출력 파일의 전체 경로를 결정합니다. `button_config` 리스트는 네 가지 유형의 네비게이션 버튼—첫 페이지, 이전 페이지, 다음 페이지, 마지막 페이지—를 정의하며, 각 버튼의 수평 위치, 트리거되는 사전 정의된 네비게이션 액션, 그리고 해당 페이지에서 버튼을 읽기 전용으로 할지 여부를 결정하는 람다 함수를 포함합니다(예: 첫 페이지에서는 "First Page"와 "Previous Page" 버튼이 읽기 전용).

그 후 코드는 PDF를 로드하고 각 페이지를 순회합니다. 각 페이지마다 버튼 구성 목록을 반복하여 각 버튼에 대한 사각형 영역을 만들고 해당 위치에 ButtonField를 인스턴스화합니다. 각 버튼에 이름을 부여하고 현재 페이지에 따라 읽기 전용 상태를 설정한 뒤, 클릭 액션을 해당 네비게이션 액션에 할당합니다. 마지막으로 버튼을 PDF 양식 필드에 추가합니다.

모든 페이지에 모든 버튼을 추가한 후 수정된 문서를 저장합니다. 이 과정에서 오류가 발생하면 잡혀서 출력됩니다. 이 방법은 모든 페이지에 일관된 네비게이션 컨트롤을 제공하여 다중 페이지 PDF의 사용성을 향상시킵니다. 미묘한 점은 `is_readonly_fn` 람다를 사용해 의미가 없을 때(예: 마지막 페이지의 "Next Page") 네비게이션 버튼을 비활성화함으로써 사용자 혼란을 방지한다는 점입니다.

### 인쇄 액션 사용

PDF 양식을 사용할 때 종종 해당 PDF 문서를 인쇄해야 할 필요가 있습니다. 이 액션은 PDF 리더를 통해 수행할 수 있지만, 특수 버튼을 사용해 문서 자체에서 직접 인쇄하는 것이 더 편리할 때도 있습니다.

사실 이것은 이름이 지정된 액션을 사용하는 또 다른 예시입니다. `PredefinedAction.FILE_PRINT`(File->Print 메뉴 아이템을 시뮬레이션) 를 사용할 것이며, 필요에 따라 `PredefinedAction.PRINT` 또는 `PredefinedAction.PRINT_DIALOG`도 사용할 수 있습니다.

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...

def add_named_action_print(self, infile, outfile):
    """
    Add a print button to the first page of the PDF.

    Creates a button labeled "Print" that triggers the system print dialog
    when clicked. The button is positioned at the bottom-left corner of
    the first page with a 1-pixel border.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Example:
        >>> actions.add_named_action_print("input.pdf", "output.pdf")
    """
    path_infile, path_outfile = self._get_file_paths(infile, outfile)

    document = ap.Document(path_infile)
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
    document.save(path_outfile)

```

이 코드 스니펫은 PDF 문서의 첫 페이지에 "Print" 버튼을 추가하는 방법을 보여줍니다. 지정된 입력 파일 경로에서 PDF를 로드하고 첫 페이지(document.pages[1])를 선택하는 것으로 시작합니다.

버튼의 위치와 크기를 위한 직사각형 영역이 페이지에 정의됩니다. 그런 다음 이 위치에 ButtonField가 생성되고 이름은 "printButton"으로 지정되며 표시값은 "Print"로 설정됩니다. 버튼은 클릭될 때(특히 마우스 버튼이 떼어질 때) 사전 정의된 "Print File" 동작을 트리거하도록 구성되어 PDF 뷰어가 인쇄 대화 상자를 열도록 합니다.

버튼의 외관을 향상시키기 위해 테두리를 만들고 버튼에 할당하며, 너비를 1 단위로 설정합니다. 그런 다음 버튼을 첫 페이지의 PDF 양식 필드에 추가합니다. 마지막으로 수정된 문서를 출력 파일 경로에 저장합니다. 이 방법은 사용자가 PDF 내부에서 직접 문서를 인쇄할 수 있는 편리한 방법을 제공합니다. 이 기능의 효과는 PDF 뷰어가 대화형 양식 필드와 사전 정의된 동작을 지원하는지 여부에 따라 달라집니다.

### Hide 동작 사용

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...

def add_named_action_hide(self, infile, outfile):
    """
    Add a hide button that toggles visibility of all checkbox fields.

    Creates a button labeled "Hide Checkboxes" that can hide or show
    all checkbox fields in the document. Useful for forms with many
    checkboxes that might clutter the interface.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Example:
        >>> actions.add_named_action_hide("form.pdf", "form_with_hide.pdf")
    """
    path_infile, path_outfile = self._get_file_paths(infile, outfile)

    try:
        document = ap.Document(path_infile)
        # Collect all checkbox fields in the document
        checkboxes = [field for field in document.form if isinstance(field, ap.CheckboxField)]

        # Create the hide button
        rect = Rectangle(10, 510, 100, 540)
        hide_button = ButtonField(document.pages[1], rect)
        hide_button.partial_name = "HideButton"
        hide_button.value = "Hide Checkboxes"

        # Add HideAction to button - will hide all checkboxes when clicked
        hide_button.actions.on_release_mouse_btn = ap.HideAction(checkboxes, True)

        # Add button to the form on page 1
        document.form.add(hide_button, 1)

        # Save the modified PDF
        document.save(path_outfile)

    except Exception as e:
        print(f"Error adding hide button: {e}")

```

이 코드 스니펫은 PDF 첫 페이지에 버튼을 추가하며, 클릭하면 문서의 모든 체크박스 필드를 숨깁니다. 헬퍼 메서드를 사용하여 전체 입력 및 출력 파일 경로를 확인하는 것으로 시작합니다. PDF를 로드하고, 양식 필드들을 `ap.CheckboxField` 인스턴스로 필터링하여 모든 체크박스 필드를 수집합니다.

새 버튼의 위치를 페이지 상단 근처에 지정하기 위해 직사각형 영역이 정의됩니다. 이 위치에 ButtonField가 생성되고 이름은 "HideButton"이며 라벨은 "Hide Checkboxes"로 지정됩니다. 버튼은 클릭될 때(마우스 버튼이 떼어질 때) 수집된 모든 체크박스를 숨기는 HideAction을 트리거하도록 구성됩니다.

버튼은 첫 페이지의 양식 필드에 추가되고 수정된 PDF는 출력 파일에 저장됩니다. 이 과정에서 오류가 발생하면 잡혀서 출력됩니다. 이 기능은 사용자가 PDF의 모든 체크박스를 빠르게 숨길 수 있는 방법을 제공하며, 문서의 외관이나 워크플로를 맞춤화하는 데 유용할 수 있습니다.

### Submit 액션 적용

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...

def add_submit_action(self, infile, outfile):
    """
    Submit form.

    Parameters:
    - infile (str): The name of the input PDF file.
    - outfile (str): The name of the output PDF file.
    """
    path_infile = self.dataDir + infile
    path_outfile = self.dataDir + outfile

    try:
        document = ap.Document(path_infile)

        # Create the submit action
        submit_action = ap.SubmitFormAction()
        submit_action.url = FileSpecification("http://localhost:3000/submit")
        submit_action.flags = (
            SubmitFormAction.EXPORT_FORMAT | SubmitFormAction.SUBMIT_COORDINATES
        )

        # Create the submit button
        rect = Rectangle(10, 10, 100, 40)
        submit_button = ButtonField(document.pages[1], rect)
        submit_button.partial_name = "SubmitButton"
        submit_button.value = "Submit"
        submit_button.actions.on_release_mouse_btn = submit_action

        # Add the button to the form on page 1
        document.form.add(submit_button, 1)

        # Save the document
        document.save(path_outfile)

    except Exception as e:
        print(f"Error adding submit button: {e}")

```

이 함수는 PDF 양식의 첫 페이지에 "Submit" 버튼을 추가하여 사용자가 지정된 웹 엔드포인트로 양식 데이터를 제출할 수 있게 합니다. 입력 및 출력 PDF 파일의 전체 경로를 구성한 후, Aspose.PDF 라이브러리를 사용하여 입력 PDF를 로드합니다.

`SubmitFormAction`이 생성되어 버튼 클릭 시 동작을 정의합니다. 액션의 url은 http://localhost:3000/submit을 가리키는 `FileSpecification`을 사용하여 설정되며, 이는 양식 데이터가 해당 URL로 전송됨을 의미합니다. flags 속성은 `EXPORT_FORMAT`와 `SUBMIT_COORDINATES`를 결합하여 양식 데이터가 표준 형식으로 내보내지고 버튼 클릭 좌표가 제출에 포함되도록 합니다.

버튼의 위치와 크기를 위한 직사각형 영역이 페이지에 정의됩니다. 첫 페이지의 해당 위치에 ButtonField가 생성되고 이름은 "SubmitButton"이며 표시값은 "Submit"으로 설정됩니다. submit 액션은 버튼의 마우스 릴리즈 이벤트에 할당되어 사용자가 버튼을 클릭할 때 액션이 트리거됩니다.

마지막으로 버튼은 첫 페이지의 양식 필드에 추가되고 수정된 PDF는 출력 파일에 저장됩니다. 이 과정에서 오류가 발생하면 잡혀서 출력됩니다. 이 방법은 PDF 사용자가 양식 데이터를 서버 엔드포인트로 직접 제출할 수 있는 사용자 친화적인 방법을 제공합니다.


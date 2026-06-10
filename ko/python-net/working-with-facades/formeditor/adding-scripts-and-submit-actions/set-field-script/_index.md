---
title: 필드 스크립트 설정
type: docs
weight: 30
url: /ko/python-net/set-field-script/
description: 이 코드 스니펫은 Python용 Aspose.PDF 를 사용하여 PDF 문서의 양식 필드에 JavaScript 작업을 할당하는 방법을 보여줍니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 양식 필드에 대한 자바스크립트 액션 설정하기
Abstract: 이 문서에서는 PDF 문서를 열고, 양식 필드에 JavaScript 코드를 할당하고, FormEditor 클래스를 사용하여 스크립트를 업데이트하고, 수정된 파일을 저장하는 방법을 설명합니다.이 예제에서는 기존 스크립트를 재정의하여 양식 필드의 동작을 수정하는 방법을 보여줍니다.
---

대화형 PDF 양식에서는 경고 표시, 입력 확인 또는 동적 양식 동작 트리거와 같은 작업을 수행하기 위해 JavaScript를 사용하는 경우가 많습니다.개발자는 Aspose.PDF for Python을 사용하여 이러한 스크립트를 프로그래밍 방식으로 관리할 수 있습니다.

이 예제에서는 먼저 필드에 JavaScript 작업을 추가한 다음 'set_field_script' 메서드를 사용하여 이 작업을 다른 스크립트로 바꿉니다.이 방법을 통해 개발자는 버튼이나 입력 필드와 같은 PDF 양식 요소의 대화형 동작을 제어하거나 업데이트할 수 있습니다.

이 예제에서 사용된 양식 필드의 이름은 'Script_Demo_Button'으로, 일반적으로 트리거 시 할당된 스크립트를 실행하는 버튼을 나타냅니다.

를 사용하여 [폼 에디터](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 에서 수업 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) 모듈을 통해 개발자는 양식 필드와 관련된 JavaScript 작업을 프로그래밍 방식으로 관리할 수 있습니다.

1. 기존 PDF 양식 문서를 엽니다.
1. 양식 필드에 자바스크립트 액션을 추가합니다.
1. 자바스크립트 액션을 새 스크립트로 설정 (바꾸기) 합니다.
1. 수정된 PDF 문서를 저장합니다.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_script(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Add JavaScript action to the field
    form_editor.add_field_script(
        "Script_Demo_Button", "app.alert('Script 1 has been executed');"
    )

    # Set JavaScript action for the field
    form_editor.set_field_script(
        "Script_Demo_Button", "app.alert('Script 2 has been executed');"
    )

    # Save output PDF file
    form_editor.save(output_file_name)
```

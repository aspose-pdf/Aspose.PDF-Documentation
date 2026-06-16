---
title: 필드 스크립트 추가
linktitle: 필드 스크립트 추가
type: docs
weight: 10
url: /ko/python-net/add-field-script/
description: 대화형 PDF 양식에는 사용자가 양식 필드와 상호 작용할 때 작업을 자동화하는 JavaScript가 포함될 수 있습니다.개발자는 Aspose.PDF for Python을 사용하여 버튼이나 텍스트 필드와 같은 양식 요소에 스크립트를 쉽게 첨부할 수 있습니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 양식 필드에 자바스크립트 액션 추가
Abstract: 이 문서에서는 PDF 양식을 열고, 특정 양식 필드에 JavaScript 코드를 할당하고, 추가 스크립트 동작을 추가하고, 업데이트된 문서를 저장하는 방법을 설명합니다.이 예제에서는 Aspose.PDF Facades API의 FormEditor 클래스를 사용하여 양식 동작을 프로그래밍 방식으로 조작합니다.
---

## Python을 사용하여 PDF 양식 필드에 자바스크립트 액션 추가

이 코드 스니펫을 사용하면 Python용 Aspose.PDF 라이브러리를 사용하여 기존 PDF 양식 필드에 자바스크립트 액션을 추가할 수 있습니다.PDF 문서를 열고 양식 필드에 JavaScript 작업을 할당하고 필드가 트리거될 때 실행되는 스크립트를 추가합니다.마지막으로 업데이트된 PDF가 새 파일로 저장됩니다.
를 사용하여 [폼 에디터](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 에서 수업 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) 모듈을 사용하면 프로그래밍 방식으로 JavaScript를 기존 양식 필드에 연결할 수 있습니다.

1. 기존 PDF 양식을 엽니다.
1. 특정 필드에 대한 자바스크립트 액션을 설정합니다.
1. 동일한 필드에 다른 JavaScript 작업을 추가합니다.
1. 수정된 PDF 문서를 저장합니다.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_field_script(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Set JavaScript action for the field
    form_editor.set_field_script(
        "Script_Demo_Button", "app.alert('Script 1 has been executed');"
    )

    # Add JavaScript action to the field
    form_editor.add_field_script(
        "Script_Demo_Button", "app.alert('Script 2 has been executed');"
    )

    # Save output PDF file
    form_editor.save(output_file_name)
```

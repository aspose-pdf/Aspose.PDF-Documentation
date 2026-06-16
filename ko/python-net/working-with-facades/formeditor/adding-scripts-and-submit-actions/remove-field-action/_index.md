---
title: 필드 작업 제거
linktitle: 필드 작업 제거
type: docs
weight: 20
url: /ko/python-net/remove-field-action/
description: 양식 필드에서 JavaScript를 제거하면 대화형 PDF 양식을 수정하거나, 이전에 할당된 작업을 비활성화하거나, 불필요한 스크립트가 포함된 문서를 정리할 때 유용할 수 있습니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 양식 필드에서 자바 스크립트 액션 제거
Abstract: 개발자는 Python용 Aspose.PDF 를 사용하여 양식 필드에 첨부된 JavaScript 액션을 프로그래밍 방식으로 제거할 수 있습니다.이 문서에서는 기존 PDF 양식을 열고, FormEditor 클래스를 사용하여 특정 필드와 연결된 스크립트를 제거하고, 작업을 확인하고, 수정된 문서를 저장하는 방법을 설명합니다.
---

PDF 양식에는 사용자가 단추나 입력 필드와 같은 양식 요소와 상호 작용할 때 실행되는 JavaScript 작업이 포함되어 있는 경우가 많습니다.경우에 따라 양식 동작을 단순화하거나 보안을 개선하거나 양식 논리를 업데이트하기 위해 이러한 스크립트를 제거해야 할 수도 있습니다.Python용 Aspose.PDF 파일을 사용하여 PDF 문서의 양식 필드에서 자바스크립트 액션을 제거합니다.코드는 기존 PDF 양식을 열고, 특정 필드를 찾고, 연관된 JavaScript 작업을 제거하고, 업데이트된 문서를 새 PDF 파일로 저장합니다.

를 사용하여 [폼 에디터](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 에서 수업 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/), 기존 PDF 양식의 특정 필드에서 JavaScript 작업을 제거할 수 있습니다.

1. 기존 PDF 양식을 엽니다.
1. 'Script_Demo_Button'이라는 양식 필드를 찾습니다.
1. 해당 필드와 관련된 JavaScript 작업을 제거합니다.
1. 제거가 성공했는지 확인하십시오.
1. 업데이트된 PDF 문서를 저장합니다.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_field_script(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Remove JavaScript action from the field
    if not form_editor.remove_field_action("Script_Demo_Button"):
        raise Exception("Failed to remove field script")

    # Save output PDF file
    form_editor.save(output_file_name)
```

---
title: 체크박스 필드 생성
type: docs
weight: 10
url: /ko/python-net/create-checkbox-field/
description: Python용 Aspose.PDF 를 사용하여 PDF 문서에 체크박스 양식 필드를 프로그래밍 방식으로 추가하는 방법을 알아봅니다.이 안내서는 FormEditor 클래스를 사용하여 기존 PDF 파일에 대화형 확인란을 삽입하고 업데이트된 문서를 저장하는 방법을 보여줍니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬용 Aspose.PDF 파일을 사용하여 PDF에 체크박스 필드 만들기
Abstract: 대화형 양식 필드를 통해 사용자는 PDF 문서를 디지털 방식으로 작성하고 상호 작용할 수 있습니다.이 자습서에서는 Aspose.PDF Python API를 사용하여 PDF에 확인란 필드를 추가하는 방법을 배웁니다.이 예제에서는 기존 PDF 문서를 바인딩하고, 지정된 좌표에 확인란 양식 필드를 만들고, 수정된 파일을 저장하는 방법을 보여줍니다.
---

PDF 양식은 응용 프로그램, 설문 조사 및 계약과 같은 문서에서 사용자 입력을 수집하는 데 널리 사용됩니다.확인란 필드를 사용하면 양식 내에서 옵션을 선택하거나 선택 취소할 수 있습니다.

개발자는 Python용 Aspose.PDF 를 사용하여 프로그래밍 방식으로 PDF 양식을 조작할 수 있습니다. [폼 에디터](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 클래스는 PDF 문서 내에서 양식 필드를 추가, 편집 및 관리하는 방법을 제공합니다.

1. 기존 PDF 파일을 로드합니다.
1. 'fieldType.check_box' 매개 변수와 함께 'add_field () '메서드를 호출하여 체크박스를 생성하고 해당 위치를 지정합니다.
1. 필드 이름, 캡션 및 위치를 정의합니다.
1. 업데이트된 PDF 문서를 저장합니다.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_checkbox_field(infile, outfile):
    """Create CheckBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add CheckBox field to PDF form
    pdf_form_editor.add_field(
        pdf_facades.FieldType.CHECK_BOX,
        "checkbox1",
        "Check Box 1",
        1,
        240,
        498,
        256,
        514,
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```

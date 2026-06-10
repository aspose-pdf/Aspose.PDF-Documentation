---
title: 라디오 버튼 필드 생성
type: docs
weight: 40
url: /ko/python-net/create-radiobutton-field/
description: Python용 Aspose.PDF 를 사용하여 PDF 문서에 라디오 버튼 양식 필드를 프로그래밍 방식으로 추가하는 방법을 알아봅니다.이 예제에서는 라디오 버튼 그룹을 만들고, 선택 가능한 옵션을 정의하고, 업데이트된 PDF 파일을 저장하는 방법을 보여줍니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬용 Aspose.PDF 파일을 사용하여 PDF에 라디오 버튼 필드 만들기
Abstract: 라디오 단추는 사용자가 미리 정의된 선택 항목 그룹에서 하나의 옵션을 선택할 수 있도록 하기 위해 일반적으로 PDF 양식에서 사용됩니다.이 자습서에서는 파이썬용 Aspose.PDF FormEditor 클래스를 사용하여 PDF에서 라디오 버튼 필드를 만드는 방법을 배웁니다.이 예제에서는 라디오 버튼 항목을 정의하고, 기본 선택을 설정하고, 업데이트된 문서를 저장하는 방법을 보여줍니다.
---

대화형 PDF 양식을 사용하면 문서 내에서 구조화된 입력을 직접 제공할 수 있습니다.라디오 버튼 필드는 사용자가 국가, 성별 또는 선호 사항 선택과 같이 여러 선택 항목 중에서 한 가지 옵션만 선택해야 하는 경우에 유용합니다.

더 [폼 에디터](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 클래스는 텍스트 상자, 확인란, 콤보 상자, 목록 상자 및 라디오 버튼을 포함하여 다양한 유형의 필드를 만드는 메서드를 제공합니다.

1. 기존 PDF 문서를 로드합니다.
1. 라디오 버튼 옵션 목록을 정의합니다.
1. 특정 페이지에 라디오 버튼 필드를 추가합니다.
1. 기본 선택 값을 설정합니다.
1. 수정된 PDF 문서를 저장합니다.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_radiobutton_field(infile, outfile):
    """Create RadioButton field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add RadioButton field to PDF form
    pdf_form_editor.items = ["Australia", "New Zealand", "Malaysia"]
    pdf_form_editor.add_field(
        pdf_facades.FieldType.RADIO, "radiobutton1", "Malaysia", 1, 240, 498, 256, 514
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```

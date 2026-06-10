---
title: 리스트 박스 필드 생성
type: docs
weight: 30
url: /ko/python-net/create-listbox-field/
description: Python용 Aspose.PDF 를 사용하여 PDF 문서에 ListBox 양식 필드를 프로그래밍 방식으로 추가하는 방법을 알아봅니다.이 안내서는 ListBox 필드를 삽입하고, 선택 가능한 항목을 정의하고, 업데이트된 PDF 파일을 저장하는 방법을 보여줍니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬용 Aspose.PDF 파일을 사용하여 PDF에 목록 상자 필드 만들기
Abstract: PDF 양식을 사용하면 옵션을 선택하고, 데이터를 입력하고, 정보를 디지털 방식으로 제출하여 문서와 상호 작용할 수 있습니다.ListBox 필드를 사용하면 표시되는 옵션 목록에서 하나 이상의 값을 선택할 수 있습니다.이 자습서에서는 파이썬용 Aspose.PDF FormEditor 클래스를 사용하여 PDF에 ListBox 필드를 만들고 미리 정의된 항목으로 채우는 방법을 배웁니다.
---

PDF 양식은 일반적으로 신청서, 설문 조사 및 등록 문서에 사용됩니다.ListBox 필드는 여러 옵션을 동시에 표시하므로 사용자가 목록에서 항목을 쉽게 검토하고 선택할 수 있습니다.

더 [폼 에디터](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 클래스는 ListBox 요소를 포함하여 다양한 유형의 대화형 필드를 추가하는 기능을 제공합니다.

1. 기존 PDF 문서를 로드합니다.
1. 선택 가능한 옵션 목록을 정의합니다.
1. 특정 페이지에 ListBox 필드를 추가합니다.
1. 기본 선택 값을 설정합니다.
1. 업데이트된 PDF 문서를 저장합니다.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_listbox_field(infile, outfile):
    """Create ListBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add ListBox field to PDF form
    pdf_form_editor.items = ["Australia", "New Zealand", "Malaysia"]
    pdf_form_editor.add_field(
        pdf_facades.FieldType.LIST_BOX, "listbox1", "Australia", 1, 230, 398, 350, 514
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```

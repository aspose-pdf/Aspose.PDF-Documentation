---
title: 필드 정렬을 세로로 설정
type: docs
weight: 40
url: /ko/python-net/set-field-alignment-vertical/
description: 이 예제에서는 Python용 Aspose.PDF 를 사용하여 PDF 문서에서 양식 필드의 세로 정렬을 설정하는 방법을 보여줍니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 양식 필드의 세로 정렬 설정하기
Abstract: 이 문서에서는 PDF를 열고, FormEditor 클래스를 사용하여 필드의 세로 정렬을 설정하고, 업데이트된 PDF를 저장하는 방법을 설명합니다.이 예제에서는 “First Name”이라는 필드의 수직 정렬을 필드 영역 아래쪽으로 설정합니다.
---

PDF 양식 필드에는 일관되고 전문적인 모양을 위해 적절한 세로 정렬이 필요한 텍스트가 포함될 수 있습니다.개발자는 Aspose.PDF for Python을 사용하여 양식 필드의 세로 정렬을 프로그래밍 방식으로 수정할 수 있습니다.
수직 정렬을 통해 개발자는 필드 텍스트를 필드 경계 상자의 상단, 중앙 또는 하단에 표시할지 여부를 제어할 수 있으므로 양식 데이터의 레이아웃과 가독성이 향상됩니다.

를 사용하여 [폼 에디터](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 클래스 및 [폼필드 파사드](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formfieldfacade/) 상수를 사용하여 개발자는 프로그래밍 방식으로 수직 정렬을 조정하여 일관된 양식 레이아웃을 얻을 수 있습니다.

1. 기존 PDF 문서를 엽니다.
1. 폼에디터 객체를 생성합니다.
1. 이름이 “First Name”인 필드의 세로 정렬을 아래쪽으로 설정합니다.
1. 수정한 문서를 저장합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_alignment_vertical(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Attempt to set vertical alignment of the "First Name" field to bottom
    if form_editor.set_field_alignment_v(
        "First Name", pdf_facades.FormFieldFacade.ALIGN_BOTTOM
    ):
        # Save updated document
        form_editor.save(outfile)
    else:
        raise Exception(
            "Failed to set field vertical alignment. Field may not support vertical alignment."
        )
```

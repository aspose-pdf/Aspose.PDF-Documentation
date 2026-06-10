---
title: 필드 정렬 설정
type: docs
weight: 30
url: /ko/python-net/set-field-alignment/
description: 이 예제에서는 Python용 Aspose.PDF 를 사용하여 PDF 문서에서 양식 필드의 텍스트 정렬을 설정하는 방법을 보여줍니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 양식 필드의 텍스트 정렬 설정하기
Abstract: 이 문서에서는 PDF 문서를 열고, FormEditor 클래스를 사용하여 특정 필드의 정렬을 설정하고, 업데이트된 PDF를 저장하는 방법을 설명합니다.이 예제에서는 “First Name”이라는 필드의 텍스트 정렬을 가운데로 설정합니다.
---

PDF 양식 필드는 일관되고 전문적인 레이아웃을 유지하기 위해 사용자 지정된 텍스트 정렬이 필요한 경우가 많습니다.개발자는 Aspose.PDF for Python을 사용하여 양식 필드의 텍스트 내용 정렬을 프로그래밍 방식으로 설정할 수 있습니다.

더 [폼 에디터](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 클래스와 함께 [폼필드 파사드](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formfieldfacade/) 상수를 사용하면 개발자가 기존 양식 필드의 정렬을 프로그래밍 방식으로 수정할 수 있습니다.

1. 기존 PDF 문서를 엽니다.
1. 폼에디터 객체를 생성합니다.
1. 이름이 “이름”인 필드의 정렬을 가운데로 설정합니다.
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


def set_field_alignment(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field alignment to center
    if form_editor.set_field_alignment(
        "First Name", pdf_facades.FormFieldFacade.ALIGN_CENTER
    ):
        # Save updated document
        form_editor.save(outfile)
    else:
        raise Exception(
            "Failed to set field alignment. Field may not support alignment."
        )
```

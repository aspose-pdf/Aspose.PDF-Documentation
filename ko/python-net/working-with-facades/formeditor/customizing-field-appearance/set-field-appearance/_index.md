---
title: 필드 모양 설정
type: docs
weight: 50
url: /ko/python-net/set-field-appearance/
description: 이 예제에서는 Python용 Aspose.PDF 를 사용하여 PDF 양식 필드의 시각적 모양을 변경하는 방법을 보여줍니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 양식 필드 모양 설정하기
Abstract: 이 문서에서는 PDF를 열고, FormEditor 클래스를 사용하여 양식 필드의 모양을 설정하고, 업데이트된 문서를 저장하는 방법을 설명합니다.이 예제에서는 AnnotationFlags.Invisible 플래그를 사용하여 이름이 “이름”이라는 필드의 모양을 보이지 않게 설정합니다.
---

PDF 양식 필드는 가시성, 인쇄 가능성 및 상호 작용을 제어하는 모양 플래그를 지원합니다.개발자는 Python용 Aspose.PDF 를 사용하여 특정 양식 필드에 대해 이러한 플래그를 프로그래밍 방식으로 수정할 수 있습니다.

를 사용하여 [폼 에디터](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 클래스를 선택하면 개발자가 이러한 플래그를 수정하여 대화형 PDF에서 양식 필드의 동작을 숨기거나 표시하거나 사용자 지정할 수 있습니다.

1. 기존 PDF 문서를 엽니다.
1. 폼에디터 객체를 생성합니다.
1. 이름이 “이름”인 필드의 모양을 보이지 않게 설정합니다.
1. 업데이트된 문서를 저장합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_appearance(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field appearance to invisible
    if not form_editor.set_field_appearance(
        "First Name", ap.annotations.AnnotationFlags.INVISIBLE
    ):
        raise Exception(
            "Failed to set field appearance. Field may not support appearance flags."
        )

    # Save updated document
    form_editor.save(outfile)
```

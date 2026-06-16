---
title: 버튼 필드 및 이미지
linktitle: 버튼 필드 및 이미지
type: docs
weight: 40
url: /ko/python-net/button-fields-and-images/
description: 이 예제에서는 Aspose.PDF Facades API를 사용하여 PDF 양식의 버튼 필드를 관리하는 방법을 보여줍니다.
lastmod: "2026-06-10"
TechArticle: true
AlternativeHeadline: 버튼 필드에 이미지 모양 추가 및 제출 플래그 읽기
Abstract: PDF 양식에는 JavaScript 작업을 트리거하거나 양식 데이터를 제출하는 대화형 단추가 포함되는 경우가 많습니다.이미지를 모양으로 추가하여 단추 필드를 시각적으로 개선하고 제출 동작을 프로그래밍 방식으로 검사할 수 있습니다.
---

## 버튼 필드에 이미지 모양 추가

이 코드 스니펫은 PDF 양식의 기존 버튼 필드에 이미지 모양을 추가하는 방법을 설명합니다.이 작업은 기본 모양을 사용자 지정 이미지로 대체하여 PDF 단추의 시각적 표현을 개선합니다.

1. Form 객체를 생성합니다.
1. PDF 파일을 양식 개체에 바인딩합니다.
1. 버튼 필드에 이미지를 추가합니다.

    - PDF와 관련된 이미지 파일의 경로 결정
    - 이미지를 바이너리 모드에서 image_stream으로 엽니다.
    - 정규화된 버튼 필드 이름을 사용하여 fill_image_field () 를 호출합니다.

1. 업데이트된 PDF를 저장합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Add image appearance to button fields
def add_image_appearance_to_button_fields(infile, outfile):
    """Add image appearance to button fields in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Add image appearance to button fields by providing the field name and image stream
    image_path = infile.replace(".pdf", ".jpg")
    with open(image_path, "rb") as image_stream:
        pdf_form.fill_image_field("Image1_af_image", image_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```

## 제출 플래그 가져오기

파이썬 라이브러리는 Aspose.PDF Facades API를 사용하여 PDF 양식의 제출 버튼의 제출 플래그를 검색하는 데 도움이 됩니다.제출 플래그는 전체 양식을 전송할지, 주석을 포함할지, FDF, XFDF, PDF 또는 HTML 형식으로 제출할지와 같은 제출 버튼의 동작을 정의합니다.

1. Form 객체를 생성합니다.
1. 완전한 제출 버튼 이름을 사용하여 양식 객체에서 get_submit_flags () 를 호출합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_submit_flags(infile, outfile):
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)
    flags = pdf_form.get_submit_flags("Submit1_af_submit")

    print(f"Submit flags: {flags}")
```

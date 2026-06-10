---
title: 필드 모양 가져오기
type: docs
weight: 20
url: /ko/python-net/get-field-appearance/
description: 이 문서에서는 PDF를 열고, 양식 필드에 액세스하고, 모양 설정을 검색하고, 표시하는 방법을 설명합니다.이 예제에서는 “성”이라는 이름의 필드 모양을 검색하는 방법을 보여 줍니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 양식 필드 모양 검색
Abstract: 이 예제에서는 Python용 Aspose.PDF 를 사용하여 PDF 문서에서 양식 필드의 시각적 모양 속성을 검색하는 방법을 보여줍니다.이 코드는 기존 PDF를 열고 특정 양식 필드에 액세스한 다음 배경색, 텍스트 색상, 테두리 색상 및 정렬을 비롯한 PDF의 모양 세부 정보를 인쇄합니다.
---

PDF 문서의 양식 필드에는 배경색, 텍스트 색상, 테두리 색상 및 정렬과 같은 시각적 속성이 있습니다.Python용 Aspose.PDF 기능을 사용하면 개발자는 다음을 사용하여 프로그래밍 방식으로 이러한 모양 설정을 검사할 수 있습니다. [폼 에디터](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 수업.

1. 기존 PDF 문서를 엽니다.
1. 폼에디터 객체를 생성합니다.
1. 특정 필드의 모양 정보를 검색합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_field_appearance(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Get field appearance
    appearance = form_editor.get_field_appearance("Last Name")
    print("Field Appearance: " + str(appearance))
```

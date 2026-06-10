---
title: 리치 텍스트 값 가져오기
type: docs
weight: 40
url: /ko/python-net/get-rich-text-values/
description: 이 단원에서는 Aspose.PDF Facades API를 사용하여 PDF 문서에서 양식 필드의 리치 텍스트 콘텐츠를 검색하는 방법을 설명합니다.일반 텍스트 필드와 달리 리치 텍스트 필드에는 굵은 텍스트, 다양한 글꼴, 색상 및 단락 스타일과 같은 서식이 지정된 콘텐츠가 포함될 수 있습니다.
lastmod: "2026-06-10"
---

PDF 양식에는 리치 텍스트 서식을 지원하는 텍스트 필드가 포함될 수 있습니다.이러한 필드에는 일반 텍스트 값 외에도 스타일 속성이 포함된 내용을 저장할 수 있습니다.

1. 양식 개체 만들기.
1. PDF 문서를 바인딩합니다.
1. 리치 텍스트 값 검색.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Get rich text values
def get_rich_text_values(infile):
    """Get rich text values from a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Get rich text values by their names
    field_names = ["Summary"]
    for field_name in field_names:
        rich_text_value = pdf_form.get_rich_text(field_name)
        print(f"Rich text value of '{field_name}': {rich_text_value}")
```

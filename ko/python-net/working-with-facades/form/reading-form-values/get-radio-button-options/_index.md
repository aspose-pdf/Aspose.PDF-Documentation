---
title: 라디오 버튼 옵션 가져오기
linktitle: 라디오 버튼 옵션 가져오기
type: docs
weight: 20
url: /ko/python-net/get-radio-button-options/
description: 이 문서에서는 Aspose.PDF Facades API를 사용하여 PDF 문서에서 현재 선택된 라디오 버튼 필드 값을 검색하는 방법을 보여줍니다.
lastmod: "2026-06-10"
---

PDF 양식의 라디오 버튼 필드는 한 번에 한 옵션만 선택할 수 있는 그룹화된 컨트롤입니다.각 그룹에는 필드 이름이 있고 각 옵션에는 해당 값이 있습니다.

1. 양식 개체 만들기.
1. PDF 문서를 바인딩합니다.
1. 선택한 라디오 버튼 옵션을 검색합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Get radio button options
def get_radio_button_options(infile):
    """Get radio button options from a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Get radio button options by their names
    field_names = ["WorkType"]
    for field_name in field_names:
        options = pdf_form.get_button_option_current_value(field_name)
        print(f"Options for '{field_name}': {options}")
```

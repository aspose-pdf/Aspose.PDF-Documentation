---
title: 필드 파사드 가져오기
type: docs
weight: 10
url: /ko/python-net/get-field-facades/
description: 이 예제는 Aspose.PDF Facades API를 사용하여 PDF 문서에서 특정 양식 필드의 값을 읽는 방법을 보여줍니다.
lastmod: "2026-06-10"
---

PDF 양식에는 텍스트 상자, 확인란 또는 라디오 단추와 같이 사용자가 데이터를 입력할 수 있는 필드가 포함되어 있습니다.이러한 양식을 프로그래밍 방식으로 처리하려면 이러한 필드의 현재 값을 검색해야 하는 경우가 많습니다.

1. Form 객체를 생성합니다.
1. PDF 문서를 양식 개체에 바인딩합니다.
1. 필드 값 검색.

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir


    # Get field values
    def get_field_values(infile):
        """Get field values from a PDF document."""
        # Create Form object
        pdf_form = pdf_facades.Form()

        # Bind PDF document
        pdf_form.bind_pdf(infile)

        # Get field values by their names
        field_names = ["First Name", "Last Name"]
        for field_name in field_names:
            value = pdf_form.get_field(field_name)
            print(f"Value of '{field_name}': {value}")
```
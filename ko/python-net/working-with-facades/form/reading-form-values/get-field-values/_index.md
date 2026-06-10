---
title: 필드 값 가져오기
linktitle: 필드 값 가져오기
type: docs
weight: 50
url: /ko/python-net/get-field-values/
description: 양식 클래스를 사용하여 Aspose.PDF 파사드가 있는 PDF 양식에서 필드 값 검색
lastmod: "2026-06-10"
---

이 코드 스니펫은 Aspose.PDF Facades API를 사용하여 PDF 문서에서 양식 필드의 현재 값을 검색하는 방법을 보여줍니다. [가져오기_필드 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/#methods) 메서드를 사용하면 텍스트 필드, 확인란, 라디오 버튼 및 기타 AcroForm 요소에 입력된 데이터에 프로그래밍 방식으로 액세스할 수 있습니다.

1. PDF를 양식 개체에 바인딩합니다.
1. 읽으려는 필드 이름을 지정합니다.
1. get_field () 를 사용하여 각 필드의 값을 검색합니다.

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
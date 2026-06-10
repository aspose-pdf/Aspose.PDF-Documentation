---
title: 이름 및 값으로 필드 채우기
type: docs
weight: 60
url: /ko/python-net/fill-fields-by-name-and-value/
description: 이 문서에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 이름과 값으로 여러 PDF 양식 필드를 동적으로 채우는 방법을 보여줍니다.각 필드를 개별적으로 설정하는 대신 딕셔너리 구조를 사용하여 필드 이름을 값에 매핑하고 값을 루프로 채웁니다.
lastmod: "2026-06-10"
---

이름-값 컬렉션을 사용하여 양식 필드를 채우면 개발자는 PDF 양식 자동화를 위한 확장 가능하고 유연한 솔루션을 만들 수 있습니다.이 예제에서는 [양식](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) 파사드 폼 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) PDF 문서를 바인딩하고 필드 데이터 사전을 반복하는 데 사용됩니다.각 항목은 'fill_field 메서드'를 사용하여 적용되므로 양식 필드를 효율적으로 일괄 업데이트할 수 있습니다.

1. 대화형 양식 필드를 사용하려면 'PDF_Facades.Form () '을 초기화하십시오.
1. 원본 PDF 문서를 첨부하려면 'bind_pdf () '를 사용하십시오.
1. 필드 이름과 삽입하려는 값이 포함된 사전을 생성합니다.
1. 딕셔너리를 반복하고 각 항목에 대해 'fill_field () '를 호출합니다.
1. 업데이트된 문서를 저장합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Fields by Name and Value
def fill_fields_by_name_and_value(infile, outfile):
    """Fill PDF form fields by name and value."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill fields by name and value
    fields = {
        "name": "Jane Smith",
        "address": "456 Elm St, Othertown, USA",
        "email": "jane.smith@example.com",
    }
    for field_name, value in fields.items():
        pdf_form.fill_field(field_name, value)

    # Save updated PDF using outfile
    pdf_form.save(outfile)
```

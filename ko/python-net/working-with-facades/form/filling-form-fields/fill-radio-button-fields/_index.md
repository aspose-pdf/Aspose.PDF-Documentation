---
title: 라디오 버튼 필드 채우기
type: docs
weight: 30
url: /ko/python-net/fill-radio-button-fields/
description: 이 예제는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 양식의 라디오 버튼 필드를 프로그래밍 방식으로 채우는 방법을 보여줍니다.PDF 문서를 바인딩하고, 색인별로 라디오 버튼 옵션을 선택하고, 업데이트된 파일을 저장하는 방법을 보여줍니다.
lastmod: "2026-06-10"
---

라디오 버튼을 사용하면 성별 또는 선호도 필드와 같은 사전 정의된 그룹에서 단일 옵션을 선택할 수 있습니다.이 예시에서는 [양식](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) 외관으로부터의 외관 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) 모듈은 소스 PDF를 바인딩하고 인덱스 값으로 선택한 옵션을 할당하는 데 사용됩니다.원하는 옵션을 선택하면 수정된 문서가 저장됩니다.

1. PDF_Facades.Form () 을 초기화하여 PDF 양식 필드를 관리합니다.
1. 라디오 버튼 필드가 포함된 PDF를 첨부하려면 'bind_pdf () '를 호출합니다.
1. 첫 번째 옵션 (인덱스 0) 을 선택하려면 'fill_field () '를 사용하십시오.
1. 업데이트된 PDF를 저장합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Radio Button Fields
def fill_radio_button_fields(infile, outfile):
    """Fill radio button fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill radio button fields by name
    pdf_form.fill_field("gender", 0)  # Select male option (index 0)
    # pdf_form.fill_field("gender", 1) # Select female option (index 1)

    # Save updated PDF
    pdf_form.save(outfile)
```

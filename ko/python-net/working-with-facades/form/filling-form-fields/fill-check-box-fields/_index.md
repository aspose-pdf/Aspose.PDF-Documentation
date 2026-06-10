---
title: 체크박스 필드 채우기
type: docs
weight: 20
url: /ko/python-net/fill-check-box-fields/
description: 이 예제는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 양식의 확인란 필드를 프로그래밍 방식으로 채우는 방법을 보여줍니다.PDF 문서를 바인딩하고, 필드 이름별로 확인란 값을 업데이트하고, 수정된 파일을 저장하는 방법을 보여줍니다.
lastmod: "2026-06-10"
---

확인란은 일반적으로 PDF 양식에서 구독 또는 계약 확인과 같은 이진 선택 항목을 나타내는 데 사용됩니다.이 예제에서는 [양식](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) 파사드 폼 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) 양식 필드에 액세스하고 해당 값을 선택된 상태로 설정하는 데 사용됩니다.확인란을 업데이트하면 채워진 PDF가 새 문서로 저장됩니다.

1. 양식 필드 상호 작용을 관리하려면 'PDF_Facades.Form () '을 초기화합니다.
1. 확인란 필드가 포함된 원본 PDF를 첨부하려면 'bind_pdf () '를 사용하십시오.
1. 'fill_field () '를 호출하여 '구독_뉴스레터' 및 '수락_용어'와 같은 필드를 선택된 것으로 표시합니다.
1. 업데이트된 문서를 저장합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Check Box Fields
def fill_check_box_fields(infile, outfile):
    """Fill check box fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill check box fields by name
    pdf_form.fill_field("subscribe_newsletter", "Yes")
    pdf_form.fill_field("accept_terms", "Yes")

    # Save updated PDF
    pdf_form.save(outfile)
```

---
title: 텍스트 필드 채우기
linktitle: 텍스트 필드 채우기
type: docs
weight: 10
url: /ko/python-net/fill-text-fields/
description: 이 예제는.NET을 통해 파이썬용 Aspose.PDF 파일을 사용하여 PDF 양식의 텍스트 필드를 자동으로 채우는 방법을 보여줍니다.PDF 문서를 로드하고, 특정 양식 필드를 이름으로 채우고, 업데이트된 파일을 저장하는 방법을 보여줍니다.
lastmod: "2026-06-10"
---

프로그래밍 방식으로 텍스트 필드를 채우면 애플리케이션에서 수동 편집 없이 PDF 템플릿을 재사용하고 동적 콘텐츠를 삽입할 수 있습니다.이 예제에서는 [양식](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) 파사드 폼 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) PDF 양식을 바인딩하고 이름, 주소 및 이메일과 같은 여러 필드를 업데이트하는 데 사용됩니다.값을 할당하면 수정된 PDF가 새 문서로 저장됩니다.

1. 양식 필드 작업을 관리하려면 'PDF_Facades.Form () '을 초기화합니다.
1. 텍스트 필드가 포함된 입력 PDF를 첨부하려면 'bind_pdf () '를 사용하십시오.
1. 'fill_field () '를 호출하여 이름, 주소, 이메일과 같은 필드에 데이터를 삽입합니다.
1. 업데이트된 PDF를 저장합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Text Fields
def fill_text_fields(infile, outfile):
    """Fill text fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill text fields by name
    pdf_form.fill_field("name", "John Doe")
    pdf_form.fill_field("address", "123 Main St, Anytown, USA")
    pdf_form.fill_field("email", "john.doe@example.com")

    # Save updated PDF
    pdf_form.save(outfile)
```

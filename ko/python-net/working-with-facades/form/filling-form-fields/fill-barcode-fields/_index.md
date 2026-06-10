---
title: 바코드 필드 채우기
type: docs
weight: 50
url: /ko/python-net/fill-barcode-fields/
description: 이 예제는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 양식의 바코드 필드를 프로그래밍 방식으로 채우는 방법을 보여줍니다.PDF 문서를 바인딩하고, 바코드 필드에 값을 할당하고, 업데이트된 파일을 저장하는 방법을 보여줍니다.
lastmod: "2026-06-10"
---

PDF 양식의 바코드 필드를 사용하면 인코딩된 정보를 저장하고 바코드로 시각적으로 표시할 수 있습니다.이 예시에서는 [양식](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) 외관으로부터의 외관 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) 모듈은 양식 필드에 액세스하고 바코드 값을 할당하는 데 사용됩니다.데이터가 채워지면 업데이트된 바코드 내용과 함께 PDF가 저장됩니다.

1. 'PDF_Facades.Form () '을 초기화하여 PDF 양식 상호 작용을 관리합니다.
1. 바코드 필드가 포함된 PDF를 첨부하려면 'bind_pdf () '를 호출합니다.
1. 'fill_field () '를 사용하여 바코드 값을 할당합니다.
1. 업데이트된 문서를 저장합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Barcode Fields
def fill_barcode_fields(infile, outfile):
    """Fill barcode fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill barcode fields by name
    pdf_form.fill_field("product_barcode", "123456789012")

    # Save updated PDF
    pdf_form.save(outfile)
```

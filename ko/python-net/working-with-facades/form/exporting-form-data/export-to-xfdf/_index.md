---
title: XFDF로 내보내기
type: docs
weight: 20
url: /ko/python-net/export-to-xfdf/
description: 이 예제에서는.NET을 통해 Python용 Aspose.PDF 파일을 사용하여 PDF 양식 필드 데이터를 XFDF (XML 양식 데이터 형식) 파일로 내보내는 방법을 보여줍니다.PDF 양식을 로드하고, 양식 파사드를 통해 해당 필드에 액세스하고, 추출된 값을 XFDF 스트림에 저장하는 방법을 보여줍니다.
lastmod: "2026-06-10"
---

XFDF는 개발자가 원본 문서와 독립적으로 양식 필드 값을 전송할 수 있는 PDF 양식 데이터의 XML 표현입니다.이 예제에서는 [양식](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) 객체 출처 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) 소스 PDF를 바인딩하고 해당 데이터를 구조화된 XFDF 파일로 내보내는 데 사용됩니다.

1. PDF_Facades.Form () 을 초기화하여 PDF 양식 데이터를 관리합니다.
1. 'bind_pdf () '를 호출하여 원본 PDF 문서를 첨부합니다.
1. 쓰기 가능한 바이너리 스트림을 만들려면 'open () '을 사용하십시오.
1. 양식 데이터 내보내기.양식 필드 값을 추출하여 XFDF 형식으로 저장하려면 'export_xfdf () '를 호출합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to XFDF
def export_pdf_form_to_xfdf(infile, outfile):
    """Export PDF form data to XFDF file."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Create XFDF file stream
    with open(outfile, "wb") as xfdf_output_stream:
        # Export form data to XFDF file
        pdf_form.export_xfdf(xfdf_output_stream)
```

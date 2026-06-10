---
title: FDF로 내보내기
type: docs
weight: 10
url: /ko/python-net/export-to-fdf/
description: 이 예제에서는 Python용 Aspose.PDF 파일을.NET을 통해 PDF 양식 필드 데이터를 FDF (양식 데이터 형식) 파일로 내보내는 방법을 설명합니다.양식 파사드를 통해 대화형 양식 데이터에 액세스하고, 소스 PDF 문서를 바인딩하고, 추출된 값을 FDF 스트림에 저장하는 방법을 보여줍니다.
lastmod: "2026-06-10"
---

FDF는 전체 문서를 포함하지 않고 PDF 양식 데이터를 저장 및 전송하기 위해 특별히 설계된 경량 형식입니다.이 예제에서는 [양식](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) 객체는 에서 초기화됩니다. [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) 모듈을 통해 개발자는 AcroForm 필드와 상호 작용하고 해당 값을 내보낼 수 있습니다.

1. PDF 양식 필드와 함께 사용할 PDF_Facades.Form () 의 인스턴스를 만드십시오.
1. 양식이 포함된 PDF 문서를 첨부하려면 'bind_pdf () '를 호출합니다.
1. FDF 파일의 쓰기 가능한 이진 스트림을 만들려면 'open (') '을 사용하십시오.
1. 양식 데이터 내보내기.모든 양식 필드 값을 추출하고 저장하려면 'export_fdf () '를 호출합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to FDF
def export_form_data_to_fdf(infile, outfile):
    """Export PDF form data to FDF file."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Create FDF file stream
    with open(outfile, "wb") as fdf_output_stream:
        # Export form data to FDF file
        pdf_form.export_fdf(fdf_output_stream)
```

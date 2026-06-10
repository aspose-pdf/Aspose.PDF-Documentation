---
title: FDF 데이터 가져오기
linktitle: FDF 데이터 가져오기
type: docs
weight: 10
url: /ko/python-net/import-fdf-data/
description: 이 예제는.NET을 통해 Python용 Aspose.PDF 를 사용하여 FDF 파일의 양식 데이터를 PDF 양식으로 가져오는 방법을 보여줍니다.PDF 문서를 바인딩하고, FDF 스트림에서 양식 필드 값을 읽고, 해당 필드를 자동으로 채우는 방법을 보여줍니다.
lastmod: "2026-06-10"
---

FDF (양식 데이터 형식) 는 전체 문서를 포함하지 않고 PDF 양식 필드 값을 저장하고 전송하는 데 사용되는 간단한 형식입니다.이 예제에서는 [양식](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) 파사드 폼 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) PDF 양식을 로드하고 외부 FDF 파일에서 필드 데이터를 가져오는 데 사용됩니다.가져오기 프로세스 후 업데이트된 PDF는 새 파일로 저장됩니다.

1. 대화형 PDF 양식 필드를 사용하려면 PDF_Facades.Form () 을 초기화하십시오.
1. 'bind_pdf () '를 호출하여 PDF 양식 템플릿을 첨부합니다.
1. 바이너리 모드에서 FDF 파일을 읽으려면 'open () '을 사용하십시오.
1. FDF 파일의 데이터로 PDF 필드를 채우려면 'import_fdf () '를 호출합니다.
1. 업데이트된 PDF를 저장합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import Data from FDF
def import_fdf_to_pdf_form(infile, datafile, outfile):
    """Import form data from FDF file into PDF form fields."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open FDF file as stream
    with open(datafile, "rb") as fdf_input_stream:
        pdf_form.import_fdf(fdf_input_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```

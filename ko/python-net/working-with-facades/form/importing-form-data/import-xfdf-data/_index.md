---
title: XFDF 데이터 가져오기
linktitle: XFDF 데이터 가져오기
type: docs
weight: 20
url: /ko/python-net/import-xfdf-data/
description: 이 예제는.NET을 통해 Python용 Aspose.PDF 를 사용하여 XFDF 파일의 양식 데이터를 PDF 양식으로 가져오는 방법을 보여줍니다.PDF 문서를 바인딩하고, 파일 스트림을 통해 XML 기반 XFDF 데이터를 읽고, 일치하는 양식 필드를 자동으로 채우는 방법을 보여줍니다.XFDF 데이터를 가져오면 양식 데이터를 효율적으로 교환할 수 있고 구조화된 XML 형식을 사용하는 자동화된 문서 워크플로우를 지원할 수 있습니다.
lastmod: "2026-06-10"
---

XFDF (XML 양식 데이터 형식) 는 상호 운용성 및 데이터 교환을 위해 설계된 PDF 양식 데이터의 XML 표현입니다.이 예제에서는 [양식](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) 외관으로부터의 외관 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) 모듈은 PDF 양식을 바인딩하고 외부 XFDF 파일에서 필드 값을 가져오는 데 사용됩니다.데이터를 가져온 후 업데이트된 PDF는 새 문서로 저장됩니다.

1. PDF_Facades.Form () 을 초기화하여 PDF 양식 필드와 상호 작용하십시오.
1. 'bind_pdf () '를 호출하여 PDF 양식 템플릿을 첨부합니다.
1. XFDF 파일을 읽으려면 'open () '을 사용하십시오.
1. 'import_xfdf () '를 호출하여 XFDF 파일의 값으로 PDF 필드를 채웁니다.
1. 업데이트된 문서를 저장합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import Data from XFDF
def import_data_from_xfdf(infile, datafile, outfile):
    """Import form data from XFDF file into PDF form fields."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open XFDF file as stream
    with open(datafile, "rb") as xfdf_input_stream:
        # Import data from XFDF into PDF form fields
        pdf_form.import_xfdf(xfdf_input_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```

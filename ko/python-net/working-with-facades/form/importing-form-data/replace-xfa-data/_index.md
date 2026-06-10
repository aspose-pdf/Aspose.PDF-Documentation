---
title: XFA 데이터 교체
type: docs
weight: 50
url: /ko/python-net/replace-xfa-data/
description: 이 예제는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF의 기존 XFA 양식 데이터를 바꾸는 방법을 보여줍니다.XFA 기반 PDF 문서를 바인딩하고, 외부 XFA 파일에서 새 데이터를 로드하고, 프로그래밍 방식으로 양식 내용을 업데이트하는 방법을 보여줍니다.
lastmod: "2026-06-10"
---

XFA (XML 양식 아키텍처) 양식은 데이터를 PDF 구조 내에 XML 형식으로 저장합니다.이 예제에서는 [양식](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) 외관으로부터의 외관 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) 모듈은 PDF를 바인딩하고 외부 XML 스트림을 사용하여 기존 XFA 데이터 세트를 대체하는 데 사용됩니다.새 데이터를 적용한 후 업데이트된 PDF는 별도의 파일로 저장됩니다.

1. PDF_Facades.Form () 을 초기화하여 XFA 양식 데이터를 관리합니다.
1. XFA 양식이 포함된 PDF를 첨부하려면 'bind_pdf () '를 호출하십시오.
1. XFA XML 파일을 읽으려면 'FileIO () '를 사용하십시오.
1. 'set_xfa_data () '를 호출하여 새 XFA 콘텐츠로 PDF를 업데이트하십시오.
1. 업데이트된 문서를 저장합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Replace from XFA data
def replace_xfa_data(infile, datafile, outfile):
    """Import form data from XFA file into PDF form fields."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    # Open XFA file as stream
    with FileIO(datafile, "r") as xfa_stream:
        # Import data from XFA into PDF form fields
        form.set_xfa_data(xfa_stream)

    # Save updated PDF
    form.save(outfile)
```

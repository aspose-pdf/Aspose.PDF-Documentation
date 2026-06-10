---
title: XFA 데이터 추출
linktitle: XFA 데이터 추출
type: docs
weight: 50
url: /ko/python-net/extract-xfa-data/
description: 이 예제에서는.NET을 통해 파이썬용 Aspose.PDF 파일을 사용하여 PDF 파일에서 XFA 양식 데이터를 추출하는 방법을 설명합니다.XFA 기반 PDF 문서를 Form 파사드에 바인딩하고 내부 데이터 구조를 파일 스트림으로 내보내는 방법을 보여줍니다.
lastmod: "2026-06-10"
---

XFA (XML 양식 아키텍처) 양식은 데이터가 PDF에 XML로 저장된다는 점에서 기존 AcroForms와 다릅니다.이 예제에서는 [양식](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) 에서 가져온 객체 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) 모듈은 PDF를 바인딩하고 XFA 데이터를 파일로 직접 추출하는 데 사용됩니다.

1. PDF_Facades.Form () 의 인스턴스를 만들어 양식 데이터를 관리합니다.
1. 'bind_pdf () '를 호출하여 XFA 양식이 포함된 소스 PDF를 첨부합니다.
1. 쓰기 가능한 파일 스트림을 만들려면 'FileIO () '를 사용하십시오.
1. 내장된 XFA XML 데이터를 내보내려면 'extract_xfa_data () '를 호출합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Extract XFA Data
def export_xfa_data(infile, outfile):
    """Export XFA form data."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    with FileIO(outfile, "w") as stream:
        # Export embedded XFA XML data to the output stream
        form.extract_xfa_data(stream)
```

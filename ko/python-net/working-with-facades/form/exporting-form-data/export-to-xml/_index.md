---
title: XML로 내보내기
linktitle: XML로 내보내기
type: docs
weight: 40
url: /ko/python-net/export-to-xml/
description: 이 예제는.NET을 통해 파이썬용 Aspose.PDF 파일을 사용하여 PDF 양식 데이터를 XML 파일로 내보내는 방법을 보여줍니다.Form Class를 사용하여 PDF 문서를 로드하고, 양식 파사드를 통해 양식 필드에 액세스하고, 추출된 데이터를 구조화된 XML로 저장하는 방법을 보여줍니다.
lastmod: "2026-06-10"
---

양식 데이터를 내보내면 개발자가 필드 값을 수동으로 복사하지 않고도 PDF AcroForms에 저장된 정보를 재사용할 수 있습니다.이 예제에서는 [양식](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) 객체는 aspose.pdf 에서 생성됩니다.파사드 모듈에서는 소스 PDF가 PDF에 바인딩되고 양식 데이터가 XML 스트림에 기록됩니다.

1. 양식 개체 만들기.양식 필드에 액세스하고 관리하려면 PDF_Facades.Form () 을 초기화하십시오.
1. 'bind_pdf () '를 사용하여 소스 PDF 문서를 양식 인스턴스에 첨부합니다.
1. 'FileIO () '를 사용하여 쓰기 가능한 파일 스트림을 생성합니다.
1. 모든 양식 필드 값을 추출하여 XML 파일에 쓰려면 'export_xml () '을 호출합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to XML
def export_pdf_form_data_to_xml(infile, datafile):
    """Export PDF form data to XML file."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open XML file as stream
    with FileIO(datafile, "w") as xml_output_stream:
        # Export data from PDF form fields to XML
        pdf_form.export_xml(xml_output_stream)
```

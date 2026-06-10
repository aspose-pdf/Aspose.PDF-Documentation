---
title: XML 데이터 가져오기
type: docs
weight: 40
url: /ko/python-net/import-xml-data/
description: 이 예제는.NET을 통해 Python용 Aspose.PDF 를 사용하여 XML 파일의 양식 데이터를 PDF 양식 필드로 가져오는 방법을 보여줍니다.PDF 문서를 바인딩하고, 파일 스트림을 통해 구조화된 XML 데이터를 읽고, 해당 양식 필드를 자동으로 채우는 방법을 보여줍니다.
lastmod: "2026-06-10"
---

XML은 일반적으로 구조화된 양식 데이터를 저장하는 데 사용되므로 시스템 간에 값을 전송하는 데 유용한 형식입니다.이 예제에서는 [양식](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) 파사드 폼 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) PDF 양식을 로드하고 XML 파일에서 직접 필드 값을 적용하는 데 사용됩니다.데이터를 가져오면 업데이트된 PDF가 새 문서로 저장됩니다.

1. PDF_Facades.Form () 을 초기화하여 PDF 양식 필드와 상호 작용하십시오.
1. 'bind_pdf () '를 호출하여 PDF 양식 템플릿을 첨부합니다.
1. 양식 데이터가 포함된 XML 파일에 액세스하려면 'FileIO () '를 사용하십시오.
1. 'import_xml () '을 호출하여 XML 파일의 값으로 PDF 필드를 채웁니다.
1. 업데이트된 PDF를 저장합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import data from XML
def import_xml_to_pdf_fields(infile, datafile, outfile):
    """Import form data from XML file into PDF form fields."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open XML file as stream
    with FileIO(datafile, "r") as xml_input_stream:
        # Import data from XML into PDF form fields
        pdf_form.import_xml(xml_input_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```

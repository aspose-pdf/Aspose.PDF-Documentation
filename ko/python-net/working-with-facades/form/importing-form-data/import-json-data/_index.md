---
title: JSON 데이터 가져오기
type: docs
weight: 30
url: /ko/python-net/import-json-data/
description: 이 예제는.NET을 통해 Python용 Aspose.PDF 를 사용하여 JSON 파일의 양식 필드 데이터를 PDF 양식으로 가져오는 방법을 보여줍니다.PDF 문서를 바인딩하고, 파일 스트림을 통해 구조화된 JSON 데이터를 읽고, 일치하는 양식 필드를 자동으로 채우는 방법을 보여줍니다.
lastmod: "2026-06-10"
---

JSON은 시스템 간에 구조화된 데이터를 저장하고 전송하는 데 널리 사용됩니다.이 예시에서는 [양식](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) 외관으로부터의 외관 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) 모듈은 PDF 양식을 바인딩하고 외부 JSON 파일에서 필드 값을 가져오는 데 사용됩니다.가져오기 프로세스 후 업데이트된 문서는 새 PDF로 저장됩니다.

1. PDF_Facades.Form () 을 초기화하여 PDF 양식 필드와 상호 작용하십시오.
1. 'bind_pdf () '를 호출하여 PDF 양식 템플릿을 첨부합니다.
1. 양식 값이 포함된 JSON 파일을 읽으려면 'fileIO () '를 사용하십시오.
1. 'import_json () '을 호출하여 JSON 키-값 쌍을 사용하여 PDF 필드를 채웁니다.
1. 업데이트된 PDF를 저장합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import from JSON
def import_json_to_pdf_form(infile, datafile, outfile):
    """Import form data from JSON file into PDF form fields."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    # Open JSON file as stream
    with FileIO(datafile, "r") as json_stream:
        # Import data from JSON into PDF form fields
        form.import_json(json_stream)

    # Save updated PDF
    form.save(outfile)
```

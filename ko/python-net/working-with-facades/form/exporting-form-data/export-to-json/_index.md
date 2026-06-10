---
title: JSON으로 내보내기
type: docs
weight: 30
url: /ko/python-net/export-to-json/
description: 이 예제는.NET을 통해 파이썬용 Aspose.PDF 파일을 사용하여 PDF 양식 필드 값을 JSON 파일로 내보내는 방법을 보여줍니다.PDF 양식을 로드하고, 양식 파사드를 통해 해당 필드에 액세스하고, 추출된 데이터를 구조화된 JSON 형식으로 저장하는 방법을 설명합니다.
lastmod: "2026-06-10"
---

JSON은 애플리케이션과 서비스 간의 원활한 교환을 가능하게 하는 널리 사용되는 데이터 형식입니다.이 예시에서는 [양식](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) 에서 가져온 객체 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) 모듈은 PDF 파일을 바인딩하고 양식 필드 값을 읽을 수 있는 JSON 구조로 내보내는 데 사용됩니다.

1. 양식 필드를 사용하려면 PDF_Facades.Form () 을 초기화하십시오.
1. 원본 PDF 문서를 첨부하려면 'bind_pdf () '를 사용하십시오.
1. 'FileIO () '를 사용하여 쓰기 가능한 스트림을 생성합니다.
1. 'export_json () '을 호출하여 양식 필드 값을 추출하고 형식이 지정된 JSON에 저장합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to JSON
def export_form_to_json(infile, outfile):
    """Export PDF form field values to JSON file."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    # Create JSON file stream
    with FileIO(outfile, "w") as json_stream:
        # Export form field values to JSON
        form.export_json(json_stream, indented=True)
```

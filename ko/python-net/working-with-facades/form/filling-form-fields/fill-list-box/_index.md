---
title: 목록 상자 채우기
linktitle: 목록 상자 채우기
type: docs
weight: 40
url: /ko/python-net/fill-list-box/
description: 이 예제는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 양식의 목록 상자와 다중 선택 필드를 프로그래밍 방식으로 채우는 방법을 보여줍니다.PDF 문서를 바인딩하고, 목록 기반 양식 필드 내에서 값을 선택하고, 업데이트된 파일을 저장하는 방법을 보여줍니다.
lastmod: "2026-06-10"
---

목록 상자와 다중 선택 필드를 통해 사용자는 사전 정의된 옵션 세트에서 하나 이상의 값을 선택할 수 있습니다.이 예에서는 [양식](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) 파사드 폼 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) PDF 양식에 액세스하고 선택한 값을 즐겨찾기_colors 필드에 할당하는 데 사용됩니다.원하는 옵션을 선택하면 업데이트된 문서가 저장됩니다.

1. 양식 필드를 관리하고 업데이트하려면 'PDF_Facades.Form () '을 초기화합니다.
1. 목록 상자 또는 다중 선택 필드가 포함된 원본 PDF를 첨부하려면 'bind_pdf () '를 호출합니다.
1. 'fill_field () '를 사용하여 사용 가능한 옵션에서 값을 선택합니다.
1. 업데이트된 문서를 저장합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill List Box / Multi-Select Fields
def fill_list_box_fields(infile, outfile):
    """Fill list box and multi-select fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill list box / multi-select fields by name
    pdf_form.fill_field("favorite_colors", "Red")

    # Save updated PDF
    pdf_form.save(outfile)
```

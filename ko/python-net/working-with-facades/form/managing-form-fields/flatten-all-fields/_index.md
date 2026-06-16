---
title: 모든 필드 평평하게 하기
linktitle: 모든 필드 평평하게 하기
type: docs
weight: 10
url: /ko/python-net/flatten-all-fields/
description: 이 예제는.NET을 통해 파이썬용 Aspose.PDF 파일을 사용하여 PDF의 모든 양식 필드를 병합하는 방법을 보여줍니다.PDF 문서를 바인딩하고, 모든 대화형 양식 요소를 정적 페이지 내용으로 변환하고, 완성된 파일을 저장하는 방법을 보여줍니다.
lastmod: "2026-06-10"
---

병합은 필드 값을 문서 레이아웃에 직접 병합하여 PDF 양식의 상호 작용을 제거합니다.이 예제에서는 [양식](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) 파사드 폼 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) 소스 PDF를 바인딩하고 모든 필드를 편집할 수 없는 내용으로 변환하는 flatten_all_fields () 메서드를 적용하는 데 사용됩니다.

1. PDF_Facades.Form () 을 초기화하여 PDF 양식 필드와 상호 작용하십시오.
1. 'bind_pdf () '를 호출하여 원본 문서를 첨부합니다.
1. 모든 대화형 필드를 정적 콘텐츠로 변환하려면 'flatten_all_fields () '를 호출하세요.
1. 업데이트된 문서를 저장합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Flatten all fields
def flatten_all_fields(infile, outfile):
    """Flatten all fields in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Flatten all fields in the PDF document
    pdf_form.flatten_all_fields()

    # Save updated PDF
    pdf_form.save(outfile)
```

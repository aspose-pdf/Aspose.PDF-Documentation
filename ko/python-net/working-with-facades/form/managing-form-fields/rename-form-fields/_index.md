---
title: 양식 필드 이름 바꾸기
linktitle: 양식 필드 이름 바꾸기
type: docs
weight: 30
url: /ko/python-net/rename-form-fields/
description: 이 예제는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서의 양식 필드 이름을 바꾸는 방법을 보여줍니다.PDF 양식을 바인딩하고, 기존 필드 이름을 프로그래밍 방식으로 업데이트하고, 수정된 파일을 저장하는 방법을 보여줍니다.필드 이름을 바꾸면 양식 구조를 표준화하고, 데이터 매핑을 개선하고, 자동화된 워크플로 또는 외부 시스템과의 통합을 간소화하는 데 도움이 됩니다.
lastmod: "2026-06-10"
---

양식 필드 이름을 바꾸는 것은 내부 명명 규칙에 맞게 PDF 양식을 정렬하거나 구조화된 데이터 처리를 위해 문서를 준비할 때 유용합니다.이 예제에서는 [양식](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) 외관으로부터의 외관 [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) 모듈은 소스 PDF를 바인딩하고 이전 필드 이름을 새 필드 이름으로 바꾸는 매핑을 적용하는 데 사용됩니다.필드 식별자를 업데이트하면 변경 내용이 적용된 상태로 문서가 저장됩니다.

1. PDF_Facades.Form () 을 초기화하여 PDF 양식 필드와 상호 작용하십시오.
1. 'bind_pdf () '를 호출하여 PDF 문서를 첨부합니다.
1. 이전 필드 이름과 해당하는 새 이름을 포함하는 튜플 목록을 만듭니다.
1. 매핑을 반복하고 각 항목에 대해 'rename_field () '를 호출합니다.
1. 업데이트된 문서를 저장합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Rename form fields
def rename_form_fields(infile, outfile):
    """Rename form fields in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Rename form fields by providing a mapping of old names to new names
    field_renaming_map = [("First Name", "NewFirstName"), ("Last Name", "NewLastName")]
    for old_name, new_name in field_renaming_map:
        pdf_form.rename_field(old_name, new_name)

    # Save updated PDF
    pdf_form.save(outfile)
```

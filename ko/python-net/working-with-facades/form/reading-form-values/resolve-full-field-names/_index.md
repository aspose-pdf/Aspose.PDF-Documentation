---
title: 전체 필드 이름 확인
linktitle: 전체 필드 이름 확인
type: docs
weight: 60
url: /ko/python-net/resolve-full-field-names/
description: 이 예제에서는 Aspose.PDF Facades API를 사용하여 PDF 문서에서 양식 필드의 정규화된 이름을 검색하는 방법을 보여줍니다.
lastmod: "2026-06-10"
---

PDF 양식에서는 특히 하위 양식을 사용할 때 필드를 계층적으로 구성할 수 있습니다.각 필드에는 짧은 이름과 완전한 이름이 있습니다.정규화된 이름은 양식 계층 구조 내 필드의 전체 경로를 나타내며 양식 데이터를 조작하거나 읽는 많은 API 메서드에서 필요합니다.

1. 양식 개체 만들기.
1. PDF 문서를 바인딩합니다.
1. 모든 양식 필드 이름에 액세스합니다.
1. 각 필드의 정규화된 이름은 get_full_field_name () 을 사용하여 확인됩니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Resolve full field names
def resolve_full_field_names(infile):
    """Resolve full field names in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Resolve full field names
    for field in pdf_form.field_names:
        name = pdf_form.get_full_field_name(field)
        print(f"Full field name: {name}")
```

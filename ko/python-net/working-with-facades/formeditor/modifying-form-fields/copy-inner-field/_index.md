---
title: 내부 필드 복사
linktitle: 내부 필드 복사
type: docs
weight: 20
url: /ko/python-net/copy-inner-field/
description: 파이썬용 Aspose.PDF 를 사용하여 파이썬을 사용하여 PDF 양식 필드를 새 위치에 복사합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 양식 필드를 새 위치로 복사
Abstract: 이 예제에서는 Python용 Aspose.PDF 를 사용하여 기존 양식 필드를 PDF 문서의 새 위치에 복사하는 방법을 보여줍니다.코드는 PDF를 열고 필드를 지정된 페이지와 좌표에 복제하고 업데이트된 문서를 저장합니다.
---

PDF 양식에서는 원래 서식과 동작을 유지하면서 필드를 복제해야 하는 경우가 많습니다.개발자는 Aspose.PDF for Python을 사용하여 프로그래밍 방식으로 기존 필드를 같은 페이지나 다른 페이지의 새 위치에 복사할 수 있습니다.

이 문서에서는 '이름'이라는 필드를 2페이지의 '이름 복사'라는 새 필드에 특정 좌표 (x=200, y=600) 로 복사하여 새로 배치된 필드가 포함된 PDF를 생성하는 방법을 설명합니다.

1. 기존 PDF 양식을 엽니다.
1. 폼에디터 객체를 생성합니다.
1. PDF 문서를 양식 편집기에 바인딩합니다.
1. '이름' 필드를 2페이지의 좌표 (200, 600) 에 있는 새 필드 '이름 복사'에 복사합니다.
1. 업데이트된 문서를 저장합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def copy_inner_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Copies an existing field to a new position specified by both page number and ordinates.
    # A new document will be produced, which contains everything the source document has except for the newly copied field.
    form_editor.copy_inner_field("First Name", "First Name Copy", 2, 200, 600)
    # Save updated document
    form_editor.save(outfile)
```

**참고: **

'복사_이너_필드' 메서드 서명은 다음과 같습니다.

```python
copy_inner_field(original_field_name, new_field_name, page_number, x, y)
```

- '원본_필드_이름' — 복제하려는 필드입니다.
- '새_필드_이름' — 새 필드의 이름.
- '페이지_번호' — 새 필드가 표시될 페이지입니다.
- x, y — 해당 페이지의 좌표

page_number는 PDF의 기존 페이지에 해당하는 양의 정수일 것으로 예상됩니다 (1 기반 색인 생성).

음수 매개변수를 전달하는 경우, 예:

```python
form_editor.copy_inner_field("First Name", "First Name Copy", -1, 200, 600)
```

그러면 프로그램이 이전 매개변수로 재설정됩니다.

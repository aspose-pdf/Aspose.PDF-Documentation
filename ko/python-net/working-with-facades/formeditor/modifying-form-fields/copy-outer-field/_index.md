---
title: 외부 필드 복사
linktitle: 외부 필드 복사
type: docs
weight: 30
url: /ko/python-net/copy-outer-field/
description: 이 예제에서는 Python용 Aspose.PDF 를 사용하여 한 PDF 문서에서 다른 PDF 문서로 양식 필드를 복사하는 방법을 보여줍니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 다른 문서에서 PDF 양식 필드 복사
Abstract: 이 문서에서는 새 PDF 문서를 만들고, 원본 PDF의 “이름” 필드를 1페이지 좌표 (200, 600) 로 복사하고, 업데이트된 대상 문서를 저장하는 방법을 설명합니다.
---

PDF 양식에서 한 문서의 필드를 다른 문서의 필드를 재사용해야 하는 경우가 있습니다.개발자는 Python용 Aspose.PDF 파일을 사용하여 소스 PDF의 양식 필드를 프로그래밍 방식으로 대상 PDF로 복사할 수 있습니다.

더 [폼 에디터](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) class는 소스 문서의 필드를 지정된 페이지 및 좌표에 있는 대상 문서로 복사하는 'copy_outer_field' 메서드를 제공합니다.

코드는 새 PDF (대상) 를 만들고 페이지를 추가한 다음 기존 PDF (소스) 의 필드를 대상 문서에 지정된 좌표로 복사합니다.

1. 새 대상 PDF 문서를 만듭니다.
1. 대상 PDF에 최소 한 페이지를 추가합니다.
1. 빈 대상 문서를 저장합니다.
1. 폼에디터 개체를 만들어 대상 PDF에 바인딩합니다.
1. 원본 PDF의 '이름' 필드를 (200, 600) 페이지의 1페이지로 복사합니다.
1. 업데이트된 대상 PDF를 저장합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def copy_outer_field(infile, outfile):
    # Since copy_outer_field() method needs to copy field from source document to target document, we need to create a new document as target document first.
    doc = ap.Document()
    doc.pages.add()
    doc.save(outfile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(outfile)
    # Copies an existing field to a new position specified by both page number and ordinates.
    # A new document will be produced, which contains everything the source document has except for the newly copied field.
    form_editor.copy_outer_field(infile, "First Name", 1, 200, 600)
    # Save updated document
    form_editor.save(outfile)
```

**참고: **

'복사_외부_필드' 메서드 서명은 다음과 같습니다.

```python
copy_outer_field(original_field_name, new_field_name, page_number, x, y)
```

- '원본_필드_이름' — 복제하려는 필드입니다.
- '새_필드_이름' — 새 필드의 이름.
- '페이지_번호' — 새 필드가 표시될 페이지입니다.
- x, y — 해당 페이지의 좌표

page_number는 PDF의 기존 페이지에 해당하는 양의 정수일 것으로 예상됩니다 (1 기반 색인 생성).

음수 매개변수를 전달하는 경우, 예:

```python
form_editor.copy_outer_field("First Name", "First Name Copy", 1, -200, 600)
```

그러면 프로그램이 이전 매개변수로 재설정됩니다.

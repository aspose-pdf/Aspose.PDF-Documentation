---
title: 필드 이름 바꾸기
type: docs
weight: 70
url: /ko/python-net/rename-field/
description: Python용 Aspose.PDF 를 사용하여 PDF 문서의 기존 양식 필드 이름을 바꿉니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 양식 필드 이름 바꾸기
Abstract: 이 예제에서는 Python용 Aspose.PDF 를 사용하여 PDF 문서의 기존 양식 필드 이름을 바꾸는 방법을 보여줍니다.코드는 입력 PDF를 열고, FormEditor 클래스를 사용하여 지정된 양식 필드의 이름을 변경하고, 업데이트된 문서를 저장합니다.
---

PDF 양식은 스크립팅, 자동화 및 데이터 처리를 위해 필드 이름을 사용하는 경우가 많습니다.개발자는 Python용 Aspose.PDF 를 사용하여 기존 필드를 다시 만들거나 양식 레이아웃을 변경하지 않고도 기존 필드의 이름을 바꿀 수 있습니다.

더 [폼 에디터](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) class는 개발자가 기존 필드의 위치, 값 및 모양을 유지하면서 기존 필드의 이름을 변경할 수 있는 'rename_field' 메서드를 제공합니다.

1. 기존 PDF 양식을 로드합니다.
1. 폼에디터 인스턴스를 생성합니다.
1. PDF 문서를 편집기에 바인딩합니다.
1. 대상 필드 이름을 변경합니다.
1. 업데이트된 PDF를 저장합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def rename_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Rename field in document
    form_editor.rename_field("City", "Town")
    # Save updated document
    form_editor.save(outfile)
```


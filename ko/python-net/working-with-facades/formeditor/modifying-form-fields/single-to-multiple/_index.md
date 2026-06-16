---
title: 한 줄 필드를 여러 줄 필드로
linktitle: 한 줄 필드를 여러 줄 필드로
type: docs
weight: 80
url: /ko/python-net/single-to-multiple/
description: Python용 Aspose.PDF 를 사용하여 PDF 문서의 한 줄 텍스트 필드를 여러 줄 필드로 변환합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF의 한 줄 텍스트 필드를 여러 줄 필드로 변환
Abstract: 이 예제에서는 Python용 Aspose.PDF 를 사용하여 PDF 문서의 한 줄 텍스트 필드를 여러 줄 필드로 변환하는 방법을 보여줍니다.코드는 기존 PDF 양식을 로드하고, 여러 줄의 텍스트를 허용하도록 지정된 필드를 수정하고, 업데이트된 문서를 저장합니다.
---

PDF 양식에는 한 줄 입력용으로 설계된 텍스트 필드가 포함되어 있는 경우가 있는데, 이 경우 특정 유형의 데이터에는 충분하지 않을 수 있습니다.Python용 Aspose.PDF 기능을 사용하면 개발자는 이러한 필드를 다시 만들지 않고도 여러 줄 텍스트 필드로 쉽게 변환할 수 있습니다.

를 사용하여 [폼 에디터](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 클래스를 사용하면 개발자는 위치나 기타 속성에 영향을 주지 않고 기존 텍스트 필드를 수정할 수 있습니다.

1. 기존 PDF 문서를 로드합니다.
1. 폼에디터 인스턴스를 생성합니다.
1. PDF 문서를 편집기에 바인딩합니다.
1. 선택한 필드를 여러 줄로 변환합니다.
1. 업데이트된 문서를 저장합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def single2multiple(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Change a single-lined text field to a multiple-lined one
    form_editor.single_2_multiple("City")
    # Save updated document
    form_editor.save(outfile)
```


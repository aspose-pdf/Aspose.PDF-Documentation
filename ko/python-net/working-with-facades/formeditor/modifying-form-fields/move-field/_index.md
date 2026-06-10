---
title: 필드 이동
type: docs
weight: 50
url: /ko/python-net/move-field/
description: 기존 양식 필드를 PDF 문서의 다른 위치로 이동합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 양식 필드를 새 위치로 이동
Abstract: 이 예제에서는 Python용 Aspose.PDF 를 사용하여 기존 양식 필드를 PDF 문서의 다른 위치로 이동하는 방법을 보여줍니다.코드는 기존 PDF를 열고, 지정된 양식 필드를 새 좌표로 재배치하고, 업데이트된 문서를 저장합니다.
---

PDF 양식을 만든 후 레이아웃을 조정해야 하는 경우가 많습니다.개발자는 Python용 Aspose.PDF 파일을 사용하여 기존 양식 필드를 다시 만들지 않고도 새 위치로 이동할 수 있습니다.

이 예제에서는 페이지 내 배치에 사용할 새 좌표를 지정하여 “국가” 필드의 위치를 변경하는 방법을 보여줍니다. [폼 에디터](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 클래스는 PDF 페이지 내에서 필드를 재배치하는 move_field 메서드를 제공합니다.

1. 기존 PDF 양식을 엽니다.
1. 폼에디터 객체를 생성합니다.
1. PDF 문서를 양식 편집기에 바인딩합니다.
1. 좌표를 사용하여 '국가' 필드를 새 위치로 이동합니다.
1. 수정한 문서를 저장합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def move_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Move field to new page
    form_editor.move_field("Country", 200, 600, 280, 620)
    # Save updated document
    form_editor.save(outfile)
```

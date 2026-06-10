---
title: 필드 제거
linktitle: 필드 제거
type: docs
weight: 60
url: /ko/python-net/remove-field/
description: 이 예제에서는 'FormEditor' 클래스의 'remove_field' 메서드를 사용하여 PDF 양식에서 '국가' 필드를 삭제하는 방법을 보여줍니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 문서에서 양식 필드 제거
Abstract: 이 예제에서는 Python용 Aspose.PDF 를 사용하여 PDF 문서에서 기존 양식 필드를 제거하는 방법을 보여줍니다.코드는 PDF 파일을 로드하고, FormEditor 클래스를 사용하여 지정된 필드를 삭제하고, 업데이트된 문서를 저장합니다.
---

PDF 양식에는 디자인 변경이나 워크플로 업데이트로 인해 더 이상 필요하지 않은 필드가 포함될 수 있습니다.Python용 Aspose.PDF 기능을 사용하면 개발자가 프로그래밍 방식으로 특정 양식 필드를 쉽게 제거할 수 있습니다.

더 [폼 에디터](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) Aspose.PDF 클래스는 개발자가 이름으로 양식 필드를 삭제할 수 있는 'remove_field' 메서드를 제공합니다.

1. PDF 문서를 로드합니다.
1. 폼에디터 객체를 생성합니다.
1. PDF를 양식 편집기에 바인딩합니다.
1. 지정된 양식 필드를 제거합니다.
1. 업데이트된 문서를 저장합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Remove field from document
    form_editor.remove_field("Country")
    # Save updated document
    form_editor.save(outfile)
```

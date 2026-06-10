---
title: 필드 제한 설정
type: docs
weight: 80
url: /ko/python-net/set-field-limit/
description: 이 예제에서는 Python용 Aspose.PDF 를 사용하여 PDF 문서의 양식 필드에 최대 문자 제한을 설정하는 방법을 보여줍니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 양식 필드의 최대 문자 제한 설정
Abstract: 이 예제에서는 “성”이라는 이름의 필드에 대한 문자 제한을 10자로 설정하여 사용자가 지정된 제한보다 많이 입력할 수 없도록 하는 방법을 보여 줍니다.
---

PDF 문서의 양식 필드는 적절한 서식을 유지하기 위해 입력 제한이 필요할 수 있습니다.Python용 Aspose.PDF 를 사용하여 개발자는 프로그래밍 방식으로 필드의 최대 문자 수를 설정할 수 있습니다.

더 [폼 에디터](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 클래스는 필드의 최대 입력 길이를 정의하는 'set_field_limit' 메서드를 제공합니다.

1. 기존 PDF 양식을 엽니다.
1. 폼에디터 객체를 생성합니다.
1. “성” 필드의 최대 문자 제한을 설정합니다.
1. 업데이트된 PDF를 저장합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_limit(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field limit to 10
    if not form_editor.set_field_limit("Last Name", 10):
        raise Exception(
            "Failed to set field limit. Field may not support specified limit."
        )

    # Save updated document
    form_editor.save(outfile)
```

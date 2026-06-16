---
title: 목록 항목 추가
linktitle: 목록 항목 추가
type: docs
weight: 10
url: /ko/python-net/add-list-item/
description: 이 예제에서는 Python용 Aspose.PDF 를 사용하여 PDF 문서의 목록 상자 양식 필드에 항목을 추가하는 방법을 보여줍니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 목록 상자 필드에 항목 추가
Abstract: 이 문서에서는 PDF 문서를 열고 “Country”라는 이름의 목록 상자 필드에 항목을 추가하고 업데이트된 문서를 저장하는 방법을 보여 줍니다.
---

PDF의 목록 상자 필드를 사용하면 사전 정의된 집합에서 하나 이상의 옵션을 선택할 수 있습니다.개발자는 Python용 Aspose.PDF 를 사용하여 프로그래밍 방식으로 이러한 필드에 새 항목을 추가할 수 있습니다. [폼 에디터](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 클래스는 기존 목록 상자 필드에 항목을 추가하는 'add_list_item' 메서드를 제공합니다.

1. 기존 PDF 양식을 엽니다.
1. 폼에디터 객체를 생성합니다.
1. PDF를 양식 편집기에 바인딩합니다.
1. 목록 상자 필드 “국가”에 항목을 추가합니다.
1. 업데이트된 문서를 저장합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_list_item(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Add list item to list box field
    form_editor.add_list_item("Country", ["New Zealand", "New Zealand"])
    # Save updated document
    form_editor.save(outfile)
```

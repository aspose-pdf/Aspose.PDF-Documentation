---
title: 목록 항목 삭제
type: docs
weight: 40
url: /ko/python-net/del-list-item/
description:
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 목록 상자 필드에서 항목 제거
Abstract: 이 예제에서는 Python용 Aspose.PDF 를 사용하여 PDF 문서의 목록 상자 양식 필드에서 항목을 제거하는 방법을 보여줍니다.코드는 기존 PDF를 열고, 목록 상자 필드에서 특정 항목을 삭제하고, 업데이트된 문서를 저장합니다.
---

PDF의 목록 상자 필드를 사용하면 미리 정의된 옵션을 하나 또는 여러 개 선택할 수 있습니다.개발자는 Python용 Aspose.PDF 를 사용하여 프로그래밍 방식으로 이러한 필드에서 항목을 제거할 수 있습니다.

이 문서에서는 'Country' 라는 목록 상자 필드에서 'UK' 항목을 삭제하여 필드에 원하는 옵션만 포함하는 방법을 설명합니다.

더 [폼 에디터](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 클래스는 목록 상자 필드에서 특정 항목을 제거하는 'del_list_item' 메서드를 제공합니다.

1. 기존 PDF 양식을 엽니다.
1. 폼에디터 객체를 생성합니다.
1. PDF 문서를 양식 편집기에 바인딩합니다.
1. “국가” 목록 상자 필드에서 “영국” 항목을 삭제합니다.
1. 업데이트된 문서를 저장합니다.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def del_list_item(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Delete list item from list box field
    form_editor.del_list_item("Country", "UK")
    # Save updated document
    form_editor.save(outfile)
```


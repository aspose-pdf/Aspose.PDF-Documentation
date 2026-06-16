---
title: ID별 스탬프 관리
linktitle: ID별 스탬프 관리
type: docs
weight: 95
url: /ko/python-net/manage-stamp-by-id/
description: Python용 Aspose.PDF 를 사용하여 PDF의 러버 스탬프 주석을 고유 ID로 조작하는 방법
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python의 PDFContentEditor를 사용하여 PDF에서 ID별로 러버 스탬프를 관리합니다.
Abstract: 이 예제에서는 Facades API를 통해 Python용 Aspose.PDF 를 사용하여 고유한 ID로 PDF의 러버 스탬프 주석을 조작하는 방법을 보여줍니다.다른 스탬프에 영향을 주지 않고 특정 페이지의 특정 스탬프를 숨기거나 표시할 수 있습니다.
---

러버 스탬프가 여러 개 있는 PDF에서는 ID를 기반으로 개별 스탬프를 제어하는 것이 유용할 수 있습니다.'hide_stamp_by_id () '및 'show_stamp_by_id ()' 메서드를 사용하면 가시성을 선택적으로 제어할 수 있습니다.이 예제에서는 다음과 같은 방법을 보여줍니다.

- 고유 ID로 스탬프 여러 개 추가
- 특정 페이지의 스탬프 숨기기
- 다른 페이지에 스탬프 보기

ID 기반 작업을 사용하면 페이지 위치나 기타 속성별로 스탬프를 추적하지 않아도 됩니다.

1. 만들기 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 예.
1. 입력 PDF 문서를 바인딩합니다.
1. 특정 ID가 있는 러버 스탬프를 추가합니다.
1. ID 및 페이지 번호를 기준으로 스탬프를 숨기고 표시합니다.
1. 업데이트된 PDF 문서를 저장합니다.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def manage_stamp_by_id(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(200, 380, 180, 60),
        "Draft",
        "Draft stamp for ID-based operations",
        apd.Color.orange,
    )

    content_editor.create_rubber_stamp(
        2,
        apd.Rectangle(200, 480, 180, 60),
        "Draft",
        "Draft stamp for ID-based operations",
        apd.Color.orange,
    )

    # Apply ID-based stamp operations
    content_editor.hide_stamp_by_id(1, 1)
    content_editor.show_stamp_by_id(1, 2)

    # Save updated document
    content_editor.save(outfile)
```

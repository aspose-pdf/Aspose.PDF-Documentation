---
title: 리스트 스탬프
linktitle: 리스트 스탬프
type: docs
weight: 70
url: /ko/python-net/list-stamps/
description: 이 예제에서는 PDF를 로드하고, 1페이지에서 모든 스탬프를 검색하고, 인쇄하고, 스탬프가 없는 경우 메시지를 표시합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python의 PDFContentEditor를 사용하여 PDF에 러버 스탬프 주석 나열하기
Abstract: 이 예제는 Facades API를 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에서 러버 스탬프 주석을 검색하고 나열하는 방법을 보여줍니다.특정 페이지의 스탬프에 액세스하여 스탬프의 세부 정보를 표시하는 방법을 보여줍니다.
---

주석이 달린 PDF로 작업할 때는 기존 러버 스탬프를 수정하거나 제거하기 전에 검사해야 할 수 있습니다.'get_stamps () '메서드를 사용하면 특정 페이지에 있는 모든 스탬프를 검색할 수 있습니다.그런 다음 결과를 반복하여 프로그래밍 방식으로 처리할 수 있습니다.

1. 만들기 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 예.
1. 입력 PDF 문서를 바인딩합니다.
1. 1페이지에서 모든 스탬프를 검색합니다.
1. 스탬프 컬렉션을 반복해서 살펴보세요.
1. 각 스탬프를 인쇄합니다.
1. 스탬프가 없는 경우 메시지를 표시합니다.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def list_stamps(infile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # List all stamps on page 1
    stamps = content_editor.get_stamps(1)

    count = 0
    for stamp in stamps:
        count += 1
        print(f"Stamp {count}: {stamp}")

    if count == 0:
        print("No stamps found")
```

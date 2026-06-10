---
title: 사용자 지정 작업 링크 추가
type: docs
weight: 20
url: /ko/python-net/add-custom-action-link/
description: 이 예제에서는 입력 PDF를 바인딩하고, 첫 페이지에 사용자 지정 작업 링크를 추가하고, 수정된 문서를 저장합니다.단순화를 위해 빈 작업 목록을 사용하지만 실제 구현에는 실제 작업이 포함될 수 있습니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python의 PDFContentEditor를 사용하여 PDF에 사용자 지정 작업 링크 추가
Abstract: 이 예제에서는 Facades API를 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에 사용자 지정 작업 링크를 추가하는 방법을 보여줍니다.페이지에 클릭 가능한 영역을 만들고, 사용자 지정 작업을 할당하고, 업데이트된 문서를 저장하는 방법을 보여줍니다.
---

사용자 정의 작업 링크를 사용하면 클릭 시 스크립트 실행, 페이지 탐색 또는 응용 프로그램별 명령 실행과 같은 특정 작업을 트리거할 수 있는 대화형 영역을 PDF에서 정의할 수 있습니다.사용 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)페이지, 사각형, 색상 및 작업을 지정하여 사용자 지정 작업 링크를 만들 수 있습니다.

1. PDF 컨텐트 편집기 인스턴스를 만듭니다.
1. 입력 PDF 문서를 바인딩합니다.
1. 클릭 가능한 링크의 사각형을 정의합니다.
1. 페이지 번호와 링크 색상을 지정합니다.
1. 사용자 지정 작업을 할당합니다 (이 예에서는 비어 있음).
1. 업데이트된 PDF 문서를 저장합니다.

```python
import aspose.pdf.facades as pdf_facades
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as apd
import aspose.pdf as ap

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_custom_action_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add custom action link. Empty action list keeps the sample runnable
    # without requiring additional enum lookups.
    content_editor.create_custom_action_link(
        apd.Rectangle(200, 500, 260, 20),
        1,
        apd.Color.dark_red,
        [],
    )
    # Save updated document
    content_editor.save(outfile)
```

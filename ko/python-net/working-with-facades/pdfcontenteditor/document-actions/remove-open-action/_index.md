---
title: 열린 작업 제거
linktitle: 열린 작업 제거
type: docs
weight: 30
url: /ko/python-net/remove-open-action/
description: 이 예제에서는 기존 PDF를 로드하고, 열린 동작을 제거하고, 정리된 문서를 저장합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에서 문서 열기 동작 제거
Abstract: 이 예제에서는 Facades API를 통해 Python용 Aspose.PDF 를 사용하여 PDF에서 문서 열기 작업을 제거하는 방법을 보여줍니다.PDF를 바인딩하고, 열린 동작을 지우고, 업데이트된 문서를 저장하는 방법을 보여줍니다.
---

PDF 문서에는 JavaScript 경고, 탐색 명령 또는 기타 동작과 같이 파일을 열 때 자동으로 실행되는 동작이 포함될 수 있습니다.일부 시나리오에서는 보안, 규정 준수 또는 사용자 경험을 위해 이러한 작업을 제거해야 할 수 있습니다.

PDFContentEditor를 사용하면 문서 열기 작업을 쉽게 제거하고 자동 동작을 실행하지 않고도 PDF가 열리도록 할 수 있습니다.

1. PDF 컨텐트 편집기 객체를 만듭니다.
1. 입력 PDF를 바인딩합니다.
1. 문서 열기 작업을 제거합니다.
1. 업데이트된 문서를 저장합니다.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_open_action(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Remove open action from the document
    content_editor.remove_document_open_action()
    # Save updated document
    content_editor.save(outfile)
```

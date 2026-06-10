---
title: 문서 추가 작업
type: docs
weight: 20
url: /ko/python-net/add-document-action/
description: 이 예제에서는 PDF를 열 때 나타나는 JavaScript 경고를 추가합니다.스크립트는 문서 열기 이벤트에 첨부되고 지원되는 PDF 뷰어에서 자동으로 실행됩니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에 문서 열기 자바스크립트 작업 추가
Abstract: 이 예제에서는 PDF를 열 때 트리거되는 문서 수준의 JavaScript 작업을 추가하는 방법을 보여 줍니다.이 샘플은 Facades API를 통해 Python용 Aspose.PDF 를 사용하여 문서를 바인딩하고, 열린 이벤트 작업을 할당하고, 업데이트된 PDF를 저장하는 방법을 보여줍니다.
---

문서 레벨 액션을 사용하면 PDF 열기와 같은 특정 이벤트가 발생할 때 자동으로 실행되는 동작을 정의할 수 있습니다.와 함께 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), 이러한 이벤트에 자바스크립트 코드를 첨부할 수 있습니다.알림, 검증 로직 또는 대화형 워크플로에 사용할 수 있습니다.

1. PDF 컨텐트 편집기 객체를 만듭니다.
1. 입력 PDF를 바인딩합니다.
1. 문서 수준 작업 추가
1. 업데이트된 문서를 저장합니다.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_document_action(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add JavaScript action for document open event
    content_editor.add_document_additional_action(
        content_editor.DOCUMENT_OPEN,
        "app.alert('Document opened with PdfContentEditor action');",
    )
    # Save updated document
    content_editor.save(outfile)
```

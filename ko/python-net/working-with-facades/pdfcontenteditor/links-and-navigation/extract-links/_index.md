---
title: 링크 추출
type: docs
weight: 70
url: /ko/python-net/extract-links/
description: 이 예제에서는 입력 PDF를 바인딩하고, 모든 링크를 추출하고, 해당 좌표와 URI를 인쇄합니다 (사용 가능한 경우).
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python의 PDF 콘텐츠 편집기를 사용하여 PDF에서 링크 추출
Abstract: 이 예제는 Python용 Aspose.PDF 를 사용하여 Facades API를 통해 PDF 문서에서 모든 링크를 추출하는 방법을 보여줍니다.PDF에 포함된 웹 링크 또는 기타 실행 가능한 링크를 식별하고 검색하는 방법을 보여줍니다.
---

PDF에는 웹 링크, 문서 링크 및 사용자 지정 작업과 같은 대화형 요소가 포함되어 있는 경우가 많습니다.사용 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), PDF에서 프로그래밍 방식으로 모든 링크 주석을 추출할 수 있습니다.이를 통해 링크를 검사하거나 처리할 수 있습니다. 예를 들어 URL의 유효성을 검사하거나 문서의 탐색 패턴을 분석할 수 있습니다.

1. PDF 컨텐트 편집기 인스턴스를 만듭니다.
1. 입력 PDF 문서를 바인딩합니다.
1. 'extract_link () '를 사용하여 모든 링크를 추출합니다.
1. 추출된 링크를 반복합니다.
1. 링크가 링크 주석인지, 해당 동작이 GoTouriAction인지 확인하세요.
1. 사각형 좌표와 URI를 출력합니다.
1. 링크를 찾을 수 없는 경우 메시지를 표시합니다.

```python
import aspose.pdf.facades as pdf_facades
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as apd
import aspose.pdf as ap

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def extract_links(infile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Extract links from the document
    links = content_editor.extract_link()

    count = 0
    for link in links:
        count += 1
        print(f"Link {count}: {link.rect}")
        if is_assignable(link, ap.annotations.LinkAnnotation):
            annotation = cast(ap.annotations.LinkAnnotation, link)
            if is_assignable(annotation.action, ap.annotations.GoToURIAction):
                action = cast(ap.annotations.GoToURIAction, annotation.action)
                print(f"  URI: {action.uri}")

    if count == 0:
        print("No links found")
```

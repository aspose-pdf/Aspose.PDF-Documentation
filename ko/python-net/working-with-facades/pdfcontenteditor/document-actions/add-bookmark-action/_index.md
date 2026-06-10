---
title: 북마크 작업 추가
type: docs
weight: 10
url: /ko/python-net/add-bookmark-action/
description: 이 예제에서는 입력 PDF를 바인딩하고 1페이지로 이동하는 “PDFContentEditor 책갈피”라는 레이블이 붙은 책갈피를 만들고 업데이트된 문서를 저장합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에서 탐색 액션이 포함된 북마크 만들기
Abstract: 이 예제에서는 Facades API를 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에 탐색 작업이 포함된 북마크를 추가하는 방법을 보여줍니다.북마크 텍스트, 모양 및 사용자를 특정 페이지로 안내하는 작업을 구성하는 방법을 보여줍니다.
---

북마크를 사용하면 PDF 문서 내에서 빠르게 탐색할 수 있습니다.사용 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)프로그래밍 방식으로 북마크를 생성하고 페이지 탐색과 같은 작업을 할당할 수 있습니다.굵게 또는 기울임꼴과 같은 색상 및 스타일 옵션을 포함하여 책갈피 모양을 사용자 지정할 수도 있습니다.

1. PDF 컨텐트 편집기 객체를 만듭니다.
1. 입력 PDF를 바인딩합니다.
1. 북마크 속성을 정의합니다.
1. 북마크 작업을 할당합니다.
1. 업데이트된 문서를 저장합니다.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_bookmark_action(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add a bookmark action to navigate to page 1
    content_editor.create_bookmarks_action(
        "PdfContentEditor Bookmark",
        apd.Color.blue,
        True,
        False,
        "",
        "GoTo",
        "1",
    )
    # Save updated document
    content_editor.save(outfile)
```
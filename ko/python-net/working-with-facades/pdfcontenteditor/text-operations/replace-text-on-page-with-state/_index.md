---
title: 페이지의 텍스트를 상태로 바꾸기
type: docs
weight: 20
url: /ko/python-net/replace-text-on-page-with-state/
description: 이 예에서는 글꼴 크기가 12인 빨간색 텍스트를 사용하여 페이지 1에 있는 “소프트웨어”라는 단어가 모두 “SOFTWARE PAGE 1"로 바뀝니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬에서 PDFContentEditor를 사용하여 특정 페이지에서 텍스트를 사용자 지정 서식으로 바꾸기
Abstract: 이 예제에서는 Facades API를 통해 Python용 Aspose.PDF 를 사용하여 사용자 지정 서식을 적용하면서 PDF의 특정 페이지에 있는 텍스트를 바꾸는 방법을 보여줍니다.텍스트 교체 시 글꼴 크기 및 색상을 제어하는 방법을 보여줍니다.
---

PDF에서 텍스트를 바꾸려면 색상이나 글꼴 크기와 같은 서식 변경도 필요할 수 있습니다.TextState를 사용하여 스타일 속성을 정의하고 교체 중에 적용할 수 있습니다.이렇게 하면 수정된 텍스트를 강조 표시하거나 문서 전체에 일관된 서식을 적용할 수 있습니다.

1. 만들기 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 예.
1. 입력 PDF 문서를 바인딩합니다.
1. 사용자 지정 서식을 사용하여 TextState를 정의합니다.
1. 교체 전략을 구성합니다.
1. 특정 페이지의 텍스트를 바꿉니다.
1. 업데이트된 PDF 문서를 저장합니다.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_on_page_with_state(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.red
    text_state.font_size = 12

    # Replace text on a specific page with explicit text formatting
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text("software", 1, "SOFTWARE PAGE 1", text_state)
    # Save updated document
    content_editor.save(outfile)
```

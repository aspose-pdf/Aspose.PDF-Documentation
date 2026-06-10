---
title: 텍스트를 상태로 바꾸기
type: docs
weight: 50
url: /ko/python-net/replace-text-with-state/
description: 이 예에서는 “소프트웨어”가 모두 “SOFTWARE”로 바뀌고 글꼴 크기가 14인 파란색 서식이 지정됩니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python의 PDFContentEditor를 사용하여 PDF에서 텍스트를 사용자 지정 서식으로 바꾸기
Abstract: 이 예제는 Facades API를 통해 Python용 Aspose.PDF 를 사용하여 사용자 지정 서식을 적용하면서 PDF 문서의 텍스트를 바꾸는 방법을 보여줍니다.바꿀 때 텍스트 색상과 글꼴 크기를 제어하는 방법을 보여줍니다.
---

PDF에서 텍스트를 업데이트할 때 대체 내용이 눈에 잘 띄도록 해야 할 수 있습니다.TextState 객체를 사용하여 색상 및 글꼴 크기와 같은 스타일을 정의한 다음 대체된 모든 텍스트에 적용할 수 있습니다.

1. 만들기 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)  예.
1. 입력 PDF 문서를 바인딩합니다.
1. 사용자 지정 서식을 사용하여 TextState를 정의합니다.
1. 교체 범위를 구성합니다.
1. 전체 문서에서 텍스트를 바꿉니다.
1. 업데이트된 PDF 문서를 저장합니다.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_with_state(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.blue
    text_state.font_size = 14

    # Replace text with explicit text formatting
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text("software", "SOFTWARE", text_state)
    # Save updated document
    content_editor.save(outfile)
```

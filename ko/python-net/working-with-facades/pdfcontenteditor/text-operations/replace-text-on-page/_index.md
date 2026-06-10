---
title: 페이지의 텍스트 바꾸기
linktitle: 페이지의 텍스트 바꾸기
type: docs
weight: 10
url: /ko/python-net/replace-text-on-page/
description: 이 예에서는 “PDF”라는 단어가 처음 나타나는 부분이 지정된 글꼴 크기를 사용하여 “페이지 1이 대체된 텍스트”로 바뀝니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python의 PDFContentEditor를 사용하여 특정 페이지의 텍스트 바꾸기
Abstract: 이 예제에서는 Facades API를 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서의 텍스트를 바꾸는 방법을 보여줍니다.페이지에서 처음 나타나는 텍스트를 바꾸고 업데이트된 문서를 저장하는 방법을 보여줍니다.
---

텍스트 교체는 PDF 문서를 업데이트할 때 일반적으로 필요한 요구 사항입니다.사용 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), 특정 텍스트를 검색하고 새 내용으로 바꿀 수 있습니다.'replace_text_strategy '속성을 사용하면 대체되는 항목 수를 제어할 수 있습니다.

1. PDF 컨텐트 편집기 인스턴스를 만듭니다.
1. 입력 PDF 문서를 바인딩합니다.
1. 텍스트 대체 전략을 구성합니다.
1. 대상 텍스트를 바꿉니다.
1. 업데이트된 PDF 문서를 저장합니다.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_on_page(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace text on page 1
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_FIRST
    )
    content_editor.replace_text("PDF", "Page 1 Replaced Text", 14)
    # Save updated document
    content_editor.save(outfile)
```

---
title: 텍스트 단순 바꾸기
type: docs
weight: 40
url: /ko/python-net/replace-text-simple/
description: 이 예에서는 전체 문서에서 “33"이 모두 “XXXIII”로 바뀝니다.이는 사용자 지정 서식 또는 정규식 없이 문자열을 간단하게 대체하는 방법을 보여줍니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python의 PDF 콘텐츠 편집기를 사용하여 PDF에서 텍스트 바꾸기
Abstract: 이 예제에서는 Facades API를 통해 Python용 Aspose.PDF 를 사용하여 전체 PDF 문서에서 텍스트를 바꾸는 방법을 보여줍니다.지정된 문자열의 모든 항목을 새 텍스트로 바꿉니다.
---

간단한 텍스트 대체는 문서에서 반복되는 값을 업데이트할 때 유용합니다.를 사용하여 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), 대체 범위를 정의하고 모든 페이지에서 텍스트를 전역으로 대체할 수 있습니다.

1. 만들기 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 예.
1. 입력 PDF 문서를 바인딩합니다.
1. 모든 항목에 대한 교체 범위를 구성합니다.
1. 대상 텍스트를 바꿉니다.
1. 업데이트된 PDF 문서를 저장합니다.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_simple(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace text in the whole document
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text("33", "XXXIII ")
    # Save updated document
    content_editor.save(outfile)
```

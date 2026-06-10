---
title: 텍스트 정규식 바꾸기
type: docs
weight: 30
url: /ko/python-net/replace-text-regex/
description: 이 예에서는 문서의 모든 4자리 숫자가 자리 표시자 “[NUMBER]”로 바뀝니다.이는 민감한 데이터를 마스킹하거나, 콘텐츠를 정규화하거나, 문서를 익명화하는 데 유용합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 정규 표현식을 사용하여 텍스트를 Python의 PDFContentEditor로 바꾸기
Abstract: 이 예제에서는 정규 표현식을 사용하여 PDF의 텍스트를 Facades API를 통해 Python용 Aspose.PDF 로 바꾸는 방법을 보여줍니다.패턴을 검색하고 문서 전체에서 일치하는 모든 항목을 바꾸는 방법을 보여줍니다.
---

정규 표현식을 사용하면 고정된 문자열 대신 패턴을 기반으로 유연한 텍스트 교체가 가능합니다.'replace_text_strategy'에서 정규식 지원을 활성화하면 숫자, 날짜 또는 서식이 지정된 문자열과 같은 동적 콘텐츠를 일치시킬 수 있습니다.

1. 만들기 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 예.
1. 입력 PDF 문서를 바인딩합니다.
1. regex를 사용하도록 대체 전략을 구성합니다.
1. 전체 문서에서 일치하는 패턴을 바꿉니다.
1. 업데이트된 PDF 문서를 저장합니다.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_regex(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace text in the whole document
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text_strategy.is_regular_expression_used = True
    content_editor.replace_text(r"\d{4}", "[NUMBER]")
    # Save updated document
    content_editor.save(outfile)
```

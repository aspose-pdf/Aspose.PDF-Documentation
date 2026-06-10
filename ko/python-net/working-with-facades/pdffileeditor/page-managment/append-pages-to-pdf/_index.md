---
title: PDF에 페이지 추가
linktitle: PDF에 페이지 추가
type: docs
weight: 10
url: /ko/python-net/append-pages-to-pdf/
description: 파이썬용 Aspose.PDF 를 사용하여 한 PDF 문서의 페이지를 다른 PDF 문서에 추가합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 한 PDF에서 다른 PDF로 페이지 추가
Abstract: Python용 Aspose.PDF 를 사용하여 한 PDF 문서의 페이지를 다른 PDF 문서에 추가하는 방법을 알아봅니다.이 예제에서는 PDFFileEditor 클래스를 사용하여 여러 PDF의 페이지를 결합하고 단일 출력 문서를 만드는 방법을 보여줍니다.
---

서로 다른 PDF 문서의 페이지를 결합하는 것은 문서 처리 워크플로의 일반적인 요구 사항입니다.개발자는 Python용 Aspose.PDF 를 사용하여 하나 이상의 PDF 파일에 있는 페이지를 기존 문서에 쉽게 추가할 수 있습니다.

이 코드 스니펫은 의 append 메서드를 사용하는 방법을 보여줍니다. [PDF 파일 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) 다른 PDF 파일에서 선택한 페이지를 소스 PDF의 끝에 추가하는 클래스입니다.페이지 범위를 지정하여 개발자는 최종 문서에 포함되는 페이지를 정확히 제어할 수 있습니다.

1. PDF 파일 편집기 개체 만들기
1. 다른 PDF에서 페이지를 추가합니다.

보조 PDF 문서의 지정된 페이지가 원본 PDF의 끝에 추가되어 결합된 출력 파일이 만들어집니다.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


# Append Pages to PDF
def append_pages_to_pdf(infile, sample_file, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    # Append pages from the specified PDF document to the end of the source PDF document
    pdf_editor.append(infile, [sample_file], 1, 2, outfile)
```

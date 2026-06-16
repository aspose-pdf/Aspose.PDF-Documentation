---
title: PDF에서 페이지 추출
linktitle: PDF에서 페이지 추출
type: docs
weight: 30
url: /ko/python-net/extract-pages-from-pdf/
description: 파이썬용 Aspose.PDF 파일을 사용하여 PDF 문서에서 선택한 페이지를 추출합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 PDF 문서에서 특정 페이지 추출하기
Abstract: Python용 Aspose.PDF 파일을 사용하여 PDF 문서에서 선택한 페이지를 추출하는 방법을 알아봅니다.이 예제에서는 필요한 페이지만 포함하는 새 PDF를 생성하여 사용자 지정 문서 생성 및 페이지 수준 조작을 가능하게 하는 방법을 보여줍니다.
---

PDF에서 페이지를 추출하면 문서의 하위 세트를 만들거나, 특정 내용만 공유하거나, 프레젠테이션, 보고서 또는 인쇄를 위해 PDF를 다시 구성해야 할 때 유용합니다.개발자는 Python용 Aspose.PDF 를 사용하여 프로그래밍 방식으로 PDF 파일에서 페이지를 추출하고 새 문서로 저장할 수 있습니다.

의 추출 방법 사용 방법 알아보기 [PDF 파일 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) 수업.추출할 페이지 목록을 지정하면 원본 내용과 서식을 유지하면서 선택한 페이지만 포함하는 새 PDF를 생성할 수 있습니다.

1. PDF 파일 편집기 개체 만들기
1. 추출할 페이지를 정의합니다.
1. 페이지를 추출합니다.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


# Extract Pages from PDF
def extract_pages_from_pdf(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()

    # Define the page numbers to be extracted (1-based index)
    pages_to_extract = [1, 4, 3]

    # Extract the specified pages from the PDF document and save to a new PDF document
    pdf_editor.extract(infile, pages_to_extract, outfile)
```

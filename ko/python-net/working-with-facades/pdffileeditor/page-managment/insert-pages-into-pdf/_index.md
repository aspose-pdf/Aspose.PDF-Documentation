---
title: PDF에 페이지 삽입
linktitle: PDF에 페이지 삽입
type: docs
weight: 40
url: /ko/python-net/insert-pages-into-pdf/
description: 파이썬용 Aspose.PDF 를 사용하여 한 PDF의 페이지를 다른 PDF로 삽입합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 다른 PDF의 페이지를 기존 PDF에 삽입하기
Abstract: Python용 Aspose.PDF 를 사용하여 한 PDF의 페이지를 다른 PDF로 삽입하는 방법을 알아봅니다.이 예제에서는 보조 PDF에서 선택한 페이지를 원본 문서의 특정 위치에 추가하여 정확한 페이지 배치를 통해 결합된 PDF를 만드는 방법을 보여줍니다.
---

기존 PDF에 페이지를 삽입하는 것은 문서를 결합하거나, 내용을 추가하거나, 보고서를 재구성할 때 일반적으로 필요한 사항입니다.개발자는 Python용 Aspose.PDF 페이지를 사용하여 프로그래밍 방식으로 특정 위치에 있는 한 PDF의 다른 PDF에 페이지를 삽입할 수 있습니다.

이 문서에서는 의 insert 메서드를 사용하는 방법을 보여줍니다. [PDF 파일 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) 수업.삽입할 페이지 번호와 대상 위치를 지정하여 원래 형식과 구조를 유지하면서 여러 PDF의 내용을 병합할 수 있습니다.

1. PDF 파일 편집기 개체 만들기
1. 삽입 위치 및 페이지를 정의합니다.
1. 페이지 삽입.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


# Insert Pages into PDF
def insert_pages_into_pdf(infile, sample_file, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()

    # Define the page number where new pages will be inserted (1-based index)
    insert_page_number = 2

    pdf_editor.insert(infile, insert_page_number, sample_file, [1, 2], outfile)
```

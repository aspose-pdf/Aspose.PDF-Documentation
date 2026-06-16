---
title: PDF 소책자 만들기
linktitle: PDF 소책자 만들기
type: docs
weight: 20
url: /ko/python-net/create-pdf-booklet/
description: 파이썬용 Aspose.PDF 파일을 사용하여 기존 문서에서 소책자 스타일의 PDF를 생성합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 기존 PDF에서 PDF 소책자 만들기
Abstract: Python용 Aspose.PDF 파일을 사용하여 기존 문서에서 소책자 스타일의 PDF를 생성하는 방법을 알아봅니다.이 예제에서는 PDFFileEditor 클래스를 사용하여 페이지를 다시 정렬하여 소책자로 인쇄하고 접을 수 있는 방법을 보여줍니다.메서드는 페이지 순서를 자동으로 지정하여 적절한 소책자 레이아웃을 생성합니다.
---

인쇄용 PDF를 준비할 때 일반적으로 소책자 스타일의 문서를 만들어야 합니다.소책자 레이아웃에서는 인쇄 및 접었을 때 페이지가 올바른 순서로 표시되도록 페이지가 재정렬됩니다.

개발자는 Python용 Aspose.PDF 파일을 사용하여 표준 PDF를 소책자로 쉽게 변환할 수 있습니다. [PDF 파일 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) 수업.'make_booklet' 메서드는 입력 문서의 페이지를 자동으로 재구성하고 소책자 인쇄에 최적화된 새 PDF를 생성합니다.

1. 기존 PDF 문서를 엽니다.
1. PDF 파일 편집기 인스턴스를 생성합니다.
1. make_booklet 메서드를 사용하여 페이지를 재구성하십시오.
1. 출력을 소책자에 바로 사용할 수 있는 PDF 파일로 저장합니다.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Create PDF Booklet
def create_pdf_booklet(infile, outfile):
    # Create BookletMaker object
    booklet_maker = pdf_facades.PdfFileEditor()
    # Make booklet from input PDF file and save to output PDF file
    booklet_maker.make_booklet(FileIO(infile), FileIO(outfile, "w"))
```

이 코드 스니펫은 'try_make_booklet' 메서드를 사용하는 방법을 보여줍니다. [PDF 파일 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) 작업이 실패할 경우 예외를 발생시키지 않고 소책자 인쇄용 페이지를 재정렬하는 클래스입니다.

소책자 레이아웃은 인쇄 및 접었을 때 문서가 올바른 순서로 읽히도록 페이지를 재정렬합니다.이 프로세스를 자동화하면 일관된 결과를 얻을 수 있으며 수동으로 페이지를 재배열할 필요가 없습니다.

'try_make_booklet' 메서드는 'make_booklet'과 유사하게 작동하지만 중요한 차이점이 있습니다.

- 작업이 실패하면 'make_booklet'에서 예외가 발생합니다.
- 'try_make_booklet'은 True 또는 False를 반환하므로 개발자가 오류를 보다 안전하게 관리할 수 있습니다.

1. 기존 PDF 문서를 엽니다.
1. PDF 파일 편집기 인스턴스를 생성합니다.
1. 소책자 만들기를 시도해 보십시오.
1. 결과를 처리하십시오.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def try_create_pdf_booklet(infile, outfile):
    # Create BookletMaker object
    booklet_maker = pdf_facades.PdfFileEditor()
    # Make booklet from input PDF file and save to output PDF file
    # The try_make_booklet method is like the make_booklet method,
    # except the try_make_booklet method does not throw an exception if the operation fails.
    if not booklet_maker.try_make_booklet(FileIO(infile), FileIO(outfile, "w")):
        print("Failed to create booklet.")
```

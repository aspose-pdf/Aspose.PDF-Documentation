---
title: N-업 PDF 문서 만들기
type: docs
weight: 10
url: /ko/python-net/create-n-up-pdf-document/
description: Python용 Aspose.PDF 를 사용하여 잠재적 오류를 안전하게 처리하면서 N-Up PDF 문서를 만드는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬으로 N-Up PDF 레이아웃 만들기
Abstract: 파이썬용 Aspose.PDF 파일을 사용하여 N-Up PDF 레이아웃을 생성하는 방법을 알아보세요.이 예제에서는 PDFFileEditor 클래스의 'make_n_up' 또는 'try_make_n_up' 메서드를 사용하여 PDF 문서의 여러 페이지를 단일 페이지로 결합하는 방법을 보여줍니다.
---

N-Up 레이아웃은 PDF 문서의 여러 페이지를 격자 형식의 단일 페이지에 배치합니다.이 레이아웃은 한 번에 여러 페이지를 볼 수 있는 프레젠테이션, 유인물 또는 보고서를 인쇄하는 데 주로 사용됩니다.

개발자는 Aspose.PDF for Python을 사용하여 각 출력 페이지에 표시되는 원본 페이지 수를 결정하는 행과 열의 수를 지정하여 N-Up 문서를 빠르게 만들 수 있습니다.

이 코드 스니펫에서 'make_n_up' 메서드는 [PDF 파일 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) 클래스는 입력 PDF의 페이지를 2x2 격자로 정렬합니다. 즉, 출력 문서의 한 페이지에 원본 페이지 4개가 표시됩니다.

표시된 예에서 레이아웃은 2행 2열과 2열을 사용하여 시트당 4페이지를 생성합니다.

1. 원본 PDF 파일을 엽니다.
1. PDF 파일 편집기 인스턴스를 생성합니다.
1. N-Up 레이아웃의 행 및 열 수를 지정합니다.
1. 페이지가 결합된 새 PDF를 생성합니다.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Create N-Up PDF Document
def create_nup_pdf_document(infile, outfile):
    # Create NUpMaker object
    nup_maker = pdf_facades.PdfFileEditor()
    # Make N-Up layout from input PDF file and save to output PDF file
    nup_maker.make_n_up(
        FileIO(infile), FileIO(outfile, "w"), 2, 2
    )  # 2 rows and 2 columns for N-Up layout
```

.NET을 통한 파이썬용 Aspose.PDF 파일을 사용하면 PDFFileEditor 클래스를 사용하여 N-Up 레이아웃을 생성할 수 있습니다.'try_make_n_up' 메서드는 make_n_up과 비슷하게 작동하지만, 작업 실패 시 예외를 발생시키는 대신 프로세스의 성공 여부를 나타내는 부울 값을 반환합니다.

N-Up 레이아웃은 행과 열로 정의된 격자를 사용하여 한 페이지에 여러 PDF 페이지를 정렬합니다.

'try_make_n_up' 메서드는 다음과 같은 이유로 이 작업을 더 안전하게 수행할 수 있는 방법을 제공합니다.

- 레이아웃이 성공적으로 생성되면 True를 반환합니다.
- 작업이 실패하면 False를 반환합니다.
- 예외를 제외하고 프로그램 실행을 중단하지 않습니다.

아래 예에서는 각 출력 페이지에 원본 페이지 4장을 배치하는 2 × 2 격자를 사용하여 문서를 정렬합니다.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Create N-Up PDF Document
def try_create_nup_pdf_document(infile, outfile):
    # Create NUpMaker object
    nup_maker = pdf_facades.PdfFileEditor()
    # Make N-Up layout from input PDF file and save to output PDF file
    if not nup_maker.try_make_n_up(FileIO(infile), FileIO(outfile, "w"), 2, 2):
        print("Failed to create N-Up PDF document.")
```

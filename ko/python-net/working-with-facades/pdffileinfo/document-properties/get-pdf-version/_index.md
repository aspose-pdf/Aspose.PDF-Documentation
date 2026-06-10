---
title: PDF 버전 가져오기
type: docs
weight: 20
url: /ko/python-net/get-pdf-version/
description: Python용 Aspose.PDF 를 사용하여 프로그래밍 방식으로 PDF 문서의 버전을 결정하는 방법을 알아봅니다.이 자습서에서는 PDFFileInfo 클래스를 사용하여 파일의 PDF 버전을 확인하는 방법을 보여줍니다.
lastmod: "2026-06-10"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬용 Aspose.PDF 파일을 사용하여 PDF 버전 가져오기
Abstract: PDF 문서에는 지원하는 기능 및 사양 (예: 1.4, 1.7, 2.0) 을 나타내는 버전 번호가 있습니다.PDF 버전을 아는 것은 호환성, 기능 지원 및 문서 처리 워크플로우에 중요합니다.이 가이드에서는 파이썬용 Aspose.PDF 내의 PDFFileInfo 클래스를 사용하여 프로그래밍 방식으로 PDF 버전을 검색하는 방법을 배웁니다.
---

PDF 버전은 양식 필드, 암호화, 주석 및 압축을 포함하여 문서에서 지원되는 기능을 정의합니다.여러 PDF로 작업하는 개발자의 경우 버전을 확인하면 이러한 파일을 처리하는 도구, 라이브러리 또는 워크플로우와의 호환성이 보장됩니다.

파이썬용 Aspose.PDF 파일을 사용하면 다음과 같이 PDF 버전을 쉽게 검사할 수 있습니다. [PDF 파일 정보](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) 수업.

1. PDF 문서를 로드합니다.
1. 해당 PDF 버전을 검색합니다.
1. 콘솔에 버전을 표시합니다.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_pdf_version(input_file_name):

    pdf_metadata = pdf_facades.PdfFileInfo(input_file_name)
    version = pdf_metadata.get_pdf_version()
    print(f"\nPDF Version: {version}")
```

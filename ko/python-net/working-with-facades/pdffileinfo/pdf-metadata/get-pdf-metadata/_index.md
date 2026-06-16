---
title: PDF 메타데이터 가져오기
linktitle: PDF 메타데이터 가져오기
type: docs
weight: 20
url: /ko/python-net/get-pdf-metadata/
description: Python용 Aspose.PDF 를 사용하여 PDF 문서에서 메타데이터를 추출하고 표시합니다.
lastmod: "2026-06-10"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬용 Aspose.PDF 를 사용하여 PDF 메타데이터를 검색하는 중입니다.
Abstract: 이 안내서는 Python용 Aspose.PDF 를 사용하여 PDF 문서에서 메타데이터를 추출하고 표시하는 방법을 보여줍니다.제목, 작성자, 키워드, 생성/수정 날짜, 사용자 지정 메타데이터 필드와 같은 표준 PDF 속성에 액세스하는 방법을 배우게 됩니다.또한 이 가이드에서는 PDF 유효성, 암호화 및 포트폴리오 상태에 대한 검사도 다룹니다.
---

PDF 문서에는 문서 내용, 저자 및 권한을 설명하는 중요한 메타데이터가 포함되어 있는 경우가 많습니다.Aspose.PDF 는 표준 및 사용자 지정 메타데이터 속성을 모두 검색할 수 있는 편리한 API를 제공합니다.이 코드 스니펫은 사용 방법을 설명합니다. [PDF 파일 정보](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) Python의 단계별 예제를 포함하여 프로그래밍 방식으로 PDF 파일을 검사하는 클래스입니다.

1. PDF 파일을 로드합니다.
1. 표준 메타데이터를 검색합니다.
1. PDF 상태 및 보안을 확인합니다.
1. 사용자 지정 메타데이터를 검색합니다.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_pdf_metadata(infile):

    # Get and display PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)
    print(f"Subject: {pdf_info.subject}")
    print(f"Title: {pdf_info.title}")
    print(f"Keywords: {pdf_info.keywords}")
    print(f"Creator: {pdf_info.creator}")
    print(f"Creation Date: {pdf_info.creation_date}")
    print(f"Modification Date: {pdf_info.mod_date}")

    # Check PDF status
    print(f"Is Valid PDF: {pdf_info.is_pdf_file}")
    print(f"Is Encrypted: {pdf_info.is_encrypted}")
    print(f"Has Open Password: {pdf_info.has_open_password}")
    print(f"Has Edit Password: {pdf_info.has_edit_password}")
    print(f"Is Portfolio: {pdf_info.has_collection}")

    # Retrieve and display a specific custom attribute
    reviewer = pdf_info.get_meta_info("Reviewer")
    print(f"Reviewer: {reviewer if reviewer else 'No Reviewer metadata found.'}")
```

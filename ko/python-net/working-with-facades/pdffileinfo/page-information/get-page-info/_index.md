---
title: 페이지 정보 가져오기
type: docs
weight: 10
url: /ko/python-net/get-page-info/
description: Python용 Aspose.PDF 를 사용하여 PDF의 페이지 수준 정보에 프로그래밍 방식으로 액세스하는 방법을 알아봅니다.이 안내서는 PDF 문서의 특정 페이지에 대한 페이지 너비, 높이, 회전 및 오프셋을 검색하는 방법을 보여줍니다.
lastmod: "2026-06-10"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬용 Aspose.PDF 를 사용하여 PDF 페이지 정보 가져오기
Abstract: 이 함수는 PDF 페이지의 너비, 높이, 회전, 가로 (X) 및 세로 (Y) 오프셋을 추출합니다.이러한 속성은 포인트 단위로 반환되며 페이지의 물리적 크기 및 PDF 내 내용 위치를 반영합니다.이 함수는 검색된 값을 인쇄하므로 개발자는 향후 PDF 조작에 필요한 페이지 레이아웃과 방향을 이해할 수 있습니다.
---

'get_page_information '유틸리티 함수는 개발자가 PDF 페이지의 구조와 레이아웃을 이해하는 데 도움이 됩니다.PDF 페이지마다 크기, 회전 및 내부 오프셋이 다를 수 있으며, 이는 콘텐츠 배치 또는 자동화 작업에 영향을 미칠 수 있습니다.

PDF 파일의 특정 페이지에 대한 주요 메타데이터 및 레이아웃 정보를 검색하는 기능이 있습니다.Aspose.PDF Facades API는 페이지 너비, 높이, 회전 및 X/Y 오프셋과 같은 세부 정보를 제공합니다.이 정보는 페이지 레이아웃 분석, 주석 배치 또는 자동화된 PDF 처리와 같은 작업에 필수적입니다.

1. PDF 파사드 오브젝트 만들기
1. 페이지 크기 및 레이아웃을 검색합니다.
1. 검색된 값을 인쇄하거나 저장합니다.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_page_information(infile):

    # Get and display PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)
    page_width = pdf_info.get_page_width(1)
    page_height = pdf_info.get_page_height(1)
    page_rotation = pdf_info.get_page_rotation(1)
    page_x_offset = pdf_info.get_page_x_offset(1)
    page_y_offset = pdf_info.get_page_y_offset(1)

    print(f"Page Width: {page_width}")
    print(f"Page Height: {page_height}")
    print(f"Page Rotation: {page_rotation}")
```

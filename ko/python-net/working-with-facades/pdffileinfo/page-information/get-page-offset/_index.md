---
title: 페이지 오프셋 가져오기
type: docs
weight: 20
url: /ko/python-net/get-page-offset/
description: 이 예제에서는 PDFFileInfo를 사용하여 특정 페이지의 X 및 Y 오프셋을 가져와서 정확한 레이아웃 및 위치 분석을 위해 이를 인치로 변환하는 방법을 보여줍니다.
lastmod: "2026-06-10"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 페이지 오프셋 가져오기
Abstract: >
    'get_page_offsets' 함수는 PDF 파일에 있는 각 페이지의 가로 (X) 및 세로 (Y) 오프셋을 추출합니다.이러한 오프셋은 PDF 원점을 기준으로 한 페이지 내용의 위치를 나타냅니다.이 함수는 포인트를 인치로 변환하여 주석, 이미지 또는 텍스트를 정확하게 배치하는 데 사용할 수 있는 정확하고 사람이 읽을 수 있는 측정값을 제공합니다.여러 페이지로 구성된 PDF를 지원하며 PDF 레이아웃, 자동화 또는 콘텐츠 정렬 작업을 수행하는 개발자를 위한 것입니다.
---

'get_page_offsets' 함수는 개발자에게 PDF 파일 내 페이지의 정확한 가로 (X) 및 세로 (Y) 오프셋을 제공합니다.PDF 문서에서 각 페이지에는 페이지 왼쪽 상단 모서리와 다른 내부 원점이 있을 수 있으며, 이는 텍스트, 이미지, 주석 또는 기타 내용의 위치에 영향을 줄 수 있습니다.

이 함수는 Aspose.PDF Facades를 사용하여 이러한 오프셋을 포인트 단위로 추출하고 쉽게 해석할 수 있도록 인치로 변환합니다.여러 페이지로 구성된 PDF를 지원하므로 정확한 콘텐츠 배치가 필요한 자동화된 워크플로우에 적합합니다.

1. PDF 파사드 오브젝트 만들기
1. PDF의 페이지 수를 구합니다.
1. 각 페이지를 반복하여 오프셋을 가져오세요.
1. 오프셋을 인쇄하거나 저장합니다.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_page_offsets(infile):
    # Get and display PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)
    page_x_offset = pdf_info.get_page_x_offset(1) / 72.0
    page_y_offset = pdf_info.get_page_y_offset(1) / 72.0
    print(f"Page X Offset: {page_x_offset} inches")
    print(f"Page Y Offset: {page_y_offset} inches")
```

---
title: Python으로 페이지 크기 변경
linktitle: 페이지 크기 변경
type: docs
weight: 40
url: /ko/python-net/change-page-size/
description: Aspose.PDF for Python via .NET 라이브러리를 사용하여 PDF 문서의 페이지 크기를 변경합니다.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용한 페이지 크기 변경
Abstract: 이 문서는 Aspose.PDF를 사용하여 PDF 페이지 크기를 읽고 수정하는 방법을 보여줍니다. Get Page Size 예제는 특정 PDF 페이지의 너비와 높이를 가져와 페이지 레이아웃을 확인하거나 형식을 검증하거나 문서 구조를 분석할 수 있게 합니다. Set Page Size 예제는 페이지의 크기를 변경하는 방법을 보여줍니다—예를 들어 첫 페이지를 A4 크기로 변환하는 등—또한 수정 전후의 박스 속성(CropBox, TrimBox, ArtBox, BleedBox, MediaBox)을 표시합니다.
---

Aspose.PDF for Python via .NET은 간단한 코드 라인으로 PDF 페이지 크기를 변경할 수 있게 합니다. 이 항목에서는 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 및 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) API를 사용하여 페이지 차원을 업데이트하는 방법을 보여줍니다.

{{% alert color="primary" %}}

높이와 너비 속성은 기본 단위로 포인트를 사용한다는 점에 유의하십시오. 1인치 = 72포인트이며 1cm = 1/2.54인치 = 0.3937인치 = 28.3포인트입니다.

{{% /alert %}}

### PDF 페이지의 페이지 크기를 A4로 설정

이 예제는 PDF 문서의 첫 페이지 크기를 표준 A4 크기로 업데이트합니다. 또한 크기 조정 전후에 페이지의 박스 차원(CropBox, TrimBox, ArtBox, BleedBox, MediaBox)을 출력하여 변경 사항을 확인할 수 있습니다.

다음 코드 스니펫은 PDF 페이지 차원을 A4 크기로 변경하는 방법을 보여줍니다:

1. [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)의 첫 번째 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)에 액세스합니다.
1. 수정 전에 페이지의 박스 크기(CropBox, TrimBox, ArtBox, BleedBox, MediaBox)를 표시합니다.
1. 페이지 API를 사용하여 A4 차원(597.6 × 842.4 포인트)을 적용합니다.
1. 업데이트된 페이지 박스 크기를 표시합니다.
1. 수정된 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)을 지정된 출력 경로에 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def set_page_size(input_file_name, output_file_name):
    """
    Set the size of the first page in the PDF document to A4 and save the updated document.

    Parameters:
    - input_file_name (str): Path to the input PDF file.
    - output_file_name (str): Path to save the output PDF file.
    """
    # Open the PDF document using the Document class
    document = ap.Document(input_file_name)
    # Get particular page (Page API)
    page = document.pages[1]

    # Set the page size as A4 (8.3 x 11.7 in). In Aspose.PDF 1 inch = 72 points.
    # A4 dimensions in points are (597.6, 842.4) for portrait orientation
    print("Before set")
    print(f"CropBox: {page.crop_box.width} x {page.crop_box.height}")
    print(f"TrimBox: {page.trim_box.width} x {page.trim_box.height}")
    print(f"ArtBox: {page.art_box.width} x {page.art_box.height}")
    print(f"BleedBox: {page.bleed_box.width} x {page.bleed_box.height}")
    print(f"MediaBox: {page.media_box.width} x {page.media_box.height}")

    # Use the Page API to set page size
    page.set_page_size(597.6, 842.4)
    print("After set")
    print(f"CropBox: {page.crop_box.width} x {page.crop_box.height}")
    print(f"TrimBox: {page.trim_box.width} x {page.trim_box.height}")
    print(f"ArtBox: {page.art_box.width} x {page.art_box.height}")
    print(f"BleedBox: {page.bleed_box.width} x {page.bleed_box.height}")
    print(f"MediaBox: {page.media_box.width} x {page.media_box.height}")

    # Save the updated document
    document.save(output_file_name)
```

## PDF 페이지 크기 가져오기

이 스니펫은 PDF를 읽고 첫 페이지의 차원(너비와 높이)을 가져옵니다. [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) API를 사용하여 페이지의 경계 [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/)을 추출하고 그 크기를 콘솔에 출력합니다. 이는 페이지 레이아웃을 검사하거나 형식을 검증하거나 문서를 추가 처리하기 위해 준비하는 데 유용합니다.

1. PDF를 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)으로 로드합니다.
1. 첫 번째 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)에 액세스합니다.
1. `get_page_rect()`를 사용하여 페이지의 경계 사각형을 가져옵니다.
1. 너비와 높이 값을 추출합니다.
1. 페이지 차원을 출력합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_size(input_file_name, output_file_name):
    # Open document (Document API)
    document = ap.Document(input_file_name)

    # Get particular page (Page API)
    page = document.pages[1]
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```

### 회전 전후 PDF 페이지 크기 가져오기

90° 회전을 적용하기 전후의 PDF 페이지 차원을 가져옵니다. 이는 회전이 너비와 높이에 어떻게 영향을 미치는지와 `get_page_rect()`를 회전 고려 여부에 따라 사용하는 방법을 보여줍니다.

1. PDF를 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)으로 엽니다.
1. 첫 번째 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)에 액세스합니다.
1. `page.rotate = ap.Rotation.ON90` 를 사용하여 90° 회전을 적용합니다(`[`Rotation`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rotation/) 열거형을 참조).
1. `get_page_rect(False)`를 사용하여 회전 없이 페이지 사각형을 가져오고 너비와 높이를 출력합니다.
1. `get_page_rect(True)`를 사용하여 회전을 고려한 페이지 사각형을 가져오고 너비와 높이를 출력합니다.
1. 회전으로 인해 차원이 어떻게 변하는지 비교합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_size_rotation(input_file_name, output_file_name):
    # Open document (Document API)
    document = ap.Document(input_file_name)
    # Get particular page (Page API)
    page = document.pages[1]
    # Apply rotation using Rotation enum
    page.rotate = ap.Rotation.ON90
    rectangle = page.get_page_rect(False)
    print(f"{rectangle.width} : {rectangle.height}")
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```

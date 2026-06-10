---
title: PDF 뷰어 클래스
type: docs
weight: 135
url: /ko/python-net/pdfviewer-class/
description: .NET을 통해 Python용 Aspose.PDF 의 PDFViewer 클래스를 사용하여 모든 PDF 페이지를 디코딩하고, 특정 페이지를 디코딩하고, 뷰어 관련 PDF 메타데이터를 검사하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDFViewer를 사용하여 PDF 페이지를 디코딩하고 파이썬에서 뷰어 데이터를 검사합니다.
Abstract: 이 문서에서는 페이지 디코딩 및 뷰어 관련 검사 작업을 위해.NET을 통해 파이썬용 Aspose.PDF 내 PDFViewer 파사드를 사용하는 방법을 설명합니다.모든 PDF 페이지를 디코딩하고, 특정 페이지를 렌더링하고, 페이지 수, 좌표 유형 및 해상도와 같은 속성을 검사하는 방법을 알아봅니다.
---

.NET을 통한 파이썬용 Aspose.PDF 는 다음을 제공합니다. [PDF 뷰어](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfviewer/) PDF 보기 및 페이지 디코딩 시나리오 작업을 위한 외관일반적인 사용 사례 중 하나는 PDF 페이지를 이미지 개체로 변환한 다음 디스크에 저장할 수 있는 것입니다.

## 재사용 가능한 PDFViewer 도우미 만들기

페이지를 디코딩하거나 뷰어 관련 속성을 읽기 전에 초기화하고 a를 반환하는 작은 도우미를 만드세요. `PdfViewer` 예.이렇게 하면 아래 예제가 독립적으로 유지되고 뷰어 객체가 PDF 문서에 바인딩되기 전에 어떻게 만들어지는지 명확하게 알 수 있습니다.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades


def _create_viewer() -> pdf_facades.PdfViewer:
    """Create a PdfViewer configured for decoding examples."""
    viewer = pdf_facades.PdfViewer()
    viewer.coordinate_type = ap.PageCoordinateType.MEDIA_BOX
    viewer.resolution = 150
    viewer.scale_factor = 1.0
    viewer.show_hidden_areas = False
    return viewer
```

## 모든 PDF 페이지 디코딩

용도 `decode_all_pages()` PDF의 모든 페이지를 개별 이미지로 변환하려는 경우그러면 반환된 페이지 이미지를 출력 디렉토리에 하나씩 저장할 수 있습니다.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def decode_all_pages(infile: str, output_dir: str) -> None:
    """Decode all pages of a PDF document into image files."""
    viewer = _create_viewer()
    try:
        viewer.open_pdf_file(infile)
        decoded_pages = viewer.decode_all_pages()

        for index, page_image in enumerate(decoded_pages, start=1):
            image_path = path.join(output_dir, f"decode_all_pages_{index}.png")
            page_image.save(image_path)
    finally:
        viewer.close_pdf_file()
```

## 특정 PDF 페이지 디코딩

용도 `decode_page()` 문서에서 한 페이지만 필요한 경우이는 미리 보기, 썸네일 또는 페이지별 내보내기를 생성할 때 유용합니다.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def decode_specific_page(infile: str, outfile: str, page_number: int = 1) -> None:
    """Decode a specific PDF page into an image file."""
    viewer = _create_viewer()
    try:
        viewer.bind_pdf(infile)
        page_image = viewer.decode_page(page_number)
        page_image.save(outfile)

    finally:
        viewer.close()
```

## PDF 메타데이터 검사

더 `inspect_pdf_metadata` 함수는 Aspose.PDF 를 사용하여 PDF 문서를 열고 기본적인 뷰어 관련 메타데이터를 검색하는 방법을 보여줍니다.문서의 내용보다는 문서가 어떻게 해석되고 표시되는지를 설명하는 정보를 추출하는 데 중점을 둡니다.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def inspect_pdf_metadata(infile: str) -> None:
    """Open a PDF and print page-count related viewer metadata."""
    viewer = _create_viewer()
    try:
        viewer.open_pdf_file(infile)
        print(f"Page count: {viewer.page_count}")
        print(f"Coordinate type: {viewer.coordinate_type}")
        print(f"Resolution: {viewer.resolution}")
    finally:
        viewer.close_pdf_file()
```

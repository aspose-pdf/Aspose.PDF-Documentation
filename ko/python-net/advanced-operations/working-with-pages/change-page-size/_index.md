---
title: 파이썬에서 PDF 페이지 크기 변경하기
linktitle: 페이지 크기 변경
type: docs
weight: 40
url: /ko/python-net/change-page-size/
description: Python에서 PDF 페이지 크기를 읽고 변경하는 방법을 알아보세요.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 페이지 크기 변경하기
Abstract: 이 문서에서는 Aspose.PDF 를 사용하여 PDF 페이지 크기를 읽고 수정하는 방법을 보여줍니다.Get Page Size 예제는 특정 PDF 페이지의 너비와 높이를 가져와서 사용자가 페이지 레이아웃을 검사하고 서식을 확인하거나 문서 구조를 분석할 수 있도록 합니다.페이지 크기 설정 예제에서는 첫 페이지를 A4 크기로 변환하는 등 페이지 크기를 변경하는 동시에 수정 전후에 상자 속성 (CropBox, TrimBox, ArtBox, BleedBox, MediaBox) 도 표시하는 방법을 보여줍니다.
---

.NET을 통한 파이썬용 Aspose.PDF 를 사용하면 간단한 코드 줄로 PDF 페이지 크기를 변경할 수 있습니다.이 항목에서는 를 사용하여 페이지 크기를 업데이트하는 방법을 보여줍니다. [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 과 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) API.

기존 PDF 페이지의 크기를 조정하거나, 문서 크기를 정규화하거나, Python에서 페이지 상자 설정을 검사해야 할 때 이 안내서를 사용하십시오.

{{% alert color="primary" %}}

높이 및 너비 속성은 포인트를 기본 단위로 사용한다는 점에 유의하십시오. 여기서 1인치는 72포인트이고 1cm는 1/2.54인치 = 0.3937인치 = 28.3포인트입니다.

{{% /alert %}}

## PDF 페이지의 페이지 크기를 A4로 설정

이 예제에서는 PDF 문서의 첫 페이지 크기를 표준 A4 크기로 업데이트합니다.또한 크기 조정 전후에 페이지의 상자 크기 (CropBox, TrimBox, ArtBox, BleedBox, MediaBox) 를 인쇄하므로 변경 사항을 확인할 수 있습니다.

다음 코드 스니펫은 PDF 페이지 크기를 A4 크기로 변경하는 방법을 보여줍니다.

1. 첫 번째 액세스 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 의 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 수정하기 전에 페이지의 상자 크기를 표시합니다 (크롭박스, 트림박스, 아트박스, 블리드박스, 미디어박스).
1. 페이지 API를 사용하여 A4 크기 (597.6 × 842.4포인트) 를 적용합니다.
1. 업데이트된 페이지 상자 크기를 표시합니다.
1. 수정한 내용 저장 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 지정된 출력 경로로

```python
import aspose.pdf as ap

def set_page_size(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    # Get particular page
    page = document.pages[1]

    # Set the page size as A4 (8.3 x 11.7 in) and in Aspose.Pdf, 1 inch = 72 points
    # So A4 dimensions in points will be (597.6, 842.4) for portrait orientation
    print("Before set")
    print(f"CropBox: {page.crop_box.width} x {page.crop_box.height}")
    print(f"TrimBox: {page.trim_box.width} x {page.trim_box.height}")
    print(f"ArtBox: {page.art_box.width} x {page.art_box.height}")
    print(f"BleedBox: {page.bleed_box.width} x {page.bleed_box.height}")
    print(f"MediaBox: {page.media_box.width} x {page.media_box.height}")

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

이 스니펫은 PDF를 읽고 첫 페이지의 크기 (너비 및 높이) 를 검색합니다.이 코드는 다음을 사용합니다. [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 페이지 경계를 추출하는 API [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) 크기를 콘솔에 출력합니다.이는 페이지 레이아웃을 검사하거나, 형식을 확인하거나, 추가 처리를 위해 문서를 준비하는 데 유용합니다.

1. PDF를 다음과 같이 로드합니다. [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 첫 번째 액세스 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. 를 사용하여 페이지의 경계 사각형을 검색합니다. `get_page_rect()`.
1. 너비 및 높이 값을 추출합니다.
1. 페이지 크기를 인쇄합니다.

```python
import aspose.pdf as ap

def get_page_size(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    # Get particular page
    page = document.pages[1]
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```

### 회전 전후의 PDF 페이지 크기 가져오기

90° 회전을 적용하기 전과 후의 PDF 페이지 크기를 검색합니다.회전이 너비와 높이에 미치는 영향과 사용 방법을 보여줍니다. `get_page_rect()` 회전을 고려하거나 고려하지 않습니다.

1. PDF를 다음과 같이 엽니다. [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 첫 번째 액세스 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. 를 사용하여 90° 회전 적용 `page.rotate = ap.Rotation.ON90` (참조 [`Rotation`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rotation/) 열거형).
1. 를 사용하여 회전하지 않고 페이지 사각형을 검색합니다. `get_page_rect(False)` 너비와 높이를 인쇄하십시오.
1. 회전을 고려하여 페이지 사각형을 검색합니다. `get_page_rect(True)` 너비와 높이를 인쇄하십시오.
1. 회전으로 인해 치수가 어떻게 변하는지 비교해 보십시오.

```python
import aspose.pdf as ap

def get_page_size_rotation(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    # Get particular page
    page = document.pages[1]
    page.rotate = ap.Rotation.ON90
    rectangle = page.get_page_rect(False)
    print(f"{rectangle.width} : {rectangle.height}")
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```

## 관련 페이지 주제

- [파이썬에서 PDF 페이지 작업하기](/pdf/ko/python-net/working-with-pages/)
- [파이썬에서 PDF 페이지 자르기](/pdf/ko/python-net/crop-pages/)
- [Python에서 PDF 페이지 속성 가져오기 및 설정](/pdf/ko/python-net/get-and-set-page-properties/)
- [파이썬에서 PDF 페이지 회전하기](/pdf/ko/python-net/rotate-pages/)
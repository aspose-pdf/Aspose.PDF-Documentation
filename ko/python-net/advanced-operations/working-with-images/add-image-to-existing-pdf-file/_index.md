---
title: Python에서 기존 PDF에 이미지 추가
linktitle: PDF에 이미지 추가
type: docs
weight: 10
url: /ko/python-net/add-image-to-existing-pdf-file/
description: Python을 사용하여 기존 PDF 파일에 이미지를 추가하고, 고정 좌표에 배치하며, 대체 텍스트를 설정하고, 이미지 압축을 사용하는 방법을 알아보세요.
lastmod: "2026-05-05"
TechArticle: true
AlternativeHeadline: Python을 사용하여 기존 PDF 파일에 이미지 추가
Abstract: 이 문서에서는 Aspose.PDF for Python via .NET을 사용하여 PDF 문서에 이미지를 추가하는 방법을 보여줍니다. 고정 좌표에 이미지를 배치하고, 저수준 PDF 연산자를 사용하여 이미지를 그리고, 접근성을 위한 대체 텍스트를 지정하며, Flate 압축으로 이미지를 삽입하는 방법을 다룹니다.
---

## Python에서 기존 PDF 파일에 이미지 추가

이 예제에서는 Aspose.PDF for Python via .NET을 사용하여 기존 PDF 페이지의 고정 위치에 이미지를 배치하는 방법을 보여줍니다.

기존 PDF 레이아웃에 로고, 사진, 스탬프, 차트 또는 기타 그래픽을 추가해야 할 때 이 예제를 사용하십시오. 페이지 좌표로 이미지를 배치하거나, 연산자를 사용해 그리고, 접근성 텍스트를 추가하거나, 이미지 압축을 제어할 수 있습니다.

1. 기존 PDF를 로드합니다 `ap.Document(infile)`.
1. 대상 페이지 선택 (`document.pages[1]` 첫 페이지에 대해).
1. 전화 `page.add_image()` 함께:
    - 이미지 파일 경로.
    - A `Rectangle` 배치 좌표 정의.
1. 업데이트된 PDF를 저장합니다.

```python
import aspose.pdf as ap


def add_image(infile, image_file, outfile):
    document = ap.Document(infile)
    page = document.pages[1]
    page.add_image(image_file, ap.Rectangle(20, 730, 120, 830, True))
    document.save(outfile)
```

## 연산자를 사용하여 PDF에 이미지 추가

이 방법은 고수준 대신 저수준 PDF 연산자를 사용하여 이미지를 추가합니다. `add_image()` 도우미.

1. 새로 만들기 `Document` 그리고 페이지를 추가합니다.
1. 페이지 리소스에 이미지를 추가합니다 (`page.resources.images`).
1. 변환 연산자 만들기 (`GSave`, `ConcatenateMatrix`, `Do`, `GRestore`).
1. 연산자를 페이지 내용에 추가합니다.
1. 결과 PDF를 저장합니다.

```python
import aspose.pdf as ap
from io import FileIO


def add_image_using_operators(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842, 595)
    resources_images = page.resources.images

    with FileIO(image_file, "rb") as image_stream:
        image_id = resources_images.add(image_stream)

    rectangle = ap.Rectangle(0, 0, page.media_box.width, page.media_box.height, True)

    operators = [
        ap.operators.GSave(),
        ap.operators.ConcatenateMatrix(
            ap.Matrix(
                rectangle.urx - rectangle.llx,
                0,
                0,
                rectangle.ury - rectangle.lly,
                rectangle.llx,
                rectangle.lly,
            )
        ),
        ap.operators.Do(image_id),
        ap.operators.GRestore(),
    ]

    page.contents.add(operators)
    document.save(outfile)
```

## 대체 텍스트가 있는 PDF에 이미지 추가

이 예제는 이미지를 추가하고 접근성을 위해 대체 텍스트를 할당합니다.

1. 새로 만들기 `Document` 그리고 페이지를 추가합니다.
1. 이미지를 페이지에 추가합니다 `page.add_image()`.
1. 이미지 리소스를 가져오기 `page.resources.images`.
1. 대체 텍스트를 설정합니다 `try_set_alternative_text()`.
1. 결과 PDF를 저장합니다.

```python
import aspose.pdf as ap


def add_image_set_alternative_text(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842, 595)

    page.add_image(image_file, ap.Rectangle(0, 0, 842, 595, True))
    resources_images = page.resources.images
    x_image = resources_images[1]
    result = x_image.try_set_alternative_text("Alternative text for image", page)

    if result:
        print("Alternative text has been added successfully")

    document.save(outfile)
```

## Flate 압축을 사용하여 PDF에 이미지를 추가합니다

이 예제는 이미지를 사용하여 삽입합니다 `ImageFilterType.FLATE` 압축.

1. 새로 만들기 `Document` 그리고 페이지를 추가합니다.
1. Flate 압축으로 이미지를 페이지 리소스에 추가합니다.
1. 행렬 연산자를 사용하여 이미지를 배치하고 그립니다.
1. 문서를 저장합니다.

```python
import aspose.pdf as ap
from io import FileIO


def add_image_to_pdf_with_flate_compression(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    resources_images = page.resources.images

    with FileIO(image_file, "rb") as image_stream:
        image_id = resources_images.add(image_stream, ap.ImageFilterType.FLATE)

    rectangle = ap.Rectangle(0, 0, 600, 600, True)
    matrix = ap.Matrix(
        rectangle.urx - rectangle.llx,
        0,
        0,
        rectangle.ury - rectangle.lly,
        rectangle.llx,
        rectangle.lly,
    )

    page.contents.add([ap.operators.GSave()])
    page.contents.add([ap.operators.ConcatenateMatrix(matrix)])
    page.contents.add([ap.operators.Do(image_id)])
    page.contents.add([ap.operators.GRestore()])

    document.save(outfile)
```

## 관련 이미지 주제

- [Python을 사용하여 PDF에서 이미지 작업하기](/pdf/ko/python-net/working-with-images/)
- [기존 PDF 파일에서 이미지 교체](/pdf/ko/python-net/replace-image-in-existing-pdf-file/)
- [PDF 파일에서 이미지 삭제](/pdf/ko/python-net/delete-images-from-pdf-file/)
- [PDF 파일에서 이미지 추출](/pdf/ko/python-net/extract-images-from-pdf-file/)

---
title: Python을 사용하여 PDF 파일에서 이미지 추출
linktitle: 이미지 추출
type: docs
weight: 30
url: /ko/python-net/extract-images-from-pdf-file/
description: Python에서 PDF 파일에서 임베디드 이미지를 추출하는 방법을 알아봅니다.
lastmod: "2026-06-10"
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 파일에서 이미지 추출하기
Abstract: 이 문서에서는.NET을 통해 파이썬용 Aspose.PDF 파일을 사용하여 PDF 문서에서 이미지를 추출하는 방법을 보여줍니다.포함된 단일 이미지를 추출하고 페이지의 특정 사각형 영역에 있는 이미지를 내보내는 방법을 다룹니다.
---

포함된 그래픽을 재사용하거나, 이미지 자산을 보관하거나, PDF 외부의 이미지 내용을 처리해야 하는 경우 이 페이지를 사용하십시오.

1. 를 사용하여 소스 PDF를 로드합니다. `ap.Document(infile)`.
1. 대상 페이지 및 이미지 리소스 색인을 선택합니다.
1. 이미지 객체를 출력 스트림에 저장합니다.

```python
import aspose.pdf as ap
from io import FileIO


def extract_image(infile, outfile):
    document = ap.Document(infile)
    x_image = document.pages[1].resources.images[1]
    with FileIO(outfile, "wb") as output_image:
        x_image.save(output_image)
```

## PDF의 특정 영역에서 이미지 추출

이 예제에서는 PDF 페이지의 지정된 사각형 영역 내에 있는 이미지를 추출하여 별도의 파일로 저장합니다.

1. 원본 PDF를 로드합니다.
1. 작성 `ImagePlacementAbsorber` 대상 페이지에서 수락하십시오.
1. 대상 사각형을 정의합니다.
1. 이미지 배치를 반복하여 각 이미지 경계가 영역에 맞는지 확인합니다.
1. 일치하는 이미지를 출력 파일에 저장합니다.

```python
import aspose.pdf as ap
from io import FileIO


def extract_image_from_specific_region(infile, outfile):
    document = ap.Document(infile)
    rectangle = ap.Rectangle(0, 0, 590, 590, True)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    index = 1
    for image_placement in absorber.image_placements:
        point1 = ap.Point(image_placement.rectangle.llx, image_placement.rectangle.lly)
        point2 = ap.Point(image_placement.rectangle.urx, image_placement.rectangle.ury)

        if rectangle.contains(point1, True) and rectangle.contains(point2, True):
            with FileIO(outfile.replace("index", str(index)), "wb") as output_image:
                image_placement.image.save(output_image)
            index += 1
```

## 관련 이미지 주제

- [Python을 사용하여 PDF의 이미지로 작업하기](/pdf/ko/python-net/working-with-images/)
- [기존 PDF 파일의 이미지 바꾸기](/pdf/ko/python-net/replace-image-in-existing-pdf-file/)
- [PDF 파일에서 이미지 삭제](/pdf/ko/python-net/delete-images-from-pdf-file/)
- [기존 PDF 파일에 이미지 추가](/pdf/ko/python-net/add-image-to-existing-pdf-file/)

---
title: Python을 사용하여 기존 PDF 파일의 이미지 바꾸기
linktitle: 이미지 바꾸기
type: docs
weight: 70
url: /ko/python-net/replace-image-in-existing-pdf-file/
description: Python에서 기존 PDF 파일에 포함된 이미지를 바꾸는 방법을 알아봅니다.
lastmod: "2026-06-10"
TechArticle: true
AlternativeHeadline: 기존 PDF 파일의 이미지를 Python으로 바꾸기
Abstract: 이 문서에서는.NET을 통해 PDF 문서의 이미지를 Python용 Aspose.PDF 로 바꾸는 방법을 보여줍니다.이미지를 리소스 인덱스로 바꾸는 방법과 검색된 특정 이미지를 ImagePlacementAbsorber로 바꾸는 방법을 다룹니다.
---

## PDF에서 이미지 바꾸기

문서 레이아웃을 다시 작성하지 않고 PDF에 있는 로고, 다이어그램 또는 기타 포함된 그래픽을 업데이트해야 하는 경우 이 페이지를 사용하십시오.

1. 를 사용하여 소스 PDF를 로드합니다. `ap.Document(infile)`.
1. 대체 이미지를 바이너리 스트림으로 엽니다.
1. 페이지의 색인으로 이미지 리소스를 바꿉니다.
1. 업데이트된 PDF를 저장합니다.

```python
import aspose.pdf as ap
from io import FileIO


def replace_image(infile, image_file, outfile):
    document = ap.Document(infile)

    with FileIO(image_file, "rb") as image_stream:
        document.pages[1].resources.images.replace(1, image_stream)

    document.save(outfile)
```

## 특정 이미지 바꾸기

이 예제는 다음에 의해 발견된 특정 이미지 배치를 대체합니다. `ImagePlacementAbsorber`.

1. 원본 PDF를 로드합니다.
1. 작성 `ImagePlacementAbsorber` 페이지에서 이미지 배치를 수집할 수 있습니다.
1. 페이지에 이미지 배치가 있는지 확인하세요.
1. 선택한 배치를 새 이미지 스트림으로 교체합니다.
1. 업데이트된 PDF를 저장합니다.

```python
import aspose.pdf as ap
from io import FileIO


def replace_image_with_absorber(infile, image_file, outfile):
    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    if len(absorber.image_placements) > 0:
        image_placement = absorber.image_placements[1]
        with FileIO(image_file, "rb") as image_stream:
            image_placement.replace(image_stream)

    document.save(outfile)
```

## 관련 이미지 주제

- [Python을 사용하여 PDF의 이미지로 작업하기](/pdf/ko/python-net/working-with-images/)
- [PDF 파일에서 이미지 삭제](/pdf/ko/python-net/delete-images-from-pdf-file/)
- [PDF 파일에서 이미지 추출](/pdf/ko/python-net/extract-images-from-pdf-file/)
- [기존 PDF 파일에 이미지 추가](/pdf/ko/python-net/add-image-to-existing-pdf-file/)

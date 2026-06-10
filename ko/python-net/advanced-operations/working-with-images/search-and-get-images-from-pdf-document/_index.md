---
title: PDF로 이미지 가져오기 및 검색
linktitle: 이미지 가져오기 및 검색
type: docs
weight: 40
url: /ko/python-net/search-and-get-images-from-pdf-document/
description: Python에서 PDF 문서의 이미지를 검색하고 검사하는 방법을 알아봅니다.
lastmod: "2026-06-10"
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 파일의 이미지를 검색하고 검사합니다.
Abstract: 이 문서에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서의 이미지를 검색하고 검사하는 방법을 보여줍니다.ImagePlacementAbsorber를 사용하여 이미지 배치, 크기, 해상도 및 대체 텍스트를 분석하는 방법을 다룹니다.
---

## PDF 페이지의 이미지 배치 속성 검사

이 예제에서는 .NET을 통해 Python용 Aspose.PDF 를 사용하여 특정 PDF 페이지에 있는 모든 이미지의 속성을 분석하고 표시하는 방법을 보여줍니다.

이미지 배치를 감사하거나, 이미지 해상도를 검사하거나, PDF 페이지에 포함된 이미지 개체를 식별해야 할 때 이 페이지를 사용하십시오.

1. 페이지의 모든 이미지를 수집하려면 '이미지 배치 흡수기'를 만드세요.
1. 'document.pages [1] .accept (흡수기) '를 호출하여 첫 페이지의 이미지 배치를 분석합니다.
1. '흡수기.image_placements'를 반복하여 각 이미지의 주요 속성을 표시합니다.
    - 너비 및 높이 (포인트).
    - 왼쪽 아래 X (LLX) 및 왼쪽 아래 Y (LLY) 좌표.
    - 수평 (X) 및 수직 (Y) 해상도 (DPI)

```python
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing

def extract_image_params(infile):
    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    for image_placement in absorber.image_placements:
        print("image width: " + str(image_placement.rectangle.width))
        print("image height: " + str(image_placement.rectangle.height))
        print("image LLX: " + str(image_placement.rectangle.llx))
        print("image LLY: " + str(image_placement.rectangle.lly))
        print("image horizontal resolution: " + str(image_placement.resolution.x))
        print("image vertical resolution: " + str(image_placement.resolution.y))
```

## PDF에서 이미지 유형 추출 및 계산

이 함수는 PDF의 첫 페이지에 있는 모든 이미지를 분석하고 회색조 이미지와 RGB 이미지의 수를 계산합니다.

1. 페이지의 모든 이미지를 수집하려면 '이미지 배치 흡수기'를 만드세요.
1. 그레이스케일 및 RGB 이미지의 카운터를 초기화합니다.
1. 'document.pages [1] .accept (흡수기) '를 호출하여 이미지 배치를 분석합니다.
1. 검색된 총 이미지 수를 출력합니다.
1. '흡수기.image_placements'에서 각 이미지를 반복해서 살펴보세요.
    - '이미지_배치.이미지.get_color_type () '을 사용하여 이미지 색상 유형을 가져옵니다.
    - 해당 카운터 (그레이스케일 또는 rgb) 를 증가시킵니다.
    - 각 이미지에 대해 그레이스케일인지 RGB인지를 나타내는 메시지를 인쇄합니다.

```python
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing

def extract_image_types_from_pdf(infile):
    """
    Extract and count image types (grayscale/RGB) with resolution analysis.

    Args:
        infile (str): Input PDF filename

    Returns:
        None

    Example:
        extract_image_types_from_pdf("sample_extr.pdf")

    Note:
        Prints total images count, color type for each image, and resolution info.
    """

    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()

    # Counters for grayscale and RGB images
    grayscaled = 0
    rgb = 0

    document.pages[1].accept(absorber)

    print("--------------------------------")
    print("Total Images = " + str(len(absorber.image_placements)))

    image_counter = 1

    for image_placement in absorber.image_placements:
        # Determine the color type of the image
        colorType = image_placement.image.get_color_type()
        if colorType == ap.ColorType.GRAYSCALE:
            grayscaled += 1
            print(f"Image {image_counter} is Grayscale...")
        elif colorType == ap.ColorType.RGB:
            rgb += 1
            print(f"Image {image_counter} is RGB...")
        image_counter += 1

    print("--------------------------------")
    print("Grayscale Images = " + str(grayscaled))
    print("RGB Images = " + str(rgb))
```

## PDF에서 상세 이미지 정보 추출

이 함수는 PDF의 첫 페이지에 있는 모든 이미지를 분석하고 페이지의 그래픽 변형을 기반으로 크기 조정 및 유효 해상도를 계산합니다.

1. PDF 로드 및 변수 초기화
1. 이미지 리소스 수집
1. 프로세스 페이지 콘텐츠 연산자:
    - 'gSave' - 현재 CTM을 스택에 푸시합니다.
    - '복원' - 스택에서 마지막 CTM을 팝합니다.
    - 'ConcatenateMatrix' - 연산자 행렬을 곱하여 현재 CTM을 업데이트합니다.
1. 이미지 이름, 크기 조정 및 계산된 해상도를 인쇄합니다.

```python
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing

def extract_image_information_from_pdf(infile):
    with ap.Document(infile) as document:
        default_resolution = 72
        graphics_state = []

        image_names = list(document.pages[1].resources.images.names)

        graphics_state.append(
            drawing.drawing2d.Matrix(
                float(1), float(0), float(0), float(1), float(0), float(0)
            )
        )

        for op in document.pages[1].contents:
            if is_assignable(op, ap.operators.GSave):
                graphics_state.append(
                    cast(drawing.drawing2d.Matrix, graphics_state[-1]).clone()
                )

            elif is_assignable(op, ap.operators.GRestore):
                graphics_state.pop()

            elif is_assignable(op, ap.operators.ConcatenateMatrix):
                op_cm = cast(ap.operators.ConcatenateMatrix, op)
                cm = drawing.drawing2d.Matrix(
                    float(op_cm.matrix.a),
                    float(op_cm.matrix.b),
                    float(op_cm.matrix.c),
                    float(op_cm.matrix.d),
                    float(op_cm.matrix.e),
                    float(op_cm.matrix.f),
                )

                graphics_state[-1].multiply(cm)
                continue

            elif is_assignable(op, ap.operators.Do):
                op_do = cast(ap.operators.Do, op)
                if op_do.name in image_names:
                    last_ctm = cast(drawing.drawing2d.Matrix, graphics_state[-1])
                    index = image_names.index(op_do.name) + 1
                    image = document.pages[1].resources.images[index]

                    scaled_width = math.sqrt(
                        last_ctm.elements[0] ** 2 + last_ctm.elements[1] ** 2
                    )
                    scaled_height = math.sqrt(
                        last_ctm.elements[2] ** 2 + last_ctm.elements[3] ** 2
                    )

                    original_width = image.width
                    original_height = image.height

                    res_horizontal = (
                        original_width * default_resolution / scaled_width
                    )
                    res_vertical = (
                        original_height * default_resolution / scaled_height
                    )

                    info = (
                        f"{infile} image {op_do.name} "
                        f"({scaled_width:.2f}:{scaled_height:.2f}): "
                        f"res {res_horizontal:.2f} x {res_vertical:.2f}\n"
                    )
                    print(info.rstrip())
```

## PDF의 이미지에서 대체 텍스트 추출

이 함수는 PDF의 첫 페이지에 있는 모든 이미지에서 대체 텍스트 (대체 텍스트) 를 검색하며, 이는 접근성 및 PDF/UA 규정 준수 검사에 유용합니다.

1. 'AP.Document () '를 사용하여 PDF 문서를 로드합니다.
1. 페이지의 모든 이미지를 수집하려면 '이미지 배치 흡수기'를 만드세요.
1. 첫 페이지의 흡수 장치를 수락하십시오 (페이지. 수락 (흡수기)).
1. '흡수기.image_placements'에서 각 이미지를 반복해서 살펴보세요.
    - 페이지의 리소스 컬렉션 (get_name_in_collection ()) 에 있는 이미지의 이름을 출력합니다.
    - 'get_alternative_text (페이지) '를 사용하여 대체 텍스트를 검색합니다.
    - 대체 텍스트의 첫 줄을 인쇄합니다.

```python
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing

def extract_image_alt_text(infile):
    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()
    page = document.pages[1]
    page.accept(absorber)

    for image_placement in absorber.image_placements:
        print(
            "Name in collection: " + str(image_placement.image.get_name_in_collection())
        )
        lines = image_placement.image.get_alternative_text(page)
        print("Alt Text: " + lines[0])
```

## 관련 이미지 주제

- [Python을 사용하여 PDF의 이미지로 작업하기](/pdf/ko/python-net/working-with-images/)
- [PDF 파일에서 이미지 추출](/pdf/ko/python-net/extract-images-from-pdf-file/)
- [기존 PDF 파일의 이미지 바꾸기](/pdf/ko/python-net/replace-image-in-existing-pdf-file/)
- [기존 PDF 파일에 이미지 추가](/pdf/ko/python-net/add-image-to-existing-pdf-file/)

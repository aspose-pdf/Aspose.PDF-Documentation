---
title: PDF에서 이미지 가져오기 및 검색
linktitle: 이미지 가져오기 및 검색
type: docs
weight: 40
url: /ko/python-net/search-and-get-images-from-pdf-document/
description: Aspose.PDF를 사용하여 Python에서 PDF 문서의 이미지를 검색하고 가져오는 방법을 배웁니다.
lastmod: "2025-09-17"
TechArticle: true
AlternativeHeadline: PDF에서 이미지 검색 및 추출
Abstract: Aspose.PDF for Python via .NET 라이브러리는 PDF 문서에서 이미지 검색 및 추출을 위한 강력한 기능을 제공합니다. 'ImagePlacementAbsorber' 클래스를 활용하면 개발자는 PDF 전체 페이지에 삽입된 이미지를 효율적으로 찾고 접근할 수 있습니다.
---

## PDF 페이지에서 이미지 배치 속성 검사

이 예제는 Aspose.PDF for Python via .NET을 사용하여 특정 PDF 페이지의 모든 이미지 속성을 분석하고 표시하는 방법을 보여줍니다.

1. 페이지의 모든 이미지를 수집하기 위해 'ImagePlacementAbsorber'를 생성합니다.
1. 첫 번째 페이지의 이미지 배치를 분석하기 위해 'document.pages[1].accept(absorber)'를 호출합니다.
1. 'absorber.image_placements'를 반복하면서 각 이미지의 주요 속성을 표시합니다:
- 너비와 높이 (포인트).
- 좌하단 X (LLX) 및 좌하단 Y (LLY) 좌표.
- 가로 (X) 및 세로 (Y) 해상도 (DPI).

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    for image_placement in absorber.image_placements:
        # Display image placement properties for all placements
        print("image width: " + str(image_placement.rectangle.width))
        print("image height: " + str(image_placement.rectangle.height))
        print("image LLX: " + str(image_placement.rectangle.llx))
        print("image LLY: " + str(image_placement.rectangle.lly))
        print("image horizontal resolution: " + str(image_placement.resolution.x))
        print("image vertical resolution: " + str(image_placement.resolution.y))
```

## PDF에서 이미지 유형 추출 및 카운트

이 함수는 PDF 첫 페이지의 모든 이미지를 분석하고 흑백 및 RGB 이미지의 수를 계산합니다.

1. 페이지의 모든 이미지를 수집하기 위해 'ImagePlacementAbsorber'를 생성합니다.
1. 흑백 및 RGB 이미지에 대한 카운터를 초기화합니다.
1. 이미지 배치를 분석하기 위해 'document.pages[1].accept(absorber)'를 호출합니다.
1. 찾아진 이미지의 총 개수를 출력합니다.
1. 'absorber.image_placements'의 각 이미지를 반복합니다:
- 'image_placement.image.get_color_type()'를 사용하여 이미지 색상 유형을 가져옵니다.
- 해당 카운터(흑백 또는 RGB)를 증가시킵니다.
- 각 이미지가 흑백인지 RGB인지에 대한 메시지를 출력합니다.

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)
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
```

## PDF에서 상세 이미지 정보 추출

이 함수는 PDF 첫 페이지의 모든 이미지를 분석하고 페이지의 그래픽 변환을 기반으로 스케일된 크기와 실제 해상도를 계산합니다.

1. PDF를 로드하고 변수를 초기화합니다
1. 이미지 리소스를 수집합니다
1. 페이지 콘텐츠 연산자를 처리합니다:
- 'GSave' - 현재 CTM을 스택에 푸시합니다.
- 'GRestore' - 마지막 CTM을 스택에서 팝합니다.
- 'ConcatenateMatrix' - 연산자 행렬과 곱하여 현재 CTM을 업데이트합니다.
1. 이미지 이름, 스케일된 크기 및 계산된 해상도를 출력합니다.

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)

    default_resolution = 72
    graphics_state = []

    image_names = list(document.pages[1].resources.images.names)

    graphics_state.append(drawing.drawing2d.Matrix(float(1), float(0), float(0), float(1), float(0), float(0)))

    for op in document.pages[1].contents:
        if is_assignable(op, ap.operators.GSave):
            graphics_state.append(cast(drawing.drawing2d.Matrix, graphics_state[-1]).clone())

        elif is_assignable(op, ap.operators.GRestore):
            graphics_state.pop()

        elif is_assignable(op, ap.operators.ConcatenateMatrix):
            opCM = cast(ap.operators.ConcatenateMatrix, op)
            cm = drawing.drawing2d.Matrix(
                float(opCM.matrix.a),
                float(opCM.matrix.b),
                float(opCM.matrix.c),
                float(opCM.matrix.d),
                float(opCM.matrix.e),
                float(opCM.matrix.f),
            )

            graphics_state[-1].multiply(cm)
            continue

        elif is_assignable(op, ap.operators.Do):
            opDo = cast(ap.operators.Do, op)
            if opDo.name in image_names:
                last_ctm = cast(drawing.drawing2d.Matrix, graphics_state[-1])
                index = image_names.index(opDo.name) + 1
                image = document.pages[1].resources.images[index]

                scaled_width = math.sqrt(last_ctm.elements[0] ** 2 + last_ctm.elements[1] ** 2)
                scaled_height = math.sqrt(last_ctm.elements[2] ** 2 + last_ctm.elements[3] ** 2)

                original_width = image.width
                original_height = image.height

                res_horizontal = original_width * default_resolution / scaled_width
                res_vertical = original_height * default_resolution / scaled_height

                print(
                    f"{self.data_dir}image {opDo.name} "
                    f"({scaled_width:.2f}:{scaled_height:.2f}): "
                    f"res {res_horizontal:.2f} x {res_vertical:.2f}"
                )
```

## PDF 이미지에서 대체 텍스트 추출

이 함수는 PDF 첫 페이지의 모든 이미지에서 대체 텍스트(alt text)를 가져와 접근성 및 PDF/UA 준수 검사에 활용됩니다.

1. 'ap.Document()'를 사용하여 PDF 문서를 로드합니다.
1. 페이지의 모든 이미지를 수집하기 위해 'ImagePlacementAbsorber'를 생성합니다.
1. 첫 번째 페이지에서 흡수기(absorber)를 수락합니다 (page.accept(absorber)).
1. 'absorber.image_placements'의 각 이미지를 반복합니다:
- 페이지 리소스 컬렉션에서 이미지 이름을 출력합니다 (get_name_in_collection()).
- 'get_alternative_text(page)'를 사용하여 대체 텍스트를 가져옵니다.
- 대체 텍스트의 첫 줄을 출력합니다.

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)
    absorber = ap.ImagePlacementAbsorber()
    page = document.pages[1]
    page.accept(absorber)

    for image_placement in absorber.image_placements:
        print(
            "Name in collection: "
            + str(image_placement.image.get_name_in_collection())
        )
        lines = image_placement.image.get_alternative_text(page)
        print("Alt Text: " + lines[0])
```

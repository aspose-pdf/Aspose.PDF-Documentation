---
title: Python을 사용하여 PDF 파일에서 이미지 추출
linktitle: 이미지 추출
type: docs
weight: 30
url: /ko/python-net/extract-images-from-pdf-file/
description: 이 섹션에서는 Python 라이브러리를 사용하여 PDF 파일에서 이미지를 추출하는 방법을 보여줍니다.
lastmod: "2025-09-27"
TechArticle: true
AlternativeHeadline: Python으로 PDF에서 이미지 추출
Abstract: 이 문서에서는 Aspose.PDF for Python을 사용하여 PDF 파일에서 이미지를 추출하는 과정을 설명합니다. 관리, 보관, 분석 또는 공유와 같은 목적을 위해 이미지를 분리하는 유용성을 강조합니다. 문서에 따르면 PDF 내부의 이미지는 각 페이지의 리소스 컬렉션, 특히 XImage 컬렉션에 저장됩니다. 이미지를 추출하려면 사용자는 특정 페이지에 접근하고 Images 컬렉션에서 인덱스를 사용하여 이미지를 가져올 수 있습니다. 인덱스로 반환된 XImage 객체는 추출된 이미지를 저장하기 위한 `save()` 메서드를 제공합니다. 코드 스니펫이 제공되어 PDF 문서를 열고, 두 번째 페이지에서 인덱스를 사용해 특정 이미지를 추출한 뒤 파일로 저장하는 단계들을 시연합니다.
---

PDF 파일에서 이미지를 분리해야 하나요? 문서 이미지의 관리, 보관, 분석 또는 공유를 간소화하려면 **Aspose.PDF for Python**을 사용하여 PDF 파일에서 이미지를 추출하세요.

1. 'ap.Document()'를 사용하여 PDF 문서를 로드합니다.
1. 문서의 원하는 페이지에 접근합니다 (document.pages[1]).
1. 페이지 리소스에서 이미지를 선택합니다 (예: resources.images[1]).
1. 대상 파일을 위한 출력 스트림(FileIO)을 생성합니다.
1. 'xImage.save(output_image)'를 사용하여 추출한 이미지를 저장합니다.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    document = ap.Document(path_infile)
    xImage = document.pages[1].resources.images[1]
    with FileIO(path_outfile, "w") as output_image:
        xImage.save(output_image)
```

## PDF에서 특정 영역의 이미지 추출

이 예제는 PDF 페이지의 지정된 사각형 영역 내에 위치한 이미지를 추출하고 별개의 파일로 저장합니다.

1. 'ap.Document'를 사용하여 PDF 문서를 로드합니다.
1. 첫 번째 페이지의 모든 이미지를 수집하기 위해 'ImagePlacementAbsorber'를 생성합니다.
1. 이미지 배치를 분석하기 위해 'document.pages[1].accept(absorber)'를 호출합니다.
1. 'absorber.image_placements'에 있는 모든 이미지를 반복합니다:
- 이미지 경계 상자(llx, lly, urx, ury)를 가져옵니다.
- 이미지 사각형의 두 모서리가 목표 사각형 내부에 있는지 확인합니다 (rectangle.contains()).
- 조건이 참이면 FileIO를 사용해 파일에 이미지를 저장하고 파일명에서 'index'를 순차 번호로 교체합니다.
1. 저장된 각 이미지마다 인덱스를 증가시킵니다.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    rectangle = ap.Rectangle(0, 0, 590, 590, True)

    document = ap.Document(path_infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)
    index = 1
    for image_placement in absorber.image_placements:
        point1 = ap.Point(
            image_placement.rectangle.llx, image_placement.rectangle.lly
        )
        point2 = ap.Point(
            image_placement.rectangle.urx, image_placement.rectangle.urx
        )
        if rectangle.contains(point1, True) and rectangle.contains(point2, True):
            with FileIO(path_outfile.replace("index", str(index)), "w") as output_image:
                image_placement.image.save(output_image)
            index = index + 1
```

## PDF에서 이미지 정보 추출

아래 예제는 PDF 페이지에 삽입된 이미지를 분석하고 실제 해상도를 계산하는 방법을 보여줍니다.

1. 'ap.Document'로 PDF를 엽니다.
1. 페이지 내용을 읽는 동안 그래픽 상태를 추적합니다.
1. 연산자를 처리합니다:
- 'GSave'/'GRestore' - 매트릭스 푸시/팝.
- 'ConcatenateMatrix' - 변환 업데이트.
- 'Do' - 이미지인 경우, 크기를 가져오고 변환을 적용합니다.
1. 실제 DPI를 계산합니다.
1. 이미지 이름, 스케일된 크기 및 DPI를 출력합니다.

```python

    import aspose.pdf as ap
    from io import FileIO
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

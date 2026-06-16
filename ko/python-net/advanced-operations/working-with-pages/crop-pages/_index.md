---
title: 파이썬에서 PDF 페이지 자르기
linktitle: PDF 페이지 자르기
type: docs
weight: 70
url: /ko/python-net/crop-pages/
description: Python에서 PDF 페이지를 자르고 자르기, 다듬기, 블리드 및 미디어 상자를 조정하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF의 페이지 속성에 액세스하고 수정하는 방법
Abstract: 이 문서에서는 Python용 Aspose.PDF 를 사용하여 PDF 문서의 페이지 속성에 액세스하고 수정하는 방법에 대한 개요를 제공합니다.이 문서에서는 미디어 박스, 블리드 박스, 트림 박스, 아트 박스, 크롭 박스를 비롯한 여러 페이지 속성에 대해 설명하고 인쇄 및 표시 목적으로 PDF 페이지의 크기와 경계를 정의하는 역할을 설명합니다.미디어 상자는 가장 큰 페이지 크기를 나타내며, 블리드 박스는 트리밍을 위해 페이지 가장자리 너머까지 잉크가 묻도록 합니다.트리밍 상자는 트리밍 후의 최종 문서 크기를 표시하고 아트 상자는 실제 페이지 내용을 포함합니다.크롭 상자는 Adobe Acrobat의 가시 영역을 정의합니다.이 문서에는 PDF 문서의 특정 페이지에 대해 다른 상자와 함께 새 자르기 상자를 설정하는 방법을 보여주는 Python 코드 스니펫이 포함되어 있습니다.시각적 예제는 크롭을 적용하기 전과 후의 페이지 모양을 보여 주며, 이러한 속성을 수정하는 실제 적용 사례를 보여줍니다.
---

## 페이지 속성 가져오기

PDF 파일의 각 페이지에는 너비, 높이, 블리드, 크롭 및 트림박스와 같은 다양한 속성이 있습니다.파이썬용 Aspose.PDF 를 사용하면 이러한 속성에 액세스할 수 있습니다.

보이는 페이지 영역을 줄이거나, 인쇄 워크플로에 사용할 파일을 준비하거나, PDF 문서의 페이지 상자 형상을 검사해야 할 때 이 페이지를 사용하십시오.

- **media_box**: 미디어 상자는 가장 큰 페이지 상자입니다.문서를 포스트스크립트 또는 PDF로 인쇄할 때 선택한 페이지 크기 (예: A4, A5, US Letter 등) 에 해당합니다.즉, 미디어 상자는 PDF 문서를 표시하거나 인쇄하는 데 사용되는 미디어의 실제 크기를 결정합니다.
- **bleed_box**: 문서에 블리드가 있는 경우 PDF에도 블리드 박스가 표시됩니다.블리드는 페이지 가장자리를 벗어나는 색상 (또는 아트워크) 의 양입니다.문서를 인쇄하고 크기에 맞게 잘라낼 때 (“트리밍”) 잉크가 페이지 가장자리까지 들어가도록 하는 데 사용됩니다.페이지의 트리밍이 잘못되어도 (트림 표시가 약간 잘려서) 페이지에 흰색 가장자리가 나타나지 않습니다.
- **trim_box**: 트림 상자는 인쇄 및 트리밍 후 문서의 최종 크기를 나타냅니다.
- **art_box**: 아트 박스는 문서에 있는 페이지의 실제 내용 주위에 그려진 상자입니다.이 페이지 상자는 다른 응용 프로그램에서 PDF 문서를 가져올 때 사용됩니다.
- **crop_box**: 크롭 박스는 Adobe Acrobat에서 PDF 문서가 표시되는 “페이지” 크기입니다.일반 보기에서는 오려내기 상자의 내용만 Adobe Acrobat에 표시됩니다.이러한 속성에 대한 자세한 설명은 Adobe.Pdf 사양, 특히 10.10.1 페이지 경계를 참조하십시오.

첫 번째 자르기 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 파이썬용 Aspose.PDF 파일을 사용하여 PDF를 특정 사각형 영역으로 변환합니다.이 함수는 여러 페이지 상자를 조정합니다.`crop_box`, `trim_box`, `art_box`, 및 `bleed_box`—일관된 시각적 결과를 보장합니다.자르기는 불필요한 여백을 제거하거나 페이지의 특정 영역에 초점을 맞추는 데 유용할 수 있습니다.

1. PDF를 다음과 같이 로드합니다. [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) (사용 `ap.Document()`).
1. 를 사용하여 자르기 사각형을 정의합니다. [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) 원하는 좌표 (포인트) 로
1. 설정 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)의 `crop_box`, `trim_box`, `art_box`, 및 `bleed_box` 정의된 직사각형으로.
1. 수정한 내용 저장 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 새 출력 파일에

```python
import sys
import aspose.pdf as ap
from os import path

def crop_page(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    new_box = ap.Rectangle(200, 220, 2170, 1520, True)
    document.pages[1].crop_box = new_box
    document.pages[1].trim_box = new_box
    document.pages[1].art_box = new_box
    document.pages[1].bleed_box = new_box

    document.save(output_file_name)
```

이 예제에서는 샘플 파일을 사용했습니다. [이리](crop_page.pdf).처음에는 페이지가 그림 1과 같이 보입니다.
![그림 1.잘린 페이지](crop_page.png)

변경 후에는 페이지가 그림 2와 같이 표시됩니다.
![그림 2.잘린 페이지](crop_page2.png)

## 첫 이미지 내용을 기반으로 PDF 페이지 자르기

첫 번째 자르기 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 페이지에서 찾은 첫 번째 이미지의 경계를 기반으로 동적으로를 사용하여 [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/), 스크립트는 첫 번째 이미지를 식별하고 페이지의 이미지를 조정합니다. `crop_box` 이미지의 크기와 일치하도록.이 방법은 미리 정의된 좌표가 아닌 특정 시각적 콘텐츠에 초점을 맞추려는 경우에 유용합니다.

1. PDF를 다음과 같이 로드합니다. [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 를 사용하여 첫 페이지에서 이미지 찾기 [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/).
1. 이미지가 존재하는지 확인:
    - 발견되면 설정 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) `crop_box` 첫 번째 이미지와 일치하도록 [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/).
    - 그렇지 않은 경우 페이지를 변경하지 않고 사용자에게 알리십시오.
1. 수정한 내용 저장 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 지정된 출력 파일에

```python
import sys
import aspose.pdf as ap
from os import path

def crop_page_by_content(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    # Find first image on first page using ImagePlacementAbsorber
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    if len(absorber.image_placements) > 0:
        first_image = absorber.image_placements[1]
        document.pages[1].crop_box = first_image.rectangle
    else:
        print("No images found on the first page")
    document.save(output_file_name)
```

## 관련 페이지 주제

- [파이썬에서 PDF 페이지 작업하기](/pdf/ko/python-net/working-with-pages/)
- [파이썬에서 PDF 페이지 크기 변경하기](/pdf/ko/python-net/change-page-size/)
- [Python에서 PDF 페이지 속성 가져오기 및 설정](/pdf/ko/python-net/get-and-set-page-properties/)
- [파이썬에서 PDF 페이지 회전하기](/pdf/ko/python-net/rotate-pages/)
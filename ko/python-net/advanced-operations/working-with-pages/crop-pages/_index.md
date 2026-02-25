---
title: Python을 사용한 PDF 페이지 자르기
linktitle: PDF 페이지 자르기
type: docs
weight: 70
url: /ko/python-net/crop-pages/
description: Aspose.PDF for Python via .NET를 사용하여 너비, 높이, Bleed-, Crop- 및 Trimbox와 같은 페이지 속성을 변경할 수 있습니다.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에서 페이지 속성에 접근하고 수정하는 방법
Abstract: 이 문서는 Aspose.PDF for Python을 사용하여 PDF 문서의 페이지 속성에 접근하고 수정하는 방법에 대한 개요를 제공합니다. 여기서는 media box, bleed box, trim box, art box, crop box와 같은 여러 페이지 속성을 설명하고, 인쇄 및 표시 목적을 위한 PDF 페이지의 치수와 경계를 정의하는 역할을 설명합니다. media box는 가장 큰 페이지 크기를 나타내며, bleed box는 트리밍을 위해 페이지 가장자리를 넘어 잉크가 도달하도록 보장합니다. trim box는 트리밍 후 최종 문서 크기를 표시하고, art box는 실제 페이지 내용을 둘러싼 영역을 포함합니다. crop box는 Adobe Acrobat에서 표시되는 가시 영역을 정의합니다. 이 문서는 특정 페이지에 대해 새로운 crop box와 다른 박스들을 설정하는 Python 코드 예제를 포함하고 있습니다. 시각적 예시는 크롭 적용 전후의 페이지 모습을 보여주어 이러한 속성을 수정하는 실제 적용을 나타냅니다.
---

## 페이지 속성 가져오기

PDF 파일의 각 페이지는 너비, 높이, bleed-, crop- 및 trimbox와 같은 여러 속성을 가지고 있습니다. Aspose.PDF for Python을 사용하면 이러한 속성에 접근할 수 있습니다.

- **media_box**: media box는 가장 큰 페이지 박스입니다. 이는 문서가 PostScript 또는 PDF로 인쇄될 때 선택된 페이지 크기(예: A4, A5, US Letter 등)에 해당합니다. 다시 말해, media box는 PDF 문서가 표시되거나 인쇄되는 매체의 물리적 크기를 결정합니다.
- **bleed_box**: 문서에 bleed가 있는 경우 PDF에도 bleed box가 있습니다. bleed는 페이지 가장자리를 넘어 확장되는 색상(또는 아트워크)의 양을 의미합니다. 이는 문서가 인쇄되고 크기로 잘릴 때(“trimmed”) 잉크가 페이지 가장자리까지 닿도록 보장하기 위해 사용됩니다. 페이지가 약간 잘리더라도(트림 마크를 약간 벗어나 잘려도) 페이지에 흰색 가장자리가 나타나지 않습니다.
- **trim_box**: trim box는 인쇄 및 트리밍 후 문서의 최종 크기를 나타냅니다.
- **art_box**: art box는 문서 페이지의 실제 내용 주변에 그려지는 박스입니다. 이 페이지 박스는 다른 애플리케이션에서 PDF 문서를 가져올 때 사용됩니다.
- **crop_box**: crop box는 PDF 문서가 Adobe Acrobat에서 표시되는 "page" 크기입니다. 일반 보기에서는 crop box의 내용만 Adobe Acrobat에 표시됩니다. 이러한 속성에 대한 자세한 설명은 Adobe.Pdf 사양, 특히 10.10.1 페이지 경계 섹션을 참고하십시오.

PDF의 첫 번째 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)를 Aspose.PDF for Python을 사용하여 특정 직사각형 영역으로 자릅니다. 이 함수는 `crop_box`, `trim_box`, `art_box`, `bleed_box`와 같은 여러 페이지 박스를 조정하여 일관된 시각적 결과를 보장합니다. 크롭은 원하지 않는 여백을 제거하거나 페이지의 특정 영역에 초점을 맞출 때 유용할 수 있습니다.

1. PDF를 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) (use `ap.Document()`) 형태로 로드합니다.
1. 원하는 좌표(포인트 단위)로 [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/)을 사용하여 크롭 직사각형을 정의합니다.
1. 정의한 직사각형으로 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)의 `crop_box`, `trim_box`, `art_box`, `bleed_box`를 설정합니다.
1. 수정된 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)를 새로운 출력 파일에 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def crop_page(input_file_name, output_file_name):
    """
    Crops the first page of a PDF document to a specified rectangular area.
    This function loads a PDF document, defines a new rectangular boundary,
    and applies this boundary to multiple box types (crop, trim, art, and bleed)
    of the first page. The modified document is then saved to a new file.
    Args:
        input_file_name (str): Path to the input PDF file to be cropped.
        output_file_name (str): Path where the cropped PDF will be saved.
    Returns:
        None
    Note:
        The cropping rectangle is set to coordinates (200, 220, 2170, 1520)
        which defines the visible area of the page. All box types are set
        to the same dimensions to ensure consistent cropping behavior.
    """
    document = ap.Document(input_file_name)

    new_box = ap.Rectangle(200, 220, 2170, 1520, True)
    document.pages[1].crop_box = new_box
    document.pages[1].trim_box = new_box
    document.pages[1].art_box = new_box
    document.pages[1].bleed_box = new_box

    document.save(output_file_name)
```

이 예제에서는 [여기](crop_page.pdf) 샘플 파일을 사용했습니다. 처음에 우리 페이지는 그림 1에 표시된 것과 같습니다.
![그림 1. 잘린 페이지](crop_page.png)

변경 후 페이지는 그림 2와 같이 보입니다.
![그림 2. 잘린 페이지](crop_page2.png)

## 첫 번째 이미지 콘텐츠 기반 PDF 페이지 자르기

PDF의 첫 번째 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)를 페이지에서 발견된 첫 번째 이미지의 경계에 따라 동적으로 자릅니다. [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/)를 사용하여 스크립트가 첫 번째 이미지를 식별하고 페이지의 `crop_box`를 이미지 크기에 맞게 조정합니다. 이 방법은 미리 정의된 좌표 대신 특정 시각적 콘텐츠에 초점을 맞추고 싶을 때 유용합니다.

1. PDF를 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)로 로드합니다.
1. [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/)를 사용하여 첫 번째 페이지에서 이미지를 찾습니다.
1. 이미지가 존재하는지 확인합니다:
- 찾은 경우, 첫 번째 이미지의 [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/)에 맞게 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) `crop_box`를 설정합니다.
- 찾지 못한 경우, 페이지를 그대로 유지하고 사용자에게 알립니다.
1. 수정된 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)을 지정된 출력 파일에 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def crop_page_by_content(input_file_name, output_file_name):
    """
    Crops the first page of a PDF document to the bounds of the first image found on that page.
    This function opens a PDF document, locates the first image on the first page,
    and sets the page's crop box to match the image's rectangle dimensions. If no
    images are found, the page remains unchanged.
    Args:
        input_file_name (str): Path to the input PDF file to be processed.
        output_file_name (str): Path where the cropped PDF will be saved.
    Returns:
        None
    Raises:
        Exception: May raise exceptions related to file I/O operations or PDF processing
                  if the input file is invalid, corrupted, or inaccessible.
    Note:
        - Only processes the first page of the document
        - Uses the first image found on the page for cropping dimensions
        - If no images are found, prints a message and saves the document unchanged
        - Requires the aspose.pdf library (imported as 'ap')
    """
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

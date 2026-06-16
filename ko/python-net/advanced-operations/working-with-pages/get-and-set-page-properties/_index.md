---
title: Python에서 PDF 페이지 속성 가져오기 및 설정하기
linktitle: 페이지 속성 가져오기 및 설정
type: docs
weight: 90
url: /ko/python-net/get-and-set-page-properties/
description: Python에서 크기, 개수 및 색상 정보와 같은 PDF 페이지 속성을 검사하고 업데이트하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 페이지 속성을 가져오고 설정하는 방법
Abstract: 이 문서에서는 Python을 사용하여 PDF 파일에서 페이지 속성을 읽고 설정하는 데 중점을 두고 .NET을 통한 Python용 Aspose.PDF 기능에 대해 설명합니다.이 문서에서는 PDF의 페이지 수 결정, 페이지 속성 액세스 및 수정, 색상 정보 처리 등 다양한 기능을 다룹니다.페이지 수를 구하기 위해 `Document` 클래스와 `PageCollection` 컬렉션을 사용하며, 문서를 저장하지 않고도 페이지 수를 검색하는 방법을 보여주는 코드 스니펫을 사용합니다.이 문서에서는 MediaBox, BleedBox, TrimBox, ArtBox 및 CropBox와 같은 다양한 페이지 속성에 대해 설명하고 이러한 속성에 액세스하기 위한 코드 예제를 제공합니다.또한 PDF에서 특정 페이지를 검색하여 별도의 문서로 저장하는 작업과 각 페이지의 색상 유형을 결정하는 방법도 설명합니다.전체 예제는 Python으로 구현되어 이러한 기능의 실제 적용을 보여줍니다.
---

.NET을 통한 파이썬용 Aspose.PDF 파일을 사용하면 파이썬 응용 프로그램에서 PDF 파일의 페이지 속성을 읽고 설정할 수 있습니다.이 단원에서는 PDF 파일의 페이지 수를 가져오는 방법, 색상과 같은 PDF 페이지 속성에 대한 정보를 가져오는 방법, 페이지 속성을 설정하는 방법을 보여줍니다.예제에서는 다음을 사용합니다. [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 과 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) API는 파이썬으로 작성되었습니다.

문서 분석 또는 정규화 작업의 일환으로 페이지 메타데이터를 검사하거나, 페이지 수를 확인하거나, 페이지 수준 특성을 업데이트해야 할 때 이 가이드를 사용하십시오.

## PDF 파일의 페이지 수 가져오기

문서 작업을 할 때 문서에 포함된 페이지 수를 알고 싶어하는 경우가 많습니다.Aspose.PDF 를 사용하면 코드를 두 줄만 사용해도 됩니다.

PDF 파일의 페이지 수를 구하려면:

1. 를 사용하여 PDF 파일을 엽니다. [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 수업.
1. 그런 다음 사용 [페이지 컬렉션](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 컬렉션의 Count 속성 (Document 객체에서) 을 사용하여 문서의 총 페이지 수를 가져옵니다.

다음 코드 스니펫은 PDF 파일의 페이지 수를 가져오는 방법을 보여줍니다.

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_count(input_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Get page count
    print("Page Count:", str(len(document.pages)))
```

### 문서를 저장하지 않고 페이지 수 가져오기

때로는 PDF 파일을 즉시 생성하고 PDF 파일 작성 중에 파일을 시스템이나 스트림에 저장하지 않고 PDF 파일의 페이지 수를 가져와야 하는 요구 사항 (목차 작성 등) 이 발생할 수 있습니다.따라서 이러한 요구 사항을 충족하기 위한 한 가지 방법이 있습니다. [프로세스_단락 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 문서 클래스에 도입되었습니다.문서를 저장하지 않고 페이지 수를 가져오는 단계를 보여주는 다음 코드 스니펫을 살펴보세요.

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_count_without_saving(input_file_name):
    # Instantiate Document instance
    document = ap.Document()
    # Add page to pages collection of PDF file
    page = document.pages.add()
    # Create loop instance
    for _ in range(0, 300):
        # Add TextFragment to paragraphs collection of page object
        page.paragraphs.add(ap.text.TextFragment("Pages count test"))
    # Process the paragraphs in PDF file to get accurate page count
    document.process_paragraphs()
    # Print number of pages in document
    print("Number of pages in document =", str(len(document.pages)))
```

## 페이지 속성 가져오기

PDF 파일의 각 페이지에는 너비, 높이, 블리드, 크롭 및 트림박스와 같은 다양한 속성이 있습니다.Aspose.PDF 를 사용하면 이러한 속성에 액세스할 수 있습니다.

### 페이지 속성에 대한 이해: 아트박스, 블리드박스, 크롭박스, 미디어박스, 트림박스, 렉트 프로퍼티의 차이점

- **미디어 상자**: 미디어 상자는 가장 큰 페이지 상자입니다.문서를 PostScript 또는 PDF로 인쇄할 때 선택한 페이지 크기 (예: A4, A5, US Letter 등) 에 해당합니다.즉, 미디어 상자는 PDF 문서를 표시하거나 인쇄하는 데 사용되는 미디어의 실제 크기를 결정합니다.
- **블리드 박스**: 문서에 블리드가 있는 경우 PDF에도 블리드 박스가 표시됩니다.블리드는 페이지 가장자리를 벗어나는 색상 (또는 아트워크) 의 양입니다.문서를 인쇄하고 크기에 맞게 잘라낼 때 (“트리밍”) 잉크가 페이지 가장자리까지 들어가도록 하는 데 사용됩니다.페이지의 트리밍이 잘못되어도 (트림 표시가 약간 잘려서) 페이지에 흰색 가장자리가 나타나지 않습니다.
- **트림 상자**: 트림 상자는 인쇄 및 트리밍 후 문서의 최종 크기를 나타냅니다.
- **아트 박스**: 아트 박스는 문서에 있는 페이지의 실제 내용 주위에 그려진 상자입니다.이 페이지 상자는 다른 응용 프로그램에서 PDF 문서를 가져올 때 사용됩니다.
- **자르기 상자**: 자르기 상자는 Adobe Acrobat에서 PDF 문서가 표시되는 “페이지” 크기입니다.일반 보기에서는 오려내기 상자의 내용만 Adobe Acrobat에 표시됩니다.
  이러한 속성에 대한 자세한 설명은 Adobe.Pdf 사양, 특히 10.10.1 페이지 경계를 참조하십시오.
-- **Page.Rect**: 미디어박스와 드롭박스의 교차점 (흔히 보이는 직사각형) (`Page.rect`).를 참조하십시오. [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) 직사각형 속성에 대한 유형아래 그림은 이러한 속성을 보여줍니다.

자세한 내용은 다음 사이트를 참조하십시오. [이 페이지](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### 페이지 속성 액세스

더 [페이지](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 클래스는 특정 PDF 페이지와 관련된 모든 속성을 제공합니다.PDF 파일의 모든 페이지는 에 포함되어 있습니다. [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 사물의 [페이지 컬렉션](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 컬렉션.

거기에서 각 개인에 액세스할 수 있습니다. `Page` 인덱스를 사용하는 객체 또는 컬렉션을 반복하여 모든 페이지를 가져옵니다.개별 페이지에 액세스하면 해당 속성을 가져올 수 있습니다.다음 코드 스니펫은 페이지 속성을 가져오는 방법을 보여줍니다 ( `Page` API).

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_properties(input_file_name):
    # Open document
    document = ap.Document(input_file_name)
    # Get particular page
    page = document.pages[1]

    # Get page properties
    boxes = {
        "ArtBox": page.art_box,
        "BleedBox": page.bleed_box,
        "CropBox": page.crop_box,
        "MediaBox": page.media_box,
        "TrimBox": page.trim_box,
        "Rect": page.rect,
    }

    # Print box properties
    for box_name, box in boxes.items():
        print(
            f"{box_name} : Height={box.height},Width={box.width},LLX={box.llx},LLY={box.lly},URX={box.urx},URY={box.ury}"
        )

    # Print other page properties
    print(f"Page Number : {page.number}")
    print(f"Rotate : {page.rotate}")
```

## 페이지 색상 결정

더 [페이지](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 클래스는 페이지에서 사용하는 색상 유형 (RGB, 흑백, 회색조 또는 정의되지 않음) 을 포함하여 PDF 문서의 특정 페이지와 관련된 속성을 제공합니다.

PDF 파일의 모든 페이지는 다음에 포함되어 있습니다. [페이지 컬렉션](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 컬렉션.더 [색상_유형](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) 속성은 페이지의 요소 색상을 지정합니다.특정 PDF 페이지의 색상 정보를 가져오거나 결정하려면 다음을 사용하십시오. [페이지](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 사물의 [색상_유형](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) 재산.

다음 코드 스니펫은 PDF 파일의 개별 페이지를 반복하여 색상 정보를 가져오는 방법을 보여줍니다.

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_color_type(input_file_name):
    # Open source PDF file
    document = ap.Document(input_file_name)
    # Iterate through all the page of PDF file
    for page_number in range(1, len(document.pages) + 1):
        # Get the color type information for particular PDF page
        page_color_type = document.pages[page_number].color_type
        color_type_map = {
            ap.ColorType.BLACK_AND_WHITE: "Black and white",
            ap.ColorType.GRAYSCALE: "Gray Scale",
            ap.ColorType.RGB: "RGB",
            ap.ColorType.UNDEFINED: "undefined",
        }
        color_description = color_type_map.get(page_color_type, "unknown")
        print(f"Page # {page_number} is {color_description}.")
```

## 관련 페이지 주제

- [파이썬에서 PDF 페이지 작업하기](/pdf/ko/python-net/working-with-pages/)
- [파이썬에서 PDF 페이지 크기 변경하기](/pdf/ko/python-net/change-page-size/)
- [파이썬에서 PDF 페이지 자르기](/pdf/ko/python-net/crop-pages/)
- [파이썬에서 PDF 페이지 회전하기](/pdf/ko/python-net/rotate-pages/)
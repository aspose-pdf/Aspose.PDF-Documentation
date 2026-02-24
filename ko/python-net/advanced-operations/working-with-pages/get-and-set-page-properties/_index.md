---
title: Python을 사용한 페이지 속성 가져오기 및 설정
linktitle: 페이지 속성 가져오기 및 설정
type: docs
weight: 90
url: /ko/python-net/get-and-set-page-properties/
description: 이 섹션에서는 PDF 파일의 페이지 수를 얻는 방법과 색상과 같은 PDF 페이지 속성 정보를 가져오고 페이지 속성을 설정하는 방법을 보여줍니다.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 페이지 속성을 가져오고 설정하는 방법
Abstract: 이 문서는 Aspose.PDF for Python via .NET의 기능을 논의하며, Python을 사용하여 PDF 파일의 페이지 속성을 읽고 설정하는 데 중점을 둡니다. 이 문서에서는 PDF의 페이지 수 결정, 페이지 속성 접근 및 수정, 색상 정보 처리 등 다양한 기능을 다룹니다. 페이지 수를 얻기 위해 `Document` 클래스와 `PageCollection` 컬렉션을 사용하며, 코드를 통해 문서를 저장하지 않고도 페이지 수를 가져오는 방법을 보여줍니다. 또한 MediaBox, BleedBox, TrimBox, ArtBox 및 CropBox와 같은 다양한 페이지 속성을 설명하고, 이러한 속성에 접근하는 코드 예제를 제공합니다. 추가로 PDF에서 특정 페이지를 추출하여 별도 문서로 저장하는 방법과 각 페이지의 색상 유형을 판단하는 방법도 다룹니다. 전체 예제는 Python으로 구현되어 이러한 기능의 실용적인 적용을 보여줍니다.
---

Aspose.PDF for Python via .NET를 사용하면 Python 애플리케이션에서 PDF 파일의 페이지 속성을 읽고 설정할 수 있습니다. 이 섹션에서는 PDF 파일의 페이지 수를 얻는 방법, 색상과 같은 PDF 페이지 속성 정보를 가져오고 페이지 속성을 설정하는 방법을 보여줍니다. 예제는 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 및 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) API를 사용하며 Python으로 작성되었습니다.

## PDF 파일의 페이지 수 가져오기

문서 작업 시, 종종 페이지 수를 알고 싶습니다. Aspose.PDF를 사용하면 두 줄의 코드만으로 가능합니다.

PDF 파일의 페이지 수를 얻으려면:

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스를 사용하여 PDF 파일을 엽니다.
1. 그런 다음 [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 컬렉션의 Count 속성(Document 객체에서)을 사용하여 문서의 전체 페이지 수를 가져옵니다.

다음 코드 스니펫은 PDF 파일의 페이지 수를 얻는 방법을 보여줍니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_count(input_file_name):
    """
    Get the total number of pages in a PDF document.
    Args:
        input_file_name (str): Path to the input PDF file.
    Returns:
        None: Prints the page count to console.
    Example:
        get_page_count("example.pdf")
        # Output: Page Count: 10
    """
    # Open document
    document = ap.Document(input_file_name)

    # Get page count
    print("Page Count:", str(len(document.pages)))
```

### 문서를 저장하지 않고 페이지 수 가져오기

때때로 우리는 PDF 파일을 즉시 생성하고, PDF 파일 생성 중에 (목차 생성 등) 파일을 시스템이나 스트림에 저장하지 않고 PDF 파일의 페이지 수를 얻어야 하는 경우가 있습니다. 이러한 요구를 충족하기 위해 Document 클래스에 [process_paragraphs()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드가 도입되었습니다. 아래 코드 스니펫을 살펴보시면 문서를 저장하지 않고 페이지 수를 얻는 단계가 설명되어 있습니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_count_without_saving(input_file_name):
    """
    Get the page count of a PDF document after adding content without saving the file.

    This function opens an existing PDF document, adds a new page with 300 text fragments,
    processes the paragraphs to ensure accurate page counting, and prints the total number
    of pages in the document. The document is not saved to disk.

    Args:
        input_file_name (str): Path to the input PDF file to be processed.

    Returns:
        None: This function prints the page count but does not return a value.

    Example:
        >>> get_page_count_without_saving("sample.pdf")
        Number of pages in document = 2
    """
    # Instantiate Document instance
    document = ap.Document(input_file_name)
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

PDF 파일의 각 페이지에는 너비, 높이, BleedBox, CropBox, TrimBox와 같은 여러 속성이 있습니다. Aspose.PDF를 사용하면 이러한 속성에 접근할 수 있습니다.

### 페이지 속성 이해: ArtBox, BleedBox, CropBox, MediaBox, TrimBox 및 Rect 속성의 차이점

- **Media box**: Media box는 가장 큰 페이지 박스이며, 문서를 PostScript 또는 PDF로 인쇄할 때 선택된 페이지 크기(예: A4, A5, US Letter 등)를 나타냅니다. 즉, Media box는 PDF 문서가 표시되거나 인쇄되는 매체의 물리적 크기를 결정합니다.
- **Bleed box**: 문서에 Bleed가 있는 경우 PDF에도 Bleed box가 있습니다. Bleed는 페이지 가장자리를 넘어서는 색상(또는 아트워크)의 양을 의미합니다. 이는 문서를 인쇄하고 크기에 맞게 자를 때(“trimmed”) 잉크가 페이지 가장자리까지 도달하도록 보장하기 위해 사용됩니다. 페이지가 잘못 잘리더라도(트림 마크에서 약간 벗어나 잘리더라도) 흰 가장자리가 나타나지 않습니다.
- **Trim box**: Trim box는 인쇄 및 트리밍 후 문서의 최종 크기를 나타냅니다.
- **Art box**: Art box는 문서 페이지의 실제 콘텐츠 주위에 그려지는 박스입니다. 이 페이지 박스는 다른 응용 프로그램에서 PDF 문서를 가져올 때 사용됩니다.
- **Crop box**: Crop box는 Adobe Acrobat에서 PDF 문서가 표시되는 “페이지” 크기입니다. 일반 보기에선 Crop box의 콘텐츠만 Adobe Acrobat에 표시됩니다.
이러한 속성에 대한 자세한 설명은 Adobe.Pdf 사양, 특히 10.10.1 페이지 경계 섹션을 참고하십시오.
-- **Page.Rect**: MediaBox와 DropBox(`Page.rect`)의 교차점(일반적으로 보이는 사각형)입니다. 사각형 속성에 대해서는 [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) 유형을 참조하십시오. 아래 그림은 이러한 속성을 보여줍니다.

자세한 내용은 [이 페이지](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html)를 방문하십시오.

### 페이지 속성 접근하기

 [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 클래스는 특정 PDF 페이지와 관련된 모든 속성을 제공합니다. PDF 파일의 모든 페이지는 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체의 [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 컬렉션에 포함됩니다.

이곳에서 인덱스를 사용해 개별 `Page` 객체에 접근하거나 컬렉션을 순회하여 모든 페이지를 가져올 수 있습니다. 개별 페이지에 접근하면 해당 페이지의 속성을 얻을 수 있습니다. 다음 코드 스니펫은 페이지 속성을 가져오는 방법(`Page` API)을 보여줍니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_properties(input_file_name):
    """
    Retrieves and displays various page properties for the first page of a PDF document.

    Args:
        input_file_name (str): Path to the PDF file to analyze.
    """
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
        "Rect": page.rect
    }

    # Print box properties
    for box_name, box in boxes.items():
        print(f"{box_name} : Height={box.height},Width={box.width},LLX={box.llx},LLY={box.lly},URX={box.urx},URY={box.ury}")

    # Print other page properties
    print(f"Page Number : {page.number}")
    print(f"Rotate : {page.rotate}")
```

## 페이지 색상 결정

[Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 클래스는 PDF 문서의 특정 페이지와 관련된 속성을 제공하며, 페이지가 사용하는 색상 종류(RGB, 흑백, 그레이스케일 또는 정의되지 않음)를 포함합니다.

PDF 파일의 모든 페이지는 [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 컬렉션에 포함됩니다. [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) 속성은 페이지의 요소 색상을 지정합니다. 특정 PDF 페이지의 색상 정보를 얻거나 결정하려면 [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 객체의 [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) 속성을 사용하십시오.

다음 코드 스니펫은 PDF 파일의 개별 페이지를 순회하면서 색상 정보를 얻는 방법을 보여줍니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_color_type(input_file_name):
    """
    Analyzes and prints the color type information for each page in a PDF document.

    This function opens a PDF file and iterates through all pages to determine
    the color type of each page (black and white, grayscale, RGB, or undefined).
    The results are printed to the console with human-readable descriptions.

    Args:
        input_file_name (str): Path to the PDF file to analyze.

    Returns:
        None: This function prints results directly to console and doesn't return a value.

    Example:
        >>> get_page_color_type("sample.pdf")
        Page # 1 is RGB.
        Page # 2 is Gray Scale.
        Page # 3 is Black and white.

    Note:
        Requires the aspose.pdf library (imported as ap) to be installed and available.
        The PDF file must be accessible at the specified path.
    """
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
            ap.ColorType.UNDEFINED: "undefined"
        }
        color_description = color_type_map.get(page_color_type, "unknown")
        print(f"Page # {page_number} is {color_description}.")
```



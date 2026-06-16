---
title: Python을 사용하여 PDF 파일에서 벡터 데이터 추출하기
linktitle: PDF에서 벡터 데이터 추출
type: docs
weight: 80
url: /ko/python-net/extract-vector-data-from-pdf/
description: Aspose.PDF 파일을 사용하면 PDF 파일에서 벡터 데이터를 쉽게 추출할 수 있습니다.위치, 색상, 선폭 등과 같은 벡터 데이터 (경로, 다각형, 폴리라인) 를 가져올 수 있습니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 문서에서 벡터 데이터에 액세스

용도 [그래픽 업소버](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/) 페이지의 벡터 그래픽 요소 검사하기 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).대상 페이지를 방문한 후 추출된 요소를 반복하여 사각형 경계, 위치, 그리기 연산자와 같은 속성을 살펴보세요.

1. 소스 PDF를 다음과 같이 엽니다. `Document`.
1. 만들기 `GraphicsAbsorber` 예.
1. 전화 `gr_absorber.visit(page)` 대상 페이지에.
1. 에서 추출한 항목 읽기 `gr_absorber.elements`.
1. 요소를 반복하고 속성을 출력 파일에 기록합니다.

```python
import aspose.pdf as ap


def extract_graphics_elements(infile, outfile):
    """
    Extract vector graphic elements from a specified page of a PDF and log basic element properties.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file for logging element info.
    """
    document = ap.Document(infile)
    try:
        gr_absorber = ap.vector.GraphicsAbsorber()
        # Visit page 2 (pages collection is 1-indexed; document.pages[1] is the second page)
        gr_absorber.visit(document.pages[1])

        elements = gr_absorber.elements
        with open(outfile, "w", encoding="utf-8") as f:
            for idx, elem in enumerate(elements, start=1):
                # Basic properties
                rect = elem.rectangle
                pos = elem.position
                ops_count = len(elem.operators)
                f.write(
                    f"Element {idx}: Rectangle = {rect}, Position = {pos}, Operators = {ops_count}\n"
                )
    finally:
        document.close()
```

## 페이지의 벡터 그래픽을 SVG 파일로 저장

PDF 페이지에서 SVG로 벡터 그래픽을 내보내 원본 PDF 외부에서 확장 가능한 경로와 모양을 유지할 수 있습니다.이 방법은 웹, 디자인 또는 게시 워크플로우에서 벡터 아트워크를 재사용하는 데 유용합니다.

1. PDF 문서를 로드합니다.
1. 대상 페이지에 접속합니다.
1. 전화 `page.try_save_vector_graphics()` 페이지의 벡터 경로를 SVG로 내보냅니다.
1. 문서를 닫습니다.

```python
import aspose.pdf as ap


def save_vector_graphics_to_svg(infile, svg_outfile):
    """
    Save vector graphics from a specified page of a PDF document into an SVG file.
    Args:
        infile (str): Path to input PDF file.
        svg_outfile (str): Path to output SVG file.
    """
    document = ap.Document(infile)
    try:
        page = document.pages[1]
        # Try to save vector graphics into SVG
        page.try_save_vector_graphics(svg_outfile)
    finally:
        document.close()
```

### 각 하위 경로를 별도의 SVG로 추출

페이지에 독립적인 벡터 경로가 여러 개 있는 경우 다음을 사용하십시오. [SVG 추출 옵션](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/svgextractionoptions/) 와 [SVG 추출기](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/svgextractor/) 각 하위 경로를 별도의 SVG 파일에 기록합니다.

1. PDF를 로드합니다.
1. 작성 `SvgExtractionOptions` 및 설정 `extract_every_subpath_to_svg`.
1. 문서의 첫 페이지에 액세스합니다.
1. 인스턴스화 `SvgExtractor` 옵션과 함께.
1. 전화 `extractor.extract()` 각 벡터 하위 경로에 대해 별도의 SVG 파일을 작성합니다.
1. 문서를 닫습니다.

```python
import aspose.pdf as ap


def extract_subpaths_to_svgs(infile, output_dir):
    """
    Extract each vector sub-path on a PDF page into separate SVG files using extraction options.
    Args:
        infile (str): Input PDF file path.
        output_dir (str): Directory path where SVG files will be saved.
    """
    document = ap.Document(infile)
    try:
        options = ap.vector.SvgExtractionOptions()
        options.extract_every_subpath_to_svg = True

        page = document.pages[1]
        extractor = ap.vector.SvgExtractor(options)
        extractor.extract(page, output_dir)
    finally:
        document.close()
```

### 요소 목록을 단일 이미지로 추출

PDF 페이지에서 여러 벡터 요소를 추출하여 하나의 결합된 SVG 이미지로 저장합니다.이는 그룹화된 도형, 다이어그램 또는 드로잉 조각 간의 시각적 관계를 보존하려는 경우에 유용합니다.

1. 를 사용하여 PDF 열기 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 페이지를 선택하고 벡터 요소 목록을 준비합니다.
1. 용도 [SVG 추출기](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/svgextractor/) 이러한 요소를 하나의 SVG로 결합합니다.
1. 출력 파일을 저장합니다.

```python
import aspose.pdf as ap


def extract_list_of_elements_to_single_image(infile, outfile):
    """
    Extracts multiple vector graphic elements from a PDF page and saves them as a single SVG image.
    Args:
        infile (str): Path to the input PDF file.
        outfile (str): Path to the output SVG file.
    """
    document = ap.Document(infile)
    try:
        page = document.pages[1]
        svg_extractor = ap.vector.SvgExtractor()
        elements = []  # Fill this list with specific graphic elements as needed
        svg_extractor.extract(elements, page, outfile)
    finally:
        document.close()
```

### 단일 요소 추출

PDF에서 특정 벡터 요소 하나를 추출하여 개별 SVG 파일로 저장합니다.이는 보다 복잡한 벡터 기반 페이지에서 로고, 아이콘 또는 독립형 모양을 분리하는 데 유용합니다.

1. 만들기 [그래픽 업소버](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/) 벡터 데이터를 캡처합니다.
1. 특정 페이지를 방문하여 벡터 요소를 수집하세요.
1. 다음과 같은 대상 요소를 선택합니다. [X폼 배치](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/xformplacement/).
1. 이 단일 요소를 SVG 파일에 저장합니다.

```python
import aspose.pdf as ap


def extract_single_vector_element(infile, outfile):
    """
    Extracts a specific vector graphic element (e.g., an XFormPlacement) from a PDF page and saves it as an SVG file.
    Args:
        infile (str): Path to the input PDF file.
        outfile (str): Path to the output SVG file.
    """
    document = ap.Document(infile)
    try:
        graphics_absorber = ap.vector.GraphicsAbsorber()
        page = document.pages[1]
        graphics_absorber.visit(page)
        xform_placement = graphics_absorber.elements[1]
        if isinstance(xform_placement, ap.vector.XFormPlacement):
            xform_placement.elements[2].save_to_svg(outfile)
    finally:
        document.close()
```

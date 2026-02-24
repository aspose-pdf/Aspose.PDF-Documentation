---
title: Python을 사용하여 PDF 파일에서 벡터 데이터 추출
linktitle: PDF에서 벡터 데이터 추출
type: docs
weight: 80
url: /ko/python-net/extract-vector-data-from-pdf/
description: Aspose.PDF를 사용하면 PDF 파일에서 벡터 데이터를 쉽게 추출할 수 있습니다. 위치, 색상, 선두께 등과 같은 벡터 데이터(경로, 폴리곤, 폴리라인)를 얻을 수 있습니다.
lastmod: "2025-11-05"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## PDF 문서에서 벡터 데이터에 접근하기

다음 코드 스니펫은 GraphicsAbsorber 클래스를 사용하여 PDF 문서의 특정 페이지에서 벡터 그래픽 요소를 추출하고 사각형 경계, 연산자 및 위치와 같은 속성을 확인하는 방법을 보여줍니다.

1. 'ap.Document'를 사용하여 PDF 문서를 로드합니다.
1. 'GraphicsAbsorber' 인스턴스를 초기화합니다.
1. 두 번째 페이지를 검사하기 위해 'gr_absorber.visit()'를 호출합니다.
1. 'gr_absorber.elements'를 통해 추출된 요소를 가져옵니다.
1. 각 요소를 반복하면서 속성(사각형, 위치, 연산자 수)을 기록합니다.
1. 정보를 텍스트 출력 파일에 기록합니다.
1. 리소스를 해제하기 위해 문서를 닫습니다.

```python

import os
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
                f.write(f"Element {idx}: Rectangle = {rect}, Position = {pos}, Operators = {ops_count}\n")
    finally:
        document.close()
```

## 페이지에서 벡터 그래픽을 SVG 파일로 저장하기

PDF 페이지에서 벡터 그래픽을 SVG 파일로 내보내어 벡터 형태와 경로를 보존합니다:

1. PDF 문서를 로드합니다.
1. 대상 페이지에 접근합니다().
1. 페이지의 벡터 경로를 SVG 파일로 내보내는 'page.try_save_vector_graphics()'를 호출합니다.
1. 문서를 닫습니다.

```python

import os
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

### 각 서브 경로를 별도의 SVG로 추출하기

추출 옵션 객체를 사용하여 벡터 그래픽의 모든 서브 경로(구성 요소)를 별도의 SVG 파일로 추출합니다.

1. PDF를 로드합니다.
1. 'SvgExtractionOptions'를 생성하고 'extract_every_subpath_to_svg'를 설정합니다.
1. 문서의 첫 페이지에 접근합니다.
1. 옵션을 사용하여 'SvgExtractor'를 인스턴스화합니다.
1. 각 벡터 서브 경로에 대한 별도 SVG 파일을 출력하기 위해 'extractor.extract()'를 호출합니다.
1. 문서를 닫습니다.

```python

import os
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

### 요소 목록을 단일 이미지로 추출하기

PDF 페이지에서 여러 벡터 요소를 추출하고 Aspose.PDF for Python을 사용하여 하나의 결합된 SVG 이미지로 저장합니다.
다이어그램이나 CAD 내보내기와 같이 그룹화된 형태나 도면의 시각적 구조를 보존하려는 경우에 유용합니다.

1. 'Document'를 사용하여 PDF를 엽니다.
1. 페이지를 선택하고 벡터 요소 목록을 준비합니다.
1. 'SvgExtractor'를 사용하여 해당 요소들을 하나의 SVG로 결합합니다.
1. 출력 파일을 저장합니다.

```python

import os
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

PDF에서 특정 벡터 요소 하나를 추출하여 개별 SVG 파일로 저장합니다.
복잡한 벡터 기반 PDF에서 로고, 아이콘 또는 독립형 형태를 분리하고 내보내는 데 유용합니다.

1. 벡터 데이터를 캡처하기 위해 'GraphicsAbsorber'를 생성합니다.
1. 특정 페이지를 방문하여 해당 페이지의 벡터 요소를 수집합니다.
1. 대상 요소를 선택합니다(예: 'XFormPlacement').
1. 해당 단일 요소를 SVG 파일로 저장합니다.

```python

import os
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

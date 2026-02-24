---
title: Python을 사용한 영역 기반 추출
linktitle: 영역 기반 추출
type: docs
weight: 20
url: /ko/python-net/region-based-extraction/
description: 이 섹션에는 Python에서 Aspose.PDF를 사용하여 PDF 문서에서 영역 기반 추출을 수행하는 기사들이 포함되어 있습니다.
lastmod: "2025-11-05"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## 페이지의 특정 영역에서 텍스트 추출

Aspose.PDF for Python을 사용하여 PDF의 특정 페이지에서 정의된 사각형 영역의 텍스트를 추출합니다. 좌표를 지정하면 표 셀, 단락 블록, 양식 필드 영역과 같은 특정 영역에 추출을 집중할 수 있습니다.

헤더, 푸터, 청구서 또는 텍스트가 예측 가능한 위치에 나타나는 고정 레이아웃 보고서와 같은 영역 기반 텍스트 추출에 이상적입니다.

1. PDF 문서를 엽니다.
1. 'TextAbsorber'를 생성합니다.
1. 'text_search_options'를 구성하여 사각형 영역으로 제한합니다.
1. 특정 페이지에 흡수기를 적용합니다.
1. 추출된 텍스트를 기록합니다.

```python

import os
import aspose.pdf as ap

def extract_text_from_region(infile, page_number, rect_coords, outfile):
    """
    Extract text from a specified rectangular region on a given page.
    Args:
        infile (str): Path to input PDF file.
        page_number (int): 1-based index of the page.
        rect_coords (tuple): (llx, lly, urx, ury) coordinates of the rectangle.
        outfile (str): Output text file path.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.TextAbsorber()
        # Set options to restrict search to the rectangle
        absorber.text_search_options.limit_to_page_bounds = True
        llx, lly, urx, ury = rect_coords
        absorber.text_search_options.rectangle = ap.Rectangle(llx, lly, urx, ury, True)
        # Accept on the specific page
        document.pages[page_number].accept(absorber)
        extracted_text = absorber.text
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        document.close()
```

## 단락을 순회하면서 추출하기

PDF 문서에서 특정 텍스트( "일반 텍스트" 또는 "정규식" 사용)를 단일 페이지나 전체 문서에서 검색하여 텍스트를 얻을 수 있으며, 단일 페이지, 페이지 범위 또는 전체 문서의 전체 텍스트를 얻을 수도 있습니다. 그러나 경우에 따라 PDF 문서에서 단락 형태의 텍스트 또는 단락 자체를 추출해야 할 필요가 있습니다. 우리는 PDF 문서 페이지의 텍스트에서 섹션 및 단락을 검색하는 기능을 구현했습니다. TextFragmentAbsorber 및 TextAbsorber와 유사한 ParagraphAbsorber 클래스를 도입했으며, 이를 사용해 PDF 문서에서 단락을 추출할 수 있습니다.

Aspose.PDF 라이브러리를 사용하면 PDF 파일을 읽고 'ParagraphAbsorber'를 사용하여 각 페이지에서 모든 단락 텍스트를 추출할 수 있습니다. 출력은 페이지, 섹션 및 단락별로 정리되며, 추출된 내용은 일반 텍스트 파일에 기록됩니다. 이는 텍스트 분석, 보관 또는 구조화된 PDF 콘텐츠를 읽기 쉬운 형식으로 변환하는 데 유용합니다.

1. PDF 문서를 엽니다.
1. 'ParagraphAbsorber'를 인스턴스화합니다.
1. 'absorber.visit(document)'를 호출하여 모든 페이지에서 단락을 스캔합니다.
1. 흡수기의 'page_markups' 컬렉션을 순회합니다.
1. 각 page‑markup에 대해 'sections'를 순회하고, 섹션 내의 각 'paragraph'를 순회합니다.
1. 각 단락 내부에서 'lines'를 순회하고, 라인 내의 각 'fragment'를 순회하여 'fragment.text'를 누적합니다.
1. 각 단락(페이지/섹션/단락 인덱스 포함)을 출력 파일에 기록합니다.
1. 작업이 끝나면 문서를 닫습니다.

```python

import os
import aspose.pdf as ap

def extract_paragraphs_from_pdf(infile, outfile):
    """
    Extract all paragraphs from a PDF document, and write each paragraph’s text into an output file.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.ParagraphAbsorber()
        absorber.visit(document)

        with open(outfile, "w", encoding="utf‑8") as tw:
            for page_markup in absorber.page_markups:
                for sec_idx, section in enumerate(page_markup.sections, start=1):
                    for para_idx, paragraph in enumerate(section.paragraphs, start=1):
                        # Concatenate all fragments/lines in the paragraph
                        parts = []
                        for line in paragraph.lines:
                            for fragment in line:
                                parts.append(fragment.text)
                            parts.append("\r\n")
                        paragraph_text = "".join(parts)
                        tw.write(f"Page {page_markup.number}, Section {sec_idx}, Paragraph {para_idx}:\n")
                        tw.write(paragraph_text + "\n")
    finally:
        document.close()
```

## 경계 폴리곤 렌더링을 사용한 단락 추출

이 코드 스니펫은 PDF의 특정 페이지에서 단락 수준 텍스트와 레이아웃 정보를 추출합니다. 각 단락의 경계 사각형 및 폴리곤 좌표와 실제 텍스트 내용을 캡처하여 결과를 텍스트 파일에 기록합니다. 이는 문서 구조 분석, 레이아웃 매핑, 혹은 접근성 및 콘텐츠 추출 작업을 위한 데이터 준비에 유용합니다.

1. PDF를 열고 문서를 로드합니다.
1. 'ParagraphAbsorber'를 인스턴스화합니다.
1. 원하는 특정 페이지에 대해 'absorber.visit(page)'를 호출합니다.
1. 'absorber.page_markups'에서 첫 번째 'page_markup'을 가져옵니다.
1. 해당 마크업의 각 섹션에 대해:
- 해당 섹션의 'rectangle'을 가져옵니다.
1. 섹션 내의 각 단락에 대해:
- 그 단락의 'points'(폴리곤)를 가져옵니다.
- 'paragraph.lines'를 순회하고 'fragment.text'를 추출합니다.
1. 기하학 및 텍스트 정보를 출력 파일에 기록합니다.
1. 문서를 닫습니다.

```python

import os
import aspose.pdf as ap

def extract_paragraphs_with_geometry(infile, outfile):
    """
    Extract paragraphs and record geometry info (rectangle / polygon) for each paragraph in a PDF.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.ParagraphAbsorber()
        absorber.visit(document.pages[1])  # Visit page 2 (pages are 1-indexed)

        page_markup = absorber.page_markups[0]
        with open(outfile, "w", encoding="utf‑8") as tw:
            for sec_idx, section in enumerate(page_markup.sections, start=1):
                tw.write(f"Section {sec_idx}: rectangle = {section.rectangle}\n")
                for para_idx, paragraph in enumerate(section.paragraphs, start=1):
                    tw.write(f"  Paragraph {para_idx}: polygon = {paragraph.points}\n")
                    # Concatenate paragraph text
                    parts = []
                    for line in paragraph.lines:
                        for fragment in line:
                            parts.append(fragment.text)
                        parts.append("\r\n")
                    tw.write("    Text: " + "".join(parts) + "\n\n")
    finally:
        document.close()
```


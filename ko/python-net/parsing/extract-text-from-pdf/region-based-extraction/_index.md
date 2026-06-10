---
title: Python을 사용한 지역 기반 추출
linktitle: 지역 기반 추출
type: docs
weight: 20
url: /ko/python-net/region-based-extraction/
description: Python용 Aspose.PDF 를 사용하여 PDF 문서의 특정 페이지 영역 또는 단락 구조에서 텍스트를 추출하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 페이지의 특정 영역에서 텍스트 추출

용도 [텍스트 업소버](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/) 와 함께 [직사각형](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) 추출을 페이지의 특정 영역으로 제한합니다.이 방법은 머리글, 바닥글, 표 셀, 양식 필드, 청구서 또는 텍스트 위치가 미리 알려진 기타 고정 레이아웃 영역에서 영역을 기반으로 추출하는 데 유용합니다.

1. 소스 PDF를 다음과 같이 엽니다. [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 만들기 `TextAbsorber` 예.
1. 구성 `text_search_options` 추출을 직사각형으로 제한합니다.
1. 대상 페이지에서 흡수 장치를 수락합니다.
1. 추출한 텍스트를 출력 파일에 씁니다.

```python
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

## 단락을 반복하여 추출하기

용도 [단락 흡수기](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/paragraphabsorber/) 일반 페이지 텍스트 대신 단락 인식 추출이 필요한 경우와는 다릅니다 [텍스트 업소버](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/) 또는 [텍스트 프래그먼트 업소버](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/), 이 API는 페이지, 섹션 및 단락별로 출력을 구성하므로 텍스트 분석, 구조화된 내보내기 및 레이아웃에 따른 처리에 유용합니다.

1. 소스 PDF를 다음과 같이 엽니다. [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 만들기 `ParagraphAbsorber` 예.
1. 전화 `absorber.visit(document)` 모든 페이지를 분석할 수 있습니다.
1. 반복 실행 `page_markups`그런 다음 각 섹션과 단락을 통해
1. 각 단락의 텍스트 조각을 읽고 결과를 파일에 씁니다.

```python
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

        with open(outfile, "w", encoding="utf-8") as tw:
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
                        tw.write(
                            f"Page {page_markup.number}, Section {sec_idx}, Paragraph {para_idx}:\n"
                        )
                        tw.write(paragraph_text + "\n")
    finally:
        document.close()
```

## 바운딩 폴리곤 렌더링으로 단락 추출

또한 사용할 수 있습니다 [단락 흡수기](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/paragraphabsorber/) 단락 지오메트리를 검사합니다.이 방법은 텍스트를 추출하는 것 외에도 각 섹션 사각형과 단락 다각형을 기록하는데, 이는 레이아웃 매핑, 문서 분석, 접근성 도구 또는 영역 인식 후처리에 유용합니다.

1. 소스 PDF를 다음과 같이 엽니다. [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 만들기 `ParagraphAbsorber` 예.
1. 대상 페이지를 방문하세요.
1. 에서 페이지 마크업 읽기 `absorber.page_markups`.
1. 섹션과 단락을 반복하여 형상과 텍스트를 캡처합니다.
1. 사각형, 다각형, 텍스트 데이터를 출력 파일에 씁니다.

```python
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
        with open(outfile, "w", encoding="utf-8") as tw:
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

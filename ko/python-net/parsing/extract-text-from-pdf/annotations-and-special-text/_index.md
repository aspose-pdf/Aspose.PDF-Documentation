---
title: Python을 사용한 주석 및 특수 텍스트
linktitle: 주석 및 특수 텍스트
type: docs
weight: 40
url: /ko/python-net/annotation-and-special-text/
description: 이 섹션에는 Python에서 Aspose.PDF를 사용하여 PDF 문서에서 주석 및 특수 텍스트를 추출하는 기사들이 포함되어 있습니다.
lastmod: "2025-11-05"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## 스탬프 주석에서 텍스트 추출

Aspose.PDF for Python 라이브러리를 사용하면 PDF 페이지의 스탬프 주석(특히 StampAnnotation)에서 텍스트를 추출할 수 있습니다.

1. 문서를 엽니다.
1. 페이지의 주석 컬렉션에서 스탬프 주석에 접근합니다.
1. 스탬프의 외형 스트림(XForm)을 가져옵니다.
1. 'TextAbsorber'를 사용하여 해당 외형에 포함된 텍스트를 추출합니다.

```python

import os
import aspose.pdf as ap

def extract_text_from_stamp(infile, page_number, annotation_index, outfile):
    """
    Extracts text from a stamp annotation on a given page in a PDF document.
    Args:
        infile (str): Path to the input PDF file.
        page_number (int): 1-based index of the page containing the stamp.
        annotation_index (int): 1-based index of the annotation in that page.
        outfile (str): Path to the output text file where extracted text will be saved.
    """
    document = ap.Document(infile)
    try:
        page = document.pages[page_number]
        annot = page.annotations[annotation_index]
        # Ensure it's a StampAnnotation
        if isinstance(annot, ap.annotations.StampAnnotation):
            # Get normal appearance XForm of the stamp
            xform = annot.appearance["N"]
            absorber = ap.text.TextAbsorber()
            absorber.visit(xform)
            extracted = absorber.text
            with open(outfile, "w", encoding="utf-8") as f:
                f.write(extracted)
    finally:
        document.close()
```

## 강조된 텍스트 추출

PDF 표준은 문서에서 텍스트 일부를 강조 표시할 수 있는 기능을 제공합니다. 이러한 강조된 내용을 추출하려면 다음 단계를 따르세요:

1. `aspose.pdf as ap`와 사용 중인 모든 헬퍼(`is_assignable`, `cast`)를 가져옵니다.
2. `ap.Document(infile)`를 호출하여 PDF를 엽니다.
3. `document.pages`를 사용하여 원하는 페이지를 선택합니다(페이지 컬렉션은 1부터 시작합니다).
4. `page.annotations`를 반복하여 해당 페이지의 각 주석을 확인합니다.
5. 주석을 필터링하여 강조 주석만 처리하도록 합니다.
6. 주석을 `HighlightAnnotation`으로 캐스팅하고 `get_marked_text()`를 호출하여 강조된 텍스트를 읽습니다.
7. 반환된 텍스트를 출력하거나 다른 방식으로 처리합니다.

```python
def extract_highlight_text(infile):
    """
    Extract text from highlight annotations.

    Args:
        infile (str): Input PDF filename

    Returns:
        None

    Example:
        extract_highlight_text("sample.pdf")

    Note:
        Prints marked text from each highlight annotation on first page.
    """
    document = ap.Document(infile)
    page = document.pages[1]

    for annotation in page.annotations:
        if is_assignable(annotation, ap.annotations.HighlightAnnotation):
            highlight_annotation = cast(ap.annotations.HighlightAnnotation, annotation)
            print(highlight_annotation.get_marked_text())
```

## 위첨자 및 아래첨자 텍스트 추출

**위첨자와 아래첨자**는 주로 수식, 수학적 표현 및 화학 화합물의 명세에 사용됩니다. 같은 텍스트 구간에 많이 포함될 경우 편집하기 어렵습니다.
최근 릴리스 중 하나에서 **Aspose.PDF for Python via .NET** 라이브러리는 PDF에서 위첨자 및 아래첨자 텍스트를 추출하는 기능을 추가했습니다. 'TextFragmentAbsorber'를 사용하여 PDF 문서의 특정 페이지에서 위첨자와 아래첨자를 포함한 모든 텍스트를 추출합니다.

1. PDF 문서를 로드합니다.
1. 'TextFragmentAbsorber()'를 인스턴스화합니다. 이 객체는 버전 기능에 따라 위첨자/아래첨자 텍스트 감지를 지원합니다.
1. 'document.pages[page_number].accept(absorber)'를 호출하여 지정된 페이지만 스캔합니다.
1. 'absorber.text'를 통해 추출된 텍스트를 가져옵니다.
1. 표준 파일 I/O를 사용하여 텍스트를 출력 파일에 씁니다.
1. 문서를 닫아 자원을 해제합니다.

```python

import os
import aspose.pdf as ap

def extract_super_sub_text(infile, outfile, page_number=1):
    """
    Extract text (including superscript/subscript) from a specified page of a PDF and write to a text file.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
        page_number (int): 1‑based index of the page to extract.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.TextFragmentAbsorber()
        # Accept only the specific page for extraction
        document.pages[page_number].accept(absorber)
        extracted_text = absorber.text
        with open(outfile, "w", encoding="utf‑8") as f:
            f.write(extracted_text)
    finally:
        document.close()
```

## TextFragment를 반복하며 위첨자/아래첨자 감지

페이지의 각 텍스트 프래그먼트를 반복하면서 위첨자인지 아래첨자인지 확인하고 그에 따라 처리합니다.

1. PDF 문서를 로드합니다.
1. 'TextFragmentAbsorber()'를 생성하고 선택한 페이지에 적용합니다.
1. 'absorber.text_fragments'에 접근합니다. 이 컬렉션은 해당 페이지에서 발견된 프래그먼트를 반환합니다.
1. 각 프래그먼트에 대해:
- 'fragment.text'를 가져옵니다.
- 'fragment.text_state.superscript'와 'fragment.text_state.subscript'를 확인합니다.
- 프래그먼트 텍스트와 플래그를 포함한 한 줄을 출력 파일에 씁니다.
1. 파일과 문서를 닫습니다.

```python

import os
import aspose.pdf as ap

def extract_super_sub_details(infile, outfile, page_number=1):
    """
    Extract details of each text fragment on a page, identifying superscript and subscript items.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
        page_number (int): 1‑based page index.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.TextFragmentAbsorber()
        document.pages[page_number].accept(absorber)

        with open(outfile, "w", encoding="utf‑8") as f:
            for fragment in absorber.text_fragments:
                text = fragment.text
                is_sup = fragment.text_state.superscript  # True if superscript
                is_sub = fragment.text_state.subscript    # True if subscript
                f.write(f"Text: '{text}' | Superscript: {is_sup} | Subscript: {is_sub}\n")
    finally:
        document.close()
```

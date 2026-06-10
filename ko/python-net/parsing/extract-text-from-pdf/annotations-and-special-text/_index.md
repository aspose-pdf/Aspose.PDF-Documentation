---
title: Python을 사용한 주석 및 특수 텍스트
linktitle: 주석 및 특수 텍스트
type: docs
weight: 40
url: /ko/python-net/annotation-and-special-text/
description: Python용 Aspose.PDF 를 사용하여 PDF 문서의 스탬프 주석, 강조 표시된 텍스트 및 위 첨자/아래 첨자 내용에서 텍스트를 추출하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 스탬프 주석에서 텍스트 추출

용도 [텍스트 업소버](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber) 에 포함된 텍스트 추출하기 [스탬프 표기법](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/stampannotation) 출연 스트림.이는 스탬프 내용을 일반 텍스트로 저장하지 않고 XObject 형식으로 렌더링할 때 유용합니다.

1. 를 여십시오 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. 에서 대상 주석에 액세스할 수 있습니다. `page.annotations`.
1. 인지 확인 `StampAnnotation`그런 다음 XForm의 정상적인 모습을 검색합니다.
1. XForm을 다음으로 전달 `TextAbsorber.visit()` 포함된 텍스트를 추출합니다.

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

## 강조 표시된 텍스트 추출

페이지 주석을 반복하고 사용하세요 [주석을 강조 표시합니다. get_Marked_text ()](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/highlightannotation) 각 하이라이트에 포함된 텍스트 범위를 읽을 수 있습니다.페이지 주석 컬렉션은 1부터 시작합니다.

1. 를 여십시오 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document) 대상 페이지를 선택합니다.
1. 루프 스루 `page.annotations`.
1. 용도 `is_assignable` 필터링 대상 [하이라이트 주석](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/highlightannotation) 사례.
1. 주석 전송 및 전화 걸기 `get_marked_text()` 강조 표시된 콘텐츠를 검색합니다.

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

## 위 첨자 및 아래 첨자 텍스트 추출

위 첨자와 아래 첨자는 공식, 수학 표현식 및 화합물 이름에 자주 나타납니다..NET을 통한 파이썬용 Aspose.PDF 기능은 다음을 통해 이 내용을 추출할 수 있도록 지원합니다. [텍스트 프래그먼트 업소버](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber), 문자 수준의 위치 지정 메타데이터를 탐지합니다.

1. 를 여십시오 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. 만들기 `TextFragmentAbsorber` 예.
1. 전화 `document.pages[page_number].accept(absorber)` 대상 페이지를 스캔합니다.
1. 에서 전체 추출된 텍스트 검색 `absorber.text`.
1. 결과를 파일에 쓰고 문서를 닫습니다.

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
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(extracted_text)
    finally:
        document.close()
```

## 텍스트 조각을 반복하여 위 첨자/아래 첨자 감지

프래그먼트별 검사의 경우 반복 반복 `absorber.text_fragments` 그리고 읽어보세요 `text_state.superscript` 과 `text_state.subscript` 각각의 부울 플래그 [텍스트 프래그먼트](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment).

1. 를 여십시오 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document) 그리고 생성하십시오 [텍스트 프래그먼트 업소버](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber).
1. 대상 페이지의 흡수 장치를 수락하여 채웁니다. `absorber.text_fragments`.
1. 각 프래그먼트에 대해 읽어보십시오. `fragment.text`, `fragment.text_state.superscript`, 및 `fragment.text_state.subscript`.
1. 결과를 출력 파일에 기록하고 문서를 닫습니다.

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

        with open(outfile, "w", encoding="utf-8") as f:
            for fragment in absorber.text_fragments:
                text = fragment.text
                is_sup = fragment.text_state.superscript  # True if superscript
                is_sub = fragment.text_state.subscript  # True if subscript
                f.write(
                    f"Text: '{text}' | Superscript: {is_sup} | Subscript: {is_sub}\n"
                )
    finally:
        document.close()
```

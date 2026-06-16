---
title: 파이썬을 사용한 기본 텍스트 추출
linktitle: 기본 텍스트 추출
type: docs
weight: 10
url: /ko/python-net/basic-text-extraction/
description: Python용 Aspose.PDF 를 사용하여 모든 페이지에서 한 번에 또는 특정 페이지에서 PDF 문서에서 텍스트를 추출하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF 문서의 모든 페이지에서 텍스트 추출

용도 [텍스트 업소버](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber) PDF 문서의 모든 페이지에서 모든 텍스트를 캡처하여 텍스트 파일에 기록합니다.이 방법은 PDF를 검색 가능한 텍스트로 변환하거나, 콘텐츠 분석을 실행하거나, 색인화 및 다운스트림 처리를 위한 텍스트를 준비하는 데 매우 적합합니다.

1. 를 사용하여 PDF 문서 열기 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. 만들기 `TextAbsorber` 예.
1. 전화 `document.pages.accept(text_absorber)` 모든 페이지를 스캔합니다.
1. 에서 추출한 텍스트 검색 `text_absorber.text`.
1. 결과를 출력 텍스트 파일에 씁니다.

```python
import os
import aspose.pdf as ap


def extract_text_from_all_pages(infile, outfile):
    """
    Extract all text from every page of the PDF and write to an output text file.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
    """
    # Open the PDF document
    document = ap.Document(infile)
    # Create a TextAbsorber to extract text
    text_absorber = ap.text.TextAbsorber()
    # Accept the absorber for all pages
    document.pages.accept(text_absorber)
    # Get extracted text
    extracted_text = text_absorber.text
    # Write the text to an output file
    with open(outfile, "w", encoding="utf-8") as tw:
        tw.write(extracted_text)
```

## 특정 페이지에서 텍스트 추출

신청하기 [텍스트 업소버](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber) 여러 페이지로 된 문서의 해당 섹션에서 텍스트를 분리하여 저장하려면 단일 페이지로 이동합니다.이는 청구서, 보고서 섹션 또는 양식 요약과 같이 한 페이지의 콘텐츠만 필요한 경우에 유용합니다.

1. 를 사용하여 PDF 문서 열기 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. 만들기 `TextAbsorber` 예.
1. 전화 `accept` 대상 페이지에서: `document.pages[page_number].accept(text_absorber)`.
1. 추출한 텍스트를 검색하여 파일에 씁니다.

```python
import os
import aspose.pdf as ap


def extract_text_from_page(infile, outfile, page_number):
    """
    Extract text from a specific page number of the PDF.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
        page_number (int): 1-based page index to extract.
    """
    document = ap.Document(infile)
    text_absorber = ap.text.TextAbsorber()
    # Accept the absorber on only the specified page
    document.pages[page_number].accept(text_absorber)
    extracted_text = text_absorber.text
    with open(outfile, "w", encoding="utf-8") as tw:
        tw.write(extracted_text)
```

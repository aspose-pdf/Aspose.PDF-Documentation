---
title: Python을 사용한 기본 텍스트 추출
linktitle: 기본 텍스트 추출
type: docs
weight: 10
url: /ko/python-net/basic-text-extraction/
description: 이 섹션에는 Python에서 Aspose.PDF를 사용하여 PDF 문서에서 기본 텍스트를 추출하는 기사들이 포함되어 있습니다.
lastmod: "2025-11-05"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## PDF 문서 전체 페이지에서 텍스트 추출

Python용 Aspose.PDF는 PDF 문서의 모든 페이지에서 텍스트를 추출하는 방법을 알려줍니다. TextAbsorber 클래스를 사용하여 전체 문서의 모든 텍스트 내용을 캡처하고 별도의 텍스트 파일에 저장합니다.
PDF를 검색 가능한 텍스트로 변환하거나, 콘텐츠 분석을 수행하거나, 인덱싱 및 처리 작업을 위해 텍스트를 내보내기에 이상적입니다.

1. PDF 파일을 로드합니다.
1. 'TextAbsorber' 객체를 생성합니다.
1. 'document.pages.accept(text_absorber)'를 호출하여 모든 페이지를 스캔합니다.
1. 'text_absorber.text'를 통해 전체 텍스트를 가져옵니다.
1. 결과를 텍스트 파일에 기록합니다.

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
    try:
        # Create a TextAbsorber to extract text
        text_absorber = ap.text.TextAbsorber()
        # Accept the absorber for all pages
        document.pages.accept(text_absorber)
        # Get extracted text
        extracted_text = text_absorber.text
        # Write the text to an output file
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        document.close()
```

## 특정 페이지에서 텍스트 추출

PDF 문서의 단일 페이지에서 텍스트를 추출합니다. 지정된 페이지에만 TextAbsorber를 적용함으로써 다중 페이지 PDF의 특정 섹션에서 텍스트를 분리하고 저장할 수 있습니다.

한 페이지의 내용만 필요할 때 유용합니다 — 예를 들어, 청구서 페이지, 보고서 섹션, 혹은 양식 필드 요약에서 텍스트를 추출하는 경우입니다.

1. PDF를 엽니다.
1. TextAbsorber를 생성합니다.
1. 지정된 페이지만 수락합니다 (pages[page_number]).
1. 텍스트를 추출하고 파일에 기록합니다.

```python

import os
import aspose.pdf as ap

def extract_text_from_page(infile, page_number, outfile):
    """
    Extract text from a specific page number of the PDF.
    Args:
        infile (str): Path to input PDF file.
        page_number (int): 1-based page index to extract.
        outfile (str): Path to output text file.
    """
    document = ap.Document(infile)
    try:
        text_absorber = ap.text.TextAbsorber()
        # Accept the absorber on only the specified page
        document.pages[page_number].accept(text_absorber)
        extracted_text = text_absorber.text
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        document.close()
```


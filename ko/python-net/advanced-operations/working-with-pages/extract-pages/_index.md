---
title: Python을 사용한 페이지 추출
linktitle: PDF 페이지 추출
type: docs
weight: 80
url: /ko/python-net/extract-pages/
description: Aspose.PDF for Python via .NET 라이브러리를 사용하여 PDF 파일에서 페이지를 추출할 수 있습니다.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 페이지를 추출하는 방법
Abstract: 이 문서는 Aspose.PDF Python 라이브러리를 사용하여 PDF 문서에서 페이지를 추출하는 방법을 보여줍니다. 이 기술은 단일 페이지 추출과 다중 페이지 추출을 모두 다루며, 개발자가 선택된 페이지만 포함된 새로운 PDF 파일을 생성할 수 있게 합니다. 예제에서는 1부터 시작하는 인덱싱으로 특정 페이지에 접근하고, 이를 새 PDF 문서에 복사한 뒤 원본 문서는 그대로 두고 결과를 저장하는 방법을 설명합니다. 이러한 방법은 큰 문서를 분할하거나, 선택된 섹션을 공유하거나, 배포 또는 분석을 위한 맞춤형 PDF 하위 집합을 만드는 데 유용합니다.
---

## PDF에서 단일 페이지 추출

PDF 문서에서 특정 페이지를 추출하여 새 파일로 저장합니다. Aspose.PDF 라이브러리를 사용하여 스크립트가 원하는 페이지를 새 PDF에 복사하고 원본 문서는 변경되지 않은 상태로 남깁니다. 이는 PDF를 분할하거나 배포를 위해 중요한 페이지를 분리하는 데 유용합니다.

1. 소스 PDF를 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) API (`ap.Document()`)를 사용하여 로드합니다.
1. 추출된 페이지를 담을 새로운 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)를 생성합니다.
1. 소스 문서에서 원하는 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)를 대상 문서의 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (`dst_document.pages.add(...)`)을 사용하여 새 PDF에 추가합니다.
- 이 예제에서는 페이지 2가 추출됩니다 (1부터 시작하는 인덱싱).
1. 추출된 페이지가 포함된 새로운 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)을 지정된 출력 파일에 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def extract_page(input_file_name, output_file_name):
    """
    Extract a single page from a PDF document.

    Demonstrates how to extract a specific page from a PDF document using
    the Aspose.PDF library. This function extracts page 2 from the input
    document and saves it as a new file containing only that page.

    Args:
        input_file_name (str): Path to the input PDF file from which to extract a page.
        output_file_name (str): Path where the extracted page will be saved.

    Returns:
        None: The function creates a new PDF containing the extracted page and saves it to the output path.

    Note:
        - Extracts page 2 (1-based indexing) from the document
        - Page numbering is 1-based (page 2 is the second page)
        - The original document is not modified; a new file is created
        - If the document has fewer than 2 pages, this may raise an error

    Example:
        >>> extract_page("input.pdf", "output.pdf")
        # Extracts page 2 from input.pdf and saves result as output.pdf
    """
    # Open source PDF as Document
    src_document = ap.Document(input_file_name)
    # Create destination Document to hold extracted pages
    dst_document = ap.Document()
    # Add a Page from source to destination using PageCollection API
    dst_document.pages.add(src_document.pages[2])
    # Save destination Document
    dst_document.save(output_file_name)
```

## PDF에서 여러 페이지 추출

PDF 문서에서 여러 특정 페이지를 추출하여 새 파일에 저장합니다. Aspose.PDF 라이브러리를 사용하여 선택된 페이지를 새 PDF에 복사하면서 원본 문서는 그대로 유지됩니다. 이는 큰 문서에서 관련 섹션만 포함한 작은 PDF를 만드는 데 유용합니다.

1. 소스 PDF를 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) API (`ap.Document()`)를 사용하여 로드합니다.
1. 추출된 페이지를 담을 새로운 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)를 생성합니다.
1. 추출할 페이지를 선택합니다 (이 예제에서는 1부터 시작하는 인덱싱으로 페이지 2와 3).
1. 소스 문서에서 선택된 각 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)를 새로운 PDF의 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)을 사용하여 추가합니다.
1. 추출된 페이지가 포함된 새로운 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)을 지정된 출력 파일에 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def extract_bunch_pages(input_file_name, output_file_name):
    """
    Extract specific pages from a PDF document and save them to a new file.

    This function reads a PDF document, extracts pages 2 and 3 (1-indexed),
    and saves them to a new PDF file.

    Args:
        input_file_name (str): Path to the input PDF file to extract pages from.
        output_file_name (str): Path where the new PDF file with extracted pages will be saved.

    Returns:
        None

    Note:
        The function specifically extracts pages 2 and 3 from the source document.
        Page indexing appears to be 1-based in this implementation.
    """
    # Open source Document
    document = ap.Document(input_file_name)
    pages = [2,3]
    # Create destination Document
    another_document = ap.Document()
    # Copy selected Page objects via PageCollection API
    for page_index in pages:
        another_document.pages.add(document.pages[page_index])
    # Save destination Document
    another_document.save(output_file_name)
```

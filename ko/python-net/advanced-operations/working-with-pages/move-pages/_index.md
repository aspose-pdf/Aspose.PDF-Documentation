---
title: Python을 이용한 프로그래밍 방식 PDF 페이지 이동
linktitle: PDF 페이지 이동
type: docs
weight: 100
url: /ko/python-net/move-pages/
description: Aspose.PDF for Python via .NET를 사용하여 PDF 파일의 원하는 위치 또는 끝으로 페이지를 이동해 보세요.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용한 PDF 문서 간 페이지 이동
Abstract: 이 문서는 Python을 사용하여 PDF 문서 간 또는 단일 PDF 문서 내에서 페이지를 이동하는 포괄적인 가이드를 제공합니다. 특히 Aspose.PDF 라이브러리를 활용합니다. 세 가지 시나리오에 대한 단계별 프로세스를 설명합니다—하나의 PDF에서 다른 PDF로 단일 페이지 이동, 여러 페이지 전송, 동일 문서 내에서 페이지 재배치. 각 시나리오에서는 원본 및 대상 PDF에 대한 `Document` 클래스 객체를 생성하고, `PageCollection` 클래스를 통해 페이지를 조작하며, 원하는 페이지 재구성을 위해 `add`, `delete`, `save` 메서드를 활용합니다. 실용적인 구현을 위해 코드 스니펫이 제공되어 Python 스크립트를 사용한 효율적인 페이지 이동 방법을 보여줍니다.
---

## 하나의 PDF 문서에서 다른 PDF 문서로 페이지 이동

Aspose.PDF for Python을 사용하면 페이지를 (복사만 하는 것이 아니라) 한 PDF에서 다른 PDF로 이동할 수 있습니다. 선택한 페이지를 원본 문서에서 제거한 다음 새 PDF 파일에 추가합니다.

한 책에서 페이지를 잘라내어 다른 책에 붙이는 것과 같습니다 — 이동 후 원본 파일에는 페이지가 더 이상 존재하지 않습니다.

1. [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스를 사용하여 소스 PDF 문서를 엽니다.
1. 이동할 특정 페이지를 선택합니다 (이 경우 페이지 2) — 이는 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)를 의미합니다.
1. 새로운 PDF 문서를 생성합니다 (다른 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)를 인스턴스화).
1. 대상 문서의 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)를 사용하여 선택한 페이지를 새 PDF 문서에 추가합니다 (예: `another_document.pages.add(page)`).
1. 원본 문서의 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)를 통해 페이지를 삭제합니다 (예: `document.pages.delete(index)`).
1. 두 문서를 모두 저장합니다.

다음 코드 스니펫은 페이지 하나를 이동하는 방법을 보여줍니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def moving_page_from_one_document_to_another(input_file_name, output_file_name):
    """
    Move a single page from one PDF document to another.

    Parameters:
    - input_file_name (str): Path to the source PDF file.
    - output_file_name (str): Path to the destination PDF file after moving the page.
    """
    document = ap.Document(input_file_name)
    page = document.pages[2]
    another_document = ap.Document()
    another_document.pages.add(page)
    document.pages.delete(2)
    document.save(input_file_name.replace(".pdf","_new.pdf"))
    another_document.save(output_file_name)
```

## 하나의 PDF 문서에서 다른 PDF 문서로 여러 페이지 이동

복사와 달리, 이 작업은 선택된 페이지들을 전송합니다 — 원본 파일에서 제거하고 새 PDF에 저장합니다.

1. 새롭고 빈 대상 문서를 생성합니다 (`Document`).
1. 소스 문서의 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)에서 여러 페이지를 선택합니다 (이 경우 페이지 1과 3).
1. 선택된 페이지들을 순회하며 각 페이지를 대상 문서의 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)에 추가합니다.
1. 이동된 페이지를 포함한 대상 문서를 저장합니다.
1. 소스 문서의 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)를 사용하여 이동된 페이지를 삭제합니다.
1. 두 버전을 보존하기 위해 새 파일 이름으로 수정된 소스 문서를 저장합니다.

다음 코드 스니펫은 PDF 파일 끝에 빈 페이지를 삽입하는 방법을 보여줍니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def moving_bunch_pages_from_one_document_to_another(input_file_name, output_file_name):
    """
    Move a set of pages from one PDF document to another.

    Parameters:
    - input_file_name (str): Path to the source PDF file.
    - output_file_name (str): Path to the destination PDF file where selected pages will be saved.
    """
    src_document = ap.Document(input_file_name)
    dst_document = ap.Document()
    pages = [1, 3]
    for page_index in pages:
        page = src_document.pages[page_index]
        dst_document.pages.add(page)
    # Save output files
    dst_document.save(output_file_name)
    src_document.pages.delete(pages)
    src_document.save(input_file_name.replace(".pdf","_new.pdf"))
```

## 현재 PDF 문서에서 페이지를 새로운 위치로 이동

같은 문서 내에서 특정 페이지를 다른 위치로 이동하는 방법을 보여줍니다 — PDF 레이아웃을 재구성하거나 편집할 때 흔히 필요한 작업입니다.

1. [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스를 사용하여 입력 PDF 문서를 로드합니다.
1. 이동하려는 페이지를 선택합니다 (페이지 2) — 이는 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)입니다.
1. 문서의 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)을 사용하여 문서 끝에 추가합니다.
1. [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)를 통해 원래 위치에서 페이지를 삭제합니다.
1. 수정된 문서를 새 파일로 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def moving_page_in_new_location_in_same_document(input_file_name, output_file_name):
    """
    Move a page to a new location within the same PDF document.

    Parameters:
    - input_file_name (str): Path to the source PDF file.
    - output_file_name (str): Path to the destination PDF file after moving the page.
    """
    srcDocument = ap.Document(input_file_name)

    page = srcDocument.pages[2]
    srcDocument.pages.add(page)
    srcDocument.pages.delete(2)

    # Save output file
    srcDocument.save(output_file_name)
```



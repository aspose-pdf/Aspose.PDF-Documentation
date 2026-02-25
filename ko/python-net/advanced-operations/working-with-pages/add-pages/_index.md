---
title: Python으로 PDF에 페이지 추가
linktitle: 페이지 추가
type: docs
weight: 10
url: /ko/python-net/add-pages/
description: Aspose.PDF를 사용하여 유연한 문서 생성 및 편집이 가능한 Python으로 PDF 문서에 페이지를 추가하는 방법을 알아보세요.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에 페이지 추가하는 방법
Abstract: 이 문서는 Aspose.PDF for Python via .NET API를 사용하여 PDF 문서의 페이지를 조작하는 방법을 안내합니다. 특히 PDF 내 모든 페이지를 관리하는 `PageCollection` 클래스를 통해 제공되는 유연성을 강조합니다. 문서에서는 PDF 파일의 특정 위치에 페이지를 추가하거나 삽입하는 절차를 상세히 설명합니다. 주요 작업 두 가지인 원하는 위치에 빈 페이지를 삽입하는 경우와 문서 끝에 빈 페이지를 추가하는 경우를 제시합니다. 두 작업 모두 `Document` 객체를 생성하고 `PageCollection`의 `insert` 또는 `add` 메서드를 사용한 뒤 수정된 문서를 저장하는 과정을 포함합니다. 이 문서에는 이러한 작업을 보여주는 코드 스니펫이 포함되어 있어 Python과 이 API를 사용하여 PDF 문서를 조작하는 것이 얼마나 간단한지 보여줍니다.
---

Aspose.PDF for Python via .NET API는 Python을 사용하여 PDF 문서의 페이지를 작업할 수 있는 완전한 유연성을 제공합니다. PDF 문서의 모든 페이지는 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)에 보관되며, 이를 통해 PDF 페이지를 작업할 수 있습니다.
Aspose.PDF for Python via .NET를 사용하면 파일 내任意 위치에 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)에 페이지를 삽입하고 PDF 파일의 끝에 페이지를 추가할 수 있습니다. 이 섹션에서는 Python을 사용하여 PDF에 페이지를 추가하는 방법을 보여줍니다.

## PDF 파일에 페이지 추가 또는 삽입

Aspose.PDF for Python via .NET를 사용하면 파일 내任意 위치에 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)에 페이지를 삽입하고 PDF 파일의 끝에 페이지를 추가할 수 있습니다.

### PDF 파일에 빈 페이지 삽입

PDF 파일에 빈 페이지를 삽입하려면:

1. 적절한 메서드를 사용하여 기존 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)을 엽니다.
1. [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)의 `insert()` 메서드를 사용하여 특정 인덱스에 새 빈 페이지를 삽입합니다.
1. 수정된 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)를 원하는 출력 경로에 저장합니다.

지정된 위치에 기존 PDF 파일에 빈 페이지를 삽입합니다:

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def insert_empty_page(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    document.pages.insert(2)
    document.save(output_file_name)
```

### PDF 파일 끝에 빈 페이지 추가

때때로 문서가 빈 페이지로 끝나도록 하고 싶을 수 있습니다. 이 항목에서는 PDF 문서 끝에 빈 페이지를 삽입하는 방법을 설명합니다.

PDF 파일 끝에 빈 페이지를 삽입하려면:

1. 적절한 메서드를 사용하여 기존 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)을 엽니다.
1. [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)의 `add()` 메서드를 사용하여 문서 끝에 새 빈 페이지를 추가합니다.
1. 업데이트된 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)을 저장합니다.

다음 코드 스니펫은 PDF 파일 끝에 빈 페이지를 삽입하는 방법을 보여줍니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_empty_page_to_end(input_file_name, output_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Insert an empty page at the end of a PDF file
    document.pages.add()

    # Save output file
    document.save(output_file_name)
```

### 다른 PDF 문서에서 페이지 추가

Aspose.PDF for Python 라이브러리를 사용하면 새 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)를 만들고 초기 페이지를 추가한 뒤, 다른 PDF에서 페이지를 가져와 삽입할 수 있습니다.

1. 새 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)를 생성합니다.
1. 새 빈 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)를 추가하고 [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/)를 사용하여 텍스트를 씁니다.
1. 다른 기존 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)를 엽니다.
1. 해당 문서에서 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)를 복사합니다.
1. 복사한 페이지를 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)를 사용하여 메인 문서에 붙여넣습니다.
1. 결합된 파일을 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_page_from_another_document(input_file_name, output_file_name):
    # Open document
    document = ap.Document()
    page = document.pages.add()
    text_fragment = ap.text.TextFragment("This is first page!")
    page.paragraphs.add(text_fragment)

    another_document = ap.Document(input_file_name)
    document.pages.add(another_document.pages[1])

    # Save output file
    document.save(output_file_name)
```

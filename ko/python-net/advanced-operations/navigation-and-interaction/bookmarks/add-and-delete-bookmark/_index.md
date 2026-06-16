---
title: 파이썬에서 PDF 북마크 추가 및 삭제
linktitle: 북마크 추가 및 삭제
type: docs
weight: 10
url: /ko/python-net/add-and-delete-bookmark/
description: Python을 사용하여 PDF 문서에서 북마크를 추가하고 삭제하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 북마크를 추가하고 제거하는 방법
Abstract: 이 문서에서는 Python용 Aspose.PDF 라이브러리를 사용하여 PDF 문서의 북마크를 관리하는 방법에 대한 포괄적인 지침을 제공합니다.이 문서에서는 PDF 내에서 북마크를 추가, 수정 및 삭제하는 프로세스를 간략하게 설명합니다.이 글은 먼저 `OutlineItemCollection` 개체를 만들어 문서의 `OutlineCollection`에 추가하여 북마크를 추가하는 방법을 안내하는 것으로 시작합니다.여기에는 상위 북마크와 하위 북마크의 생성 및 추가를 보여 주는 코드 예제가 포함되어 있으며, 계층적 관계를 강조 표시합니다.또한 이 문서에서는 제목별로 모든 북마크 또는 특정 북마크를 삭제하는 방법을 설명합니다.각 섹션에는 작업을 설명하는 Python 코드 스니펫이 포함되어 있어 독자가 PDF 조작 작업에서 설명된 기능을 쉽게 구현할 수 있습니다.
---

## PDF 문서에 책갈피 추가

북마크는 문서 객체에 보관됩니다. [아웃라인 항목 컬렉션](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) 컬렉션 그 자체 [아웃라인 컬렉션](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 컬렉션.

PDF에 북마크를 추가하려면:

1. 를 사용하여 PDF 문서 열기 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 목적.
1. 북마크를 만들고 해당 속성을 정의합니다.
1. 추가 [아웃라인 항목 컬렉션](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) 컬렉션을 아웃라인 컬렉션으로 이동합니다.

다음 코드 스니펫은 PDF 문서에 북마크를 추가하는 방법을 보여줍니다.

```python
import aspose.pdf as ap
import sys
from os import path

def add_bookmark(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Create a bookmark object
    pdf_outline = ap.OutlineItemCollection(document.outlines)
    pdf_outline.title = "Test Outline"
    pdf_outline.italic = True
    pdf_outline.bold = True

    # Set the destination page number
    pdf_outline.action = ap.annotations.GoToAction(document.pages[1])

    # Add bookmark to the document's outline collection
    outlines = document.outlines
    outlines.append(pdf_outline)

    # Save PDF document
    document.save(outfile)
```

## PDF 문서에 하위 북마크 추가

북마크는 중첩될 수 있으며, 이는 부모 및 하위 북마크와의 계층 관계를 나타냅니다.이 문서에서는 PDF에 하위 북마크, 즉 두 번째 수준의 북마크를 추가하는 방법을 설명합니다.

PDF 파일에 하위 북마크를 추가하려면 먼저 상위 북마크를 추가합니다.

1. 문서를 엽니다.
1. 에 북마크 추가 [아웃라인 항목 컬렉션](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/), 속성을 정의합니다.
1. 아웃라인 항목 컬렉션을 문서 객체에 추가합니다. [아웃라인 컬렉션](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 컬렉션.

하위 북마크는 위에서 설명한 부모 북마크와 마찬가지로 생성되지만 부모 북마크의 Outlines 컬렉션에 추가됩니다.

다음 코드 스니펫은 PDF 문서에 하위 북마크를 추가하는 방법을 보여줍니다.

```python
import aspose.pdf as ap
import sys
from os import path

def add_child_bookmark(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Create a parent bookmark object
    pdf_outline = ap.OutlineItemCollection(document.outlines)
    pdf_outline.title = "Parent Outline"
    pdf_outline.italic = True
    pdf_outline.bold = True

    # Create a child bookmark object
    pdf_child_outline = ap.OutlineItemCollection(document.outlines)
    pdf_child_outline.title = "Child Outline"
    pdf_child_outline.italic = True
    pdf_child_outline.bold = True

    # Add child bookmark to parent bookmark's collection
    pdf_outline.append(pdf_child_outline)

    # Add parent bookmark to the document's outline collection
    document.outlines.append(pdf_outline)

    # Save PDF document
    document.save(outfile)
```

## PDF 문서에서 모든 책갈피 삭제

PDF의 모든 북마크는 에 보관됩니다. [아웃라인 컬렉션](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 컬렉션.이 문서에서는 PDF 파일에서 모든 북마크를 삭제하는 방법을 설명합니다.

PDF 파일에서 모든 북마크를 삭제하려면:

1. 전화해 [아웃라인 컬렉션](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 컬렉션의 삭제 메서드
1. 를 사용하여 수정된 파일을 저장합니다. [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 사물의 [저장 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 방법.

다음 코드 스니펫은 PDF 문서에서 모든 북마크를 삭제하는 방법을 보여줍니다.

```python
import aspose.pdf as ap
import sys
from os import path

def delete_bookmarks(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Delete all bookmarks in the PDF document
    document.outlines.delete()

    # Save PDF document
    document.save(outfile)
```

## PDF 문서에서 특정 북마크 삭제

PDF 파일에서 특정 북마크를 삭제하려면:

1. 북마크 제목을 매개 변수로 전달하십시오. [아웃라인 컬렉션](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 컬렉션의 삭제 메서드
1. 그런 다음 Document 객체 Save 메서드를 사용하여 업데이트된 파일을 저장합니다.

더 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스'는 다음을 제공합니다. [아웃라인 컬렉션](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 컬렉션.더 [삭제 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/#methods) 메서드는 제목이 메서드에 전달된 모든 북마크를 제거합니다.

다음 코드 스니펫은 PDF 문서에서 특정 북마크를 삭제하는 방법을 보여줍니다.

```python
import aspose.pdf as ap
import sys
from os import path

def delete_bookmark(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Delete a specific bookmark by title.
    # Note: If multiple bookmarks have the same title, only the first matching bookmark will be deleted.
    document.outlines.delete("Child Outline")

    # Save PDF document
    document.save(outfile)
```

## 관련 북마크 주제

- [파이썬에서 PDF 북마크로 작업하기](/pdf/ko/python-net/bookmarks/)
- [Python에서 PDF 북마크를 가져오고, 업데이트하고, 확장하세요](/pdf/ko/python-net/get-update-and-expand-bookmark/)
- [Python을 사용한 PDF 탐색 및 상호 작용](/pdf/ko/python-net/navigation-and-interaction/)


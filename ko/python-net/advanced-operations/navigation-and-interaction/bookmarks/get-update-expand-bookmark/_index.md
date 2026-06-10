---
title: Python에서 PDF 북마크 가져오기, 업데이트 및 확장하기
linktitle: 북마크 가져오기, 업데이트 및 확장
type: docs
weight: 20
url: /ko/python-net/get-update-and-expand-bookmark/
description: Python을 사용하여 PDF 문서에서 북마크를 검색, 업데이트 및 확장하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python으로 PDF에서 북마크를 사용하는 방법
Abstract: 이 문서에서는 Python의 Aspose.PDF 라이브러리를 사용하여 PDF 문서 내에서 북마크를 관리하는 방법에 대한 포괄적인 가이드를 제공합니다.먼저 모든 북마크를 포함하는 'OutlineCollection'을 통해 PDF 파일에서 북마크를 검색하는 방법과 'OutlineItemCollection'을 통해 북마크 속성에 액세스하는 세부 정보를 설명합니다.그런 다음 이 문서에서는 `PDFBookmarkEditor'를 사용하여 북마크와 관련된 페이지 번호를 결정하는 과정을 설명합니다.또한 각 `OutlineItemCollection` 내에서 하위 북마크를 검색하여 계층적 북마크 구조를 처리하는 방법을 설명합니다.또한 북마크 속성 업데이트, 북마크 속성 수정 및 변경 내용을 PDF에 저장하는 방법을 설명합니다.마지막으로 이 문서에서는 문서를 볼 때 북마크를 확장해야 하는 요구 사항을 다루며, 기본적으로 북마크가 확장되도록 각 북마크의 열린 상태를 설정하는 방법을 보여줍니다.각 섹션에는 코드 스니펫이 함께 제공되어 이러한 기능을 구현하는 실제 사례를 제공합니다.
---

## 북마크 가져오기

더 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 사물의 [아웃라인 컬렉션](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 컬렉션에는 모든 PDF 파일의 북마크가 포함됩니다.이 문서에서는 PDF 파일에서 북마크를 가져오는 방법과 특정 북마크가 있는 페이지를 가져오는 방법을 설명합니다.

북마크를 가져오려면 다음을 반복하세요. [아웃라인 컬렉션](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 컬렉션을 선택하고 아웃라인 항목 컬렉션의 각 북마크를 가져옵니다. [아웃라인 항목 컬렉션](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) 북마크의 모든 속성에 대한 액세스를 제공합니다.다음 코드 스니펫은 PDF 파일에서 북마크를 가져오는 방법을 보여줍니다.

```python
from os import path
import sys
import aspose.pdf as ap

def get_bookmarks(input_pdf):
    document = ap.Document(input_pdf)
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
```

## 북마크의 페이지 번호 가져오기

북마크를 추가한 후에는 북마크 객체와 관련된 대상 페이지 번호를 가져와서 북마크가 어떤 페이지에 있는지 확인할 수 있습니다.

```python
from os import path
import sys
import aspose.pdf as ap

def get_bookmark_page_number(input_pdf):
    # Create PdfBookmarkEditor
    bookmark_editor = ap.facades.PdfBookmarkEditor()
    # Open PDF file
    bookmark_editor.bind_pdf(input_pdf)
    # Extract bookmarks
    bookmarks = bookmark_editor.extract_bookmarks()
    for bookmark in bookmarks:
        str_level_separator = ""
        for i in range(bookmark.level):
            str_level_separator += "----"

        print(str_level_separator, "Title:", bookmark.title)
        print(str_level_separator, "Page Number:", bookmark.page_number)
        print(str_level_separator, "Page Action:", bookmark.action)
```

## PDF 문서에서 하위 북마크 가져오기

북마크는 부모 및 자녀와 함께 계층 구조로 구성할 수 있습니다.모든 북마크를 가져오려면 Document 객체의 Outlines 컬렉션을 반복해서 살펴보세요.하지만 하위 북마크도 가져오려면 각 북마크의 모든 북마크를 반복해서 살펴보세요. [아웃라인 항목 컬렉션](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) 첫 번째 루프에서 얻은 객체.다음 코드 스니펫은 PDF 문서에서 하위 북마크를 가져오는 방법을 보여줍니다.

```python
from os import path
import sys
import aspose.pdf as ap

def get_child_bookmarks(input_pdf):
    document = ap.Document(input_pdf)
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
        count = len(outline_item)
        if count > 0:
            print("Child Bookmarks")
            # There are child bookmarks then loop through that as well
            for j in range(len(outline_item)):
                child_outline_item = outline_item[j + 1]
                print(child_outline_item.title)
                print(child_outline_item.italic)
                print(child_outline_item.bold)
                print(child_outline_item.color)
```

## PDF 문서의 북마크 업데이트

PDF 파일에서 북마크를 업데이트하려면 먼저 북마크의 색인을 지정하여 문서 객체의 OutlineColletion 컬렉션에서 특정 북마크를 가져옵니다.북마크를 다음 위치로 가져오면 [아웃라인 항목 컬렉션](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) 객체의 속성을 업데이트한 다음 Save 메서드를 사용하여 업데이트된 PDF 파일을 저장할 수 있습니다.다음 코드 스니펫은 PDF 문서의 북마크를 업데이트하는 방법을 보여줍니다.

```python
from os import path
import sys
import aspose.pdf as ap

def update_bookmarks(input_pdf, output_pdf):
    # Open document
    document = ap.Document(input_pdf)

    # Get a bookmark object
    outline = document.outlines[1]

    # Get child bookmark object
    child_outline = outline[1]
    child_outline.title = "Updated Outline"
    child_outline.italic = True
    child_outline.bold = True

    # Save output
    document.save(output_pdf)
```

## 문서를 볼 때 확장된 북마크

북마크는 문서 객체에 보관됩니다. [아웃라인 항목 컬렉션](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) 컬렉션 그 자체 [아웃라인 컬렉션](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 컬렉션.그러나 PDF 파일을 볼 때 모든 북마크를 확장해야 할 수도 있습니다.

이 요구 사항을 충족하기 위해 각 아웃라인/북마크 항목의 열기 상태를 [열림] 으로 설정할 수 있습니다.다음 코드 스니펫은 PDF 문서에서 각 북마크의 열림 상태를 확장된 상태로 설정하는 방법을 보여줍니다.

```python
from os import path
import sys
import aspose.pdf as ap

def expanded_bookmarks(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.page_mode = ap.PageMode.USE_OUTLINES
    for i in range(len(document.outlines)):
        item = document.outlines[i + 1]
        item.open = True
    document.save(output_pdf)
```

## 관련 북마크 주제

- [파이썬에서 PDF 북마크로 작업하기](/pdf/ko/python-net/bookmarks/)
- [Python에서 PDF 북마크 추가 및 삭제](/pdf/ko/python-net/add-and-delete-bookmark/)
- [Python을 사용한 PDF 탐색 및 상호 작용](/pdf/ko/python-net/navigation-and-interaction/)


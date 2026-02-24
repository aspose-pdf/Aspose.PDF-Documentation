---
title: Python을 사용하여 즐겨찾기 추가 및 삭제
linktitle: 즐겨찾기 추가 및 삭제
type: docs
weight: 10
url: /ko/python-net/add-and-delete-bookmark/
description: Python을 사용하여 PDF 문서에 즐겨찾기를 추가할 수 있습니다. PDF 문서에서 모든 즐겨찾기 또는 특정 즐겨찾기를 삭제할 수도 있습니다.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 즐겨찾기 추가 및 제거하는 방법
Abstract: 이 문서는 Aspose.PDF 파이썬 라이브러리를 사용하여 PDF 문서에서 즐겨찾기를 관리하는 포괄적인 지침을 제공합니다. PDF 내에서 즐겨찾기를 추가, 수정 및 삭제하는 프로세스를 개요합니다. 문서는 `OutlineItemCollection` 객체를 생성하고 이를 문서의 `OutlineCollection`에 추가하여 즐겨찾기를 추가하는 방법에 대한 안내로 시작합니다. 부모 및 자식 즐겨찾기의 생성과 추가를 보여주는 코드 예제가 포함되어 있어 계층 관계를 강조합니다. 또한, 모든 즐겨찾기 또는 제목으로 특정 즐겨찾기를 삭제하는 방법도 다룹니다. 각 섹션에는 파이썬 코드 스니펫이 포함되어 있어 독자가 PDF 조작 작업에서 설명된 기능을 쉽게 구현할 수 있도록 합니다.
---

## PDF 문서에 즐겨찾기 추가

즐겨찾기는 Document 객체의 [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) 컬렉션에 저장되며, 이 컬렉션은 다시 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 컬렉션에 포함됩니다.

PDF에 즐겨찾기를 추가하려면:

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체를 사용하여 PDF 문서를 엽니다.
1. 즐겨찾기를 만들고 해당 속성을 정의합니다.
1. [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) 컬렉션을 Outlines 컬렉션에 추가합니다.

다음 코드 스니펫은 PDF 문서에 즐겨찾기를 추가하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Create a bookmark object
    outline = ap.OutlineItemCollection(document.outlines)
    outline.title = "Test Bookmark"
    outline.italic = True
    outline.bold = True
    # Set the destination page number
    outline.action = ap.annotations.GoToAction(document.pages[1])
    # Add bookmark in the document's outline collection.
    document.outlines.append(outline)

    # Save output
    document.save(output_pdf)
```

## PDF 문서에 자식 즐겨찾기 추가

즐겨찾기는 중첩될 수 있으며, 부모와 자식 즐겨찾기 간의 계층 관계를 나타냅니다. 이 문서는 PDF에 자식 즐겨찾기, 즉 2단계 즐겨찾기를 추가하는 방법을 설명합니다.

PDF 파일에 자식 즐겨찾기를 추가하려면 먼저 부모 즐겨찾기를 추가합니다:

1. 문서를 엽니다.
1. [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/)에 즐겨찾기를 추가하고 속성을 정의합니다.
1. OutlineItemCollection을 Document 객체의 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 컬렉션에 추가합니다.

자식 즐겨찾기는 위에서 설명한 부모 즐겨찾기와 동일하게 생성되지만, 부모 즐겨찾기의 Outlines 컬렉션에 추가됩니다.

다음 코드 스니펫은 PDF 문서에 자식 즐겨찾기를 추가하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Create a parent bookmark object
    outline = ap.OutlineItemCollection(document.outlines)
    outline.title = "Parent Outline"
    outline.italic = True
    outline.bold = True

    # Create a child bookmark object
    childOutline = ap.OutlineItemCollection(document.outlines)
    childOutline.title = "Child Outline"
    childOutline.italic = True
    childOutline.bold = True

    # Add child bookmark in parent bookmark's collection
    outline.append(childOutline)
    # Add parent bookmark in the document's outline collection.
    document.outlines.append(outline)

    # Save output
    document.save(output_pdf)
```

## PDF 문서에서 모든 즐겨찾기 삭제

PDF의 모든 즐겨찾기는 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 컬렉션에 저장됩니다. 이 문서는 PDF 파일에서 모든 즐겨찾기를 삭제하는 방법을 설명합니다.

PDF 파일에서 모든 즐겨찾기를 삭제하려면:

1. [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 컬렉션의 Delete 메서드를 호출합니다.
1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체의 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 사용하여 수정된 파일을 저장합니다.

다음 코드 스니펫은 PDF 문서에서 모든 즐겨찾기를 삭제하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Delete all bookmarks
    document.outlines.delete()

    # Save updated file
    document.save(output_pdf)

```

## PDF 문서에서 특정 즐겨찾기 삭제

PDF 파일에서 특정 즐겨찾기를 삭제하려면:

1. 즐겨찾기의 제목을 매개변수로 전달하여 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 컬렉션의 Delete 메서드를 호출합니다.
1. 그런 다음 Document 객체의 Save 메서드로 업데이트된 파일을 저장합니다.

 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스는 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 컬렉션을 제공합니다. [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/#methods) 메서드는 메서드에 전달된 제목을 가진 모든 즐겨찾기를 제거합니다.

다음 코드 스니펫은 PDF 문서에서 특정 즐겨찾기를 삭제하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Delete particular outline by Title
    document.outlines.delete("Child Outline")

    # Save updated file
    document.save(output_pdf)
```



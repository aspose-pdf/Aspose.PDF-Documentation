---
title: Python을 사용하여 북마크 가져오기, 업데이트 및 확장
linktitle: 북마크 가져오기, 업데이트 및 확장
type: docs
weight: 20
url: /ko/python-net/get-update-and-expand-bookmark/
description: 이 문서에서는 Aspose.PDF for Python 라이브러리를 사용하여 PDF 파일에서 북마크를 사용하는 방법을 설명합니다.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python으로 PDF에서 북마크를 사용하는 방법
Abstract: 이 문서는 Python에서 Aspose.PDF 라이브러리를 사용하여 PDF 문서 내의 북마크를 관리하는 포괄적인 가이드를 제공합니다. 먼저 모든 북마크를 포함하고 있는 `OutlineCollection`을 통해 PDF 파일에서 북마크를 가져오는 방법을 설명하고, `OutlineItemCollection`을 사용해 북마크 속성에 접근하는 방법을 상세히 다룹니다. 이후 `PdfBookmarkEditor`를 사용하여 북마크와 연결된 페이지 번호를 확인하는 과정을 설명합니다. 또한 각 `OutlineItemCollection` 내에서 자식 북마크를 가져와 계층 구조의 북마크를 처리하는 방법을 설명합니다. 북마크 속성을 업데이트하는 방법도 다루며, 북마크 속성을 수정하고 PDF에 변경 사항을 저장하는 방법을 시연합니다. 마지막으로 문서를 볼 때 북마크를 확장해야 하는 요구 사항을 다루어, 각 북마크의 열림 상태를 설정하여 기본적으로 확장되도록 하는 방법을 보여줍니다. 각 섹션마다 코드 스니펫이 함께 제공되어 이러한 기능을 구현하는 실용적인 예제를 제공합니다.
---

## 북마크 가져오기

[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체의 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 컬렉션에는 PDF 파일의 모든 북마크가 포함되어 있습니다. 이 문서에서는 PDF 파일에서 북마크를 가져오는 방법과 특정 북마크가 위치한 페이지를 확인하는 방법을 설명합니다.

북마크를 가져오려면 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 컬렉션을 순회하면서 OutlineItemCollection에 포함된 각 북마크를 가져옵니다. [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/)는 모든 북마크 속성에 접근할 수 있게 해줍니다. 다음 코드 스니펫은 PDF 파일에서 북마크를 가져오는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Loop through all the bookmarks
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
```

## 북마크 페이지 번호 가져오기

북마크를 추가한 후에는 해당 북마크 객체와 연결된 목적지 PageNumber를 가져와 해당 페이지를 확인할 수 있습니다.

```python

    import aspose.pdf as ap

    # Create PdfBookmarkEditor
    bookmarkEditor = ap.facades.PdfBookmarkEditor()
    # Open PDF file
    bookmarkEditor.bind_pdf(input_pdf)
    # Extract bookmarks
    bookmarks = bookmarkEditor.extract_bookmarks()
    for bookmark in bookmarks:
        str_level_seprator = ""
        for i in range(bookmark.level):
            str_level_seprator += "----"

        print(str_level_seprator, "Title:", bookmark.title)
        print(str_level_seprator, "Page Number:", bookmark.page_number)
        print(str_level_seprator, "Page Action:", bookmark.action)
```

## PDF 문서에서 자식 북마크 가져오기

북마크는 부모와 자식으로 구성된 계층 구조로 조직될 수 있습니다. 모든 북마크를 가져오려면 Document 객체의 Outlines 컬렉션을 순회합니다. 그러나 자식 북마크도 가져오려면 첫 번째 순회에서 얻은 각 [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) 객체 내의 모든 북마크를 추가로 순회해야 합니다. 다음 코드 스니펫은 PDF 문서에서 자식 북마크를 가져오는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Loop through all the bookmarks
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
                child_outline_item = outline_item[i + 1]
                print(child_outline_item.title)
                print(child_outline_item.italic)
                print(child_outline_item.bold)
                print(child_outline_item.color)
```

## PDF 문서에서 북마크 업데이트

PDF 파일에서 북마크를 업데이트하려면 먼저 Document 객체의 OutlineCollection 컬렉션에서 해당 북마크의 인덱스를 지정하여 특정 북마크를 가져옵니다. 가져온 북마크를 [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) 객체에 저장한 후 속성을 업데이트하고 Save 메서드를 사용해 업데이트된 PDF 파일을 저장할 수 있습니다. 다음 코드 스니펫은 PDF 문서에서 북마크를 업데이트하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

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

## 문서 보기 시 확장된 북마크

북마크는 Document 객체의 [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) 컬렉션에 보관되며, 이는 다시 [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) 컬렉션에 포함됩니다. 하지만 PDF 파일을 볼 때 모든 북마크가 확장된 상태로 표시되어야 하는 요구 사항이 있을 수 있습니다.

이 요구 사항을 달성하기 위해 각 outline/북마크 항목의 열림 상태를 Open으로 설정할 수 있습니다. 다음 코드 스니펫은 PDF 문서에서 각 북마크를 확장된 상태로 설정하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Set page view mode i.e. show thumbnails, full-screen, show attachment panel
    document.page_mode = ap.PageMode.USE_OUTLINES
    # Traverse through each Ouline item in outlines collection of PDF file
    for i in range(len(document.outlines)):
        item = document.outlines[i + 1]
        # Set open status for outline item
        item.open = True

    # Save output
    document.save(output_pdf)
```



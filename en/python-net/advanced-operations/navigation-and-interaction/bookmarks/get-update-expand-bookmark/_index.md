---
title: Get, Update and Expand a Bookmark using Python
linktitle: Get, Update and Expand a Bookmark
type: docs
weight: 20
url: /python-net/get-update-and-expand-bookmark/
description: This article describes how to use bookmarks in a PDF file with our Aspose.PDF for Python library.
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to use bookmarks in PDF with Python
Abstract: This article provides a comprehensive guide on managing bookmarks within a PDF document using the Aspose.PDF library in Python. It begins by explaining how to retrieve bookmarks from a PDF file through the `OutlineCollection`, which contains all bookmarks, and details accessing bookmark attributes via the `OutlineItemCollection`. The article then describes the process of determining the page number associated with a bookmark using the `PdfBookmarkEditor`. It further explains how to handle hierarchical bookmark structures by retrieving child bookmarks within each `OutlineItemCollection`. It also covers updating bookmark properties, demonstrating how to modify bookmark attributes and save changes to a PDF. Lastly, the article addresses the requirement of expanding bookmarks when viewing a document, showing how to set the open status of each bookmark to ensure they are expanded by default. Code snippets accompany each section, providing practical examples of implementing these functionalities.
---

## Get Bookmarks

The [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object's [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) collection contains all a PDF file's bookmarks. This article explains how to get bookmarks from a PDF file, and how to get which page a particular bookmark is on.

To get the bookmarks, loop through the [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) collection and get each bookmark in the OutlineItemCollection. The [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) provides access to all the bookmark's attributes. The following code snippet shows you how to get bookmarks from the PDF file.

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

## Getting a Bookmark's Page Number

Once you have added a bookmark you can find out what page it is on by getting the destination PageNumber associated with the Bookmark object.

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

## Get Child Bookmarks from a PDF Document

Bookmarks can be organized in a hierarchical structure, with parents and children. To get all bookmarks, loop through the Document object's Outlines collections. However, to get child bookmarks as well, also loop through all the bookmarks in each [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) object obtained in the first loop. The following code snippets show how to get child bookmarks from a PDF document.

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

## Update Bookmarks in a PDF Document

To update a bookmark in a PDF file, first, get the particular bookmark from the Document object's OutlineColletion collection by specifying the bookmark's index. Once you have retrieved the bookmark into [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) object, you can update its properties and then save the updated PDF file using the Save method. The following code snippets show how to update bookmarks in a PDF document.

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

## Expanded Bookmarks when viewing document

Bookmarks are held in the Document object's [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) collection, itself in the [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) collection. However, we may have a requirement to have all the bookmarks expanded when viewing the PDF file.

In order to accomplish this requirement, we can set open status for each outline/bookmark item as Open. The following code snippet shows you how to set the open status for each bookmark as expanded in a PDF document.

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


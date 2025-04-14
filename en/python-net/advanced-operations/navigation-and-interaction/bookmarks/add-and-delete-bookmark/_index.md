---
title: Add and Delete a Bookmark using Python
linktitle: Add and Delete a Bookmark
type: docs
weight: 10
url: /python-net/add-and-delete-bookmark/
description: You can add a bookmark to a PDF document with Python. It is possible to delete all or particular bookmarks from a PDF document.
lastmod: "2025-02-27"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to add, and remove Bookmarks using Python
Abstract: This article provides comprehensive instructions on managing bookmarks in PDF documents using the Aspose.PDF library for Python. It outlines the processes for adding, modifying, and deleting bookmarks within a PDF. The article begins with a guide on adding a bookmark by creating an `OutlineItemCollection` object and appending it to the document's `OutlineCollection`. It includes code examples demonstrating the creation and addition of both parent and child bookmarks, highlighting a hierarchical relationship. Additionally, the article covers methods for deleting all bookmarks or a specific bookmark by title. Each section includes Python code snippets to illustrate the operations, ensuring readers can easily implement the described functionalities in their PDF manipulation tasks.
---

## Add a Bookmark to a PDF Document

Bookmarks are held in the Document object's [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) collection, itself in the [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) collection.

To add a bookmark to a PDF:

1. Open a PDF document using [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object.
1. Create a bookmark and define its properties.
1. Add the [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) collection to the Outlines collection.

The following code snippet shows you how to add a bookmark in a PDF document.

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

## Add a Child Bookmark to the PDF Document

Bookmarks can be nested, indicating a hierarchical relationship with parent and child bookmarks. This article explains how to add a child bookmark, that is, a second-level bookmark, to a PDF.

To add a child bookmark to a PDF file, first add a parent bookmark:

1. Open a document.
1. Add a bookmark to the [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/), defining its properties.
1. Add the OutlineItemCollection to the Document object's [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) collection.

The child bookmark is created just like the parent bookmark, explained above, but is added to the parent bookmark's Outlines collection

The following code snippets show how to add child bookmark to a PDF document.

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

## Delete all Bookmarks from a PDF Document

All bookmarks in a PDF are held in the [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) collection. This article explains how to delete all bookmarks from a PDF file.

To delete all bookmarks from a PDF file:

1. Call the [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) collection's Delete method.
1. Save the modified file using the [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object's [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method.

The following code snippets show how to delete all bookmarks from a PDF document.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Delete all bookmarks
    document.outlines.delete()

    # Save updated file
    document.save(output_pdf)

```

## Delete a Particular Bookmark from a PDF Document

To delete a particular bookmark from a PDF file:

1. Pass the bookmark's title as parameter to the [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) collection's Delete method.
1. Then save the updated file with the Document object Save method.

The [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class’ provides the [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) collection. The [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/#methods) method removes any bookmark with the title passed to the method.

The following code snippets show how to delete a particular bookmark from the PDF document.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Delete particular outline by Title
    document.outlines.delete("Child Outline")

    # Save updated file
    document.save(output_pdf)
```


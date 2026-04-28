---
title: Add and Delete PDF Bookmarks in Python
linktitle: Add and Delete a Bookmark
type: docs
weight: 10
url: /python-net/add-and-delete-bookmark/
description: Learn how to add and delete bookmarks in PDF documents using Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
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

## Delete all Bookmarks from a PDF Document

All bookmarks in a PDF are held in the [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) collection. This article explains how to delete all bookmarks from a PDF file.

To delete all bookmarks from a PDF file:

1. Call the [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) collection's Delete method.
1. Save the modified file using the [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object's [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method.

The following code snippets show how to delete all bookmarks from a PDF document.

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

## Delete a Particular Bookmark from a PDF Document

To delete a particular bookmark from a PDF file:

1. Pass the bookmark's title as parameter to the [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) collection's Delete method.
1. Then save the updated file with the Document object Save method.

The [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class’ provides the [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) collection. The [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/#methods) method removes any bookmark with the title passed to the method.

The following code snippets show how to delete a particular bookmark from the PDF document.

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

## Related Bookmark Topics

- [Work with PDF bookmarks in Python](/pdf/python-net/bookmarks/)
- [Get, update, and expand PDF bookmarks in Python](/pdf/python-net/get-update-and-expand-bookmark/)
- [Navigation and interaction in PDF using Python](/pdf/python-net/navigation-and-interaction/)


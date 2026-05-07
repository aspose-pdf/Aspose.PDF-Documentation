---
title: Work with Vector Graphics in Python
linktitle: Working with Vector Graphics
type: docs
weight: 100
url: /python-net/working-with-vector-graphics/
description: Learn how to extract, move, remove, and copy vector graphics between PDF pages using GraphicsAbsorber in Python.
lastmod: "2026-05-07"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Use GraphicsAbsorber to inspect and manipulate PDF vector graphics in Python
Abstract: This article explains how to work with vector graphics in Aspose.PDF for Python via .NET using the GraphicsAbsorber class. Learn how to extract vector elements from PDF pages, move or remove them, and copy graphics between pages with low-level control in Python workflows.
---

[Aspose.PDF for Python via .NET](/pdf/python-net/) provides the [GraphicsAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/) class for accessing and manipulating vector graphics already present in a PDF page. Call its `visit` method on any page to extract paths, shapes, and other graphical operators, then move, remove, or copy those elements as needed.

Use this page when you need to inspect or modify vector drawing elements embedded in an existing PDF, rather than drawing new shapes from scratch.

## Extracting Graphics

Extraction is the starting point for all vector graphics tasks. `GraphicsAbsorber` reads the content stream of a page and exposes each graphic element with its page reference, position, and raw operators.

1. Open the PDF document.
1. Create a [GraphicsAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/) instance.
1. Call `visit` on the target page to populate `elements`.
1. Iterate over `elements` to inspect position and operator counts.

```python
import aspose.pdf as ap
import sys
from os import path

def using_graphics_absorber(infile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            graphics_absorber.visit(page)
            for element in graphics_absorber.elements:
                print(f"Page Number: {element.source_page.number}")
                print(f"Position: ({element.position.x}, {element.position.y})")
                print(f"Number of Operators: {element.operators.length}")
```

`GraphicsAbsorber` is part of the `aspose.pdf.vector` namespace and is specifically designed to interact with vector graphics in PDF content streams.

## Moving Graphics

After extraction, set a new `position` on each element to relocate it on the same page. Wrap the updates in `suppress_update` / `resume_update` calls to batch content-stream writes into a single operation and avoid redundant repaints.

1. Open the PDF document.
1. Create a `GraphicsAbsorber` and call `visit` on the target page.
1. Call `suppress_update` to pause content-stream writes.
1. Update the `position` of each element.
1. Call `resume_update` to commit all changes at once.
1. Save the modified document.

```python
import aspose.pdf as ap
import sys
from os import path

def move_graphics(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            graphics_absorber.visit(page)
            graphics_absorber.suppress_update()
            for element in graphics_absorber.elements:
                position = element.position
                element.position = ap.Point(position.x + 150, position.y - 10)
            graphics_absorber.resume_update()
        document.save(outfile)
```

## Removing Graphics

To delete specific vector elements from a page, filter by position or bounding rectangle and then remove them. Aspose.PDF for Python provides two approaches depending on whether you want to remove elements inline or collect them first.

### Method 1: Remove Inline Using Rectangle Boundary

This approach checks each element's position against a rectangle and calls `element.remove()` directly inside the loop. Use it when you want concise code and do not need to inspect the removed set afterward.

1. Open the PDF document.
1. Create a `GraphicsAbsorber` and call `visit` on the target page.
1. Define the target [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/).
1. Call `suppress_update` to pause content-stream writes.
1. Iterate `elements`, calling `remove()` on each element whose position falls inside the rectangle.
1. Call `resume_update` to commit the deletions.
1. Save the modified document.

```python
import aspose.pdf as ap
import sys
from os import path

def remove_graphics_method_1(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            graphics_absorber.visit(page)
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            graphics_absorber.suppress_update()
            for element in graphics_absorber.elements:
                if rectangle.contains(element.position, False):
                    element.remove()
            graphics_absorber.resume_update()
        document.save(outfile)
```

### Method 2: Collect Elements First, Then Delete

This approach gathers matching elements into a [GraphicElementCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicelementcollection/) and passes the collection to `page.delete_graphics`. Use it when you need to review or log what will be removed before committing the deletion.

1. Open the PDF document.
1. Create a `GraphicsAbsorber` and call `visit` on the target page.
1. Define the target rectangle.
1. Iterate `elements` and add matching elements to a `GraphicElementCollection`.
1. Call `page.contents.suppress_update` to pause content-stream writes.
1. Call `page.delete_graphics` with the collection.
1. Call `page.contents.resume_update` to commit the deletions.
1. Save the modified document.

```python
import aspose.pdf as ap
import sys
from os import path

def remove_graphics_method_2(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            graphics_absorber.visit(page)
            removed_elements_collection = ap.vector.GraphicElementCollection()
            for element in graphics_absorber.elements:
                if rectangle.contains(element.position, False):
                    removed_elements_collection.add(element)
            page.contents.suppress_update()
            page.delete_graphics(removed_elements_collection)
            page.contents.resume_update()
        document.save(outfile)
```

## Adding Graphics to Another Page

Vector elements extracted from one page can be placed on any other page in the same document. Two methods are available: adding elements one by one, or passing the entire collection in a single call.

### Method 1: Add Elements Individually

Use this method when you need per-element control, such as filtering or transforming individual elements before placing them on the destination page.

1. Open the PDF document.
1. Create a `GraphicsAbsorber` and call `visit` on the source page.
1. Add a new destination page to the document.
1. Call `page_2.contents.suppress_update` to pause content-stream writes.
1. Call `element.add_on_page(page_2)` for each element.
1. Call `page_2.contents.resume_update` to commit all additions.
1. Save the modified document.

```python
import aspose.pdf as ap
import sys
from os import path

def add_to_another_page_method_1(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page_1 = document.pages[1]
            page_2 = document.pages.add()
            graphics_absorber.visit(page_1)
            page_2.contents.suppress_update()
            for element in graphics_absorber.elements:
                element.add_on_page(page_2)
            page_2.contents.resume_update()
        document.save(outfile)
```

### Method 2: Add the Entire Collection at Once

Use this method when you want to copy all extracted elements to a page in a single operation without iterating manually.

1. Open the PDF document.
1. Create a `GraphicsAbsorber` and call `visit` on the source page.
1. Add a new destination page to the document.
1. Call `page_2.contents.suppress_update` to pause content-stream writes.
1. Call `page_2.add_graphics` with the full `elements` collection.
1. Call `page_2.contents.resume_update` to commit all additions.
1. Save the modified document.

```python
import aspose.pdf as ap
import sys
from os import path

def add_to_another_page_method_2(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page_1 = document.pages[1]
            page_2 = document.pages.add()
            graphics_absorber.visit(page_1)
            page_2.contents.suppress_update()
            page_2.add_graphics(graphics_absorber.elements, None)
            page_2.contents.resume_update()
        document.save(outfile)
```

## Related Topics

- [Advanced PDF operations in Python](/pdf/python-net/advanced-operations/)
- [Work with PDF graphs in Python](/pdf/python-net/working-with-graphs/)
- [Work with PDF operators in Python](/pdf/python-net/working-with-operators/)
- [Work with PDF pages in Python](/pdf/python-net/working-with-pages/)

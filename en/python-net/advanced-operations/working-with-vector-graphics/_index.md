---
title: Work with Vector Graphics in Python
linktitle: Working with Vector Graphics
type: docs
weight: 100
url: /python-net/working-with-vector-graphics/
description: Learn how to extract, move, remove, and reuse vector graphics in PDF files using Python.
lastmod: "2026-04-17"
TechArticle: true 
AlternativeHeadline: Use GraphicsAbsorber to inspect and manipulate PDF vector graphics in Python
Abstract: This article explains how to work with vector graphics in Aspose.PDF for Python via .NET using the GraphicsAbsorber class. Learn how to extract vector elements from PDF pages, move or remove them, and copy graphics between pages with low-level control in Python workflows.
---

In this chapter, we'll explore how to use the powerful `GraphicsAbsorber` class to interact with vector graphics within PDF documents. Whether you need to move, remove, or add graphics, this guide will show you how to perform these tasks effectively.

Use this page when you need to inspect or manipulate vector drawing elements already present in a PDF page, such as paths, shapes, and reusable graphical objects.

## Introduction

Vector graphics are a crucial component of many PDF documents, used to represent images, shapes, and other graphical elements. Aspose.PDF provides the `GraphicsAbsorber` class, which allows developers to programmatically access and manipulate these graphics. By using the `Visit` method of `GraphicsAbsorber`, you can extract vector graphics from a specified page and perform various operations, such as moving, removing, or copying them to other pages.

## Common Vector Graphics Tasks

## Extracting Graphics

The first step in working with vector graphics is to extract them from a PDF document. Here’s how you can do it using the `GraphicsAbsorber` class:

1. Open the PDF Document.
1. Initialize the GraphicsAbsorber.
1. Select the Target Page.
1. Extract Graphics from the Page.
1. Iterate and Display Extracted Elements.

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

The GraphicsAbsorber class is part of the aspose.pdf.vector namespace and is specifically designed to interact with vector graphics within PDF documents.

## Moving Graphics

Once you have extracted the graphics, you can move them to a different position on the same page. Here’s how you can achieve this:

1. Open the PDF Document.
1. Initialize the GraphicsAbsorber.
1. Select the Target Page.
1. Extracting Graphic Elements.
1. Suspending Updates for Performance.
1. Modifying Graphic Element Positions.
1. Resuming Updates and Applying Changes.
1. Saving the Updated Document.

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

There are scenarios where you might want to remove specific graphics from a page. Aspose.PDF for Python offers two methods to accomplish this:

### Method 1: Using Rectangle Boundary

The next example demonstrates how to remove vector graphic elements located within a specific rectangular area on the first page of a PDF document using the Aspose.PDF for Python via .NET library. This process involves identifying graphic elements within the defined rectangle and removing them to clean up or modify the PDF content.

1. Open the PDF Document.
1. Initialize the GraphicsAbsorber.
1. Select the Target Page.
1. Extracting Graphic Elements.
1. Defining the Target Rectangle.
1. Suspending Updates for Performance.
1. Removing Graphic Elements Within the Rectangle.
1. Resuming Updates and Applying Changes.
1. Saving the Updated Document.

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

### Method 2: Using a Collection of Removed Elements

The next example demonstrates how to remove vector graphic elements located within a specific rectangular area on the first page of a PDF document using the Aspose.PDF for Python via .NET library. This process involves identifying graphic elements within the defined rectangle and removing them to clean up or modify the PDF content.

1. Open the PDF Document.
1. Initialize the GraphicsAbsorber.
1. Select the Target Page.
1. Defining the Target Rectangle.
1. Extracting Graphic Elements.
1. Creating a Collection for Removal.
1. Identifying Elements Within the Rectangle.
1. Suspending Updates for Performance.
1. Removing Graphic Elements.
1. Resuming Updates and Applying Changes.
1. Saving the Updated Document.

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

Graphics absorbed from one page can be added to another page within the same document.
Here are two methods to achieve this:

### Method 1: Adding Graphics Individually

The next example to copy vector graphic elements from the first page of a PDF document and paste them onto the second page. This operation is facilitated by the GraphicsAbsorber class, which allows for the extraction and manipulation of vector graphics within PDF documents.

1. Open the PDF Document.
1. Initialize the GraphicsAbsorber.
1. Select the Target Page.
1. Extracting Graphic Elements from the First Page.
1. Suspending Updates on the Second Page for Performance.
1. Adding Extracted Graphic Elements to the Second Page.
1. Resuming Updates and Applying Changes.
1. Saving the Updated Document.

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

### Method 2: Adding Graphics as a Collection

The next example to duplicate vector graphic elements from the first page of a PDF document and place them into the second page. This is achieved through the use of the GraphicsAbsorber class, which facilitates the extraction and manipulation of vector graphics within PDF documents.

1. Open the PDF Document.
1. Initialize the GraphicsAbsorber.
1. Select the Target Page.
1. Extracting Graphic Elements from the First Page.
1. Suspending Updates on the Second Page for Performance.
1. Adding Extracted Graphic Elements to the Second Page.
1. Resuming Updates and Applying Changes.
1. Saving the Updated Document.

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
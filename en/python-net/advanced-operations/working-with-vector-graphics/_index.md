---
title: Working with Vector Graphics using Python
linktitle: Working with Vector Graphics
type: docs
weight: 100
url: /python-net/working-with-vector-graphics/
description: This article describes the features of working with GraphicsAbsorber tool using Python.
lastmod: "2025-05-17"
TechArticle: true 
AlternativeHeadline: Use the GraphicsAbsorber tool in PDF with Python
Abstract: The Aspose.PDF for Python via .NET documentation on Working with Vector Graphics article  provides a comprehensive guide for developers aiming to manipulate vector graphics within PDF documents using the GraphicsAbsorber class. This class facilitates the extraction, movement, removal, and duplication of vector graphic elements across PDF pages.
---

In this chapter, we'll explore how to use the powerful `GraphicsAbsorber` class to interact with vector graphics within PDF documents. Whether you need to move, remove, or add graphics, this guide will show you how to perform these tasks effectively.

## Introduction

Vector graphics are a crucial component of many PDF documents, used to represent images, shapes, and other graphical elements. Aspose.PDF provides the `GraphicsAbsorber` class, which allows developers to programmatically access and manipulate these graphics. By using the `Visit` method of `GraphicsAbsorber`, you can extract vector graphics from a specified page and perform various operations, such as moving, removing, or copying them to other pages.

## Extracting Graphics

The first step in working with vector graphics is to extract them from a PDF document. Here’s how you can do it using the `GraphicsAbsorber` class:

1. Open the PDF Document.
1. Initialize the GraphicsAbsorber.
1. Select the Target Page.
1. Extract Graphics from the Page.
1. Iterate and Display Extracted Elements.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create an instance of GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Select the first page of the document
            page = document.pages[1]
            # Use the `Visit` method to extract graphics from the page
            graphics_absorber.visit(page)
            # Display information about the extracted elements
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

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create a GraphicsAbsorber instance
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Select the first page of the document
            page = document.pages[1]
            # Extract graphic elements from the page
            graphics_absorber.visit(page)
            # Temporarily suspend updates to improve performance
            graphics_absorber.suppress_update()
            # Loop through each extracted graphic element and shift its position
            for element in graphics_absorber.elements:
                position = element.position
                # Move graphics by shifting its X and Y coordinates
                element.position = ap.Point(position.x + 150, position.y - 10)
            # Resume updates and apply changes
            graphics_absorber.resume_update()
        # Save PDF document
        document.save(path_outfile)
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

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first page of the document
            page = document.pages[1]
            # Extract graphic elements from the page
            graphics_absorber.visit(page)
            # Define the rectangle where graphics will be removed
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            # Temporarily suspend updates for better performance
            graphics_absorber.suppress_update()
            # Iterate through the extracted graphic elements and remove elements inside the rectangle
            for element in graphics_absorber.elements:
                # Check if the graphic's position falls within the rectangle
                if rectangle.contains(element.position, False):
                    # Remove the graphic element
                    element.remove()
            # Resume updates and apply changes
            graphics_absorber.resume_update()
        # Save PDF document
        document.save(path_outfile)
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

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first page of the document
            page = document.pages[1]
            # Define the rectangle where graphics will be removed
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            # Extract graphic elements from the page
            graphics_absorber.visit(page)
            # Create a collection for the removed elements
            removed_elements_collection = ap.vector.GraphicElementCollection()
            # Add elements within the rectangle to the collection
            for element in graphics_absorber.elements:
                if rectangle.contains(element.position,False):
                    removed_elements_collection.add(item)
            # Temporarily suppress updates for better performance
            page.contents.suppress_update()
            # Delete the selected graphic elements
            page.delete_graphics(removed_elements_collection)
            # Resume updates and apply changes
            page.contents.resume_update()
        # Save PDF document
        document.save(path_outfile)
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

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first and second pages
            page_1 = document.pages[1]
            page_2 = document.pages[2]
            # Extract graphic elements from the first page
            graphics_absorber.visit(page_1)
            # Temporarily suppress updates for better performance
            page_2.contents.suppress_update()
            # Add each graphic element from the first page to the second page
            for element in graphics_absorber.elements:
                element.add_on_page(page_2) # Add each graphic element to the second page.
            # Resume updates and apply changes
            page_2.contents.resume_update()
        # Save PDF document
        document.save(path_outfile)
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

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first and second pages
            page_1 = document.pages[1]
            page_2 = document.pages[2]
            # Extract graphic elements from the first page
            graphics_absorber.visit(page_1)
            # Temporarily suppress updates for better performance
            page_2.contents.suppress_update()
            # Add all graphics at once from the first page to the second page
            page_2.add_graphics(graphics_absorber.elements, None)
            # Resume updates and apply changes
            page_2.contents.resume_update()
        # Save PDF document
        document.save(path_outfile)
```
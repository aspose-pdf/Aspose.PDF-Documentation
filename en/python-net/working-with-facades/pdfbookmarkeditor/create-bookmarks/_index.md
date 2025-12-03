---
title: Create Bookmarks
type: docs
weight: 10
url: /python-net/create-bookmarks/
description: This section explains how to create bookmarks to your PDF file with Aspose.PDF Facades using PdfBookmarEditor Class.
lastmod: "2025-11-05"
---

## Create Bookmarks of All Pages

Aspose.PDF for Python via .NET demonstrates how to automatically create bookmarks for each page in a PDF document. Bookmarks establish a navigational structure, making it easier for users to move between pages in large files.

1. Create a PdfBookmarkEditor.
1. Attach the input PDF file using BindPdf().
1. Use CreateBookmarks() to generate bookmarks for all pages automatically.
1. Save the modified PDF.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def create_bookmarks_of_all_pages():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create PdfBookmarkEditor
    bookmark_editor = pdf_facades.PdfBookmarkEditor()

    # Bind PDF document
    bookmark_editor.BindPdf(os.path.join(data_dir, "CreateBookmarksAll.pdf"))

    # Create bookmarks for all pages
    bookmark_editor.CreateBookmarks()

    # Save updated PDF document
    bookmark_editor.Save(os.path.join(data_dir, "CreateBookmarksOfAllPages_out.pdf"))

    # Dispose resources
    bookmark_editor.Dispose()

    print("Bookmarks created successfully for all pages.")
```

## Create Bookmarks of All Pages with Properties

Create bookmarks for all pages in a PDF document with custom properties. Bookmarks provide a navigational structure, and you can customize their appearance (color, bold, italic) to improve readability and emphasize sections.

1. Create PdfBookmarkEditor.
1. Attach the input PDF file with BindPdf().
1. Use CreateBookmarks(color, bold, italic) to generate bookmarks for all pages with custom styling.
1. Save the updated PDF.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")
clr.AddReference("System.Drawing")  # Needed for color

import Aspose.Pdf.Facades as pdf_facades
from System.Drawing import Color

def create_bookmarks_of_all_pages_with_properties():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create PdfBookmarkEditor
    bookmark_editor = pdf_facades.PdfBookmarkEditor()

    # Bind PDF document
    bookmark_editor.BindPdf(os.path.join(data_dir, "CreateBookmarks-PagesProperties.pdf"))

    # Create bookmarks for all pages with properties:
    # Color = Green, Bold = True, Italic = True
    bookmark_editor.CreateBookmarks(Color.Green, True, True)

    # Save updated PDF document
    bookmark_editor.Save(os.path.join(data_dir, "CreateBookmarks-PagesProperties_out.pdf"))

    # Dispose resources
    bookmark_editor.Dispose()

    print("Bookmarks created successfully for all pages with properties (green, bold, italic).")
```

## Create Bookmark of a Particular Page

Create a bookmark for a specific page in a PDF document. Bookmarks provide a navigational structure, and targeting a particular page allows you to highlight important sections or chapters.

1. Create PdfBookmarkEditor.
1. Attach the input PDF file with BindPdf().
1. Create a bookmark for a specific page.
1. Save the updated PDF.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def create_bookmark_of_a_particular_page():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create PdfBookmarkEditor
    bookmark_editor = pdf_facades.PdfBookmarkEditor()

    # Bind PDF document
    bookmark_editor.BindPdf(os.path.join(data_dir, "CreateBookmark-Page.pdf"))

    # Create bookmark for page 2 with a custom name
    bookmark_editor.CreateBookmarkOfPage("Bookmark Name", 2)

    # Save updated PDF document
    bookmark_editor.Save(os.path.join(data_dir, "CreateBookmark-Page_out.pdf"))

    # Dispose resources
    bookmark_editor.Dispose()

    print("Bookmark created successfully for page 2.")
```

## Create Bookmarks of a Range of Pages

Create bookmarks for a specific range of pages in a PDF document. Instead of generating bookmarks for all pages, you can target selected pages and assign custom names to their bookmarks.

1. Create PdfBookmarkEditor.
1. Attach the input PDF file with BindPdf().
1. Define bookmark names and page list.
1. Create bookmarks for the range.
1. Save the updated PDF.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def create_bookmarks_of_a_range_of_pages():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create PdfBookmarkEditor
    bookmark_editor = pdf_facades.PdfBookmarkEditor()

    # Bind PDF document
    bookmark_editor.BindPdf(os.path.join(data_dir, "CreateBookmark-Page.pdf"))

    # Bookmark name list
    bookmark_list = ["First"]
    # Page list
    page_list = [1]

    # Create bookmarks for the specified range of pages
    bookmark_editor.CreateBookmarkOfPage(bookmark_list, page_list)

    # Save updated PDF document
    bookmark_editor.Save(os.path.join(data_dir, "CreateBookmarkPageRange_out.pdf"))

    # Dispose resources
    bookmark_editor.Dispose()

    print("Bookmarks created successfully for the specified range of pages.")
```

## Add Bookmark in an Existing PDF File

Add a new bookmark to an existing PDF file. Bookmarks provide a navigational structure, allowing readers to quickly jump to specific pages or sections.

1. Create a bookmark object.
1. Create PdfBookmarkEditor.
1. Attach the input PDF file with BindPdf().
1. Use CreateBookmarks(bookmark) to insert the new bookmark into the document.
1. Save the updated PDF.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def add_bookmark_in_existing_pdf_file():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create a new bookmark
    bookmark = pdf_facades.Bookmark()
    bookmark.PageNumber = 1
    bookmark.Title = "New Bookmark"

    # Create PdfBookmarkEditor
    bookmark_editor = pdf_facades.PdfBookmarkEditor()

    # Bind PDF document
    bookmark_editor.BindPdf(os.path.join(data_dir, "AddBookmark.pdf"))

    # Add the bookmark to the PDF
    bookmark_editor.CreateBookmarks(bookmark)

    # Save updated PDF document
    bookmark_editor.Save(os.path.join(data_dir, "AddBookmark_out.pdf"))

    # Dispose resources
    bookmark_editor.Dispose()

    print("Bookmark 'New Bookmark' added successfully to page 1.")
```

## Add Child Bookmark in an Existing PDF File

Add a parent bookmark with child bookmarks in a PDF document. Child bookmarks allow you to create a hierarchical navigation structure, making it easier for readers to explore sections and subsections within a document.

1. Create child bookmarks.
1. Use Bookmarks() to group child bookmarks together.
1. Create a parent bookmark.
1. Assign child bookmarks to the parent.
1. Create PdfBookmarkEditor.
1. Attach the input PDF file with BindPdf().
1. Use CreateBookmarks() to insert the hierarchical structure.
1. Save the updated PDF.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def add_child_bookmark_in_existing_pdf_file():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create child bookmarks
    bookmarks = pdf_facades.Bookmarks()

    child_bookmark1 = pdf_facades.Bookmark()
    child_bookmark1.PageNumber = 1
    child_bookmark1.Title = "First Child"

    child_bookmark2 = pdf_facades.Bookmark()
    child_bookmark2.PageNumber = 2
    child_bookmark2.Title = "Second Child"

    # Add child bookmarks to collection
    bookmarks.Add(child_bookmark1)
    bookmarks.Add(child_bookmark2)

    # Create parent bookmark
    parent_bookmark = pdf_facades.Bookmark()
    parent_bookmark.Action = "GoTo"
    parent_bookmark.PageNumber = 1
    parent_bookmark.Title = "Parent"
    parent_bookmark.ChildItems = bookmarks

    # Create PdfBookmarkEditor
    bookmark_editor = pdf_facades.PdfBookmarkEditor()

    # Bind PDF document
    bookmark_editor.BindPdf(os.path.join(data_dir, "AddChildBookmark.pdf"))

    # Add parent bookmark with children
    bookmark_editor.CreateBookmarks(parent_bookmark)

    # Save updated PDF document
    bookmark_editor.Save(os.path.join(data_dir, "AddChildBookmark_out.pdf"))

    # Dispose resources
    bookmark_editor.Dispose()

    print("Parent bookmark with child bookmarks added successfully.")
```
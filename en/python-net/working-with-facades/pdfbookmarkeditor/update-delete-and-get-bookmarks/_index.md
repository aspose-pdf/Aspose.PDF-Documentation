---
title: Update, Delete and Get Bookmarks
type: docs
weight: 30
url: /python-net/update-delete-and-get-bookmarks/
description: This section explains how to update, delete and get Bookmarkswith Aspose.PDF Facades.
lastmod: "2025-11-05"
---

## Update an Existing Bookmark in the PDF File

Update an existing bookmark in a PDF document. The PdfBookmarkEditor class allows you to locate a bookmark by its current title and assign a new title, effectively renaming it.

1. Create PdfBookmarkEditor.
1. Attach the input PDF file with BindPdf().
1. Use ModifyBookmarks(oldTitle, newTitle) to rename the bookmark.
1. Save the updated PDF.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def update_existing_bookmark():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create PdfBookmarkEditor
    bookmark_editor = pdf_facades.PdfBookmarkEditor()

    # Bind PDF document
    bookmark_editor.BindPdf(os.path.join(data_dir, "UpdateBookmark.pdf"))

    # Modify the existing bookmark, assigning a new title
    bookmark_editor.ModifyBookmarks("New Bookmark", "New Title")

    # Save updated PDF document
    bookmark_editor.Save(os.path.join(data_dir, "UpdateBookmark_out.pdf"))

    # Dispose resources
    bookmark_editor.Dispose()

    print("Bookmark updated successfully with new title.")
```

## Delete All Bookmarks from the PDF File

Delete all bookmarks from a PDF document. Bookmarks provide navigation, but sometimes you may need to remove them entirely—for example, when preparing a clean version of a document without navigation aids.

1. Create PdfBookmarkEditor.
1. Attach the input PDF file with BindPdf().
1. Use DeleteBookmarks() to remove every bookmark in the document.
1. Save the updated PDF.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def delete_all_bookmarks():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create PdfBookmarkEditor
    bookmark_editor = pdf_facades.PdfBookmarkEditor()

    # Bind PDF document
    bookmark_editor.BindPdf(os.path.join(data_dir, "DeleteAllBookmarks.pdf"))

    # Delete all bookmarks in the document
    bookmark_editor.DeleteBookmarks()

    # Save updated PDF document
    bookmark_editor.Save(os.path.join(data_dir, "DeleteAllBookmarks_out.pdf"))

    # Dispose resources
    bookmark_editor.Dispose()

    print("All bookmarks deleted successfully from the PDF.")
```

## Delete a Particular Bookmark from a PDF File

Delete a specific bookmark by its title in a PDF document. Instead of removing all bookmarks, you can target a particular one by name and remove it.

1. Create PdfBookmarkEditor.
1. Attach the input PDF file with BindPdf().
1. Use DeleteBookmarks("title") to remove the bookmark with the given title.
1. Save the updated PDF.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def delete_particular_bookmark():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create PdfBookmarkEditor
    bookmark_editor = pdf_facades.PdfBookmarkEditor()

    # Bind PDF document
    bookmark_editor.BindPdf(os.path.join(data_dir, "DeleteABookmark.pdf"))

    # Delete a bookmark with the title "Page2"
    bookmark_editor.DeleteBookmarks("Page2")

    # Save updated PDF document
    bookmark_editor.Save(os.path.join(data_dir, "DeleteABookmark_out.pdf"))

    # Dispose resources
    bookmark_editor.Dispose()

    print("Bookmark with title 'Page2' deleted successfully.")
```

## Get Bookmarks from the PDF Document Facades

Extract all bookmarks from a PDF document. Bookmarks provide a navigational structure, and extracting them allows you to inspect or reuse their metadata (title, page number, action).

1. Create PdfBookmarkEditor.
1. Attach the input PDF file with BindPdf().
1. Use ExtractBookmarks() to retrieve all bookmarks in the document.
1. Loop through each bookmark and display its properties:
    - Title
    - PageNumber
    - Action

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def get_bookmarks_from_document():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create PdfBookmarkEditor
    bookmark_editor = pdf_facades.PdfBookmarkEditor()

    # Bind PDF document
    bookmark_editor.BindPdf(os.path.join(data_dir, "GetFromPDF.pdf"))

    # Extract all bookmarks from the document
    bookmarks = bookmark_editor.ExtractBookmarks()

    # Iterate through each bookmark and display information
    for bookmark in bookmarks:
        print(f"Title: {bookmark.Title}")
        print(f"Page Number: {bookmark.PageNumber}")
        print(f"Bookmark Action: {bookmark.Action}")

    # Dispose resources
    bookmark_editor.Dispose()

    print("Bookmarks extracted successfully.")
```

## Extract Bookmarks from an Existing PDF File

Extract bookmarks from a PDF document and export them to an XML file. Bookmarks provide a navigational structure, and exporting them allows you to preserve or reuse this structure in other documents or applications.

1. Create PdfBookmarkEditor.
1. Attach the input PDF file with BindPdf().
1. Use ExtractBookmarks() to retrieve all bookmarks in the document.
1. Loop through each bookmark and display its properties:
    - Title
    - PageNumber
1. Export bookmarks to XML.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def extract_bookmarks_from_pdf_file():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create PdfBookmarkEditor
    bookmark_editor = pdf_facades.PdfBookmarkEditor()

    # Bind PDF document
    bookmark_editor.BindPdf(os.path.join(data_dir, "ExtractBookmarks.pdf"))

    # Extract bookmarks from the document
    bookmarks = bookmark_editor.ExtractBookmarks()

    # Iterate through each extracted bookmark
    for bookmark in bookmarks:
        print(f"Title: {bookmark.Title}")
        print(f"Page Number: {bookmark.PageNumber}")

    # Export bookmarks to an XML file
    bookmark_editor.ExportBookmarksToXML(os.path.join(data_dir, "bookmarks.xml"))

    # Dispose resources
    bookmark_editor.Dispose()

    print("Bookmarks extracted and exported to XML successfully.")
```

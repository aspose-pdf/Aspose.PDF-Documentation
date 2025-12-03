---
title: Import and Export Bookmarks
type: docs
weight: 20
url: /python-net/import-and-export-bookmarks/
description: This section explains how to import and export Bookmarks with Aspose.PDF Facades.
lastmod: "2025-11-05"
---

## Import Bookmarks from XML to an Existing PDF File

Import bookmarks from an XML file into a PDF document. Bookmarks stored in XML format can be reused across multiple documents, making it easy to apply a consistent navigation structure.

1. Create PdfBookmarkEditor.
1. Attach the input PDF file with BindPdf().
1. Use ImportBookmarksWithXML(xmlFilePath) to bring bookmarks into the PDF.
1. Save the updated PDF.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def import_bookmarks_from_xml():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create PdfBookmarkEditor
    bookmark_editor = pdf_facades.PdfBookmarkEditor()

    # Bind PDF document
    bookmark_editor.BindPdf(os.path.join(data_dir, "ImportFromXML.pdf"))

    # Import bookmarks from XML file
    bookmark_editor.ImportBookmarksWithXML(os.path.join(data_dir, "bookmarks.xml"))

    # Save updated PDF document
    bookmark_editor.Save(os.path.join(data_dir, "ImportFromXML_out.pdf"))

    # Dispose resources
    bookmark_editor.Dispose()

    print("Bookmarks imported successfully from XML into the PDF.")
```

## Export Bookmarks to XML from an Existing PDF File

Export bookmarks from a PDF document into an XML file. Exporting bookmarks allows you to preserve or reuse the navigational structure of a PDF in a portable format.

1. Create PdfBookmarkEditor.
1. Attach the input PDF file with BindPdf().
1. Use ExportBookmarksToXML(xmlFilePath) to save the bookmarks into an XML file.

The following code snippet shows you how to export bookmarks to an XML file.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def export_bookmarks_to_xml():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create PdfBookmarkEditor
    bookmark_editor = pdf_facades.PdfBookmarkEditor()

    # Bind PDF document
    bookmark_editor.BindPdf(os.path.join(data_dir, "ExportToXML.pdf"))

    # Export bookmarks to an XML file
    bookmark_editor.ExportBookmarksToXML(os.path.join(data_dir, "bookmarks.xml"))

    # Dispose resources
    bookmark_editor.Dispose()

    print("Bookmarks exported successfully to XML.")
```

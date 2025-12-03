---
title: Import and Export Form Field
type: docs
weight: 80
url: /python-net/import-export-form-field/
description: Fill Form fields using DataTable with  FormEditor Class by Aspose.PDF for Python via .NET
lastmod: "2025-11-05"
---

Aspose.PDF for .NET provides great capabilities for create/manipulating form fields inside PDF document.

## Import Data from PDF into FDF

Import form data into a PDF document from multiple formats (FDF, XML, XFDF). The Form class provides methods to bind a PDF and populate its fields with external data sources.

1. Create a Form object.
1. Attach the input PDF file with BindPdf().
1. Use ImportFdf() to load field values from a .fdf file.
1. Use ImportXml() to load field values from a .xml file.
1. Use ImportXfdf() to load field values from a .xfdf file.
1. Save the updated PDF.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades
from System.IO import FileStream, FileMode

def import_data():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.BindPdf(os.path.join(data_dir, "input.pdf"))

    # Import data from FDF
    fdf_stream = FileStream(os.path.join(data_dir, "student.fdf"), FileMode.Open)
    form.ImportFdf(fdf_stream)
    fdf_stream.Close()

    # Import data from XML
    xml_stream = FileStream(os.path.join(data_dir, "input.xml"), FileMode.Open)
    form.ImportXml(xml_stream)
    xml_stream.Close()

    # Import data from XFDF
    xfdf_stream = FileStream(os.path.join(data_dir, "input.xfdf"), FileMode.Open)
    form.ImportXfdf(xfdf_stream)
    xfdf_stream.Close()

    # Save updated PDF document
    form.Save(os.path.join(data_dir, "ImportDataUpdated_out.pdf"))

    # Dispose resources
    form.Dispose()

    print("Data imported from FDF, XML, and XFDF successfully into the PDF form.")
```

## Export Data from FDF into PDF File

Export PDF form data into multiple formats (FDF, XML, XFDF). Each format serves different integration needs:

 - FDF (Forms Data Format) - Lightweight, PDF‑specific format storing only field values.
 - XML - General structured format, widely supported for data exchange.
 - XFDF (XML Forms Data Format) - XML‑based representation of FDF, structured and easy to parse.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades
from System.IO import FileStream, FileMode

def export_data():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.BindPdf(os.path.join(data_dir, "input.pdf"))

    # Export to FDF
    fdf_stream = FileStream(os.path.join(data_dir, "data_out.fdf"), FileMode.Create)
    form.ExportFdf(fdf_stream)
    fdf_stream.Close()

    # Export to XML
    xml_stream = FileStream(os.path.join(data_dir, "data_out.xml"), FileMode.Create)
    form.ExportXml(xml_stream)
    xml_stream.Close()

    # Export to XFDF
    xfdf_stream = FileStream(os.path.join(data_dir, "data_out.xfdf"), FileMode.Create)
    form.ExportXfdf(xfdf_stream)
    xfdf_stream.Close()

    # Dispose resources
    form.Dispose()

    print("Form data exported successfully to FDF, XML, and XFDF formats.")
```

---
title: Import and Export Data
type: docs
weight: 70
url: /python-net/import-and-export-data/
description: This section explains how to import and Export Data with Aspose.PDF Facades using Form Class.
lastmod: "2025-11-05"
---

Import data from an XML file into a PDF form using Python. The workflow binds a PDF document to the Form class, opens an XML file containing field values, and then uses ImportXml() to populate the PDF's corresponding fields. Finally, the updated PDF is saved with the imported data.

1. Create a Form object.
1. Attach the input PDF file with BindPdf().
1. Open the XML file.
1. Import XML data.
1. Save the updated PDF.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades
from System.IO import FileStream, FileMode

def import_data_from_xml():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.BindPdf(os.path.join(data_dir, "input.pdf"))

    # Open XML file as stream
    xml_input_stream = FileStream(os.path.join(data_dir, "input.xml"), FileMode.Open)

    # Import data from XML into PDF form fields
    pdf_form.ImportXml(xml_input_stream)

    # Save updated PDF
    pdf_form.Save(os.path.join(data_dir, "ImportDataFromXML_out.pdf"))

    # Dispose resources
    xml_input_stream.Close()
    pdf_form.Dispose()

    print("PDF form successfully filled with data from XML.")
```

## Export Data to XML from a PDF File

Import data from an XML file into a PDF form. The workflow binds a PDF document to the Form class, opens an XML file containing field values, and then uses ImportXml() to populate the PDF's corresponding fields. Finally, the updated PDF is saved with the imported data.

1. Initialize the PDF form handler.
1. Attach the input PDF file with BindPdf().
1. Use FileStream to read the XML data.
1. Import XML data.
1. Save the updated PDF.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades
from System.IO import FileStream, FileMode

def import_data_from_xml():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.BindPdf(os.path.join(data_dir, "input.pdf"))

    # Open XML file as stream
    xml_input_stream = FileStream(os.path.join(data_dir, "input.xml"), FileMode.Open)

    # Import data from XML into PDF form fields
    pdf_form.ImportXml(xml_input_stream)

    # Save updated PDF
    pdf_form.Save(os.path.join(data_dir, "ImportDataFromXML_out.pdf"))

    # Dispose resources
    xml_input_stream.Close()
    pdf_form.Dispose()

    print("PDF form successfully filled with data from XML.")
```

## Import Data from FDF into a PDF File

Import form data from an FDF file into a PDF document using Python. FDF (Forms Data Format) files store values for PDF form fields separately from the PDF itself. By binding a PDF form and calling ImportFdf(), developers can automatically populate the form fields with the data contained in the FDF file.

1. Create a Form object.
1. Bind the PDF document.
1. Use FileStream to read the external form data.
1. Call ImportFdf() to populate PDF form fields.
1. Save the updated PDF.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades
from System.IO import FileStream, FileMode

def import_data_from_pdf_into_pdf():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.BindPdf(os.path.join(data_dir, "input.pdf"))

    # Open FDF file as stream
    fdf_input_stream = FileStream(os.path.join(data_dir, "student.fdf"), FileMode.Open)

    # Import data from FDF into PDF form fields
    pdf_form.ImportFdf(fdf_input_stream)

    # Save updated PDF
    pdf_form.Save(os.path.join(data_dir, "ImportDataFromPdf_out.pdf"))

    # Dispose resources
    fdf_input_stream.Close()
    pdf_form.Dispose()

    print("PDF form successfully filled with data from FDF file.")
```

## Export Data to FDF from a PDF File

Export PDF form data into an FDF file. FDF (Forms Data Format) is a lightweight file format designed to store form field values separately from the PDF. By binding a PDF document to the Form class and calling ExportFdf(), developers can extract all field values into an external FDF file. The updated PDF is then saved, ensuring both the original document and the exported data are available for further use.

1. Create a Form object
1. Bind the PDF document.
1. Create an FDF file stream.
1. Call ExportFdf() to write field values into the FDF file.
1. Save the updated PDF.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades
from System.IO import FileStream, FileMode

def export_data_to_pdf_from_pdf():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.BindPdf(os.path.join(data_dir, "input.pdf"))

    # Create FDF file stream
    fdf_output_stream = FileStream(os.path.join(data_dir, "student.fdf"), FileMode.Create)

    # Export form data to FDF file
    pdf_form.ExportFdf(fdf_output_stream)

    # Save updated PDF
    pdf_form.Save(os.path.join(data_dir, "ExportDataToPdf_out.pdf"))

    # Dispose resources
    fdf_output_stream.Close()
    pdf_form.Dispose()

    print("Form data successfully exported to FDF and PDF saved.")
```

## Import Data from XFDF into a PDF File

Import form data from an XFDF file into a PDF document. XFDF (XML Forms Data Format) is an XML‑based format used to represent PDF form field values. By binding a PDF form and calling ImportXfdf(), developers can automatically populate the form fields with the data contained in the XFDF file.

1. Create a Form object.
1. Attach the input PDF file with BindPdf().
1. Use FileStream to read the external XML‑based form data.
1. Import XFDF data.
1. Save the updated PDF.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades
from System.IO import FileStream, FileMode

def import_data_from_xfdf_into_pdf():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.BindPdf(os.path.join(data_dir, "input.pdf"))

    # Open XFDF file as stream
    xfdf_input_stream = FileStream(os.path.join(data_dir, "test2.xfdf"), FileMode.Open)

    # Import data from XFDF into PDF form fields
    pdf_form.ImportXfdf(xfdf_input_stream)

    # Save updated PDF
    pdf_form.Save(os.path.join(data_dir, "ImportDataFromXFDF_out.pdf"))

    # Dispose resources
    xfdf_input_stream.Close()
    pdf_form.Dispose()

    print("PDF form successfully filled with data from XFDF file.")
```

## Export Data to XFDF from a PDF File

Export PDF form data into an XFDF file. XFDF (XML Forms Data Format) is an XML‑based standard for representing PDF form field values. By binding a PDF document to the Form class and calling ExportXfdf(), developers can extract all field values into an external XFDF file. The updated PDF is then saved, ensuring both the original document and the exported data are available for further use.

1. Create a Form object.
1. Attach the input PDF file with BindPdf().
1. Create an XFDF file stream.
1. Call ExportXfdf() to write field values into the XFDF file.
1. Save the updated PDF.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades
from System.IO import FileStream, FileMode

def export_data_to_xfdf_from_pdf():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.BindPdf(os.path.join(data_dir, "input.pdf"))

    # Create XFDF file stream
    xfdf_output_stream = FileStream(os.path.join(data_dir, "out.xfdf"), FileMode.Create)

    # Export form data to XFDF file
    pdf_form.ExportXfdf(xfdf_output_stream)

    # Save updated PDF
    pdf_form.Save(os.path.join(data_dir, "ExportDataToXFDF_out.pdf"))

    # Dispose resources
    xfdf_output_stream.Close()
    pdf_form.Dispose()

    print("Form data successfully exported to XFDF and PDF saved.")
```

## Export values from fields to the JSON file

Export PDF form field values into a JSON file. By binding a PDF document to the Form class and calling ExportJson(), developers can extract all field values from the form and save them in a structured JSON format. This workflow is useful for integrating PDF form data into modern applications, APIs, or databases that rely on JSON.

1. Create a Form object.
1. Attach the input PDF file with BindPdf().
1. Create a JSON file stream.
1. Call ExportJson() to write field values into the JSON file.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades
from System.IO import FileStream, FileMode

def export_values_from_fields_to_json():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.BindPdf(os.path.join(data_dir, "Test2.pdf"))

    # Create JSON file stream
    json_stream = FileStream(os.path.join(data_dir, "Test2.json"), FileMode.Create)

    # Export form field values to JSON
    form.ExportJson(json_stream)

    # Dispose resources
    json_stream.Close()
    form.Dispose()

    print("Form field values successfully exported to JSON.")
```

## Import values to fields from the JSON file

Import form field values from a JSON file into a PDF document. JSON provides a lightweight, structured format for storing and exchanging data. By binding a PDF form and calling ImportJson(), developers can automatically populate the form fields with values defined in the JSON file.

1. Create a Form object.
1. Attach the input PDF file with BindPdf().
1. Open the JSON file.
1. Call ImportJson() to populate PDF form fields.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades
from System.IO import FileStream, FileMode

def import_values_from_json_to_form():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.BindPdf(os.path.join(data_dir, "Test2.pdf"))

    # Open JSON file as stream
    json_stream = FileStream(os.path.join(data_dir, "Test2.json"), FileMode.Open)

    # Import data from JSON into PDF form fields
    form.ImportJson(json_stream)

    # Dispose resources
    json_stream.Close()
    form.Dispose()

    print("PDF form successfully filled with data from JSON file.")
```

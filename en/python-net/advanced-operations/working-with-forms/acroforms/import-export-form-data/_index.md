---
title: Import and Export Form Data
type: docs
weight: 80
url: /python-net/import-export-form-data/
description: This section explains how to import and Export Form Data.
lastmod: "2025-08-05"
TechArticle: true
AlternativeHeadline: Import and Export techniques using Aspose.PDF for Python via .NET.
Abstract: This compilation presents a comprehensive suite of form data import and export techniques using Aspose.PDF for Python via .NET. It covers workflows for integrating PDF forms with external data formats including XML, FDF, XFDF, and JSON. Users can automate bulk form filling by importing structured data into interactive fields, or extract field values for analysis, backup, or integration with other systems. The examples demonstrate how to bind PDF forms, transfer data between formats, and save updated documents, enabling scalable and consistent document processing across diverse applications.
---

This page summarizes the available workflows for importing and exporting AcroForm data with Aspose.PDF for Python via .NET. These operations are performed through the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) facade, so the canonical step-by-step examples are documented in the **Working with Facades** section.

## Import and export examples

Use the following articles for the standard data exchange scenarios:

1. Create a Form object using Aspose.PDF.
1. Bind the PDF Form.
1. Load XML Data.
1. Import XML into PDF.
1. Save Updated PDF.

```python
from io import FileIO, StringIO
import json
import sys
from os import path
import aspose.pdf as ap

def import_data_from_xml(input_file_name, data_file_name, output_file_name):

    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(data_file_name, "r") as f:
        form.import_xml(f)

    form.save(output_file_name)
```

## Export Form field Data from a PDF document to an XML file

Python library shows how to export form field data from a PDF document to an XML file using Aspose.PDF for Python. By binding a PDF form and saving its field values in XML format, you can easily store, process, or reuse the form data in other applications or workflows. This approach is ideal for data backup, analysis, and integration with external systems.

Use the following steps:

1. Create a Form object using Aspose.PDF.
1. Bind the PDF Form
1. Export Form Data
1. Save Field Values to XML

```python
from io import FileIO, StringIO
import json
import sys
from os import path
import aspose.pdf as ap

def export_data_to_xml(input_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)
    with FileIO(output_file_name, "w") as f:
        form.export_xml(f)
```

## Import Form field Data from an FDF

The 'import_data_from_fdf' method imports form field data from an FDF (Forms Data Format) file into an existing PDF form and saves the updated document. This approach is useful for pre-filling or updating PDF forms programmatically without modifying the structure of the document.

Use the following steps:

1. Create a Form object using Aspose.PDF.
1. Bind the input PDF.
1. Import the form data with import_fdf().
1. Save the PDF with the imported data to the specified output file path.

```python
from io import FileIO, StringIO
import json
import sys
from os import path
import aspose.pdf as ap

def import_data_from_fdf(input_file_name, data_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(data_file_name, "r") as f:
        form.import_fdf(f)
        form.save(output_file_name)
```

## Export Form field Data to FDF

This example demonstrates how to export form data from a PDF document into an FDF (Forms Data Format) file using Aspose.PDF for Python via .NET.

1. Create a Form object using Aspose.PDF.
1. Bind the PDF document.
1. Export form data with export_fdf().

```python
from io import FileIO, StringIO
import json
import sys
from os import path
import aspose.pdf as ap

def export_data_to_fdf(input_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(output_file_name, "w") as f:
        form.export_fdf(f)
```

## Import Form field Data from an XFDF

This example exports form field data from a PDF document into an XFDF (XML Forms Data Format) file and then saves the updated PDF using Aspose.PDF for Python via .NET.

1. Create a Form object using Aspose.PDF.
1. Bind the PDF document to the form.
1. Export form data to an XFDF file.
1. Save the processed form.

```python
from io import FileIO, StringIO
import json
import sys
from os import path
import aspose.pdf as ap

def import_data_from_xfdf(input_file_name, data_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(data_file_name, "r") as f:
        form.import_xfdf(f)
        form.save(output_file_name)
```

## Export Form field Data to XFDF

This code extracts form field data from a PDF document and exports it into an XFDF (XML Forms Data Format) file using Aspose.PDF for Python.

1. Create a Form object using Aspose.PDF.
1. Bind the PDF document to the form.
1. Export form data to an FDF file.

```python
from io import FileIO, StringIO
import json
import sys
from os import path
import aspose.pdf as ap

def export_data_to_xfdf(input_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(output_file_name, "w") as f:
        form.export_xfdf(f)
```

## Import Data from another PDF

This code snippet demonstrates how to transfer form field data from a source PDF to a destination PDF. The form data is exported to an XFDF stream from the source PDF and then imported into the target PDF using Aspose.PDF for Python via .NET.

1. Create a Form object using Aspose.PDF.
1. Bind the PDF document to the form.
1. Export form data from source PDF.
1. Import form data into destination PDF.
1. Save the updated destination PDF.

```python
from io import FileIO, StringIO
import json
import sys
from os import path
import aspose.pdf as ap

def import_data_from_another_pdf(input_file_name, output_file_name):
    form_source = ap.facades.Form()
    form_dest = ap.facades.Form()

    form_source.bind_pdf(input_file_name)
    form_dest.bind_pdf(output_file_name)

    with StringIO() as f:
        form_source.export_xfdf(f)
        form_dest.import_xfdf(f)
        form_dest.save()
```

## Extract Form Fields to JSON

This method extracts form fields from an input file and exports them to a JSON file using the built-in `export_json()` method.

1. Create a Form object using Aspose.PDF.
1. Open the output file in write mode using FileIO().
1. Export form fields to the JSON file using form.export_json() method.

```python
from io import FileIO, StringIO
import json
import sys
from os import path
import aspose.pdf as ap

def extract_form_fields_to_json(input_file_name, output_file_name):
    form = ap.facades.Form(input_file_name)
    with FileIO(output_file_name, "w") as json_file:
        form.export_json(json_file, True)
```

## Extract Form Fields to JSON Document

1. Create a Form object from the input file.
1. Initialize an empty dictionary to store form field data.
1. Iterate through all form fields and extract their values.
1. Serialize the form data dictionary to a JSON string with 4-space indentation.
1. Write the JSON string to the output file with UTF-8 encoding.

```python
from io import FileIO, StringIO
import json
import sys
from os import path
import aspose.pdf as ap

def extract_form_fields_to_json_doc(input_file_name, output_file_name):
    form = ap.facades.Form(input_file_name)
    form_data = {}
    for formField in form.field_names:
        form_data[formField] = form.get_field(formField)

    json_string = json.dumps(form_data, indent=4)

    with open(output_file_name, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

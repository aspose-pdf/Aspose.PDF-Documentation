---
title: Import and Export Form Data
linktitle: Import and Export Form Data
type: docs
weight: 80
url: /python-net/import-export-form-data/
description: Import and export AcroForm field data in XML, FDF, XFDF, and JSON formats using Aspose.PDF for Python via .NET.
lastmod: "2026-04-28"
TechArticle: true
AlternativeHeadline: Import and Export techniques using Aspose.PDF for Python via .NET.
Abstract: This compilation presents a comprehensive suite of form data import and export techniques using Aspose.PDF for Python via .NET. It covers workflows for integrating PDF forms with external data formats including XML, FDF, XFDF, and JSON. Users can automate bulk form filling by importing structured data into interactive fields, or extract field values for analysis, backup, or integration with other systems. The examples demonstrate how to bind PDF forms, transfer data between formats, and save updated documents, enabling scalable and consistent document processing across diverse applications.
---

This page shows common workflows for importing and exporting AcroForm data with Aspose.PDF for Python via .NET. All operations use the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) facade.

## Import form field data from XML

Use this approach to populate a PDF form from external XML data.

1. Create a `Form` object.
1. Bind the input PDF.
1. Open the XML data file.
1. Import XML data into the form.
1. Save the updated PDF.

```python
from io import FileIO
import aspose.pdf as ap

def import_data_from_xml(input_file_name, data_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(data_file_name, "r") as f:
        form.import_xml(f)

    form.save(output_file_name)
```

## Export form field data to XML

This method exports form field values from a PDF document to XML.

1. Create a `Form` object.
1. Bind the input PDF.
1. Open the XML output file.
1. Export form data to XML.

```python
from io import FileIO
import aspose.pdf as ap

def export_data_to_xml(input_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)
    with FileIO(output_file_name, "w") as f:
        form.export_xml(f)
```

## Import form field data from FDF

The `import_data_from_fdf` method imports form field data from an FDF (Forms Data Format) file into a PDF form.

1. Create a `Form` object.
1. Bind the input PDF.
1. Import the form data with `import_fdf()`.
1. Save the updated PDF.

```python
from io import FileIO
import aspose.pdf as ap

def import_data_from_fdf(input_file_name, data_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(data_file_name, "r") as f:
        form.import_fdf(f)
        form.save(output_file_name)
```

## Export form field data to FDF

This example exports form data from a PDF document to an FDF file.

1. Create a `Form` object.
1. Bind the PDF document.
1. Export form data with `export_fdf()`.

```python
from io import FileIO
import aspose.pdf as ap

def export_data_to_fdf(input_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(output_file_name, "w") as f:
        form.export_fdf(f)
```

## Import form field data from XFDF

Use this method to import form field data from an XFDF (XML Forms Data Format) file into a PDF form.

1. Create a `Form` object.
1. Bind the input PDF.
1. Import form data from an XFDF file.
1. Save the updated PDF.

```python
from io import FileIO
import aspose.pdf as ap

def import_data_from_xfdf(input_file_name, data_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(data_file_name, "r") as f:
        form.import_xfdf(f)
        form.save(output_file_name)
```

## Export form field data to XFDF

This code exports form field data from a PDF document to an XFDF file.

1. Create a `Form` object.
1. Bind the input PDF.
1. Export form data to XFDF.

```python
from io import FileIO
import aspose.pdf as ap

def export_data_to_xfdf(input_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(output_file_name, "w") as f:
        form.export_xfdf(f)
```

## Import data from another PDF

This example transfers form field data from a source PDF to a destination PDF by exporting XFDF to an in-memory stream and importing it into the target form.

1. Create source and destination `Form` objects.
1. Bind the source and destination PDFs.
1. Export form data from source PDF.
1. Import form data into destination PDF.
1. Save the updated destination PDF.

```python
from io import StringIO
import aspose.pdf as ap

def import_data_from_another_pdf(source_pdf_name, destination_pdf_name, output_file_name):
    form_source = ap.facades.Form()
    form_dest = ap.facades.Form()

    form_source.bind_pdf(source_pdf_name)
    form_dest.bind_pdf(destination_pdf_name)

    with StringIO() as xfdf_stream:
        form_source.export_xfdf(xfdf_stream)
        xfdf_stream.seek(0)
        form_dest.import_xfdf(xfdf_stream)

    form_dest.save(output_file_name)
```

## Extract Form Fields to JSON

This method exports form fields to a JSON file by using `export_json()`.

1. Create a `Form` object.
1. Open the JSON output file.
1. Export form fields by using `export_json()`.

```python
from io import FileIO
import aspose.pdf as ap

def extract_form_fields_to_json(input_file_name, output_file_name):
    form = ap.facades.Form(input_file_name)
    with FileIO(output_file_name, "w") as json_file:
        form.export_json(json_file, True)
```

## Extract Form Fields to JSON Document

This example creates a custom JSON document from form field names and values.

1. Create a Form object from the input file.
1. Initialize an empty dictionary to store form field data.
1. Iterate through all form fields and extract their values.
1. Serialize the form data dictionary to a JSON string with 4-space indentation.
1. Write the JSON string to the output file with UTF-8 encoding.

```python
import json
import aspose.pdf as ap

def extract_form_fields_to_json_doc(input_file_name, output_file_name):
    form = ap.facades.Form(input_file_name)
    form_data = {}
    for field_name in form.field_names:
        form_data[field_name] = form.get_field(field_name)

    json_string = json.dumps(form_data, indent=4)

    with open(output_file_name, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

## Related Topics (Facades approach)

- [Import XML Data](/pdf/python-net/import-xml-data/)
- [Import FDF Data](/pdf/python-net/import-fdf-data/)
- [Import XFDF Data](/pdf/python-net/import-xfdf-data/)
- [Import JSON Data](/pdf/python-net/import-json-data/)
- [Export to XML](/pdf/python-net/export-to-xml/)
- [Export to FDF](/pdf/python-net/export-to-fdf/)
- [Export to XFDF](/pdf/python-net/export-to-xfdf/)
- [Export to JSON](/pdf/python-net/export-to-json/)

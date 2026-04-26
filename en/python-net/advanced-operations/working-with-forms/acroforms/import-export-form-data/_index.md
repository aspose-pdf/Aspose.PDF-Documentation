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

- [Import XML Data](/pdf/python-net/import-xml-data/)
- [Import FDF Data](/pdf/python-net/import-fdf-data/)
- [Import XFDF Data](/pdf/python-net/import-xfdf-data/)
- [Import JSON Data](/pdf/python-net/import-json-data/)
- [Export to XML](/pdf/python-net/export-to-xml/)
- [Export to FDF](/pdf/python-net/export-to-fdf/)
- [Export to XFDF](/pdf/python-net/export-to-xfdf/)
- [Export to JSON](/pdf/python-net/export-to-json/)

## Import Data from another PDF

This code snippet demonstrates how to transfer form field data from a source PDF to a destination PDF. The form data is exported to an XFDF stream from the source PDF and then imported into the target PDF using Aspose.PDF for Python via .NET.

1. Create a Form object using Aspose.PDF.
1. Bind the PDF document to the form.
1. Export form data from source PDF.
1. Import form data into destination PDF.
1. Save the updated destination PDF.

```python
from io import StringIO
from os import path
import aspose.pdf as ap

path_infile = path.join(self.workdir_path, infile)
path_outfile = path.join(self.workdir_path, outfile)

# Create Form objects for the source and destination PDFs
form_source = ap.facades.Form()
form_dest = ap.facades.Form()

# Bind the PDF documents
form_source.bind_pdf(path_infile)
form_dest.bind_pdf(path_outfile)

# Transfer form data through an XFDF stream
with StringIO() as xfdf_stream:
    form_source.export_xfdf(xfdf_stream)
    form_dest.import_xfdf(xfdf_stream)
    form_dest.save()
```

## Extract Form Fields to JSON

This method extracts form fields from an input file and exports them to a JSON file using the built-in `export_json()` method.

1. Create a Form object using Aspose.PDF.
1. Open the output file in write mode using FileIO().
1. Export form fields to the JSON file using form.export_json() method.

```python
from io import FileIO
from os import path
import aspose.pdf as ap

path_infile = path.join(self.workdir_path, infile)
path_outfile = path.join(self.workdir_path, outfile)

form = ap.facades.Form(path_infile)
with FileIO(path_outfile, "w") as json_file:
    form.export_json(json_file, True)
```

## Extract Form Fields to JSON Document

1. Create a Form object from the input file.
1. Initialize an empty dictionary to store form field data.
1. Iterate through all form fields and extract their values.
1. Serialize the form data dictionary to a JSON string with 4-space indentation.
1. Write the JSON string to the output file with UTF-8 encoding.

```python
import json
from os import path
import aspose.pdf as ap

path_infile = path.join(self.workdir_path, infile)
path_outfile = path.join(self.workdir_path, outfile)

form = ap.facades.Form(path_infile)
form_data = {}

# Get values from all fields
for form_field in form.field_names:
    form_data[form_field] = form.get_field(form_field)

# Serialize to JSON
json_string = json.dumps(form_data, indent=4)

with open(path_outfile, "w", encoding="utf-8") as json_file:
    json_file.write(json_string)
```

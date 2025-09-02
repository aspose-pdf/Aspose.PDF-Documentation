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

## Import Form Data from an XML file

Next example demonstrates how to import form data from an XML file into an existing PDF form using Aspose.PDF for Python. By binding a PDF form, loading XML data, and saving the updated file, you can quickly populate interactive form fields without manually editing each page. This method is ideal for automating bulk form filling, processing large datasets, and ensuring data consistency across multiple documents.

Use the following steps:

1. Create a Form object using Aspose.PDF.
1. Bind the PDF Form.
1. Load XML Data.
1. Import XML into PDF.
1. Save Updated PDF.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    # Construct full file paths using the working directory
    path_infile = path.join(self.workdir_path, infile)
    path_datafile = path.join(self.workdir_path, datafile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create a Form object from Aspose.PDF
    form = ap.facades.Form()
    
    # Bind the input PDF form
    form.bind_pdf(path_infile)

    # Import XML data into the form
    with FileIO(path_datafile, "r") as f:
        form.import_xml(f)

    # Save the form with imported data to a new PDF file
    form.save(path_outfile)
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
    from os import path
    import aspose.pdf as ap
    
    # Combine the working directory path with the input PDF file name
    path_infile = path.join(self.workdir_path, infile)

    # Combine the working directory path with the output XML file name
    path_outfile = path.join(self.workdir_path, datafile)

    # Create a Form object to work with PDF form fields
    form = ap.facades.Form()

    # Bind the PDF document containing the form
    form.bind_pdf(path_infile)

    # Open the XML file in write mode to store exported form data
    with FileIO(path_outfile, "w") as f:
        # Export form field data from the PDF to the XML file
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
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_datafile = path.join(self.workdir_path, datafile)
    path_outfile = path.join(self.workdir_path, outfile)

    form = ap.facades.Form()
    form.bind_pdf(path_infile)

    with FileIO(path_datafile, "r") as f:
        form.import_fdf(f)
        form.save(path_outfile)
```

## Export Form field Data to FDF

This example demonstrates how to export form data from a PDF document into an FDF (Forms Data Format) file using Aspose.PDF for Python via .NET.

1. Create a Form object using Aspose.PDF.
1. Bind the PDF document.
1. Export form data with export_fdf().

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form = ap.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an FDF file
    with FileIO(path_outfile, "w") as f:
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
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_datafile = path.join(self.workdir_path, datafile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form = ap.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an XFDF file
    with FileIO(path_datafile, "w") as f:
        form.export_xfdf(f)
        form.save(path_outfile)
```

## Export Form field Data to XFDF

This code extracts form field data from a PDF document and exports it into an XFDF (XML Forms Data Format) file using Aspose.PDF for Python.

1. Create a Form object using Aspose.PDF.
1. Bind the PDF document to the form.
1. Export form data to an FDF file.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form = ap.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an FDF file
    with FileIO(path_outfile, "w") as f:
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
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form_source = ap.facades.Form()
    form_dest = ap.facades.Form()

    # Bind PDF document
    form_source.bind_pdf(path_infile)
    form_dest.bind_pdf(path_outfile)

    # Export form data to an FDF file
    with StringIO() as f:
        form_source.export_xfdf(f)
        form_dest.import_xfdf(f)
        form_dest.save()
```

## Extract Form Fields to Json

This method extracts form fields from an input file and exports them to a JSON file.

1. Create a Form object using Aspose.PDF.
1. Open the output file in write mode using FileIO().
1. Export form fields to the JSON file using form.export_json() method.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap 

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    form = ap.facades.Form(path_infile)
    with FileIO(path_outfile, "w") as json_file:
        form.export_json(json_file, True)
```

## Extract Form Fields to Json DOC

1. Create a Form object from the input file.
1. Initialize an empty dictionary to store form field data.
1. Iterate through all form fields and extract their values.
1. Serialize the form data dictionary to a JSON string with 4-space indentation.
1. Write the JSON string to the output file with UTF-8 encoding.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap 

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    form = ap.facades.Form(path_infile)
    form_data = {}
    # Get values from all fields
    for formField in form.field_names:
        # Analyze names and values if needed
        form_data[formField] = form.get_field(formField)

    # Serialize to JSON
    json_string = json.dumps(form_data, indent=4)

    with open(path_outfile, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```
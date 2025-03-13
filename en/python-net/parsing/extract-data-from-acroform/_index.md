---
title: Extract Data from AcroForm using Python
linktitle: Extract Data from AcroForm
type: docs
weight: 50
url: /python-net/extract-data-from-acroform/
description: Aspose.PDF makes it easy to extract form field data from PDF files. Learn how to extract data from AcroForms and save it into JSON, XML, or FDF format.
lastmod: "2025-03-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Get Data from AcroForm using the Aspose.PDF for Python
Abstract: The article provides a comprehensive guide on using Aspose.PDF for Python to extract and export form field data from PDF documents. It details several code snippets demonstrating how to handle PDF forms, including extracting form field data into a dictionary, exporting form data to JSON, XML, FDF, and XFDF formats. The first section describes a method to iterate through form field names, retrieve their values, and store them in a Python dictionary, which is then printed. Another section shows how to serialize this data into a JSON file. Subsequent sections illustrate the process of exporting PDF form data to XML, FDF, and XFDF formats. Each code snippet imports necessary modules, constructs file paths for input and output, and utilizes Aspose.PDF's `Form` class methods to perform the data extraction and export operations efficiently. These examples highlight the versatility of Aspose.PDF for managing PDF form data programmatically.
---

## Extract form fields from PDF document

As well as enabling you to generate form fields and fill form fields, Aspose.PDF for Python makes it easy to extract form field data or information about form fields from PDF files.

The code snippet creates a dictionary to store the values of all fields in the PDF form. It iterates through the form's field names, retrieves their values, and populates the dictionary with this data. Finally, it prints the collected form values.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = self.dataDir + infile
    form = apdf.facades.Form(path_infile)

    form_values = {}
    # Get values from all fields
    for formField in form.field_names:
        # Analyze names and values if needed
        form_values[formField] = form.get_field(formField)

    print(form_values)
```

## Retrieve form field value by title

## Extract form fields from PDF document to JSON

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    with FileIO(path_outfile, "w") as json_file:
        form.export_json(json_file, True)
```

The provided Python code snippet extracts the values of its fields and serializes this data into a JSON format. It imports necessary modules, constructs input and output file paths, retrieves field names and values from the PDF form, and writes the serialized JSON string to a specified output file.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    form_data = {}
    # Get values from all fields
    for formField in form.field_names:
        # Analyze names and values if need
        form_data[formField] = form.get_field(formField)

    # Serialize to JSON
    json_string = json.dumps(form_data, indent=4)

    # Output the JSON string
    print(json_string)

    with open(path_outfile, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

## Extract Data to XML from a PDF File

The next Python code snippet creates a form object, binds a PDF document to that object, and exports the form data to an XML file. The code automatically extracts data from a PDF form and saves it in a structured XML format.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Create Form object
    form = apdf.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export data to XML file
    with FileIO(path_outfile, "w") as f:
        form.export_xml(f)
```

## Export Data to FDF from a PDF File

The following code snippet creates a form object, binds a PDF document to that form, and then exports the form data to an FDF (Forms Data Format) file. The FDF file is a format used to store form data from PDF documents, allowing for easy data interchange.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Create Form object
    form = apdf.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an FDF file
    with FileIO(path_outfile, "w") as f:
        form.export_fdf(f)
```

## Export Data to XFDF from a PDF File

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Create Form object
    form = apdf.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an XFDF file
    with FileIO(path_outfile, "w") as f:
        form.export_xfdf(f)
```

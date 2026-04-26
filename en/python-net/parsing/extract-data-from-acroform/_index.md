---
title: Extract Data from AcroForm using Python
linktitle: Extract Data from AcroForm
type: docs
weight: 50
url: /python-net/extract-data-from-acroform/
description: Aspose.PDF makes it easy to extract form field data from PDF files. Learn how to extract data from AcroForms and save it into JSON, XML, or FDF format.
lastmod: "2025-03-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to Extract Data from AcroForm via Python
Abstract: The article provides a comprehensive guide on using Aspose.PDF for Python to manage form fields within PDF documents. It details various methods for extracting, manipulating, and exporting form data from PDFs. The article begins by demonstrating how to extract form field values and store them in a dictionary, subsequently outputting the data in JSON format. It further illustrates exporting form data directly to JSON files, enhancing data serialization capabilities. Additionally, the article covers exporting form data to other formats such as XML, FDF (Forms Data Format), and XFDF, which are useful for data interchange and structured data storage. Each section includes Python code snippets to aid in understanding and implementation. Overall, the article serves as a practical resource for developers looking to integrate PDF form handling into their Python applications.
---

## Extract form fields from PDF document

[Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) from the `aspose.pdf.facades` namespace provides a straightforward way to read AcroForm field data without opening the full document object model. Iterate over `form.field_names` to get every field name present in the form, then call `form.get_field(name)` to retrieve its current value.

1. Construct a `Form` object by passing the input file path.
1. Iterate over `form.field_names` to enumerate all field names.
1. Call `form.get_field(name)` for each name and store the result in a dictionary.

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

When you know the exact field name (title) defined in the PDF form, you can retrieve its value directly with `form.get_field(name)` without iterating over the entire field collection. This is the fastest approach when only specific fields are needed.

1. Construct a [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) object with the input file path.
1. Call `form.get_field("FieldName")` using the exact field title as it appears in the PDF.
1. Use the returned string value as needed in your application.

```python

    import aspose.pdf as apdf

    form = apdf.facades.Form(path_infile)

    # Retrieve a single field value by its name
    value = form.get_field("FirstName")
    print(value)
```

## Extract form fields from PDF document to JSON

There are two ways to export AcroForm data to JSON. The first uses the built-in `export_json` method on [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form), which serializes all field data directly to a file stream in a single call.

1. Construct a `Form` object with the input file path.
1. Open the output file as a binary stream using `FileIO`.
1. Call `form.export_json(stream, True)` to write the JSON output.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    with FileIO(path_outfile, "w") as json_file:
        form.export_json(json_file, True)
```

The second approach builds a Python dictionary from `field_names` and `get_field`, then serializes it with `json.dumps`. Use this when you need to transform or filter the data before writing it.

1. Iterate over `form.field_names` and populate a dictionary with field values.
1. Serialize the dictionary with `json.dumps(form_data, indent=4)`.
1. Write the resulting JSON string to the output file.

```python

    import aspose.pdf as apdf
    from os import path
    import json

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    form_data = {}
    # Get values from all fields
    for formField in form.field_names:
        form_data[formField] = form.get_field(formField)

    # Serialize to JSON
    json_string = json.dumps(form_data, indent=4)
    print(json_string)

    with open(path_outfile, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

## Extract Data to XML from a PDF File

XML export is useful for integrating PDF form data with systems that consume structured XML feeds or schemas. The [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) class provides `export_xml` to handle the conversion in one step.

1. Create a `Form` instance and bind the PDF with `form.bind_pdf(path)`.
1. Open the output file as a binary stream.
1. Call `form.export_xml(stream)` to write all field data as XML.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

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

FDF (Forms Data Format) is the standard interchange format for AcroForm data and is widely supported by PDF viewers and processing tools. Use `export_fdf` on the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) class to produce a standalone FDF file that can be imported back into the original PDF or another compatible form.

1. Create a `Form` instance and bind the source PDF with `form.bind_pdf(path)`.
1. Open the output file as a binary stream.
1. Call `form.export_fdf(stream)` to write the FDF data.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

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

XFDF (XML Forms Data Format) is the XML-based successor to FDF and is better suited for use in web services and modern data pipelines. Like FDF, an XFDF file can be imported back into a compatible PDF form. Use `export_xfdf` on the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) class to generate the output.

1. Create a `Form` instance and bind the source PDF with `form.bind_pdf(path)`.
1. Open the output file as a binary stream.
1. Call `form.export_xfdf(stream)` to write the XFDF data.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

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

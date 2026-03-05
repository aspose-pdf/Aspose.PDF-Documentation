---
title: Button Fields and Images
type: docs
weight: 40
url: /python-net/button-fields-and-images/
description: This example demonstrates how to manage button fields in a PDF form using the Aspose.PDF Facades API.
lastmod: "2026-02-19"
TechArticle: true 
AlternativeHeadline: Adding Image Appearance to Button Fields & Reading Submit Flags
Abstract: PDF forms often include interactive buttons that either trigger JavaScript actions or submit the form data. You can enhance button fields visually by adding images as their appearance and programmatically inspect their submission behavior.
---

## Add Image Appearance to Button Fields

This code snippet explains how to add an image appearance to an existing button field in a PDF form. The operation enhances the visual presentation of a PDF button by replacing its default appearance with a custom image.

1. Create a Form object.
1. Bind the PDF file to the form object.
1. Add Image to Button Field.
  - Determine the path to the image file associated with the PDF
  - Open the image in binary mode as image_stream.
  - Call fill_image_field() with the fully qualified button field name.
1. Save the Updated PDF.

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    # Add image appearance to button fields
    def add_image_appearance_to_button_fields(infile, outfile):
        """Add image appearance to button fields in a PDF document."""
        # Create Form object
        pdf_form = pdf_facades.Form()

        # Bind PDF document
        pdf_form.bind_pdf(infile)

        # Add image appearance to button fields by providing the field name and image stream
        image_path = infile.replace(".pdf", ".jpg")
        with open(image_path, "rb") as image_stream:
            pdf_form.fill_image_field("Image1_af_image", image_stream)

        # Save updated PDF
        pdf_form.save(outfile)
```

## Get Submit Flags

Python library helps you to retrieve the submit flags of a submit button in a PDF form using Aspose.PDF Facades API. Submit flags define the behavior of a submit button, such as whether it sends the entire form, includes annotations, or submits in FDF, XFDF, PDF, or HTML format.

1. Create a Form object.
1. Call get_submit_flags() on the form object using the fully qualified submit button name.

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    def get_submit_flags(infile, outfile):
        # Create Form object
        pdf_form = pdf_facades.Form()

        # Bind PDF document
        pdf_form.bind_pdf(infile)    
        flags=pdf_form.get_submit_flags("Submit1_af_submit")
        
        print(f"Submit flags: {flags}")
```
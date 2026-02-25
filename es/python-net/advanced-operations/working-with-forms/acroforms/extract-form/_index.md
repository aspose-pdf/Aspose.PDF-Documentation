---
title: Extraer AcroForm - Extraer datos de formulario de PDF en Python
linktitle: Extraer AcroForm
type: docs
weight: 30
url: /es/python-net/extract-form/
description: Extrae el formulario de tu documento PDF con la biblioteca Aspose.PDF para Python. Obtén el valor de un campo individual del archivo PDF.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo obtener datos de formulario de PDF usando Python
Abstract: Este artículo ofrece una guía sobre cómo extraer datos de los campos de formulario dentro de un documento PDF usando Python. Describe cómo navegar a través de todos los campos utilizando la biblioteca Aspose.PDF, específicamente accediendo a la colección `Form` y utilizando el tipo `Field` y su propiedad `value`. Se incluye un fragmento de código Python de ejemplo, que muestra cómo abrir un documento PDF, iterar por sus campos de formulario y imprimir el nombre y el valor de cada campo. Este método es útil para recuperar programáticamente los datos de formulario de archivos PDF.
---

## Extraer datos del formulario

### Obtener valores de todos los campos del documento PDF

Para obtener valores de todos los campos en un documento PDF, necesitas navegar a través de todos los campos de formulario y luego obtener el valor utilizando la propiedad Value. Obtén cada campo de la colección Form, en el tipo base de campo llamado [Campo](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/field/) y accede a su propiedad [valor](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/field/#properties).

Los siguientes fragmentos de código Python muestran cómo obtener los valores de todos los campos de un documento PDF.

```python

    import aspose.pdf as ap

    # Construct the full path to the input PDF file
    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)

    # Create a Form object from the PDF file
    form = ap.facades.Form(path_infile)

    # Initialize an empty dictionary to store form values
    form_values = {}

    # Iterate through all form fields in the PDF
    for formField in form.field_names:
        # Retrieve the value for each form field and store in the dictionary
        form_values[formField] = form.get_field(formField)

    # Print and return the extracted form values
    print(form_values)
```


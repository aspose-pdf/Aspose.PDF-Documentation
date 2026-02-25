---
title: Rellenar AcroForm - Rellenar formulario PDF usando Python
linktitle: Rellenar AcroForm
type: docs
weight: 20
url: /es/python-net/fill-form/
description: Puedes rellenar formularios en tu documento PDF con la biblioteca Aspose.PDF para Python.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo rellenar un campo de formulario en PDF usando Python
Abstract: El artículo ofrece una guía sobre cómo rellenar un campo de formulario en un documento PDF usando la biblioteca Aspose.PDF para Python. Explica el proceso de acceder a un campo de formulario desde la colección de formularios del documento y establecer su valor mediante la propiedad value del campo. El código de ejemplo muestra cómo abrir un documento PDF, iterar a través de sus campos de formulario para encontrar un campo específico por su nombre parcial (en este caso, "Field 1"), y modificar el valor de un TextBoxField a "777". Finalmente, el documento actualizado se guarda en un archivo de salida. Se proporcionan enlaces a la documentación relevante de Aspose para referencia adicional.
---

## Rellenar campo de formulario en un documento PDF

El siguiente ejemplo rellena los campos de formulario PDF con nuevos valores usando Aspose.PDF para Python a través de .NET y guarda el documento actualizado. Soporta la actualización de varios campos especificando un diccionario de nombres de campos y valores.

```python

    import aspose.pdf as ap

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    # Define the new field values
    new_field_values = {
        "First Name": "Alexander_New",
        "Last Name": "Greenfield_New",
        "City": "Yellowtown_New",
        "Country": "Redland_New"
    }

    # Create a Form object from the input PDF file
    form = ap.facades.Form(path_infile)

    # Fill out the form fields with the new values
    for formField in form.field_names:
        if formField in new_field_values:
            form.fill_field(formField, new_field_values[formField])

    # Save the modified form to the output PDF file
    form.save(path_outfile)
```




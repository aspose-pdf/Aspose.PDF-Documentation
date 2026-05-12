---
title: Obtener fachadas de campo
linktitle: Obtener fachadas de campo
type: docs
weight: 10
url: /es/python-net/get-field-facades/
description: Este ejemplo demuestra cómo leer los valores de campos de formulario específicos de un documento PDF usando la API Aspose.PDF Facades.
lastmod: "2026-02-19"
---

Los formularios PDF contienen campos donde los usuarios pueden ingresar datos, como cuadros de texto, casillas de verificación o botones de radio. Para procesar estos formularios programáticamente, a menudo es necesario obtener los valores actuales de estos campos.

1. Crear un objeto Form.
1. Vincular el documento PDF al objeto de formulario.
1. Obtener valores de campos.

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir


    # Get field values
    def get_field_values(infile):
        """Get field values from a PDF document."""
        # Create Form object
        pdf_form = pdf_facades.Form()

        # Bind PDF document
        pdf_form.bind_pdf(infile)

        # Get field values by their names
        field_names = ["First Name", "Last Name"]
        for field_name in field_names:
            value = pdf_form.get_field(field_name)
            print(f"Value of '{field_name}': {value}")
```
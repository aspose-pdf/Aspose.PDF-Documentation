---
title: Obtener valores de campo
type: docs
weight: 50
url: /es/python-net/get-field-values/
description: Recuperando valores de campo de un formulario PDF con Aspose.PDF Facades usando la clase Form.
lastmod: "2026-02-19"
---

Este fragmento de código muestra cómo recuperar los valores actuales de los campos de formulario de un documento PDF usando la API Aspose.PDF Facades. El [get_field()](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/#methods) método le permite acceder programáticamente a los datos ingresados en campos de texto, casillas de verificación, botones de opción y otros elementos AcroForm.

1. Vincule el PDF a un objeto Form.
1. Especifique los nombres de los campos que desea leer.
1. Recupere el valor de cada campo usando get_field().

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
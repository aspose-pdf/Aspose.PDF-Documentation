---
title: Rellenar campos por nombre y valor
type: docs
weight: 60
url: /es/python-net/fill-fields-by-name-and-value/
description: Este artículo muestra cómo rellenar dinámicamente múltiples campos de formulario PDF por nombre y valor usando Aspose.PDF for Python via .NET. En lugar de establecer cada campo individualmente, utiliza una estructura de diccionario para mapear los nombres de los campos a sus valores y los completa en un bucle.
lastmod: "2026-02-19"
---

Rellenar campos de formulario usando una colección de nombre‑valor permite a los desarrolladores crear soluciones escalables y flexibles para la automatización de formularios PDF. En este ejemplo, el [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fachada de [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) se utiliza para vincular un documento PDF e iterar a través de un diccionario de datos de campos. Cada entrada se aplica usando el ’fill_field method’, lo que permite actualizaciones masivas eficientes de los campos de formulario.

1. Inicializa ’pdf_facades.Form()’ para trabajar con campos de formulario interactivos.
1. Utilice 'bind_pdf()' para adjuntar el documento PDF de origen.
1. Crea un diccionario que contenga los nombres de los campos y los valores que deseas insertar.
1. Itera a través del diccionario y llama a 'fill_field()' para cada entrada.
1. Guarda el Documento actualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Fields by Name and Value
def fill_fields_by_name_and_value(infile, outfile):
    """Fill PDF form fields by name and value."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill fields by name and value
    fields = {
        "name": "Jane Smith",
        "address": "456 Elm St, Othertown, USA",
        "email": "jane.smith@example.com",
    }
    for field_name, value in fields.items():
        pdf_form.fill_field(field_name, value)

    # Save updated PDF using outfile
    pdf_form.save(outfile)
```

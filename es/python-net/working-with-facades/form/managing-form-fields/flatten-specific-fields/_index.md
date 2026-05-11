---
title: Aplanar campos específicos
type: docs
weight: 20
url: /es/python-net/flatten-specific-fields/
description: Esta sección muestra cómo gestionar y modificar los campos de formulario PDF usando Aspose.PDF for Python via .NET. Incluye ejemplos prácticos de aplanado de campos específicos, aplanado de todos los campos de formulario y renombrado de campos existentes de forma programática.
lastmod: "2026-02-19"
---

Gestionar los campos de formulario es una parte importante de los flujos de trabajo de procesamiento de PDF. Aplanar los campos elimina la interactividad al convertir los elementos del formulario en contenido de página regular, mientras que renombrar los campos ayuda a estandarizar las convenciones de nomenclatura para un manejo de datos más sencillo.

1. Inicializa pdf_facades.Form() para acceder y gestionar los campos de formulario PDF.
1. Utiliza \u0027bind_pdf()\u0027 para adjuntar el documento de entrada.
1. Proporciona los nombres de los campos y llama a \u0027flatten_field()\u0027 para convertir los campos seleccionados en contenido estático.
1. Llame a 'flatten_all_fields()' para eliminar la interactividad de cada campo de formulario.
1. Defina los nombres de campo antiguos y nuevos y aplique 'rename_field()'.
1. Guarde el PDF actualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Flatten specific fields
def flatten_specific_fields(infile, outfile):
    """Flatten specific fields in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Flatten specific fields by their names
    fields_to_flatten = ["First Name", "Last Name"]
    for field_name in fields_to_flatten:
        pdf_form.flatten_field(field_name)

    # Save updated PDF
    pdf_form.save(outfile)
```

---
title: Exportar a JSON
type: docs
weight: 30
url: /es/python-net/export-to-json/
description: Este ejemplo muestra cómo exportar los valores de los campos de formulario PDF a un archivo JSON usando Aspose.PDF for Python via .NET. Explica cómo cargar un formulario PDF, acceder a sus campos mediante la fachada Form y guardar los datos extraídos en un formato JSON estructurado.
lastmod: "2026-02-19"
---

JSON es un formato de datos ampliamente utilizado que permite el intercambio fluido entre aplicaciones y servicios. En este ejemplo, el [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) objeto del [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) módulo se utiliza para enlazar un archivo PDF y exportar sus valores de campo de formulario a una estructura JSON legible.

1. Inicializa pdf_facades.Form() para trabajar con los campos de formulario.
1. Utilice 'bind_pdf()' para adjuntar el documento PDF de origen.
1. Cree un flujo escribible usando 'FileIO()'.
1. Llame a 'export_json()' para extraer los valores de los campos del formulario y guardarlos en JSON formateado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to JSON
def export_form_to_json(infile, outfile):
    """Export PDF form field values to JSON file."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    # Create JSON file stream
    with FileIO(outfile, "w") as json_stream:
        # Export form field values to JSON
        form.export_json(json_stream, indented=True)
```

---
title: Importar datos JSON
linktitle: Importar datos JSON
type: docs
weight: 30
url: /es/python-net/import-json-data/
description: Este ejemplo muestra cómo importar datos de campos de formulario desde un archivo JSON a un formulario PDF usando Aspose.PDF for Python via .NET. Demuestra cómo vincular un documento PDF, leer datos JSON estructurados a través de un flujo de archivo y rellenar automáticamente los campos de formulario coincidentes.
lastmod: "2026-02-19"
---

JSON se utiliza ampliamente para almacenar y transferir datos estructurados entre sistemas. En este ejemplo, el [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fachada del [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) el módulo se utiliza para vincular un formulario PDF e importar valores de campos desde un archivo JSON externo. Después del proceso de importación, el documento actualizado se guarda como un nuevo PDF.

1. Inicializar pdf_facades.Form() para interactuar con los campos de formulario PDF.
1. Llama a 'bind_pdf()' para adjuntar la plantilla del formulario PDF.
1. Usar 'FileIO()' para leer el archivo JSON que contiene los valores del formulario.
1. Llame a 'import_json()' para rellenar los campos PDF usando pares clave‑valor JSON.
1. Guarde el PDF actualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import from JSON
def import_json_to_pdf_form(infile, datafile, outfile):
    """Import form data from JSON file into PDF form fields."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    # Open JSON file as stream
    with FileIO(datafile, "r") as json_stream:
        # Import data from JSON into PDF form fields
        form.import_json(json_stream)

    # Save updated PDF
    form.save(outfile)
```

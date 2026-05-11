---
title: Exportar a FDF
linktitle: Exportar a FDF
type: docs
weight: 10
url: /es/python-net/export-to-fdf/
description: Este ejemplo explica cómo exportar datos de campos de formulario PDF a un archivo FDF (Forms Data Format) utilizando Aspose.PDF for Python via .NET. Demuestra cómo acceder a los datos de formularios interactivos a través de la fachada Form, vincular un documento PDF de origen y guardar los valores extraídos en un flujo FDF.
lastmod: "2026-02-19"
---

FDF es un formato liviano diseñado específicamente para almacenar y transferir datos de formularios PDF sin incrustar el documento completo. En este ejemplo, un [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) objeto se inicializa desde el [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) módulo, lo que permite a los desarrolladores interactuar con los campos AcroForm y exportar sus valores.

1. Cree una instancia de pdf_facades.Form() para trabajar con los campos de formulario PDF.
1. Llama a 'bind_pdf()' para adjuntar el documento PDF que contiene el formulario.
1. Utiliza 'open(')' para crear un flujo binario escribible para el archivo FDF.
1. Exportar datos del formulario. Llama a 'export_fdf()' para extraer y guardar todos los valores de los campos del formulario.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to FDF
def export_form_data_to_fdf(infile, outfile):
    """Export PDF form data to FDF file."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Create FDF file stream
    with open(outfile, "wb") as fdf_output_stream:
        # Export form data to FDF file
        pdf_form.export_fdf(fdf_output_stream)
```

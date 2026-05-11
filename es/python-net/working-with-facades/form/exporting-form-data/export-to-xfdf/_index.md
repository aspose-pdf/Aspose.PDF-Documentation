---
title: Exportar a XFDF
type: docs
weight: 20
url: /es/python-net/export-to-xfdf/
description: Este ejemplo muestra cómo exportar los datos de los campos de formulario PDF a un archivo XFDF (XML Forms Data Format) utilizando Aspose.PDF for Python via .NET. Demuestra cómo cargar un formulario PDF, acceder a sus campos a través de la fachada Form, y guardar los valores extraídos en un flujo XFDF.
lastmod: "2026-02-19"
---

XFDF es una representación XML de los datos de formulario PDF que permite a los desarrolladores transferir los valores de los campos de formulario de forma independiente del documento original. En este ejemplo, el [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) objeto de [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) se utiliza para vincular el PDF fuente y exportar sus datos a un archivo XFDF estructurado.

1. Inicialice pdf_facades.Form() para gestionar los datos del formulario PDF.
1. Llame a 'bind_pdf()' para adjuntar el documento PDF de origen.
1. Utilice 'open()' para crear un flujo binario escribible.
1. Exportar datos del formulario. Llame a 'export_xfdf()' para extraer y guardar los valores de los campos del formulario en formato XFDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to XFDF
def export_pdf_form_to_xfdf(infile, outfile):
    """Export PDF form data to XFDF file."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Create XFDF file stream
    with open(outfile, "wb") as xfdf_output_stream:
        # Export form data to XFDF file
        pdf_form.export_xfdf(xfdf_output_stream)
```

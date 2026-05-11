---
title: Importar datos FDF
type: docs
weight: 10
url: /es/python-net/import-fdf-data/
description: Este ejemplo muestra cómo importar datos de formulario desde un archivo FDF a un formulario PDF usando Aspose.PDF for Python via .NET. Muestra cómo vincular un documento PDF, leer los valores de los campos del formulario desde un flujo FDF y rellenar automáticamente los campos correspondientes.
lastmod: "2026-02-19"
---

FDF (Forms Data Format) es un formato ligero utilizado para almacenar y transferir los valores de los campos de formularios PDF sin incluir todo el documento. En este ejemplo, el [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fachada de [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) se utiliza para cargar un formulario PDF e importar datos de campos desde un archivo FDF externo. Después del proceso de importación, el PDF actualizado se guarda como un archivo nuevo.

1. Inicializa pdf_facades.Form() para trabajar con campos de formulario PDF interactivos.
1. Llama a 'bind_pdf()' para adjuntar la plantilla del formulario PDF.
1. Utilice 'open()' para leer el archivo FDF en modo binario.
1. Llame a 'import_fdf()' para rellenar los campos PDF con datos del archivo FDF.
1. Guarde el PDF actualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import Data from FDF
def import_fdf_to_pdf_form(infile, datafile, outfile):
    """Import form data from FDF file into PDF form fields."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open FDF file as stream
    with open(datafile, "rb") as fdf_input_stream:
        pdf_form.import_fdf(fdf_input_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```

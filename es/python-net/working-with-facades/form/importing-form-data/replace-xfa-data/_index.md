---
title: Reemplazar datos XFA
type: docs
weight: 50
url: /es/python-net/replace-xfa-data/
description: Este ejemplo demuestra cómo reemplazar los datos de formulario XFA existentes en un PDF utilizando Aspose.PDF for Python via .NET. Muestra cómo vincular un documento PDF basado en XFA, cargar nuevos datos desde un archivo XFA externo y actualizar el contenido del formulario de forma programática.
lastmod: "2026-02-19"
---

Los formularios XFA (XML Forms Architecture) almacenan sus datos en formato XML dentro de la estructura PDF. En este ejemplo, el [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fachada del [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) módulo se utiliza para vincular un PDF y reemplazar su conjunto de datos XFA existente usando una secuencia XML externa. Después de aplicar los nuevos datos, el PDF actualizado se guarda como un archivo separado.

1. Inicialice pdf_facades.Form() para gestionar los datos del formulario XFA.
1. Llame 'bind_pdf()' para adjuntar el PDF que contiene formularios XFA.
1. Utilice 'FileIO()' para leer el archivo XML XFA.
1. Llame a 'set_xfa_data()' para actualizar el PDF con nuevo contenido XFA.
1. Guarda el Documento actualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Replace from XFA data
def replace_xfa_data(infile, datafile, outfile):
    """Import form data from XFA file into PDF form fields."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    # Open XFA file as stream
    with FileIO(datafile, "r") as xfa_stream:
        # Import data from XFA into PDF form fields
        form.set_xfa_data(xfa_stream)

    # Save updated PDF
    form.save(outfile)
```

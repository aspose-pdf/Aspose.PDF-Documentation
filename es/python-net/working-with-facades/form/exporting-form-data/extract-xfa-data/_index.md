---
title: Extraer datos XFA
type: docs
weight: 50
url: /es/python-net/extract-xfa-data/
description: Este ejemplo explica cómo extraer datos de formulario XFA de un archivo PDF usando Aspose.PDF for Python via .NET. Demuestra cómo vincular un documento PDF basado en XFA a la fachada Form y exportar su estructura de datos interna a un flujo de archivo.
lastmod: "2026-02-19"
---

Los formularios XFA (XML Forms Architecture) difieren de los AcroForms tradicionales porque sus datos se almacenan como XML dentro del PDF. En este ejemplo, el [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) objeto del [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) módulo se utiliza para vincular el PDF y extraer sus datos XFA directamente a un archivo.

1. Cree una instancia de pdf_facades.Form() para gestionar los datos del formulario.
1. Llame a 'bind_pdf()' para adjuntar el PDF de origen que contiene formularios XFA.
1. Utilice 'FileIO()' para crear un flujo de archivo con capacidad de escritura.
1. Llame a 'extract_xfa_data()' para exportar los datos XML XFA incrustados.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Extract XFA Data
def export_xfa_data(infile, outfile):
    """Export XFA form data."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    with FileIO(outfile, "w") as stream:
        # Export embedded XFA XML data to the output stream
        form.extract_xfa_data(stream)
```

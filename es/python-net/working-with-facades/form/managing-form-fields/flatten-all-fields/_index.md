---
title: Aplanar todos los campos
linktitle: Aplanar todos los campos
type: docs
weight: 10
url: /es/python-net/flatten-all-fields/
description: Este ejemplo demuestra cómo aplanar todos los campos de formulario en un PDF usando Aspose.PDF for Python via .NET. Muestra cómo vincular un documento PDF, convertir cada elemento de formulario interactivo en contenido estático de página y guardar el archivo finalizado.
lastmod: "2026-02-19"
---

Aplanar elimina la interactividad de los formularios PDF al combinar los valores de los campos directamente en el diseño del documento. En este ejemplo, el [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fachada de [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) se usa para vincular el PDF de origen y aplicar el método flatten_all_fields(), que convierte todos los campos en contenido no editable.

1. Inicializar pdf_facades.Form() para interactuar con los campos de formulario PDF.
1. Llame a 'bind_pdf()' para adjuntar el documento de origen.
1. Llame a 'flatten_all_fields()' para convertir todos los campos interactivos en contenido estático.
1. Guarda el Documento actualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Flatten all fields
def flatten_all_fields(infile, outfile):
    """Flatten all fields in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Flatten all fields in the PDF document
    pdf_form.flatten_all_fields()

    # Save updated PDF
    pdf_form.save(outfile)
```

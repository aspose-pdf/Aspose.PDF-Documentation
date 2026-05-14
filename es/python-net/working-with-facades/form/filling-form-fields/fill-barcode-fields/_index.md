---
title: Rellenar campos de código de barras
linktitle: Rellenar campos de código de barras
type: docs
weight: 50
url: /es/python-net/fill-barcode-fields/
description: Este ejemplo muestra cómo rellenar programáticamente campos de código de barras en un formulario PDF utilizando Aspose.PDF for Python via .NET. Demuestra cómo enlazar un documento PDF, asignar un valor a un campo de código de barras y guardar el archivo actualizado.
lastmod: "2026-02-19"
---

Los campos de código de barras en formularios PDF permiten que la información codificada se almacene y se muestre visualmente como códigos de barras. En este ejemplo, el [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fachada del [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) módulo se utiliza para acceder a los campos del formulario y asignar un valor de código de barras. Una vez que los datos se rellenan, el PDF se guarda con el contenido de código de barras actualizado.

1. Inicializa 'pdf_facades.Form()' para gestionar interacciones con formularios PDF.
1. Llama a 'bind_pdf()' para adjuntar el PDF que contiene campos de código de barras.
1. Usa 'fill_field()' para asignar un valor de código de barras.
1. Guarda el Documento actualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Barcode Fields
def fill_barcode_fields(infile, outfile):
    """Fill barcode fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill barcode fields by name
    pdf_form.fill_field("product_barcode", "123456789012")

    # Save updated PDF
    pdf_form.save(outfile)
```

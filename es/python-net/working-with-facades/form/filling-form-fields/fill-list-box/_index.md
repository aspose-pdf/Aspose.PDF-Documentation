---
title: Rellenar cuadro de lista
linktitle: Rellenar cuadro de lista
type: docs
weight: 40
url: /es/python-net/fill-list-box/
description: Este ejemplo demuestra cómo rellenar programáticamente campos de cuadro de lista y de selección múltiple en un formulario PDF utilizando Aspose.PDF for Python via .NET. Muestra cómo enlazar un documento PDF, seleccionar valores dentro de un campo de formulario basado en listas y guardar el archivo actualizado.
lastmod: "2026-02-19"
---

Los campos de cuadro de lista y de selección múltiple permiten a los usuarios elegir uno o varios valores de un conjunto de opciones predefinido. En este ejemplo, el [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fachada de [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) se utiliza para acceder al formulario PDF y asignar un valor seleccionado al campo favorite_colors. Una vez que se selecciona la opción deseada, el documento actualizado se guarda.

1. Inicializa 'pdf_facades.Form()' para gestionar y actualizar los campos del formulario.
1. Llama a 'bind_pdf()' para adjuntar el PDF origen que contiene campos de cuadro de lista o de selección múltiple.
1. Utilice 'fill_field()' para seleccionar un valor de las opciones disponibles.
1. Guarda el Documento actualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill List Box / Multi-Select Fields
def fill_list_box_fields(infile, outfile):
    """Fill list box and multi-select fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill list box / multi-select fields by name
    pdf_form.fill_field("favorite_colors", "Red")

    # Save updated PDF
    pdf_form.save(outfile)
```

---
title: Rellenar campos de texto
type: docs
weight: 10
url: /es/python-net/fill-text-fields/
description: Este ejemplo muestra cómo rellenar automáticamente campos de texto en un formulario PDF usando Aspose.PDF for Python via .NET. Muestra cómo cargar un documento PDF, rellenar campos de formulario específicos por nombre y guardar el archivo actualizado.
lastmod: "2026-02-19"
---

Rellenar programáticamente campos de texto permite a las aplicaciones reutilizar plantillas PDF e insertar contenido dinámico sin edición manual. En este ejemplo, el [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fachada de [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) se utiliza para enlazar un formulario PDF y actualizar varios campos como nombre, dirección y correo electrónico. Después de asignar los valores, el PDF modificado se guarda como un nuevo documento.

1. Inicialice 'pdf_facades.Form()' para gestionar operaciones de campos de formulario.
1. Utilice 'bind_pdf()' para adjuntar el PDF de entrada que contiene campos de texto.
1. Llame a 'fill_field()' para insertar datos en campos como nombre, dirección y correo electrónico.
1. Guarde el PDF actualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Text Fields
def fill_text_fields(infile, outfile):
    """Fill text fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill text fields by name
    pdf_form.fill_field("name", "John Doe")
    pdf_form.fill_field("address", "123 Main St, Anytown, USA")
    pdf_form.fill_field("email", "john.doe@example.com")

    # Save updated PDF
    pdf_form.save(outfile)
```

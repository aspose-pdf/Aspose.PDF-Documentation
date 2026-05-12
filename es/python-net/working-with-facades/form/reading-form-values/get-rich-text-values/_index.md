---
title: Obtener valores de texto enriquecido
linktitle: Obtener valores de texto enriquecido
type: docs
weight: 40
url: /es/python-net/get-rich-text-values/
description: Esta sección explica cómo recuperar el contenido de texto enriquecido de un campo de formulario en un documento PDF usando la API Aspose.PDF Facades. A diferencia de los campos de texto simple, los campos de texto enriquecido pueden contener contenido con formato, como texto en negrita, diferentes fuentes, colores y estilo de párrafo.
lastmod: "2026-02-19"
---

Los formularios PDF pueden incluir campos de texto que admiten formato de texto enriquecido. Estos campos pueden almacenar contenido con atributos de estilo además de valores de texto simple.

1. Crear un objeto Form.
1. Vincular el documento PDF.
1. Recuperar valores de texto enriquecido.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Get rich text values
def get_rich_text_values(infile):
    """Get rich text values from a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Get rich text values by their names
    field_names = ["Summary"]
    for field_name in field_names:
        rich_text_value = pdf_form.get_rich_text(field_name)
        print(f"Rich text value of '{field_name}': {rich_text_value}")
```

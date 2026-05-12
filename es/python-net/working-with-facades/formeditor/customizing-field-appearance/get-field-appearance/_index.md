---
title: Obtener apariencia del campo
linktitle: Obtener apariencia del campo
type: docs
weight: 20
url: /es/python-net/get-field-appearance/
description: Este artículo explica cómo abrir un PDF, acceder a un campo de formulario, obtener sus configuraciones de apariencia y mostrarlas. El ejemplo demuestra la obtención de la apariencia de un campo llamado "Last Name".
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Recuperar la apariencia del campo de formulario PDF usando Python
Abstract: Este ejemplo demuestra cómo recuperar las propiedades visuales de apariencia de un campo de formulario en un documento PDF usando Aspose.PDF for Python. El código abre un PDF existente, accede a un campo de formulario específico e imprime los detalles de su apariencia, incluyendo el color de fondo, el color del texto, el color del borde y la alineación.
---

Los campos de formulario en documentos PDF tienen propiedades visuales como el color de fondo, el color del texto, el color del borde y la alineación. Con Aspose.PDF for Python, los desarrolladores pueden inspeccionar programáticamente estas configuraciones de apariencia usando el [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) clase.

1. Abra un documento PDF existente.
1. Cree un objeto FormEditor.
1. Recupere la información de apariencia de un campo específico.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_field_appearance(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Get field appearance
    appearance = form_editor.get_field_appearance("Last Name")
    print("Field Appearance: " + str(appearance))
```

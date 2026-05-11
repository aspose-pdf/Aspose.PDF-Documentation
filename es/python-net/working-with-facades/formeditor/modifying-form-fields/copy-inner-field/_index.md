---
title: Copiar campo interno
linktitle: Copiar campo interno
type: docs
weight: 20
url: /es/python-net/copy-inner-field/
description: Copiar campos de formulario PDF a una nueva posición usando Python con Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Copiar campos de formulario PDF a una nueva posición usando Python
Abstract: Este ejemplo demuestra cómo copiar un campo de formulario existente a una nueva posición en un documento PDF usando Aspose.PDF for Python. El código abre un PDF, duplica un campo a una página y coordenadas especificadas, y guarda el documento actualizado.
---

Los formularios PDF a menudo requieren duplicar campos mientras se mantiene el formato y comportamiento original. Usando Aspose.PDF for Python, los desarrolladores pueden copiar un campo existente a una nueva posición en la misma u otra página de forma programática.

Este artículo explica cómo copiar un campo llamado ‘First Name’ a un nuevo campo llamado ‘First Name Copy’ en la página 2 en coordenadas específicas (x=200, y=600), generando un PDF con el campo recién posicionado.

1. Abra un formulario PDF existente.
1. Cree un objeto FormEditor.
1. Vincula el documento PDF al FormEditor.
1. Copia el campo ‘First Name’ a un nuevo campo ‘First Name Copy’ en la página 2 en las coordenadas (200, 600).
1. Guarde el documento actualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def copy_inner_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Copies an existing field to a new position specified by both page number and ordinates.
    # A new document will be produced, which contains everything the source document has except for the newly copied field.
    form_editor.copy_inner_field("First Name", "First Name Copy", 2, 200, 600)
    # Save updated document
    form_editor.save(outfile)
```

**Tenga en cuenta:**

La firma del método 'copy_inner_field' se ve así:

```python
copy_inner_field(original_field_name, new_field_name, page_number, x, y)
```

- 'original_field_name' – el campo que desea duplicar.
- 'new_field_name' – el nombre del nuevo campo.
- 'page_number' – la página en la que aparecerá el nuevo campo.
- x, y – coordenadas en esa página.

Se espera que page_number sea un entero positivo que corresponda a una página existente en el PDF (indexación basada en 1).

Si pasa un parámetro negativo, p. ej.:

```python
form_editor.copy_inner_field("First Name", "First Name Copy", -1, 200, 600)
```

El programa entonces restablecerá los parámetros anteriores.

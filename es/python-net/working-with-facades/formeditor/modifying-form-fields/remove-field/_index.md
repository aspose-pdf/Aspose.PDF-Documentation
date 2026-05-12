---
title: Eliminar campo
linktitle: Eliminar campo
type: docs
weight: 60
url: /es/python-net/remove-field/
description: Este ejemplo muestra cómo eliminar el campo ‘Country’ de un formulario PDF usando el método ‘remove_field’ de la clase ‘FormEditor’.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar un campo de formulario de un documento PDF usando Python
Abstract: Este ejemplo demuestra cómo eliminar un campo de formulario existente de un documento PDF usando Aspose.PDF for Python. El código carga un archivo PDF, elimina el campo especificado usando la clase FormEditor y guarda el documento actualizado.
---

Los formularios PDF pueden contener campos que ya no son necesarios debido a cambios de diseño o actualizaciones del flujo de trabajo. Con Aspose.PDF for Python, los desarrolladores pueden eliminar fácilmente campos de formulario específicos de forma programática.

El [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) La clase en Aspose.PDF proporciona el método ‘remove_field’, que permite a los desarrolladores eliminar un campo de formulario por su nombre.

1. Cargar el documento PDF.
1. Cree un objeto FormEditor.
1. Vincular el PDF al FormEditor.
1. Eliminar el campo de formulario especificado.
1. Guarde el documento actualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Remove field from document
    form_editor.remove_field("Country")
    # Save updated document
    form_editor.save(outfile)
```

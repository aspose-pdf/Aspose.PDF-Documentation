---
title: Establecer alineación de campo
linktitle: Establecer alineación de campo
type: docs
weight: 30
url: /es/python-net/set-field-alignment/
description: Este ejemplo muestra cómo establecer la alineación del texto de un campo de formulario en un documento PDF usando Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Establecer alineación de texto para campos de formulario PDF usando Python
Abstract: Este artículo explica cómo abrir un documento PDF, establecer la alineación de un campo específico usando la clase FormEditor y guardar el PDF actualizado. El ejemplo establece la alineación del texto de un campo llamado "First Name" al centro.
---

Los campos de formulario PDF a menudo requieren una alineación de texto personalizada para mantener un diseño consistente y profesional. Usando Aspose.PDF for Python, los desarrolladores pueden establecer programáticamente la alineación del contenido de texto de un campo de formulario.

El [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) clase, en combinación con el [FormFieldFacade](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formfieldfacade/) constantes, permite a los desarrolladores modificar la alineación de los campos de formulario existentes de forma programática.

1. Abra un documento PDF existente.
1. Cree un objeto FormEditor.
1. Establece la alineación de un campo llamado "First Name" al centro.
1. Guarde el documento modificado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_alignment(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field alignment to center
    if form_editor.set_field_alignment(
        "First Name", pdf_facades.FormFieldFacade.ALIGN_CENTER
    ):
        # Save updated document
        form_editor.save(outfile)
    else:
        raise Exception(
            "Failed to set field alignment. Field may not support alignment."
        )
```

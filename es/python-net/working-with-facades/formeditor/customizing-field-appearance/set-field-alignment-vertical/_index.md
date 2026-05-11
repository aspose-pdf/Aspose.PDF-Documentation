---
title: Establecer alineación vertical del campo
type: docs
weight: 40
url: /es/python-net/set-field-alignment-vertical/
description: Este ejemplo muestra cómo establecer la alineación vertical de un campo de formulario en un documento PDF usando Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Establecer alineación vertical para campos de formulario PDF usando Python
Abstract: Este artículo explica cómo abrir un PDF, establecer la alineación vertical de un campo usando la clase FormEditor y guardar el PDF actualizado. El ejemplo establece la alineación vertical de un campo llamado "First Name" en la parte inferior del área del campo.
---

Los campos de formulario PDF pueden contener texto que necesita una alineación vertical adecuada para una apariencia coherente y profesional. Usando Aspose.PDF for Python, los desarrolladores pueden modificar programáticamente la alineación vertical de los campos de formulario.
La alineación vertical permite a los desarrolladores controlar si el texto del campo aparece en la parte superior, central o inferior del cuadro delimitador del campo, mejorando el diseño y la legibilidad de los datos del formulario.

Usando el [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) clase y el [FormFieldFacade](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formfieldfacade/) constantes, los desarrolladores pueden ajustar la alineación vertical programáticamente para lograr un diseño de formulario coherente:

1. Abra un documento PDF existente.
1. Cree un objeto FormEditor.
1. Establezca la alineación vertical de un campo llamado "First Name" en la parte inferior.
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


def set_field_alignment_vertical(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Attempt to set vertical alignment of the "First Name" field to bottom
    if form_editor.set_field_alignment_v(
        "First Name", pdf_facades.FormFieldFacade.ALIGN_BOTTOM
    ):
        # Save updated document
        form_editor.save(outfile)
    else:
        raise Exception(
            "Failed to set field vertical alignment. Field may not support vertical alignment."
        )
```

---
title: Crear campo TextBox
linktitle: Crear campo TextBox
type: docs
weight: 60
url: /es/python-net/create-textbox-field/
description: Aprenda cómo agregar programáticamente campos TextBox a un documento PDF usando Aspose.PDF for Python. Este tutorial muestra cómo insertar múltiples campos de texto, establecer valores predeterminados y guardar el documento PDF actualizado.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Crear campos TextBox en un PDF usando Aspose.PDF for Python
Abstract: Los campos TextBox en formularios PDF permiten a los usuarios introducir y editar texto, haciendo que los documentos sean interactivos y fáciles de usar. En este tutorial, aprenderá cómo crear campos de formulario TextBox en un PDF usando la clase FormEditor en Aspose.PDF for Python. El ejemplo demuestra cómo agregar múltiples campos, especificar valores predeterminados y guardar el PDF modificado.
---

Los formularios PDF a menudo requieren la entrada de texto por parte de los usuarios, como nombres, direcciones o comentarios. Los campos TextBox habilitan esta funcionalidad al proporcionar campos editables directamente dentro del documento PDF.

El [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) class permite agregar campos de texto, casillas de verificación, botones de radio, listas desplegables, combo boxes y botones, facilitando la creación de PDFs interactivos.

1. Cargar un documento PDF existente.
1. Agregar varios campos TextBox para la entrada del usuario.
1. Establecer valores predeterminados para cada campo.
1. Guarde el documento PDF actualizado.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_textbox_field(infile, outfile):
    """Create TextBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add TextBox field to PDF form
    pdf_form_editor.add_field(
        pdf_facades.FieldType.TEXT, "first_name", "Alexander", 1, 50, 570, 150, 590
    )
    pdf_form_editor.add_field(
        pdf_facades.FieldType.TEXT, "last_name", "Smith", 1, 235, 570, 330, 590
    )

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)
```

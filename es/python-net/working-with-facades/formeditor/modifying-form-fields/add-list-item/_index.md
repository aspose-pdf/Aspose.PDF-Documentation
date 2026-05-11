---
title: Agregar elemento a la lista
type: docs
weight: 10
url: /es/python-net/add-list-item/
description: Este ejemplo muestra cómo agregar elementos a un campo de formulario de cuadro de lista en un documento PDF usando Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar elementos a los campos de cuadro de lista PDF usando Python
Abstract: Este artículo muestra cómo abrir un documento PDF, añadir elementos a un campo de cuadro de lista llamado "Country", y guardar el documento actualizado.
---

Los campos de cuadro de lista en los PDF permiten a los usuarios seleccionar una o varias opciones de un conjunto predefinido. Usando Aspose.PDF for Python, los desarrolladores pueden agregar programáticamente nuevos elementos a estos campos. El [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) la clase proporciona el método ‘add_list_item’ para añadir elementos a un campo de cuadro de lista existente.

1. Abra un formulario PDF existente.
1. Cree un objeto FormEditor.
1. Vincular el PDF al FormEditor.
1. Agregar elementos al campo de lista "Country".
1. Guarde el documento actualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_list_item(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Add list item to list box field
    form_editor.add_list_item("Country", ["New Zealand", "New Zealand"])
    # Save updated document
    form_editor.save(outfile)
```

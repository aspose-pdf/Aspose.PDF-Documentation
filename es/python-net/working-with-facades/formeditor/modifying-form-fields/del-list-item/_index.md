---
title: Eliminar elemento de la lista
type: docs
weight: 40
url: /es/python-net/del-list-item/
description:
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar elementos de los campos de cuadro de lista PDF usando Python
Abstract: Este ejemplo muestra cómo eliminar un elemento de un campo de formulario de cuadro de lista en un documento PDF usando Aspose.PDF for Python. El código abre un PDF existente, elimina un elemento específico de un campo de cuadro de lista y guarda el documento actualizado.
---

Los campos de cuadro de lista en los PDF permiten a los usuarios seleccionar una o varias opciones predefinidas. Usando Aspose.PDF for Python, los desarrolladores pueden eliminar programáticamente elementos de estos campos.

Este artículo explica cómo eliminar el elemento 'UK' de un campo de cuadro de lista llamado 'Country', asegurando que el campo solo contenga las opciones deseadas.

El [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) La clase proporciona el método 'del_list_item' para eliminar un elemento específico de un campo de cuadro de lista.

1. Abra un formulario PDF existente.
1. Cree un objeto FormEditor.
1. Vincula el documento PDF al FormEditor.
1. Eliminar el elemento "UK" del campo de lista "Country".
1. Guarde el documento actualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def del_list_item(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Delete list item from list box field
    form_editor.del_list_item("Country", "UK")
    # Save updated document
    form_editor.save(outfile)
```


---
title: Establecer número de comb del campo
type: docs
weight: 70
url: /es/python-net/set-field-comb-number/
description: Este ejemplo muestra cómo establecer un número de comb para un campo de formulario PDF usando Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Establecer número de comb para campos de formulario PDF usando Python
Abstract: Con Aspose.PDF for Python, los desarrolladores pueden establecer programáticamente el número de casillas (número de comb) para un campo de formulario y forzar una entrada de longitud fija. Este artículo muestra cómo establecer el número de comb para un campo llamado "PIN".
---

El número de comb define cómo el contenido del campo se divide en casillas equidistantes, a menudo usado para códigos PIN, números de serie u otros campos de entrada de longitud fija. El código abre un PDF existente, establece el número de comb para un campo y guarda el documento modificado.

El [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) La clase proporciona el método ‘set_field_comb_number’ para definir el número de casillas (caracteres) en un campo de formulario.

1. Abra un formulario PDF existente.
1. Crea un objeto FormEditor.
1. Establece el número de comb de un campo llamado "PIN" a 5.
1. Guarde el documento actualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_comb_number(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field comb number to 5
    form_editor.set_field_comb_number("PIN", 5)

    # Save updated document
    form_editor.save(outfile)
```

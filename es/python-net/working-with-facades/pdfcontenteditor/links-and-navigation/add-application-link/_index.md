---
title: Agregar enlace de aplicación
type: docs
weight: 10
url: /es/python-net/add-application-link/
description: Este ejemplo enlaza un PDF de entrada, agrega un enlace de lanzamiento de aplicación en la primera página y guarda el documento modificado.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar un enlace de lanzamiento de aplicación a un PDF usando PdfContentEditor en Python
Abstract: Este ejemplo demuestra cómo agregar un enlace de lanzamiento de aplicación a un documento PDF usando Aspose.PDF for Python via the Facades API. Muestra cómo crear un área clicable que abre una aplicación especificada al hacer clic y guardar el PDF actualizado.
---

Los PDF pueden incluir elementos interactivos como enlaces que lanzan aplicaciones externas. Usando [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), puede definir una región rectangular en una página que, al hacer clic, abre un archivo ejecutable específico.

1. Cree una instancia de PdfContentEditor.
1. Enlace el documento PDF de entrada.
1. Defina un área rectangular para el enlace clicable.
1. Especifique la ruta de la aplicación a lanzar.
1. Establezca el color del enlace.
1. Guarde el documento PDF actualizado.

```python
import aspose.pdf.facades as pdf_facades
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as apd
import aspose.pdf as ap

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_application_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add application launch link
    content_editor.create_application_link(
        apd.Rectangle(180, 530, 260, 20),
        "notepad.exe",
        1,
        apd.Color.purple,
    )
    # Save updated document
    content_editor.save(outfile)
```

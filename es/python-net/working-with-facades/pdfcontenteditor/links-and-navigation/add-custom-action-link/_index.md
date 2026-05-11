---
title: Agregar enlace de acción personalizada
type: docs
weight: 20
url: /es/python-net/add-custom-action-link/
description: Este ejemplo enlaza un PDF de entrada, agrega un enlace de acción personalizada en la primera página y guarda el documento modificado. Se utiliza una lista de acciones vacía por simplicidad, pero las implementaciones reales pueden incluir acciones reales.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar un enlace de acción personalizada a un PDF usando PdfContentEditor en Python
Abstract: Este ejemplo muestra cómo agregar un enlace de acción personalizada a un documento PDF usando Aspose.PDF for Python via the Facades API. Demuestra cómo crear un área clicable en una página, asignar una acción personalizada y guardar el documento actualizado.
---

Los enlaces de acción personalizada le permiten definir áreas interactivas en un PDF que pueden desencadenar acciones específicas al hacer clic, como ejecutar scripts, navegar páginas o ejecutar comandos específicos de la aplicación. Usando [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), puede crear un enlace de acción personalizada especificando la página, el rectángulo, el color y las acciones.

1. Cree una instancia de PdfContentEditor.
1. Enlace el documento PDF de entrada.
1. Defina un rectángulo para el enlace clicable.
1. Especifique el número de página y el color del enlace.
1. Asigne acciones personalizadas (vacías en este ejemplo).
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


def add_custom_action_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add custom action link. Empty action list keeps the sample runnable
    # without requiring additional enum lookups.
    content_editor.create_custom_action_link(
        apd.Rectangle(200, 500, 260, 20),
        1,
        apd.Color.dark_red,
        [],
    )
    # Save updated document
    content_editor.save(outfile)
```

---
title: Agregar anotaciones emergentes
type: docs
weight: 40
url: /es/python-net/add-popup-annotation/
description: Este ejemplo carga un PDF, agrega una anotación emergente a la primera página y guarda el documento modificado. La anotación emergente está configurada para ser visible de forma predeterminada y muestra el texto de comentario especificado.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar anotaciones emergentes a un PDF usando Python
Abstract: Este ejemplo muestra cómo insertar una anotación emergente en un documento PDF usando Aspose.PDF for Python via the Facades API. Explica cómo definir el área de la anotación emergente, establecer el texto de la anotación, controlar la visibilidad y guardar el documento actualizado.
---

Las anotaciones emergentes son útiles para agregar comentarios, explicaciones o notas interactivas en archivos PDF. Usando [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), puedes crear anotaciones emergentes programáticamente especificando la ubicación, el contenido, la visibilidad y el número de página.

1. Crea el objeto PdfContentEditor.
1. Vincular el PDF de entrada.
1. Define el rectángulo de la anotación Popup.
1. Añade la anotación Popup.
1. Guardar el documento actualizado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_popup_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add popup annotation to page 1
    content_editor.create_popup(
        apd.Rectangle(220, 520, 180, 80),
        "This is a popup annotation",
        True,
        1,
    )
    # Save updated document
    content_editor.save(outfile)
```

---
title: Eliminar acción de apertura
linktitle: Eliminar acción de apertura
type: docs
weight: 30
url: /es/python-net/remove-open-action/
description: Este ejemplo carga un PDF existente, elimina la acción de apertura y guarda el documento limpio.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar la acción de apertura de documento de un PDF usando Python
Abstract: Este ejemplo muestra cómo eliminar una acción de apertura de documento de un PDF usando Aspose.PDF para Python a través de la API Facades. Muestra cómo enlazar un PDF, limpiar la acción de apertura y guardar el documento actualizado.
---

Los documentos PDF pueden contener acciones que se ejecutan automáticamente al abrir el archivo, como alertas de JavaScript, comandos de navegación u otros comportamientos. En algunos escenarios, es posible que necesite eliminar estas acciones por razones de seguridad, cumplimiento o experiencia del usuario.

Usando PdfContentEditor, puede eliminar fácilmente la acción de apertura del documento y garantizar que el PDF se abra sin ejecutar ningún comportamiento automático.

1. Crea el objeto PdfContentEditor.
1. Vincular el PDF de entrada.
1. Eliminar la acción de apertura del documento.
1. Guardar el documento actualizado.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_open_action(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Remove open action from the document
    content_editor.remove_document_open_action()
    # Save updated document
    content_editor.save(outfile)
```

---
title: Eliminar archivos adjuntos
linktitle: Eliminar archivos adjuntos
type: docs
weight: 50
url: /es/python-net/remove-attachments/
description: Este ejemplo vincula un PDF de entrada, elimina todos los archivos adjuntos y guarda el PDF modificado sin ningún archivo incrustado.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar todos los archivos adjuntos de un PDF usando Python
Abstract: Este ejemplo demuestra cómo eliminar todos los archivos adjuntos de un documento PDF usando Aspose.PDF for Python via the Facades API. Muestra cómo vincular un PDF, eliminar los adjuntos incrustados y guardar el documento actualizado.
---

Los PDFs pueden contener adjuntos como documentos, imágenes u otros archivos. Hay escenarios en los que necesita limpiar un PDF de todos los adjuntos por motivos de seguridad, privacidad o distribución. Usando [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), puede eliminar programáticamente todos los adjuntos incrustados en un documento.

1. Crea el objeto PdfContentEditor. 
1. Vincular el PDF de entrada.
1. Eliminar todos los adjuntos.
1. Guardar el documento actualizado.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_attachments(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Remove all attachments from document
    content_editor.delete_attachments()
    # Save updated document
    content_editor.save(outfile)
```

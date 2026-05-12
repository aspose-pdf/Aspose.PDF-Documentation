---
title: Obtener preferencias del visor PDF
linktitle: Obtener preferencias del visor PDF
type: docs
weight: 20
url: /es/python-net/get-viewer-preferences/
description: Cómo leer y modificar las preferencias del visor PDF programáticamente usando Aspose.PDF para Python
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Administrar las preferencias del visor PDF con Aspose.PDF en Python
Abstract: Esta guía muestra cómo leer y modificar las preferencias del visor PDF programáticamente usando Aspose.PDF para Python. Las preferencias del visor controlan cómo se muestra un PDF al abrirse en un visor PDF, como abrir con marcadores, ocultar barras de herramientas o usar un diseño de una sola página.
---

Aspose.PDF proporciona herramientas para acceder y actualizar las preferencias del visor PDF. Estas preferencias definen la disposición inicial y el comportamiento de presentación de un documento PDF en los lectores PDF. Esto incluye opciones como habilitar la vista de marcadores, ocultar barras de menús o especificar modos de diseño de página. Usando PdfContentEditor, puedes recuperar las preferencias existentes, verificar banderas específicas y actualizarlas según sea necesario.

1. Definir banderas de ViewerPreference.
1. Inicializar [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) y Vincular PDF.
1. Obtener las preferencias de ViewerPreference actuales.
1. Verificar banderas específicas.
1. Mostrar preferencias actuales.

```python
import aspose.pdf.facades as pdf_facades
import sys
from enum import IntFlag
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_viewer_preferences(infile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Read current viewer preference flags
    viewer_preference = ViewerPreference(content_editor.get_viewer_preference())
    if viewer_preference & ViewerPreference.PAGE_MODE_USE_OUTLINES:
        print("PageModeUseOutlines is enabled")
    print(f"Current viewer preference: {viewer_preference}")
```

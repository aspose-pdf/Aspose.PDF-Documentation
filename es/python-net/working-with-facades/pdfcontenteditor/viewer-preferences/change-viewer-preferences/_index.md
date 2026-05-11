---
title: Cambiar preferencias del visor PDF
type: docs
weight: 10
url: /es/python-net/change-viewer-preferences/
description: Este módulo demuestra cómo ajustar la configuración del visor de un documento PDF usando Aspose.PDF for Python.
lastmod: "2026-03-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Personalizar la experiencia del visor PDF con Python
Abstract: Controla cómo se muestra tu documento PDF al abrirse modificando programáticamente las preferencias del visor. Esta funcionalidad te permite adaptar la interfaz de usuario y el diseño, garantizando una experiencia de visualización coherente.
---

Los archivos PDF tienen preferencias de visor incorporadas que controlan aspectos como la disposición de página, la visibilidad de la barra de herramientas y el comportamiento de la ventana. Con este script, puedes:

- Inspeccionar las preferencias actuales del visor de un PDF.
- Modificar opciones de diseño (p. ej., una página, una columna, dos columnas).
- Alternar elementos de la interfaz de usuario, como barra de herramientas, barra de menús o visualización del título.
- Guardar el PDF con las preferencias actualizadas para una experiencia de visualización controlada.

1. Definir banderas de ViewerPreference.
1. Obtener las preferencias de ViewerPreference actuales.
1. Modificar preferencias.
1. Aplicar Preferencias Actualizadas.
1. Guarda el PDF.

```python
import aspose.pdf.facades as pdf_facades
import sys
from enum import IntFlag
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Define ViewerPreference flags
class ViewerPreference(IntFlag):
    HIDE_TOOLBAR = 1
    HIDE_MENUBAR = 2
    HIDE_WINDOW_UI = 4
    FIT_WINDOW = 8
    CENTER_WINDOW = 16
    DISPLAY_DOC_TITLE = 32
    NON_FULL_SCREEN_PAGE_MODE_USE_NONE = 64
    NON_FULL_SCREEN_PAGE_MODE_USE_OUTLINES = 128
    NON_FULL_SCREEN_PAGE_MODE_USE_THUMBS = 256
    NON_FULL_SCREEN_PAGE_MODE_USE_OC = 512
    DIRECTION_L2R = 1024
    DISPLAY_DOC_TITLE_IN_TITLE_BAR = 2048
    PAGE_LAYOUT_SINGLE_PAGE = 4096
    PAGE_LAYOUT_ONE_COLUMN = 8192
    PAGE_LAYOUT_TWO_COLUMN_LEFT = 16384
    PAGE_LAYOUT_TWO_COLUMN_RIGHT = 32768
    PAGE_LAYOUT_TWO_PAGE_LEFT = 65536
    PAGE_LAYOUT_TWO_PAGE_RIGHT = 131072


def change_viewer_preferences(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    # Get current viewer preference and toggle single-page layout
    current_preference = ViewerPreference(content_editor.get_viewer_preference())
    updated_preference = current_preference | ViewerPreference.PAGE_LAYOUT_SINGLE_PAGE
    content_editor.change_viewer_preference(int(updated_preference))

    # Save updated document
    content_editor.save(outfile)
```

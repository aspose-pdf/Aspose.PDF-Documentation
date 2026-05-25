---
title: Alterar Preferências de Exibição do PDF
type: docs
weight: 10
url: /pt/python-net/change-viewer-preferences/
description: Este módulo demonstra como ajustar as configurações de exibição de um documento PDF usando o Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Personalize a Experiência de Exibição de PDF com Python
Abstract: Controle como seu documento PDF aparece ao ser aberto, modificando as preferências de exibição programaticamente. Essa funcionalidade permite personalizar a interface do usuário e o layout, garantindo uma experiência de visualização consistente.
---

Os arquivos PDF possuem preferências de exibição integradas que controlam aspectos como layout da página, visibilidade da barra de ferramentas e comportamento da janela. Usando este script, você pode:

- Inspecionar as preferências de exibição atuais de um PDF.
- Modificar opções de layout (por exemplo, página única, uma coluna, duas colunas).
- Alternar elementos da interface do usuário, como barra de ferramentas, barra de menus ou exibição de título.
- Salvar o PDF com as preferências atualizadas para uma experiência de visualização controlada.

1. Definir sinalizadores de ViewerPreference.
1. Obter as preferências de visualização atuais.
1. Modificar preferências.
1. Aplicar Preferências Atualizadas.
1. Salvar o PDF.

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

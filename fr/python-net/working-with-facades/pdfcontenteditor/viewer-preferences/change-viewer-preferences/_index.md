---
title: Modifier les préférences du visualiseur PDF
type: docs
weight: 10
url: /fr/python-net/change-viewer-preferences/
description: Ce module montre comment ajuster les paramètres du visualiseur d’un document PDF en utilisant Aspose.PDF for Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Personnaliser l’expérience du visualiseur PDF avec Python
Abstract: Contrôlez la façon dont votre document PDF apparaît lorsqu’il est ouvert en modifiant les préférences du visualiseur de manière programmatique. Cette fonctionnalité vous permet d’adapter l’interface utilisateur et la mise en page, garantissant une expérience de visualisation cohérente.
---

Les fichiers PDF possèdent des préférences de visualiseur intégrées qui contrôlent des aspects tels que la mise en page, la visibilité de la barre d’outils et le comportement de la fenêtre. En utilisant ce script, vous pouvez :

- Inspectez les préférences actuelles du visualiseur d’un PDF.
- Modifier les options de mise en page (par exemple, page unique, une colonne, deux colonnes).
- Basculer les éléments de l’interface utilisateur tels que la barre d’outils, la barre de menus ou l’affichage du titre.
- Enregistrez le PDF avec les préférences mises à jour pour une expérience de visualisation contrôlée.

1. Définir les indicateurs ViewerPreference.
1. Obtenir les Viewer Preferences actuelles.
1. Modifier les préférences.
1. Appliquer les préférences mises à jour.
1. Enregistrer le PDF.

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

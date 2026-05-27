---
title: Obtenir les préférences du visualiseur PDF
type: docs
weight: 20
url: /fr/python-net/get-viewer-preferences/
description: Comment lire et modifier les préférences du visualiseur PDF programmétiquement à l'aide d'Aspose.PDF for Python
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gérer les préférences du visualiseur PDF avec Aspose.PDF en Python
Abstract: Ce guide montre comment lire et modifier les préférences du visualiseur PDF programmétiquement à l'aide d'Aspose.PDF for Python. Les préférences du visualiseur contrôlent la façon dont un PDF est affiché lorsqu'il est ouvert dans un visualiseur PDF, par exemple en s'ouvrant avec le plan, en masquant les barres d'outils ou en utilisant une mise en page mono-page.
---

Aspose.PDF fournit des outils pour accéder et mettre à jour les préférences du visualiseur PDF. Ces préférences définissent la disposition initiale et le comportement de présentation d'un document PDF dans les lecteurs PDF. Cela comprend des options telles que l'activation de la vue plan, le masquage des barres de menus ou la spécification des modes de mise en page. En utilisant PdfContentEditor, vous pouvez récupérer les préférences existantes, vérifier des indicateurs spécifiques et les mettre à jour si nécessaire.

1. Définir les indicateurs ViewerPreference.
1. Initialiser [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) et lier le PDF.
1. Obtenir les préférences actuelles du visualiseur.
1. Vérifier les indicateurs spécifiques.
1. Afficher les préférences actuelles.

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

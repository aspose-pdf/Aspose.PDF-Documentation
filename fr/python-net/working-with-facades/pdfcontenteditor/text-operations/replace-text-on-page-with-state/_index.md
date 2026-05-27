---
title: Remplacer le texte sur la page avec l’état
type: docs
weight: 20
url: /fr/python-net/replace-text-on-page-with-state/
description: Dans cet exemple, toutes les occurrences du mot "software" sur la page 1 sont remplacées par "SOFTWARE PAGE 1", en utilisant du texte rouge avec une taille de police de 12.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remplacer du texte avec un formatage personnalisé sur une page spécifique en utilisant PdfContentEditor en Python
Abstract: Cet exemple montre comment remplacer du texte sur une page spécifique dans un PDF tout en appliquant un formatage personnalisé en utilisant Aspose.PDF for Python via l'API Facades. Il montre comment contrôler la taille de police et la couleur lors du remplacement du texte.
---

Parfois, remplacer du texte dans un PDF nécessite également des changements de formatage tels que la couleur ou la taille de police. En utilisant TextState, vous pouvez définir des propriétés de style et les appliquer lors du remplacement. Cela vous permet de mettre en évidence le texte modifié ou d'imposer un formatage cohérent à travers les documents.

1. Créer un [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instance.
1. Lier le document PDF d'entrée.
1. Définissez un TextState avec un formatage personnalisé.
1. Configurez la stratégie de remplacement.
1. Remplacez le texte sur une page spécifique.
1. Enregistrer le document PDF mis à jour.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_on_page_with_state(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.red
    text_state.font_size = 12

    # Replace text on a specific page with explicit text formatting
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text("software", 1, "SOFTWARE PAGE 1", text_state)
    # Save updated document
    content_editor.save(outfile)
```

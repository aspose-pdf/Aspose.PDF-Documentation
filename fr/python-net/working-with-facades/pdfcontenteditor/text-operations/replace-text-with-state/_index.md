---
title: Remplacer le texte avec état
type: docs
weight: 50
url: /fr/python-net/replace-text-with-state/
description: Dans cet exemple, toutes les occurrences de "software" sont remplacées par "SOFTWARE" et formatées en bleu avec une taille de police de 14.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remplacer le texte avec un format personnalisé dans un PDF à l'aide de PdfContentEditor en Python
Abstract: Cet exemple montre comment remplacer du texte dans un document PDF tout en appliquant un format personnalisé à l'aide d'Aspose.PDF for Python via l'API Facades. Il montre comment contrôler la couleur du texte et la taille de la police lors du remplacement.
---

Lors de la mise à jour du texte dans un PDF, vous pouvez souhaiter que le contenu remplacé se démarque. En utilisant un objet TextState, vous pouvez définir le style tel que la couleur et la taille de la police, puis l'appliquer à tout le texte remplacé.

1. Créer un [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)  instance.
1. Liez le document PDF d'entrée.
1. Définissez un TextState avec un formatage personnalisé.
1. Configurez la portée du remplacement.
1. Remplacez le texte dans l'ensemble du document.
1. Enregistrez le document PDF mis à jour.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_with_state(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.blue
    text_state.font_size = 14

    # Replace text with explicit text formatting
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text("software", "SOFTWARE", text_state)
    # Save updated document
    content_editor.save(outfile)
```

---
title: Remplacer le texte sur la page
type: docs
weight: 10
url: /fr/python-net/replace-text-on-page/
description: Dans cet exemple, la première occurrence du mot "PDF" est remplacée par "Page 1 Replaced Text" en utilisant une taille de police spécifiée.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remplacer le texte sur une page spécifique en utilisant PdfContentEditor en Python
Abstract: Cet exemple montre comment remplacer du texte dans un document PDF en utilisant Aspose.PDF for Python via l'API Facades. Il montre comment remplacer la première occurrence de texte sur une page et enregistrer le document mis à jour.
---

Le remplacement de texte est une exigence courante lors de la mise à jour de documents PDF. En utilisant [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), vous pouvez rechercher un texte spécifique et le remplacer par un nouveau contenu. La propriété ‘replace_text_strategy’ vous permet de contrôler le nombre d'occurrences remplacées.

1. Créer une instance de PdfContentEditor.
1. Lier le document PDF d'entrée.
1. Configurer la stratégie de remplacement de texte.
1. Remplacer le texte cible.
1. Enregistrer le document PDF mis à jour.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_on_page(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace text on page 1
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_FIRST
    )
    content_editor.replace_text("PDF", "Page 1 Replaced Text", 14)
    # Save updated document
    content_editor.save(outfile)
```

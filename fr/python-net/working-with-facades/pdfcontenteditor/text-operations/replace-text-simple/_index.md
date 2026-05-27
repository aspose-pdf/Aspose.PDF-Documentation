---
title: Remplacer le texte simple
type: docs
weight: 40
url: /fr/python-net/replace-text-simple/
description: Dans cet exemple, toutes les occurrences de "33" sont remplacées par "XXXIII " dans l'ensemble du document. Cela montre un remplacement simple de chaîne sans mise en forme personnalisée ni expression régulière.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remplacer du texte dans un PDF à l'aide de PdfContentEditor en Python
Abstract: Cet exemple montre comment remplacer du texte dans l'ensemble d'un document PDF à l'aide d'Aspose.PDF for Python via l'API Facades. Il remplace toutes les occurrences d'une chaîne spécifiée par un nouveau texte.
---

Le remplacement simple de texte est utile lors de la mise à jour de valeurs répétées dans un document. Avec [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), vous pouvez définir une portée de remplacement et substituer le texte globalement sur toutes les pages.

1. Créer un [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instance.
1. Lier le document PDF d'entrée.
1. Configurez la portée du remplacement pour toutes les occurrences.
1. Remplacer le texte cible.
1. Enregistrer le document PDF mis à jour.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_simple(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace text in the whole document
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text("33", "XXXIII ")
    # Save updated document
    content_editor.save(outfile)
```

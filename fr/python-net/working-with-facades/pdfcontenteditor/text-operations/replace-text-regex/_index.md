---
title: Remplacer le texte Regex
type: docs
weight: 30
url: /fr/python-net/replace-text-regex/
description: Dans cet exemple, tous les nombres à quatre chiffres du document sont remplacés par le texte de substitution "[NUMBER]". Cela est utile pour masquer des données sensibles, normaliser le contenu ou anonymiser les documents.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remplacer du texte à l'aide d'expressions régulières avec PdfContentEditor en Python
Abstract: Cet exemple montre comment remplacer du texte dans un PDF en utilisant des expressions régulières avec Aspose.PDF for Python via l'API Facades. Il montre comment rechercher des motifs et remplacer toutes les correspondances dans l'ensemble du document.
---

Les expressions régulières permettent un remplacement flexible du texte basé sur des motifs plutôt que sur des chaînes fixes. En activant la prise en charge des regex dans 'replace_text_strategy', vous pouvez faire correspondre du contenu dynamique tel que les nombres, les dates ou les chaînes formatées.

1. Créer un [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instance.
1. Lier le document PDF d'entrée.
1. Configurer la stratégie de remplacement pour utiliser les regex.
1. Remplacez les modèles correspondants dans l'ensemble du document.
1. Enregistrer le document PDF mis à jour.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_regex(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace text in the whole document
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text_strategy.is_regular_expression_used = True
    content_editor.replace_text(r"\d{4}", "[NUMBER]")
    # Save updated document
    content_editor.save(outfile)
```

---
title: Supprimer l'action d'ouverture
type: docs
weight: 30
url: /fr/python-net/remove-open-action/
description: Cet exemple charge un PDF existant, supprime l'action d'ouverture et enregistre le document nettoyé.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Supprimer l'action d'ouverture du document d'un PDF à l'aide de Python
Abstract: Cet exemple montre comment supprimer une action d'ouverture de document d'un PDF en utilisant Aspose.PDF for Python via the Facades API. Il montre comment lier un PDF, effacer l'action d'ouverture et enregistrer le document mis à jour.
---

Les documents PDF peuvent contenir des actions qui s'exécutent automatiquement lorsque le fichier est ouvert, telles que des alertes JavaScript, des commandes de navigation ou d'autres comportements. Dans certains scénarios, il peut être nécessaire de supprimer ces actions pour des raisons de sécurité, de conformité ou d'expérience utilisateur.

En utilisant PdfContentEditor, vous pouvez facilement supprimer l'action d'ouverture du document et garantir que le PDF s'ouvre sans exécuter aucun comportement automatique.

1. Créer l'objet PdfContentEditor.
1. Lier le PDF d'entrée.
1. Supprimer l'action d'ouverture du document.
1. Enregistrer le Document mis à jour.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_open_action(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Remove open action from the document
    content_editor.remove_document_open_action()
    # Save updated document
    content_editor.save(outfile)
```

---
title: Supprimer le champ
type: docs
weight: 60
url: /fr/python-net/remove-field/
description: Cet exemple montre comment supprimer le champ 'Country' d'un formulaire PDF en utilisant la méthode 'remove_field' de la classe 'FormEditor'.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Supprimer un champ de formulaire d'un document PDF en utilisant Python
Abstract: Cet exemple démontre comment supprimer un champ de formulaire existant d'un document PDF en utilisant Aspose.PDF for Python. Le code charge un fichier PDF, supprime le champ spécifié en utilisant la classe FormEditor, et enregistre le document mis à jour.
---

Les formulaires PDF peuvent contenir des champs qui ne sont plus nécessaires en raison de modifications de conception ou de mises à jour du flux de travail. Avec Aspose.PDF for Python, les développeurs peuvent facilement supprimer des champs de formulaire spécifiques par programme.

Le [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) La classe dans Aspose.PDF fournit la méthode 'remove_field', qui permet aux développeurs de supprimer un champ de formulaire par son nom.

1. Chargez le document PDF.
1. Créer un objet FormEditor.
1. Lier le PDF au FormEditor.
1. Supprimez le champ de formulaire spécifié.
1. Enregistrez le document mis à jour.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Remove field from document
    form_editor.remove_field("Country")
    # Save updated document
    form_editor.save(outfile)
```

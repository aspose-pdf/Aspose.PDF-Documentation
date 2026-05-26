---
title: Renommer le champ
type: docs
weight: 70
url: /fr/python-net/rename-field/
description: Renommer un champ de formulaire existant dans un document PDF à l'aide d'Aspose.PDF pour Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Renommer un champ de formulaire PDF en utilisant Python
Abstract: Cet exemple montre comment renommer un champ de formulaire existant dans un document PDF à l'aide d'Aspose.PDF pour Python. Le code ouvre un PDF d'entrée, modifie le nom d'un champ de formulaire spécifié en utilisant la classe FormEditor, et enregistre le document mis à jour.
---

Les formulaires PDF reposent souvent sur les noms de champs pour le scripting, l'automatisation et le traitement des données. En utilisant Aspose.PDF pour Python, les développeurs peuvent renommer des champs existants sans les recréer ni modifier la mise en page du formulaire.

Le [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) La classe fournit la méthode ‘rename_field’, qui permet aux développeurs de changer le nom d'un champ existant tout en préservant sa position, sa valeur et son apparence.

1. Chargez le formulaire PDF existant.
1. Créez une instance de FormEditor.
1. Liez le document PDF à l'éditeur.
1. Renommez le champ cible.
1. Enregistrez le PDF mis à jour.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def rename_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Rename field in document
    form_editor.rename_field("City", "Town")
    # Save updated document
    form_editor.save(outfile)
```


---
title: Champ à ligne unique vers champ à plusieurs lignes
type: docs
weight: 80
url: /fr/python-net/single-to-multiple/
description: Convertir un champ de texte à ligne simple en champ à plusieurs lignes dans un document PDF à l'aide d'Aspose.PDF for Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Convertir un champ de texte à ligne simple en champ à plusieurs lignes dans un PDF en utilisant Python
Abstract: Cet exemple montre comment convertir un champ de texte à ligne simple en champ à plusieurs lignes dans un document PDF à l'aide d'Aspose.PDF for Python. Le code charge un formulaire PDF existant, modifie le champ spécifié pour autoriser plusieurs lignes de texte, puis enregistre le document mis à jour.
---

Les formulaires PDF contiennent parfois des champs de texte conçus pour une entrée à ligne unique, ce qui peut ne pas être suffisant pour certains types de données. Avec Aspose.PDF for Python, les développeurs peuvent facilement convertir ces champs en champs de texte à plusieurs lignes sans les recréer.

En utilisant le [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) class, les développeurs peuvent modifier les champs de texte existants sans affecter leur position ni leurs autres propriétés.

1. Chargez le document PDF existant.
1. Créez une instance de FormEditor.
1. Liez le document PDF à l'éditeur.
1. Convertissez le champ sélectionné en plusieurs lignes.
1. Enregistrez le document mis à jour.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def single2multiple(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Change a single-lined text field to a multiple-lined one
    form_editor.single_2_multiple("City")
    # Save updated document
    form_editor.save(outfile)
```


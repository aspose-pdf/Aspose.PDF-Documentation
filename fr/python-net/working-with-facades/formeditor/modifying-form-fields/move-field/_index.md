---
title: Déplacer le champ
type: docs
weight: 50
url: /fr/python-net/move-field/
description: Déplacer un champ de formulaire existant vers une position différente dans un document PDF.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Déplacer un champ de formulaire PDF vers une nouvelle position à l'aide de Python
Abstract: Cet exemple montre comment déplacer un champ de formulaire existant vers une position différente dans un document PDF en utilisant Aspose.PDF for Python. Le code ouvre un PDF existant, déplace le champ de formulaire spécifié vers de nouvelles coordonnées et enregistre le document mis à jour.
---

Les formulaires PDF nécessitent souvent des ajustements de mise en page après leur création. En utilisant Aspose.PDF for Python, les développeurs peuvent déplacer des champs de formulaire existants vers une nouvelle position sans les recréer.

Cet exemple montre comment repositionner le champ \u0022Country\u0022 en spécifiant de nouvelles coordonnées pour son placement dans la page. Le [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) La classe fournit la méthode move_field pour repositionner les champs au sein d'une page PDF.

1. Ouvrez le formulaire PDF existant.
1. Créer un objet FormEditor.
1. Liez le document PDF au FormEditor.
1. Déplacez le champ 'Country' vers une nouvelle position en utilisant des coordonnées.
1. Enregistrez le document modifié.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def move_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Move field to new page
    form_editor.move_field("Country", 200, 600, 280, 620)
    # Save updated document
    form_editor.save(outfile)
```

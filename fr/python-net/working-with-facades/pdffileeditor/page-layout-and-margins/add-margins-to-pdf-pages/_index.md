---
title: Ajouter des marges aux pages PDF
type: docs
weight: 10
url: /fr/python-net/add-margins-to-pdf-pages/
description: Ajouter des marges personnalisées aux pages sélectionnées d'un PDF à l'aide d'Aspose.PDF for Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter des marges personnalisées à des pages PDF spécifiques en Python
Abstract: Apprenez comment ajouter des marges personnalisées aux pages sélectionnées d'un PDF à l'aide d'Aspose.PDF for Python. Cet exemple montre comment étendre les limites des pages en spécifiant les marges supérieure, inférieure, gauche et droite pour chaque page, rendant les PDF plus imprimables ou visuellement cohérents.
---

L'ajout de marges aux pages PDF peut améliorer la lisibilité, préparer les documents pour l'impression ou allouer de l'espace pour les annotations. En utilisant Aspose.PDF for Python, les développeurs peuvent ajouter programmétiquement des marges à des pages spécifiques d'un PDF sans modifier la disposition du contenu.

Dans cet extrait de code, le [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) class est utilisé pour ajouter des marges de 0,5 pouce aux pages 1 et 3 du document d'entrée. Les marges sont définies en points (1 pouce = 72 points) et appliquées individuellement à la gauche, à la droite, en haut et en bas de chaque page.

1. Ouvrez le document PDF source.
1. Créez une instance de 'PdfFileEditor'.
1. Définissez les marges et les pages à modifier.
1. Appliquez les marges en utilisant la méthode 'add_margins'.
1. Enregistrez le PDF mis à jour dans le fichier de sortie.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Add Margins to PDF Pages
def add_margins_to_pdf_pages(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    # Define the margins to be added (in points)
    left_margin = 36  # 0.5 inch
    right_margin = 36  # 0.5 inch
    top_margin = 36  # 0.5 inch
    bottom_margin = 36  # 0.5 inch

    pdf_editor.add_margins(
        infile, outfile, [1, 3], left_margin, right_margin, top_margin, bottom_margin
    )
```

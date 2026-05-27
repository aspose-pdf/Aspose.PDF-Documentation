---
title: Obtenir le décalage de la page
type: docs
weight: 20
url: /fr/python-net/get-page-offset/
description: Cet exemple montre comment utiliser PdfFileInfo pour obtenir les décalages X et Y d'une page spécifique et les convertir en pouces afin d'effectuer une analyse précise de la mise en page et du positionnement.
lastmod: "2026-05-22"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Obtenir les décalages de pages PDF avec Python
Abstract: La fonction 'get_page_offsets' extrait les décalages horizontaux (X) et verticaux (Y) de chaque page d'un fichier PDF. Ces décalages représentent la position du contenu de la page par rapport à l'origine du PDF. En convertissant les points en pouces, la fonction fournit des mesures précises et lisibles qui peuvent être utilisées pour placer avec exactitude des annotations, des images ou du texte. Elle prend en charge les PDF multi‑pages et est destinée aux développeurs travaillant sur la mise en page PDF, l'automatisation ou les tâches d'alignement de contenu.
---

La fonction 'get_page_offsets' fournit aux développeurs les décalages horizontaux (X) et verticaux (Y) exacts des pages d'un fichier PDF. Dans les documents PDF, chaque page peut avoir un point d'origine interne différent du coin supérieur gauche de la page, ce qui peut affecter le positionnement du texte, des images, des annotations ou d'autres contenus.

En utilisant les façades Aspose.PDF, cette fonction extrait ces décalages en points et les convertit en pouces pour une interprétation aisée. Elle prend en charge les PDF multi-pages, ce qui la rend adaptée aux flux de travail automatisés nécessitant un placement précis du contenu.

1. Créez l'objet façade PDF.
1. Obtenez le nombre de pages dans le PDF.
1. Parcourez chaque page pour obtenir les décalages.
1. Imprimez ou stockez les décalages.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_page_offsets(infile):
    # Get and display PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)
    page_x_offset = pdf_info.get_page_x_offset(1) / 72.0
    page_y_offset = pdf_info.get_page_y_offset(1) / 72.0
    print(f"Page X Offset: {page_x_offset} inches")
    print(f"Page Y Offset: {page_y_offset} inches")
```

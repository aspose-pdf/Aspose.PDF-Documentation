---
title: Obtenir les informations de la page
type: docs
weight: 10
url: /fr/python-net/get-page-info/
description: Apprenez comment accéder programmatique aux informations au niveau de la page dans un PDF en utilisant Aspose.PDF pour Python. Ce guide montre comment récupérer la largeur, la hauteur, la rotation et les décalages d’une page spécifique dans un document PDF.
lastmod: "2026-05-22"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Obtenir les informations de page PDF à l’aide d’Aspose.PDF pour Python
Abstract: La fonction extrait la largeur, la hauteur, la rotation ainsi que les décalages horizontaux (X) et verticaux (Y) d’une page PDF. Ces propriétés sont renvoyées en points et reflètent la taille physique de la page ainsi que le positionnement du contenu dans le PDF. La fonction affiche les valeurs récupérées, permettant aux développeurs de comprendre la mise en page et l’orientation de la page pour de futures manipulations de PDF.
---

La fonction utilitaire « get_page_information » aide les développeurs à comprendre la structure et la mise en page des pages PDF. Chaque page PDF peut avoir des dimensions, une rotation et des décalages internes différents, ce qui peut affecter le placement du contenu ou les tâches d’automatisation.

Il permet de récupérer les métadonnées clés et les informations de mise en page pour une page spécifique d’un fichier PDF. L’API Aspose.PDF Facades fournit des détails tels que la largeur, la hauteur, la rotation de la page et les décalages X/Y. Ces informations sont essentielles pour des tâches telles que l’analyse de la mise en page, le placement d’annotations ou le traitement automatisé de PDF.

1. Créer un objet façade PDF.
1. Récupérer les dimensions et la mise en page de la page.
1. Afficher ou stocker les valeurs récupérées.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_page_information(infile):

    # Get and display PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)
    page_width = pdf_info.get_page_width(1)
    page_height = pdf_info.get_page_height(1)
    page_rotation = pdf_info.get_page_rotation(1)
    page_x_offset = pdf_info.get_page_x_offset(1)
    page_y_offset = pdf_info.get_page_y_offset(1)

    print(f"Page Width: {page_width}")
    print(f"Page Height: {page_height}")
    print(f"Page Rotation: {page_rotation}")
```

---
title: Déplacer le tampon par index
type: docs
weight: 90
url: /fr/python-net/move-stamp-by-index/
description: Comment repositionner les annotations de tampon en caoutchouc dans un PDF en utilisant leur index sur une page avec Aspose.PDF for Python
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Déplacer les tampons en caoutchouc dans un PDF en utilisant le positionnement basé sur l'index
Abstract: Cet exemple montre comment repositionner les annotations de tampon en caoutchouc dans un PDF en utilisant leur index sur une page avec Aspose.PDF for Python via l'API Facades. Il met en évidence la création de plusieurs tampons et leur préparation aux opérations de déplacement.
---

Lors de l'édition de PDF, il peut être nécessaire d'ajuster la position des tampons en caoutchouc existants. Cet extrait de code montre comment :

- Ajouter plusieurs tampons sur la même page
- Préparez-les pour le repositionnement en utilisant leur index
- Déplacez éventuellement un tampon en spécifiant sa page, son index et ses nouvelles coordonnées

La méthode 'move_stamp(page_number, stamp_index, new_x, new_y)' peut repositionner les tampons avec précision.

1. Créer un [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) objet.
1. Liez le PDF à l'éditeur.
1. Ajoutez plusieurs tampons en caoutchouc à une page.
1. Enregistrez le document avant d'effectuer des opérations de déplacement.
1. Déplacez un tampon spécifique par son indice.
1. Enregistrez le PDF mis à jour.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def move_stamp_by_index(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    content_editor.create_rubber_stamp(
        2,
        apd.Rectangle(200, 380, 180, 60),
        "Draft",
        "Draft stamp for ID-based operations",
        apd.Color.orange,
    )

    content_editor.create_rubber_stamp(
        2,
        apd.Rectangle(200, 480, 180, 60),
        "Draft",
        "Draft stamp for ID-based operations",
        apd.Color.orange,
    )
    content_editor.save(outfile)

    # Move first stamp on page 1 by index
    # content_editor.move_stamp(1, 1, 10, 10)
    # Save updated document
    content_editor.save(outfile)
```    

---
title: Ajouter une annotation de polygone
type: docs
weight: 40
url: /fr/python-net/add-polygon-annotation/
description: Cet exemple lie un PDF d'entrée, dessine un polygone plein sur la première page et enregistre le document modifié avec une annotation.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter une annotation de polygone à un PDF en utilisant PdfContentEditor en Python
Abstract: Cet exemple montre comment ajouter une annotation de polygone à un document PDF en utilisant Aspose.PDF for Python via le Facades API. Il montre comment définir les sommets du polygone, le style de bordure, les limites de l'annotation, le texte descriptif, et enregistrer le document mis à jour.
---

Les annotations de polygone sont utilisées pour mettre en valeur des zones ou formes irrégulières dans un PDF, offrant une emphase visuelle ou marquant des régions spécifiques. En utilisant [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), vous pouvez créer des polygones en spécifiant les coordonnées des sommets, le style de bordure, le numéro de page et le rectangle d'annotation.

1. Créer l'objet PdfContentEditor.
1. Lier le PDF d'entrée.
1. Configurer les propriétés du Polygon.
1. Ajouter l'annotation Polygon.
1. Enregistrer le Document mis à jour.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_polygon_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    line_info = pdf_facades.LineInfo()
    line_info.border_style = 0  # 0 - Solid
    line_info.vertice_coordinate = [100, 200, 150, 260, 220, 220, 200, 160]
    content_editor.create_polygon(
        line_info,
        1,
        apd.Rectangle(90, 150, 150, 120),
        "This is polygon annotation",
    )

    # Save output PDF file
    content_editor.save(outfile)
```

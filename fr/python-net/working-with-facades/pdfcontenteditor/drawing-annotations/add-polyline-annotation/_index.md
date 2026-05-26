---
title: Ajouter une Annotation de Polyligne
type: docs
weight: 50
url: /fr/python-net/add-polyline-annotation/
description: L'exemple lie un PDF d'entrée, crée une polyligne solide sur la première page et enregistre le document modifié avec une annotation.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter une Annotation de Polyligne à un PDF en utilisant PdfContentEditor en Python
Abstract: Cet exemple montre comment ajouter une annotation de polyligne à un document PDF en utilisant Aspose.PDF for Python via l'API Facades. Il montre comment définir une séquence de sommets, le style de bordure, le rectangle d'annotation, le texte, et enregistrer le document mis à jour.
---

Les annotations de polyligne vous permettent de mettre en évidence une série de segments de ligne connectés dans un PDF. En utilisant [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), vous pouvez dessiner une polyligne en spécifiant les coordonnées des sommets, le style de bordure, le numéro de page et les limites de l'annotation. Ceci est utile pour représenter visuellement des chemins, des tendances ou des connexions dans des diagrammes et des documents.

1. Créer l'objet PdfContentEditor.
1. Lier le PDF d'entrée.
1. Configurer les propriétés du polyligne.
1. Ajouter l'annotation du polyligne.
1. Enregistrer le Document mis à jour.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_polyline_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    line_info = pdf_facades.LineInfo()
    line_info.border_style = 0  # 0 - Solid
    line_info.vertice_coordinate = [120, 420, 180, 460, 230, 430, 290, 470]
    content_editor.create_poly_line(
        line_info,
        1,
        apd.Rectangle(110, 410, 200, 90),
        "This is polyline annotation",
    )

    # Save output PDF file
    content_editor.save(outfile)
```

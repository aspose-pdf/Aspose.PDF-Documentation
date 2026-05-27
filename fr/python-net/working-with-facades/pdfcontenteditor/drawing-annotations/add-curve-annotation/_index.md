---
title: Ajouter une annotation de courbe
type: docs
weight: 20
url: /fr/python-net/add-curve-annotation/
description: Cet exemple lie un PDF d'entrée, dessine une courbe pointillée sur la première page et enregistre le document modifié.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter une annotation de courbe à un PDF à l'aide de PdfContentEditor en Python
Abstract: Cet exemple montre comment ajouter une annotation de courbe à un document PDF en utilisant Aspose.PDF for Python via l'API Facades. Il montre comment définir les sommets de la courbe, le style de bordure, les limites de l'annotation, le contenu du texte, et enregistrer le document mis à jour.
---

Les annotations de courbe sont utilisées pour mettre en évidence des chemins ou des formes irréguliers dans un PDF, offrant un accent visuel ou marquant des zones importantes. En utilisant [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), vous pouvez dessiner des courbes en spécifiant une séquence de sommets, le style de bordure, la visibilité, le rectangle de l'annotation et le texte descriptif.

1. Créer l'objet PdfContentEditor.
1. Lier le PDF onput.
1. Configurer les propriétés de la courbe.
1. Dessiner l'annotation de la courbe.
1. Enregistrer le Document mis à jour.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_curve_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    line_info = pdf_facades.LineInfo()
    line_info.border_style = 1  # 1 - Dashed
    line_info.vertice_coordinate = [120, 520, 160, 560, 220, 540, 280, 580]
    line_info.visibility = True
    content_editor.draw_curve(
        line_info,
        1,
        apd.Rectangle(110, 510, 220, 100),
        "This is curve annotation",
    )

    # Save output PDF file
    content_editor.save(outfile)
```

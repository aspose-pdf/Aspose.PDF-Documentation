---
title: Ajouter une annotation circulaire
type: docs
weight: 10
url: /fr/python-net/add-circle-annotation/
description: Cet exemple lie un PDF d'entrée, crée une annotation circulaire sur la première page et enregistre le document modifié.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter une annotation circulaire à un PDF en utilisant PdfContentEditor en Python
Abstract: Cet exemple montre comment ajouter une annotation circulaire à un document PDF en utilisant Aspose.PDF for Python via l'API Facades. Il montre comment définir les limites de l'annotation, définir le texte du contenu, configurer la couleur et l'apparence, et enregistrer le document mis à jour.
---

Les annotations circulaires sont utiles pour mettre en évidence des zones d'intérêt dans un document PDF. Avec [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), vous pouvez créer des formes circulaires en spécifiant le rectangle qui définit les limites du cercle, ainsi que le texte de l'annotation, la couleur, les options de remplissage, le numéro de page et la largeur de la bordure.

1. Créer l'objet PdfContentEditor.
1. Lier le PDF d'entrée.
1. Définir les limites du cercle.
1. Ajouter l'annotation du cercle.
1. Enregistrer le Document mis à jour.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_circle_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    # Create CircleAnnotation object
    rect = apd.Rectangle(300, 300, 400, 400)
    contents = "This is circle annotation"
    content_editor.create_square_circle(rect, contents, apd.Color.blue, False, 1, 3)

    # Save output PDF file
    content_editor.save(outfile)
```

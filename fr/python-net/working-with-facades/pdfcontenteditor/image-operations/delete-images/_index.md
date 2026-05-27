---
title: Supprimer les images du PDF
type: docs
weight: 20
url: /fr/python-net/delete-images/
description:
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Supprimer des images spécifiques d’une page PDF à l’aide de PdfContentEditor en Python
Abstract: Cet exemple montre comment supprimer des images spécifiques d’un document PDF en utilisant Aspose.PDF for Python via the Facades API. Il montre comment cibler les images sur une page spécifique et enregistrer le document mis à jour.
---

Parfois, vous pouvez vouloir supprimer uniquement certaines images d’un PDF plutôt que d’effacer tous les éléments visuels. Avec [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), vous pouvez supprimer des images sélectionnées en spécifiant le numéro de page et l’indice de l’image.

Ce fragment de code lie un PDF d’entrée, supprime la deuxième image de la page 1 et enregistre le PDF modifié, en laissant les autres images intactes.

1. Créer une instance de PdfContentEditor.
1. Lier le document PDF d'entrée.
1. Supprimer des images spécifiques d'une page désignée.
1. Enregistrer le document PDF mis à jour.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_images(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Delete image on page 1
    content_editor.delete_image(1, [2])
    # Save updated document
    content_editor.save(outfile)
```

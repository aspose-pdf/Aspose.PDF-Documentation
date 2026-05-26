---
title: Remplacer des images dans le PDF
type: docs
weight: 30
url: /fr/python-net/replace-image/
description: Cet exemple lie un PDF d'entrée, remplace la première image de la page 1 par une nouvelle image et enregistre le document modifié.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remplacer une image dans un PDF à l'aide de PdfContentEditor en Python
Abstract: Cet exemple montre comment remplacer une image existante dans un document PDF en utilisant Aspose.PDF for Python via l'API Facades. Il montre comment cibler une image spécifique sur une page et la remplacer par une nouvelle image, puis enregistrer le PDF mis à jour.
---

Les PDF contiennent souvent des images qui peuvent devoir être mises à jour ou remplacées, telles que des logos, des diagrammes ou des photos. Avec [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), vous pouvez remplacer une image spécifique sur une page donnée en fournissant le numéro de page, l'index de l'image et le chemin du nouveau fichier image.

1. Créer une instance de PdfContentEditor.
1. Lier le document PDF d'entrée.
1. Remplacer une image spécifique sur une page donnée.
1. Enregistrer le document PDF mis à jour.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_image(infile, image_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace image on page 1
    content_editor.replace_image(1, 1, image_file)
    # Save updated document
    content_editor.save(outfile)
```

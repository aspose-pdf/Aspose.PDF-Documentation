---
title: Ajouter une annotation vidéo
type: docs
weight: 10
url: /fr/python-net/add-movie-annotation/
description: Cet exemple lie un PDF d'entrée, ajoute une annotation vidéo à la page 1 et enregistre le PDF mis à jour.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter une annotation vidéo à un PDF en utilisant PdfContentEditor en Python
Abstract: Cet exemple montre comment incorporer un film (vidéo) dans un document PDF en utilisant Aspose.PDF for Python via the Facades API. Il montre comment ajouter une annotation cliquable qui lit une vidéo directement dans le PDF.
---

Les annotations vidéo dans les PDF vous permettent d'incorporer du contenu multimédia, tel que des vidéos, dans vos documents. En utilisant [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), vous pouvez définir un rectangle sur une page où la vidéo apparaîtra. Lorsqu'elle est cliquée, la vidéo peut être lue directement depuis le PDF, rendant vos documents plus interactifs et attrayants.

1. Créer une instance de PdfContentEditor.
1. Lier le document PDF d'entrée.
1. Définir un rectangle pour l'annotation de film.
1. Spécifiez le fichier vidéo à incorporer.
1. Attribuer le numéro de page à l'annotation.
1. Enregistrer le document PDF mis à jour.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_movie_annotation(infile, movie_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add movie annotation to page 1
    content_editor.create_movie(apd.Rectangle(80, 500, 220, 120), movie_file, 1)
    # Save updated document
    content_editor.save(outfile)
```

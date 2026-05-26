---
title: Ajouter une annotation de pièce jointe à partir d’un flux
type: docs
weight: 40
url: /fr/python-net/add-file-attachment-annotation-from-stream/
description: L’exemple charge un PDF, lit un fichier externe dans un flux mémoire, ajoute une annotation de pièce jointe à la première page et enregistre le document modifié.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter des annotations de pièce jointe à un PDF à partir d’un flux en Python
Abstract: Cet exemple montre comment créer une annotation de pièce jointe dans un PDF en utilisant un flux de fichier avec Aspose.PDF for Python via l’API Facades. Il montre comment spécifier la position de l’annotation, définir une description, inclure une valeur d’opacité et enregistrer le document modifié.
---

Les annotations de pièce jointe permettent d’intégrer des fichiers sous forme d’icônes interactives au sein d’une page PDF. En utilisant une approche basée sur les flux, vous pouvez attacher des fichiers dynamiquement sans dépendre d’un chemin de fichier physique. Cette méthode prend également en charge la personnalisation de l’apparence de l’annotation, y compris l’opacité.

1. Créer l'objet PdfContentEditor.
1. Lier le PDF d'entrée.
1. Lire le fichier joint en tant que flux.
1. Ajouter l'annotation de pièce jointe de fichier.
1. Enregistrer le Document mis à jour.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_file_attachment_annotation_from_stream(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    with open(attachment_file, "rb") as source_stream:
        attachment_stream = BytesIO(source_stream.read())

    # Create file attachment annotation using stream+opacity overload
    content_editor.create_file_attachment(
        apd.Rectangle(130, 520, 20, 20),
        "Attachment annotation from stream",
        attachment_stream,
        path.basename(attachment_file),
        1,
        "Tag",
        0.75,
    )
    # Save updated document
    content_editor.save(outfile)
```

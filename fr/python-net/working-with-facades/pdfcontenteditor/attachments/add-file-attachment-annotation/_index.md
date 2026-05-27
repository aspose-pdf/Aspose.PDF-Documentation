---
title: Ajouter une annotation de pièce jointe de fichier
type: docs
weight: 30
url: /fr/python-net/add-file-attachment-annotation/
description: L'exemple lie un PDF d'entrée, ajoute une annotation de pièce jointe de fichier à la première page en utilisant le chemin du fichier, et enregistre le document mis à jour.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter des annotations de pièce jointe de fichier à un PDF en Python
Abstract: Cet exemple montre comment créer une annotation de pièce jointe de fichier dans un PDF en utilisant un chemin de fichier avec Aspose.PDF for Python via the Facades API. Il montre comment définir le placement de l'annotation, définir le texte de description, choisir un type d'icône, et enregistrer le document modifié.
---

Les annotations de pièce jointe de fichier vous permettent d'intégrer des fichiers externes sous forme d'icônes interactives sur une page PDF. En utilisant la surcharge de chemin de fichier, vous pouvez attacher des fichiers directement depuis le disque sans ouvrir manuellement les flux. Cette méthode vous permet également de personnaliser l'icône de l'annotation et de fournir une description aux utilisateurs.

1. Créer le [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) objet.
1. Lier le PDF d'entrée.
1. Définir le rectangle de l'annotation.
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


def add_file_attachment_annotation(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Create file attachment annotation on page 1
    content_editor.create_file_attachment(
        apd.Rectangle(100, 520, 20, 20),
        "Attachment annotation contents",
        attachment_file,
        1,
        "PushPin",
    )
    # Save updated document
    content_editor.save(outfile)
```

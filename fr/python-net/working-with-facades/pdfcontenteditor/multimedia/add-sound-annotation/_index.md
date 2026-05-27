---
title: Ajouter une annotation sonore
type: docs
weight: 20
url: /fr/python-net/add-sound-annotation/
description: Cet exemple lie un PDF d'entrée, ajoute une annotation sonore à la page 1 et enregistre le PDF modifié.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter une annotation sonore à un PDF en utilisant PdfContentEditor en Python
Abstract: Cet exemple montre comment intégrer de l'audio dans un document PDF en utilisant Aspose.PDF for Python via l'API Facades. Il montre comment ajouter une annotation sonore cliquable qui lit un fichier audio directement dans le PDF.
---

Les annotations sonores dans les PDF vous permettent d'ajouter du contenu audio tel que des notes vocales, de la musique ou des effets sonores à vos documents. En utilisant [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), vous pouvez définir un petit rectangle cliquable sur une page qui lit un fichier audio spécifié lorsqu'il est activé.

1. Créer une instance de PdfContentEditor.
1. Lier le document PDF d'entrée.
1. Définissez un rectangle pour l'annotation sonore.
1. Spécifiez le fichier audio, le nom de l'annotation, le numéro de page et la fréquence d'échantillonnage.
1. Enregistrer le document PDF mis à jour.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_sound_annotation(infile, sound_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add sound annotation to page 1
    content_editor.create_sound(
        apd.Rectangle(80, 450, 30, 30), sound_file, "Speaker", 1, "8000"
    )
    # Save updated document
    content_editor.save(outfile)
```

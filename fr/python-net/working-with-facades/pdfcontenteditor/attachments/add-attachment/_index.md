---
title: Ajouter une pièce jointe
type: docs
weight: 10
url: /fr/python-net/add-attachment/
description: Cet exemple lie un PDF d'entrée, attache un fichier externe à la première page et enregistre le PDF modifié avec la pièce jointe intégrée.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter des pièces jointes de fichiers à un PDF avec Python
Abstract: Cet exemple démontre comment attacher des fichiers externes à un document PDF en utilisant Aspose.PDF for Python via l'API Facades. Il montre comment lier un PDF, ajouter des pièces jointes avec des descriptions et enregistrer le document mis à jour.
---

Les pièces jointes de fichiers dans les PDF vous permettent d'inclure des documents supplémentaires, des images ou d'autres ressources directement dans le PDF. Avec [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), vous pouvez attacher des fichiers de manière programmatique à des pages spécifiques, définir le nom de la pièce jointe et fournir une description.

1. Créer l'objet PdfContentEditor.
1. Lier le PDF d'entrée.
1. Ouvrez le fichier de pièce jointe.
1. Ajoutez la pièce jointe au PDF.
1. Enregistrer le Document mis à jour.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_attachment(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add attachment to page 1
    with open(attachment_file, "rb") as attachment_stream:
        content_editor.add_document_attachment(
            attachment_stream,
            path.basename(attachment_file),
            "This is a sample attachment for demonstration purposes.",
        )
    # Save updated document
    content_editor.save(outfile)
```

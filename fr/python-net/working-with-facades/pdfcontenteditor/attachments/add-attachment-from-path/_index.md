---
title: Ajouter une pièce jointe depuis le chemin
type: docs
weight: 20
url: /fr/python-net/add-attachment-from-path/
description: Cet exemple lie un PDF d'entrée, attache un fichier externe en utilisant son chemin d'accès, et enregistre le PDF modifié avec la pièce jointe intégrée.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Attacher des fichiers à un PDF en utilisant la surcharge du chemin d'accès dans Python
Abstract: Cet exemple montre comment attacher des fichiers externes à un document PDF en utilisant la surcharge du chemin d'accès de 'add_document_attachment()' dans Aspose.PDF for Python via l'API Facades. Il simplifie l'ajout de pièces jointes sans ouvrir manuellement un flux de fichier.
---

Le PDF peut inclure des fichiers intégrés tels que des documents, des feuilles de calcul ou des images à des fins de référence ou de distribution. La surcharge du chemin d'accès de 'add_document_attachment()' vous permet d'ajouter des pièces jointes directement à partir d'un chemin de fichier, éliminant ainsi la nécessité d'ouvrir le fichier manuellement.

1. Créer le [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) objet.
1. Lier le PDF d'entrée.
1. Ajouter la pièce jointe en utilisant le chemin d'accès.
1. Enregistrer le Document mis à jour.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_attachment_from_path(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add attachment using file-path overload
    content_editor.add_document_attachment(
        attachment_file,
        "Attachment added using file path overload.",
    )
    # Save updated document
    content_editor.save(outfile)
```

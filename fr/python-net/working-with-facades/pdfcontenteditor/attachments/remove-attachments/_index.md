---
title: Supprimer les pièces jointes
type: docs
weight: 50
url: /fr/python-net/remove-attachments/
description: Cet exemple lie un PDF d'entrée, supprime toutes les pièces jointes et enregistre le PDF modifié sans aucun fichier intégré.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Supprimer toutes les pièces jointes d'un PDF à l'aide de Python
Abstract: Cet exemple montre comment supprimer toutes les pièces jointes d'un document PDF en utilisant Aspose.PDF for Python via l'API Facades. Il montre comment lier un PDF, supprimer les pièces jointes intégrées et enregistrer le document mis à jour.
---

Les PDF peuvent contenir des pièces jointes telles que des documents, des images ou d'autres fichiers. Il existe des scénarios où vous devez nettoyer un PDF de toutes les pièces jointes pour des raisons de sécurité, de confidentialité ou de distribution. En utilisant [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), vous pouvez supprimer programmétiquement toutes les pièces jointes intégrées dans un document.

1. Créer l'objet PdfContentEditor. 
1. Lier le PDF d'entrée.
1. Supprimer toutes les pièces jointes.
1. Enregistrer le Document mis à jour.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_attachments(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Remove all attachments from document
    content_editor.delete_attachments()
    # Save updated document
    content_editor.save(outfile)
```

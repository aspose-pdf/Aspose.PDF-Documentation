---
title: Supprimer toutes les images du PDF
type: docs
weight: 10
url: /fr/python-net/delete-all-images/
description: Supprimer toutes les images d'un document PDF en utilisant Aspose.PDF for Python via l'API Facades.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Supprimer toutes les images d'un PDF en utilisant PdfContentEditor en Python
Abstract: Cet exemple montre comment supprimer toutes les images d'un document PDF en utilisant Aspose.PDF for Python via l'API Facades. Il montre comment lier un PDF, supprimer toutes les images intégrées et enregistrer le document mis à jour.
---

Les documents PDF contiennent souvent des images à des fins d'illustration, d'image de marque ou de décoration. Il peut arriver que vous deviez supprimer toutes les images d'un PDF, par exemple pour réduire la taille du fichier, protéger des visuels sensibles ou préparer une version texte uniquement.

Utilisation [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), vous pouvez supprimer programmatiquement toutes les images d'un PDF, en vous assurant que le document ne contient que du contenu textuel. Cet exemple lie un PDF d'entrée, supprime toutes les images et enregistre le fichier modifié.

1. Créer l'objet PdfContentEditor.
1. Lier le PDF d'entrée.
1. Supprimer toutes les images.
1. Enregistrer le Document mis à jour.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_all_image(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Delete all images from the document
    content_editor.delete_image()
    # Save updated document
    content_editor.save(outfile)
```

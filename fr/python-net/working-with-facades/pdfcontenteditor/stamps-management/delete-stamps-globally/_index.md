---
title: Supprimer les tampons globalement
type: docs
weight: 60
url: /fr/python-net/delete-stamps-globally/
description: Cet exemple montre comment supprimer les annotations de tampons en caoutchouc globalement sur toutes les pages d’un PDF en utilisant Aspose.PDF for Python via l’API Facades. Il montre comment supprimer les tampons par ID sans spécifier les pages individuelles.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Supprimer les tampons en caoutchouc globalement dans un PDF en utilisant PdfContentEditor en Python
Abstract: Cet exemple montre comment supprimer les annotations de tampons en caoutchouc globalement sur toutes les pages d’un PDF en utilisant Aspose.PDF for Python via l’API Facades. Il montre comment supprimer les tampons par ID sans spécifier les pages individuelles.
---

Lorsque vous travaillez avec plusieurs pages, vous pouvez avoir besoin de supprimer certains tampons dans l’ensemble du document. Les méthodes 'delete_stamp_by_id()' et 'delete_stamp_by_ids()' vous permettent de supprimer les tampons globalement par leurs identifiants, éliminant ainsi la nécessité d’itérer manuellement chaque page.

1. Créer un [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instance.
1. Lier le document PDF d'entrée.
1. Ajouter des tampons en caoutchouc à plusieurs pages.
1. Supprimer les tampons globalement en utilisant leurs ID.
1. Enregistrer le document PDF mis à jour.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_stamps_globally(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    # Add stamps across multiple pages so global deletion is meaningful
    for page in range(1, 5):
        content_editor.create_rubber_stamp(
            page,
            apd.Rectangle(120, 500, 180, 60),
            "Draft",
            "Stamp for global deletion",
            apd.Color.gray,
        )

    # delete_stamp_by_id without page number removes stamp ID from all pages
    content_editor.delete_stamp_by_id(1)
    # delete_stamp_by_ids without page number removes a list of IDs from all pages
    content_editor.delete_stamp_by_ids([2, 3])

    # Save updated document
    content_editor.save(outfile)
```

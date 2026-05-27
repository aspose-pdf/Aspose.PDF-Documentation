---
title: Déplacer le tampon par ID
type: docs
weight: 80
url: /fr/python-net/move-stamp-by-id-example/
description: Dans cet exemple, un tampon en caoutchouc est ajouté à la page 1, puis déplacé vers une nouvelle position en utilisant son ID avant d'enregistrer le document mis à jour.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Déplacer un tampon en caoutchouc par ID dans un PDF à l'aide de PdfContentEditor en Python
Abstract: Cet exemple montre comment repositionner une annotation de tampon en caoutchouc existante dans un PDF en utilisant Aspose.PDF for Python via l'API Facades. Il montre comment créer un tampon puis le déplacer programmatiquement en utilisant son ID.
---

Après avoir ajouté une annotation de tampon en caoutchouc à un PDF, vous pouvez avoir besoin d'ajuster sa position. La méthode 'move_stamp_by_id()' vous permet de repositionner un tampon en fonction de son identifiant, sans le recréer. Cela est utile dans les flux de travail automatisés où le placement du tampon doit être ajusté dynamiquement.

1. Créer un [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instance.
1. Lier le document PDF d'entrée.
1. Ajouter une annotation de tampon en caoutchouc.
1. Déplacer le tampon en utilisant son ID.
1. Enregistrer le document PDF mis à jour.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def move_stamp_by_id_example(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(300, 420, 180, 60),
        "Approved",
        "Move this stamp by ID",
        apd.Color.green,
    )

    # Move stamp by ID overload
    content_editor.move_stamp_by_id(1, 1, 240, 360)

    # Save updated document
    content_editor.save(outfile)
```    

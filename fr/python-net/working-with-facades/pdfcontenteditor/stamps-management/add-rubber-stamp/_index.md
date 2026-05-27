---
title: Ajouter un tampon en caoutchouc
type: docs
weight: 10
url: /fr/python-net/add-rubber-stamp/
description: Cet exemple lie un PDF d'entrée, ajoute un tampon en caoutchouc vert “Approved” aux quatre premières pages et enregistre le document modifié.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter une annotation de tampon en caoutchouc à un PDF en utilisant PdfContentEditor en Python
Abstract: Cet exemple montre comment ajouter une annotation de tampon en caoutchouc à un document PDF en utilisant Aspose.PDF for Python via l'API Facades. Les tampons en caoutchouc vous permettent de marquer visuellement les pages avec des approbations, des révisions ou des libellés personnalisés.
---

Les annotations de tampon en caoutchouc sont couramment utilisées dans les PDF pour indiquer une approbation, un statut de révision ou d'autres notes. En utilisant [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), vous pouvez définir un rectangle pour le tampon, définir son texte et ses commentaires, choisir une couleur et l'appliquer à plusieurs pages d'un document.

1. Créer une instance de PdfContentEditor.
1. Lier le document PDF d'entrée.
1. Parcourir les pages 1–4.
1. Ajouter une annotation de tampon en caoutchouc avec du texte personnalisé, des commentaires et une couleur.
1. Enregistrer le document PDF mis à jour.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_rubber_stamp(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    for i in range(1, 5):
        content_editor.create_rubber_stamp(
            i,
            apd.Rectangle(120, 450, 180, 60),
            "Approved",
            "Approved by reviewer",
            apd.Color.green,
        )
    # Save updated document
    content_editor.save(outfile)
```

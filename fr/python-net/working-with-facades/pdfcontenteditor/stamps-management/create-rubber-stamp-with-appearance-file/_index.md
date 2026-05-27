---
title: Créer un tampon en caoutchouc avec un fichier d'apparence
type: docs
weight: 20
url: /fr/python-net/create-rubber-stamp-with-appearance-file/
description: L'exemple lie un PDF d'entrée, crée un tampon en caoutchouc sur la page 1 en utilisant un fichier image comme apparence du tampon, et enregistre le PDF mis à jour.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Créer un tampon en caoutchouc avec une apparence personnalisée dans un PDF en utilisant PdfContentEditor
Abstract: Cet exemple montre comment ajouter une annotation de tampon en caoutchouc avec une apparence personnalisée (image) à un document PDF en utilisant Aspose.PDF for Python via l'API Facades. Les tampons personnalisés vous permettent d'inclure des logos, des signatures ou des visuels de marque dans le tampon.
---

Les annotations de tampon en caoutchouc peuvent être personnalisées non seulement avec du texte mais aussi en utilisant un fichier image comme apparence. Cette approche est utile pour ajouter des logos d'entreprise, des tampons de signature ou tout indicateur visuel à vos pages PDF.

1. Créer un [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instance.
1. Lier le document PDF d'entrée.
1. Définissez un rectangle pour le tampon.
1. Utilisez un fichier image personnalisé pour définir l'apparence du tampon en caoutchouc.
1. Définissez le texte et la couleur du tampon.
1. Enregistrer le document PDF mis à jour.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_rubber_stamp_with_appearance_file(infile, image_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Create rubber stamp using appearance_file overload (image path)
    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(100, 400, 200, 60),
        "Stamp with custom appearance",
        apd.Color.dark_green,
        image_file,
    )
    # Save updated document
    content_editor.save(outfile)
```

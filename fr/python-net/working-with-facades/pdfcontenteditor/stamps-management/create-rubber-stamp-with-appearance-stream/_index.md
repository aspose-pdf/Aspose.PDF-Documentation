---
title: Créer un tampon en caoutchouc avec un flux d’apparence
type: docs
weight: 30
url: /fr/python-net/create-rubber-stamp-with-appearance-stream/
description: Cet exemple charge un PDF, crée un tampon en caoutchouc sur la page 1 en utilisant un fichier image pour son apparence, et enregistre le document modifié. ✨
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Créer un tampon en caoutchouc avec une apparence d'image personnalisée en utilisant PdfContentEditor en Python
Abstract: Cet exemple montre comment créer une annotation de tampon en caoutchouc avec une apparence d'image personnalisée dans un PDF en utilisant Aspose.PDF for Python via l'API Facades. Cette approche vous permet d'appliquer des tampons de marque ou visuellement riches tels que des logos, des sceaux ou des signatures.
---

Les annotations de tampon en caoutchouc peuvent être personnalisées à l'aide d'un fichier image externe. Au lieu de se limiter aux tampons basés sur du texte, vous pouvez définir une apparence visuelle (par exemple, le logo d'une entreprise ou un badge d'approbation) et la placer sur une page.

1. Créer un [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instance.
1. Lier le document PDF d'entrée.
1. Définissez un rectangle pour l'emplacement du tampon.
1. Utilisez un fichier image comme apparence du tampon.
1. Appliquez les paramètres de texte et de couleur.
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

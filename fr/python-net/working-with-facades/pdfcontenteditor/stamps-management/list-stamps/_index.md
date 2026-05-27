---
title: Lister les tampons
type: docs
weight: 70
url: /fr/python-net/list-stamps/
description: Cet exemple charge un PDF, récupère tous les tampons de la page 1, les imprime et affiche un message si aucun tampon n’est trouvé.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Lister les annotations de tampons en caoutchouc dans un PDF à l’aide de PdfContentEditor en Python
Abstract: Cet exemple montre comment récupérer et lister les annotations de tampons en caoutchouc d’un document PDF en utilisant Aspose.PDF for Python via l’API Facades. Il montre comment accéder aux tampons sur une page spécifique et afficher leurs détails.
---

Lorsque vous travaillez avec des PDF annotés, vous pourriez avoir besoin d’inspecter les tampons en caoutchouc existants avant de les modifier ou de les supprimer. La méthode 'get_stamps()' vous permet de récupérer tous les tampons placés sur une page donnée. Vous pouvez ensuite parcourir les résultats et les traiter par programme.

1. Créer un [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instance.
1. Lier le document PDF d'entrée.
1. Récupérer tous les tampons de la page 1.
1. Parcourir la collection de tampons.
1. Imprimer chaque tampon.
1. Afficher un message si aucun tampon n'existe.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def list_stamps(infile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # List all stamps on page 1
    stamps = content_editor.get_stamps(1)

    count = 0
    for stamp in stamps:
        count += 1
        print(f"Stamp {count}: {stamp}")

    if count == 0:
        print("No stamps found")
```

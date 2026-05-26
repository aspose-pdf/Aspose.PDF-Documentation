---
title: Supprimer le tampon par indice
type: docs
weight: 50
url: /fr/python-net/delete-stamp-by-index/
description: Cet exemple crée deux tampons en caoutchouc sur la page 2. Après cela, un tampon peut être supprimé en spécifiant son indice.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Supprimer un tampon en caoutchouc par indice dans un PDF à l'aide de PdfContentEditor en Python
Abstract: Cet exemple démontre comment supprimer une annotation de tampon en caoutchouc dans un PDF en utilisant son indice avec Aspose.PDF for Python via l'API Facades. Il montre comment ajouter plusieurs tampons puis en supprimer un en fonction de leur ordre sur la page.
---

Lorsque plusieurs tampons en caoutchouc existent sur une page, vous pouvez supprimer un spécifique en utilisant son indice. La méthode delete_stamp() permet de supprimer des annotations selon leur séquence, ce qui est utile lorsque vous ne suivez pas les ID des tampons mais que vous connaissez leur ordre.

1. Créer un [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instance.
1. Lier le document PDF d'entrée.
1. Liez le fichier PDF d'entrée à l'instance PdfContentEditor en utilisant bind_pdf(infile).
1. Appelez 'delete_stamp(1, [2, 3])' pour supprimer le tampon avec l'index 1 des pages 2 et 3.
1. Enregistrez le document PDF modifié dans le fichier de sortie en utilisant save(outfile).

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_stamp_by_index(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    content_editor.delete_stamp(1, [2, 3])
    # Save updated document
    content_editor.save(outfile)
```

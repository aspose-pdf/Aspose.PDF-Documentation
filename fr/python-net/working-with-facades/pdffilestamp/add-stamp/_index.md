---
title: Ajouter un tampon au PDF
type: docs
weight: 40
url: /fr/python-net/add-stamp/
description: Apprenez comment ajouter un tampon aux pages PDF en utilisant PdfFileStamp en Python.
lastmod: "2026-05-22"
TechArticle: true
AlternativeHeadline: Ajouter des tampons texte au PDF en Python
Abstract: Cet article explique comment ajouter du contenu de tampon aux documents PDF avec Aspose.PDF for Python via .NET en utilisant la façade PdfFileStamp. Il montre comment créer un tampon, le positionner sur la page, contrôler la rotation et l'opacité, et enregistrer le PDF mis à jour.
---

Aspose.PDF for Python via .NET fournit le [PdfFileStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) façade pour ajouter du contenu récurrent aux pages PDF. En plus des en-têtes, pieds de page et numéros de page, vous pouvez l'utiliser pour placer des tampons basés sur du texte sur chaque document.

## Ajouter le tampon à un PDF

Après la configuration du tampon, liez le PDF d'entrée à `PdfFileStamp`, ajouter le tampon, et enregistrer le fichier de sortie. Cela applique le tampon configuré sur l'ensemble du document.

```python
import sys
from os import path

import aspose.pdf.facades as pdf_facades

CURRENT_DIR = path.dirname(__file__)
EXAMPLES_DIR = path.abspath(path.join(CURRENT_DIR, "..", ".."))
if EXAMPLES_DIR not in sys.path:
    sys.path.insert(0, EXAMPLES_DIR)

from config import initialize_data_dir, set_license


def add_stamp_to_pdf(infile: str, image_file: str, outfile: str) -> None:
    """Add an image stamp to a PDF file."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

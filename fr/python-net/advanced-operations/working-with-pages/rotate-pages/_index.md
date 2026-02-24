---
title: Faire pivoter les pages PDF avec Python
linktitle: Faire pivoter les pages PDF
type: docs
weight: 110
url: /fr/python-net/rotate-pages/
description: Ce sujet décrit comment faire pivoter l'orientation des pages d'un fichier PDF existant de manière programmatique avec Python.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment faire pivoter les pages d'un PDF avec Python
Abstract: Cet article propose un guide sur la façon de mettre à jour ou de modifier l'orientation des pages d'un fichier PDF existant de manière programmatique en utilisant Python. En utilisant Aspose.PDF pour Python via .NET, les utilisateurs peuvent facilement basculer entre les orientations paysage et portrait en ajustant les propriétés MediaBox de la page. L'article inclut un extrait de code Python montrant comment parcourir les pages d'un document PDF, modifier leurs dimensions et positions MediaBox, et ajuster le CropBox si nécessaire. De plus, il explique comment définir l'angle de rotation des pages à l'aide de la méthode 'rotate' pour obtenir l'orientation souhaitée. Le processus se termine par l'enregistrement du fichier PDF mis à jour.
---

Ce sujet décrit comment mettre à jour ou modifier l'orientation des pages d'un fichier PDF existant de manière programmatique avec Python.

## Modifier l'orientation des pages

Cette fonction fait pivoter chaque page d'un PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) de 90 degrés dans le sens des aiguilles d'une montre en utilisant Aspose.PDF pour Python.
Elle est utile pour corriger les problèmes d'orientation des pages, comme les documents numérisés qui sont de travers. Le PDF original reste inchangé, et la version pivotée est enregistrée en tant que nouveau fichier.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_page(infile, outfile):
    """
    Rotate all pages in a PDF document by 90 degrees clockwise.

    Demonstrates how to rotate PDF pages using the Aspose.PDF library.
    This function applies a 90-degree clockwise rotation to every page
    in the input document and saves the result to a new file.

    Args:
        infile (str): Path to the input PDF file to rotate.
        outfile (str): Path where the rotated PDF will be saved.

    Returns:
        None: The function modifies the PDF pages and saves to the output path.

    Note:
        - Applies 90-degree clockwise rotation (ap.Rotation.ON90) to all pages
        - Rotates every page in the document uniformly
        - The original document is not modified; a new file is created
        - Rotation options include: ON90 (90°), ON180 (180°), ON270 (270°)
        - Useful for correcting page orientation or adjusting layout

    Example:
        >>> rotate_page("input.pdf", "rotated_output.pdf")
        # Rotates all pages 90 degrees clockwise and saves to rotated_output.pdf
    """
    document = ap.Document(infile)
    for page in document.pages:
        # `page` is a `Page` object; `rotate` uses the `Rotation` enum
        page.rotate = ap.Rotation.ON90

    document.save(outfile)
```



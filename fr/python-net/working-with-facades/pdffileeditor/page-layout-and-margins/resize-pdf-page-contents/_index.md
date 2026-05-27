---
title: Redimensionner le contenu des pages PDF
type: docs
weight: 30
url: /fr/python-net/resize-pdf-page-contents/
description: Redimensionner le contenu de pages PDF spécifiques à l'aide d'Aspose.PDF for Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Redimensionner le contenu des pages PDF de manière programmatique en Python
Abstract: Apprenez comment redimensionner le contenu de pages PDF spécifiques à l'aide d'Aspose.PDF for Python. Cet exemple démontre comment ajuster la largeur et la hauteur du contenu d'une page tout en préservant la structure du document, facilitant ainsi l'optimisation des mises en page pour l'impression ou la visualisation.
---

L'ajustement de la taille du contenu des pages PDF est souvent nécessaire lors de la préparation de documents pour l'impression, de l'adaptation du contenu à une mise en page spécifique ou de la normalisation des formats de page dans un document. En utilisant Aspose.PDF for Python, les développeurs peuvent redimensionner le contenu des pages sélectionnées de manière programmatique sans modifier manuellement le document.

Cet article montre comment utiliser la méthode 'resize_contents' de [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) classe permettant de modifier les dimensions du contenu de page pour des pages spécifiques dans un fichier PDF. En spécifiant la largeur et la hauteur cibles, le contenu des pages sélectionnées est redimensionné en conséquence.

1. Créer un objet PdfFileEditor.
1. Redimensionner le contenu des pages.

Paramètres :

- [1, 3] – liste des numéros de pages dont le contenu sera redimensionné.
- 400 – la nouvelle largeur du contenu de la page (en points).
- 750 – la nouvelle hauteur du contenu de la page (en points).

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Resize PDF Page Contents
def resize_pdf_page_contents(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()

    if not pdf_editor.resize_contents(
        FileIO(infile), FileIO(outfile, "w"), [1, 3], 400, 750
    ):
        raise Exception("Failed to resize PDF page contents.")
```

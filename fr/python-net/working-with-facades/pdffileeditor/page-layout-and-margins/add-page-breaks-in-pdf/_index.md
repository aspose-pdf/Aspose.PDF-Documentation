---
title: Ajouter des sauts de page dans le PDF
type: docs
weight: 20
url: /fr/python-net/add-page-breaks-in-pdf/
description: Insérer des sauts de page dans un document PDF à l'aide d'Aspose.PDF pour Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter des sauts de page aux pages PDF programmatiquement en Python
Abstract: Apprenez comment insérer des sauts de page dans un document PDF à l'aide d'Aspose.PDF pour Python. Cet exemple montre comment diviser une page à une position verticale spécifiée, permettant aux développeurs de réorganiser le contenu et de créer des pages supplémentaires de manière dynamique.
---

Les sauts de page sont utiles lorsque vous devez diviser de longues pages PDF en plusieurs pages ou contrôler la façon dont le contenu est distribué dans un document. En utilisant Aspose.PDF pour Python, les développeurs peuvent insérer des sauts de page à des positions spécifiques sans modifier manuellement le PDF.

Cet article montre comment utiliser la méthode 'add_page_break' de [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) classe pour insérer un saut de page à une coordonnée verticale définie sur une page sélectionnée. La méthode crée une nouvelle page et déplace le contenu situé sous le point de rupture vers cette page.

1. Créer un objet PdfFileEditor.
1. Définir la position du saut de page.
1. Insérer le saut de page.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Add Page Breaks in PDF
def add_page_breaks_in_pdf(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.add_page_break(
        infile,
        outfile,
        [
            pdf_facades.PdfFileEditor.PageBreak(1, 400),
        ],
    )
```

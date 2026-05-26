---
title: Ajouter des pages au PDF
type: docs
weight: 10
url: /fr/python-net/append-pages-to-pdf/
description: Ajouter des pages d'un document PDF à un autre en utilisant Aspose.PDF for Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter des pages d'un PDF à un autre en Python
Abstract: Apprenez comment ajouter des pages d'un document PDF à un autre en utilisant Aspose.PDF for Python. Cet exemple montre comment utiliser la classe PdfFileEditor pour combiner des pages de plusieurs PDF et créer un document de sortie unique.
---

Combiner des pages de différents documents PDF est une exigence courante dans les flux de travail de traitement de documents. En utilisant Aspose.PDF for Python, les développeurs peuvent facilement ajouter des pages d'un ou plusieurs fichiers PDF à un document existant.

Cet extrait de code montre comment utiliser la méthode append de [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) classe permettant d'ajouter des pages sélectionnées d'un autre fichier PDF à la fin d'un PDF source. En spécifiant la plage de pages, les développeurs peuvent contrôler exactement quelles pages sont incluses dans le document final.

1. Créer un objet PdfFileEditor.
1. Ajouter des pages d'un autre PDF.

Les pages spécifiées du document PDF secondaire sont ajoutées à la fin du PDF original, créant un fichier de sortie combiné.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


# Append Pages to PDF
def append_pages_to_pdf(infile, sample_file, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    # Append pages from the specified PDF document to the end of the source PDF document
    pdf_editor.append(infile, [sample_file], 1, 2, outfile)
```

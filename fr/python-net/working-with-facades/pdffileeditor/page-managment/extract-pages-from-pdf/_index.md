---
title: Extraire des pages du PDF
type: docs
weight: 30
url: /fr/python-net/extract-pages-from-pdf/
description: Extraire les pages sélectionnées d'un document PDF à l'aide d'Aspose.PDF for Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraire des pages spécifiques d'un document PDF en Python
Abstract: Apprenez comment extraire des pages sélectionnées d'un document PDF à l'aide d'Aspose.PDF for Python. Cet exemple montre comment créer un nouveau PDF contenant uniquement les pages dont vous avez besoin, permettant la création de documents personnalisés et la manipulation au niveau des pages.
---

Extraire des pages d'un PDF est utile lorsque vous devez créer un sous-ensemble d'un document, partager uniquement un contenu spécifique, ou réorganiser des PDF pour des présentations, des rapports ou l'impression. En utilisant Aspose.PDF for Python, les développeurs peuvent extraire programmatiquement des pages d'un fichier PDF et les enregistrer en tant que nouveau document.

Apprenez comment utiliser la méthode extract de [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) class. En spécifiant une liste de pages à extraire, vous pouvez générer un nouveau PDF contenant uniquement les pages sélectionnées tout en préservant le contenu et le formatage d'origine.

1. Créer un objet PdfFileEditor.
1. Définir les pages à extraire.
1. Extraire les pages.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


# Extract Pages from PDF
def extract_pages_from_pdf(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()

    # Define the page numbers to be extracted (1-based index)
    pages_to_extract = [1, 4, 3]

    # Extract the specified pages from the PDF document and save to a new PDF document
    pdf_editor.extract(infile, pages_to_extract, outfile)
```

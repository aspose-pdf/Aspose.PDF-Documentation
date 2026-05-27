---
title: Insérer des pages dans un PDF
type: docs
weight: 40
url: /fr/python-net/insert-pages-into-pdf/
description: Insérer des pages d'un PDF dans un autre à l'aide d'Aspose.PDF for Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Insérer des pages d'un autre PDF dans un PDF existant en Python
Abstract: Apprenez comment insérer des pages d'un PDF dans un autre à l'aide d'Aspose.PDF for Python. Cet exemple montre comment ajouter des pages sélectionnées d'un PDF secondaire à une position précise du document original, créant ainsi un PDF combiné avec un placement de pages précis.
---

Insérer des pages dans un PDF existant est une exigence courante lors de la combinaison de documents, de l'ajout de contenu ou de la réorganisation de rapports. En utilisant Aspose.PDF for Python, les développeurs peuvent insérer programmétiquement des pages d'un PDF dans un autre à un emplacement spécifié.

Cet article montre comment utiliser la méthode insert de [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) class. En spécifiant les numéros de pages à insérer et l'emplacement cible, vous pouvez fusionner du contenu provenant de différents PDF tout en conservant le formatage et la structure d'origine.

1. Créer un objet PdfFileEditor.
1. Définir la position d'insertion et les pages.
1. Insérer des pages.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


# Insert Pages into PDF
def insert_pages_into_pdf(infile, sample_file, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()

    # Define the page number where new pages will be inserted (1-based index)
    insert_page_number = 2

    pdf_editor.insert(infile, insert_page_number, sample_file, [1, 2], outfile)
```

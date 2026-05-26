---
title: Diviser le PDF depuis le début
type: docs
weight: 10
url: /fr/python-net/split-pdf-from-beginning/
description: Divisez un document PDF depuis le début en utilisant Aspose.PDF for Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Diviser le PDF depuis le début en Python avec Aspose.PDF
Abstract: Apprenez comment diviser un document PDF depuis le début en utilisant Aspose.PDF for Python. Cet exemple montre comment extraire un nombre spécifique de pages à partir de la première page pour créer un nouveau document PDF.
---

Diviser les PDF depuis le début est utile lorsque vous avez besoin des premières pages d'un document en tant que fichier séparé. En utilisant Aspose.PDF for Python, la méthode split_from_first dans le [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) classe vous permet d'extraire un nombre défini de pages à partir de la page un. Cette fonctionnalité est idéale pour générer des extraits, des aperçus ou des sections plus petites d'un PDF plus volumineux sans modifier manuellement le fichier original.

1. Créer un objet PdfFileEditor.
1. Diviser le PDF à partir de la première page.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Split PDF from Beginning
def split_pdf_from_beginning(input_pdf_path, output_pdf_path):
    pdf_file_editor = pdf_facades.PdfFileEditor()
    pdf_file_editor.split_from_first(input_pdf_path, 3, output_pdf_path)
```

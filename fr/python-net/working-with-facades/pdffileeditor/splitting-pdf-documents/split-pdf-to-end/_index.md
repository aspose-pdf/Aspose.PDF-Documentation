---
title: Diviser le PDF jusqu'à la fin
type: docs
weight: 40
url: /fr/python-net/split-pdf-to-end/
description: Divisez un document PDF à partir d'une page donnée jusqu'à la dernière page en utilisant Aspose.PDF for Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Divisez un PDF d'une page spécifique jusqu'à la fin en Python
Abstract: Apprenez comment diviser un document PDF à partir d'une page donnée jusqu'à la dernière page en utilisant Aspose.PDF for Python. Cet exemple montre comment extraire toutes les pages à partir d'une page spécifiée afin de créer un nouveau fichier PDF.
---

Diviser un PDF d'une page spécifique jusqu'à la fin est utile lorsque vous avez besoin de la partie finale d'un document en tant que fichier séparé. En utilisant Aspose.PDF for Python, la méthode split_to_end de la [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) classe vous permet d'extraire les pages à partir de n'importe quel numéro de page jusqu'à la dernière page du document. Ceci est idéal pour créer des extraits, extraire des chapitres ou traiter des parties d'un grand PDF sans le modifier manuellement.

1. Créer un objet PdfFileEditor.
1. Diviser le PDF à partir d'une page spécifique jusqu'à la fin.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Split PDF to End
def split_pdf_to_end(input_pdf_path, output_pdf_path):
    pdf_file_editor = pdf_facades.PdfFileEditor()
    pdf_file_editor.split_to_end(input_pdf_path, 2, output_pdf_path)
```

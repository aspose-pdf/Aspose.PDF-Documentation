---
title: Diviser le PDF en pages uniques
type: docs
weight: 30
url: /fr/python-net/split-pdf-into-single-pages/
description: Divisez le document PDF en PDFs d’une seule page en utilisant Aspose.PDF for Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Diviser un PDF en pages individuelles en Python
Abstract: Apprenez comment diviser un document PDF en PDFs d’une seule page en utilisant Aspose.PDF for Python. Cette méthode extrait chaque page du PDF original et l’enregistre comme fichier séparé pour une gestion et un traitement flexibles des documents.
---

Diviser un PDF en pages uniques est utile pour le traitement au niveau de la page, l’impression ou la distribution de sections d’un document individuellement. En utilisant Aspose.PDF for Python, la méthode \u0027split_to_pages\u0027 de la [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) La classe crée des fichiers PDF distincts pour chaque page du document source. Cette approche permet l'extraction automatisée de pages pour l'archivage, la révision ou le partage individuel tout en préservant la mise en page et le contenu d'origine.

1. Créer un objet PdfFileEditor.
1. Diviser le PDF en pages individuelles.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Split PDF into Single Pages
def split_pdf_into_single_pages(input_pdf_path, output_pdf_path):
    pdf_file_editor = pdf_facades.PdfFileEditor()
    pdf_file_editor.split_to_pages(input_pdf_path, output_pdf_path)
```

---
title: Concaténer plusieurs fichiers PDF
type: docs
weight: 20
url: /fr/python-net/concatenate-pdf-files/
description: Combinez plusieurs fichiers PDF en un seul document à l'aide d'Aspose.PDF for Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Fusionner plusieurs fichiers PDF en un seul PDF en Python
Abstract: Apprenez comment combiner plusieurs fichiers PDF en un seul document à l'aide d'Aspose.PDF for Python. Cet exemple montre comment utiliser la méthode concatenate pour fusionner plusieurs PDF de manière fluide tout en préservant leur contenu et leur mise en forme.
---

La fusion de fichiers PDF est une tâche courante dans la gestion de documents, les rapports et les flux de travail automatisés. En utilisant Aspose.PDF for Python, les développeurs peuvent facilement combiner plusieurs fichiers PDF en un seul document consolidé. La méthode concatenate de la [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) classe assure que toutes les pages des fichiers d'entrée sont préservées dans la sortie finale, en maintenant leur mise en page et leur contenu d'origine. Cette approche est utile pour créer des rapports complets, combiner des formulaires ou archiver plusieurs documents efficacement.

1. Créer un objet PdfFileEditor.
1. Fusionner plusieurs fichiers PDF.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_pdf_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.concatenate(files_to_merge, output_file)
```

---
title: Concaténer des fichiers PDF avec optimisation
type: docs
weight: 30
url: /fr/python-net/concatenate-pdf-files-with-optimization/
description: Concaténez plusieurs fichiers PDF en un seul PDF optimisé en utilisant Aspose.PDF for Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Fusionner des fichiers PDF avec une sortie optimisée en Python
Abstract: Apprenez comment concaténer plusieurs fichiers PDF en un seul PDF optimisé en utilisant Aspose.PDF for Python. Cet exemple montre comment activer l'optimisation de taille afin de réduire la taille du fichier de sortie tout en préservant le contenu et la mise en forme.
---

Lors de la fusion de plusieurs PDF, le fichier résultant peut devenir volumineux, surtout s'il contient des images ou du contenu complexe. En utilisant Aspose.PDF for Python, les développeurs peuvent activer l'optimisation lors de la concaténation pour réduire la taille du fichier sans perdre de qualité. La propriété optimize_size dans le [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) classe garantit que le PDF fusionné est compact et efficace, ce qui le rend adapté au partage, au stockage ou à l'archivage.

1. Créer un objet PdfFileEditor et activer l'optimisation.
1. Fusionner des fichiers PDF.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_pdf_files_with_optimization(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.optimize_size = True  # Enable optimization for smaller output file size
    pdf_editor.concatenate(files_to_merge, output_file)
```

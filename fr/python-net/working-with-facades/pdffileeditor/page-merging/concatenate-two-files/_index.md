---
title: Concaténer deux fichiers PDF
type: docs
weight: 60
url: /fr/python-net/concatenate-two-files/
description: Concaténer deux fichiers PDF en un seul document en utilisant Aspose.PDF for Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Fusionner deux fichiers PDF en un seul PDF en Python
Abstract: Apprenez comment concaténer deux fichiers PDF en un seul document à l'aide d'Aspose.PDF for Python. Cet exemple montre comment fusionner deux PDF de façon transparente tout en préservant leur contenu et leur mise en forme d'origine.
---

Combiner deux fichiers PDF est une tâche courante lors de la consolidation de rapports, de contrats ou de formulaires. En utilisant Aspose.PDF for Python, vous pouvez fusionner programmétiquement deux PDF en un seul document en utilisant la méthode concatenate de la [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) classe. Cela garantit que toutes les pages des deux fichiers sont incluses dans le PDF de sortie tout en conservant la mise en page, le contenu et la structure d'origine.

1. Créer un objet PdfFileEditor.
1. Fusionner deux fichiers PDF.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_two_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.concatenate(files_to_merge[0], files_to_merge[1], output_file)
```
